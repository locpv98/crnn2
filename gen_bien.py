import random
import string
save_path = './trdg/valid.txt'

def rand_int(n):
    letters = string.digits
    r =  str(''.join(random.choice(letters) for i in range(n)))
    return r

character = string.ascii_uppercase
f = open(save_path, "w")
for i in range(2000):
    res = str(random.randint(11, 99))+str(random.choice(character))+'-'+rand_int(3)+'.'+rand_int(2)+'\n'
    # res = str(random.randint(11, 99))
    f.write(res)
