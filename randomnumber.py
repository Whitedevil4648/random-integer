def randbelow(n):
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)
        
def random(a, b):
    return a + randbelow(b - a + 1)


#use randint(lower limit,upper limit)
print(random(1,100))