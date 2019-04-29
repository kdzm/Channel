#import magic
#magic.from_file('C:\\Users\\Administrator\\Downloads\\channelsfc (3)')
import filetype
import base64
import binascii
import time
import base64
import hmac
from MD5 import get_token
'''
def main():
    kind = filetype.guess('C:\\Users\\Administrator\\Downloads\\channelsfc (3)')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()
'''#区分文件类型
a=base64.b64decode(b'Secw8G2xbkfLXIMVPmoVaiAu2BUimjubGrjmHo1cQkQ2rSOqmZd3ltthYYbQFX5zydMheqwyx57/dK/hI5MBFw=="')
print(a)
#string=str(a,'utf-8')
#print(string)

b=type(a)
print(b)
#c=a.decode('ascii')
#print(c)
c=binascii.b2a_hex(a)
print(c)
d=c.decode('ascii')
print(d)
print(len('6482f52d0cad8fd6fb9b486b6b913bae33c7821c0bbce9af42042d0d3cfddb17'))
def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")
n=time.time()
    #print(n)
millis = int(n * 1000)
print(millis)
s=str(millis)
i=get_token(s+'3600')
j=get_token('mtop.common.getTimestamp')
#i=i.lower()
print(i+j)