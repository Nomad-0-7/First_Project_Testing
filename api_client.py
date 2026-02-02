import requests
import urllib3
from config import BASE_URL, TIMEOUT

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.verify = False # Since you're on localhost

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=payload, timeout=TIMEOUT, verify=self.verify)