import subprocess
import os

def download_url(url):
    out = "/tmp/file"
    subprocess.run([
        "aria2c", "-x", "8", "-s", "8", "-o", out, url
    ], check=True)
    return out
