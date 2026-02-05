import string
import pytest
import os
from pathlib import Path
import time
import datetime
from api_client import APIClient

client=APIClient()
filepath = Path("D:\Testing data\test.txt")
stats=filepath.stat()

ext=Path(r"D:\Testing data\test.txt").suffix

filename=filepath.name


Meta_data={
    "file_name":filepath.name,
    "file_type":ext,
    "file_size":stats.st_size,
    "file_path":
}

def test_upload():
    response = client.post("/api/File_Storage_Operations/Upload_File",file_type,'13')
    assert response.status_code==200
    assert "success" in response.text.lower()
