import os
from uploader import pixeldrain, gofile, catbox

def route(path):
    size = os.path.getsize(path)

    if size < 20 * 1024 * 1024:
        return catbox.upload(path)

    try:
        return pixeldrain.upload(path)
    except:
        return gofile.upload(path)
