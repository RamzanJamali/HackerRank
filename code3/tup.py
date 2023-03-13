name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di= dict()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        line = line.split()
        new = line[5]
        time = new.split(':')
        hour = time[0]
        di[hour]= di.get(hour, 0) + 1
for k,v in sorted(di.items()):
    print(k,v)
    
