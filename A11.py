#Find numbers in a file and sum all of those number
#file 1: regex_sum_42.txt
#file 2: regex_sum_24925

#setup for the file
import re
handle = open('regex_sum_42.txt')
lst = []
intlst = []

#Go through the text and put all numbers into a list
for line in handle:
    tmp = re.findall('[0-9]+', line)
    if tmp == []:
        continue
    else:
        lst.append(tmp)

#convert a list of strings into a list of integers so they can be summed

y = len(lst)
x = 0

while (x < y):
    tmp1 = lst(x)
    tmp = int(tmp1)
    print(tmp)
    numlst.append(tmp)
    x =+ 1
    
print(sum(intlst))
