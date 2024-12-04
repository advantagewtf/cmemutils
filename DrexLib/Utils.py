from imports import time
def delay(seconds: int):
    time.sleep(seconds)
class logging:

    @staticmethod
    def _get_current_time() -> str:
        """Returns the current timestamp formatted as [HH:MM:SS]"""
        return time.strftime("%H:%M:%S", time.localtime())
    
    @staticmethod
    def _get_color_for_log(log_type: str) -> str:
        """Returns the corresponding color for a log type."""
        if log_type == "+":
            return "\033[38;2;0;255;0m"  # Green for success
        elif log_type == "!":
            return "\033[38;2;255;0;0m"  # Red for error
        else:
            return "\033[38;2;255;255;255m"  # White for regular log

    @staticmethod
    def log(log_type: str, message: str):
        global DEBUG
        if DEBUG:
            if log_type != " ":
                timestamp = logging._get_current_time()
                color = logging._get_color_for_log(log_type)
                reset_color = "\033[0m"  # Reset color after log message
                log_message = f"[{log_type}] {timestamp}: {message}"
                print(f"{color}{log_message}{reset_color}")
            else:
                # For normal logs, just print the message without timestamp and brackets
                color = logging._get_color_for_log(log_type)
                reset_color = "\033[0m"
                print(f"{color}{message}{reset_color}")

    @staticmethod
    def success(message: str):
        """Logs a success message."""
        logger.log("+", message)
    
    @staticmethod
    def error(message: str):
        """Logs an error message."""
        logger.log("!", message)
    
    @staticmethod
    def info(message: str):
        """Logs a regular info message."""
        logger.log(" ", message)


# --- text utilities ---
class fade:
    @staticmethod
    def random(text: str) -> str:
        faded = ""
        for line in text.splitlines():
            for character in line:
                faded += (f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{character}\033[0m")
            faded += "\n"
        return faded

    @staticmethod
    def greenblue(text: str) -> str:
        faded = ""
        blue = 100
        for line in text.splitlines():
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
            if blue != 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    @staticmethod
    def redyellow(text: str) -> str:
        faded = ""
        yellow = 255
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{yellow};0m{line}\033[0m\n")
            if yellow != 255:
                yellow -= 15
                if yellow < 0:
                    yellow = 0
        return faded

    @staticmethod
    def rainbow(text: str) -> str:
        faded = ""
        color_cycle = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
        color_index = 0
        for line in text.splitlines():
            for character in line:
                color = color_cycle[color_index]
                faded += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{character}\033[0m"
                color_index = (color_index + 1) % len(color_cycle)
            faded += "\n"
        return faded

# --- Json class ---
class JSON:

    @staticmethod
    def decode(json_data: str) -> dict:
        """Decodes a JSON string into a Python dictionary."""
        try:
            return json.loads(json_data)
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"

    @staticmethod
    def dump(data: dict, file_path: str) -> str:
        """Dumps a Python dictionary into a JSON file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            return f"JSON data successfully written to {file_path}"
        except Exception as e:
            return f"Error writing JSON to file: {e}"

    @staticmethod
    def load(file_path: str) -> dict:
        """Loads a JSON file and returns it as a Python dictionary."""
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except Exception as e:
            return f"Error loading JSON file: {e}"
