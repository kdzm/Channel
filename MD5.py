import hashlib
def get_token(str):
    m1= hashlib.md5()
    m1.update(str.encode("utf-8"))
    token = m1.hexdigest()
    return token