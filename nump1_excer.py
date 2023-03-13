import numpy as np

list1 = [1, 2, 3, 4.4, 5.5]
print(list1, "\n")
nlist1 = np.array(list1)
print(nlist1, "\n")

list2 = np.linspace(-2.0, 2.0, 21)
print(list2, "\n")

list3 = np.linspace(0.5, 1.5, 11)
print(list3, "\n")

str1 = "Never google your symptoms"
char1 = np.array(str1, dtype="c")
print(repr(char1), "\n")
