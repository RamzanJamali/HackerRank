fname = input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    c[email] = c.get(email, 0) + 1

c = list(sorted(c.items(), key = lambda item:item[1]))
leng = c.__len__() - 1
bigg = c[leng]
print(bigg)

# bigc = None
# bige = None
# for word in c:
#     value = c[word]
#     if bigc is None or value > bigc:
#         bigw = word
#         bigc = value

# print(bigw, bigc)
