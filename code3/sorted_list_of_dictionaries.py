dictionaries = [ {'number':7, 'eight':8, 'nine':9},
                {'name':1, 'number':2, 'three':3}, 
                {'noun':4, 'five':5, 'number':6}]

list1 = sorted(dictionaries, key=lambda x: x['number'])

print(list1)

