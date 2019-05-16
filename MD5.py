import hashlib
import base64
def get_token(message=''):
    md5= hashlib.md5()
    md5.update(message.encode("utf-8"))
    token = md5.hexdigest()
    return token