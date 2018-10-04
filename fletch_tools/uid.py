import random
import string

def generate_uid(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def gen_next_hex(key_list=[]):
    if not key_list:
        keylist = ['000']
    """take a list of hex values and return the next one."""
    l = []
    for key in key_list:
        l.append(int('0x' + key, 16))
    l.sort()
    try:
        max = l[-1]
    except:
        max = 000
    new_key = hex(max+1)[2:].zfill(3)
    return new_key

if __name__ == '__main__':
    key_list = []
    for i in range(124):
        key_list.append(str(hex(i))[2:].zfill(3))
    print(key_list)
    print(gen_next_hex(key_list))
