
#Write a program to look for the lines of the form:

#New Revision: 39772

#Extract the numbers from each lines using the regular expression and the
#findall() method. Compute the average of the numbers and print out the
#average as an integer.



import re
handle = open(input('Enter file name: '))
numList = list()
for line in handle:
     line = line.rstrip()
     strNum = re.findall('^New Revision: ([0-9.]+)',line)
     #if len(strNum)>0:
        # print(strNum)
     numList.append(strNum)
print(numList)
