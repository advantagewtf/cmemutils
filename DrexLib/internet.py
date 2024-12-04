from imports import *

class internet:
	@staticmethod
	def get_ip() -> str:
	        """Returns the external IP address of the machine."""
	        try:
	            response = requests.get("https://api.ipify.org?format=json")
	            ip_info = response.json()
	            return ip_info.get("ip", "Unable to fetch IP")
	        except requests.RequestException as e:
	            return f"Error getting external IP: {e}"
	@staticmethod
	def check_internet() -> bool:
	        """Checks if the machine is connected to the internet."""
	        try:
	            requests.get("https://www.google.com", timeout=5)
	            return True
	        except requests.RequestException:
	            return False
