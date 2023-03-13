name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        lin = line.split()
        di[lin[1]] = di.get(lin[1], 0)+ 1
    
bigword = 0
bigcount = 0
for email in di:
    if bigcount < di[email]:
        bigword = email
        bigcount = di[email]

print(bigword, bigcount)
