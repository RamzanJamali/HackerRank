name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    #line = line.rstrip()
    if line not startswith('From'):continue
    new = line.split()
    for w in new:
        di[w] = di.get(w, 0)+ 1

print(di)
