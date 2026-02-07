import requests
import urllib3
from config import BASE_URL, TIMEOUT

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.verify = False # Since you're on localhost

    # def post(self, endpoint, payload):

    #     url = f"{self.base_url}{endpoint}"

    #     return requests.post(url, json=payload, timeout=TIMEOUT, verify=self.verify)
    def post(self, endpoint, payload=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        
        # If the old tests send 'payload', we treat it as JSON
        if payload is not None and 'json' not in kwargs:
            kwargs['json'] = payload
            
        return requests.post(url, timeout=TIMEOUT, verify=self.verify, **kwargs)
    