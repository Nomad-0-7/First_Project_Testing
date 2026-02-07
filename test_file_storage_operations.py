import string
import pytest
import os
from pathlib import Path
import time
import datetime
from api_client import APIClient

client=APIClient()
filepath = Path(r"D:\Testing data\test.txt")


def test_upload():
    url="/api/File_Storage_Operations/Upload_File"
    params={'userId':15}

    with open(filepath,"rb") as f:
        files = {'file': (filepath.name, f, 'text/plain')}
        response=client.post(url,params=params, files=files)

    assert response.status_code==200
    assert "success" in response.text.lower()