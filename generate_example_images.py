from avatar_generator import Avatar


def randsize(i):
    return pow(1003, i, 128) + 32
def randname(i):
    return chr(ord('A') + i)

for i in range(16):
    av, = Avatar.generate(randsize(i), randname(i), 'PNG'),
    with open('test_%s.png' % i, 'wb') as outf:
        outf.write(av)
