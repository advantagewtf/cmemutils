from imports import *
class KeyValidation:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt_data(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padding_length = 16 - (len(data) % 16)
        data += chr(padding_length) * padding_length
        encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
        return base64.b64encode(iv + encrypted_data).decode()

    def decrypt_data(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        padding_length = ord(decrypted_data[-1:])
        return decrypted_data[:-padding_length].decode()

    def generate_key(self, expiration_seconds):
        timestamp = int(time.time())
        expiration_timestamp = timestamp + expiration_seconds
        key_data = f"{timestamp},{expiration_timestamp}"
        encrypted_key = self.encrypt_data(key_data)
        return encrypted_key

    def validate_key(self, encrypted_key):
        try:
            decrypted_key = self.decrypt_data(encrypted_key)
            current_timestamp = int(time.time())
            timestamp, expiration_timestamp = map(int, decrypted_key.split(','))
            if current_timestamp > expiration_timestamp:
                return False
            return True
        except Exception:
            return False
