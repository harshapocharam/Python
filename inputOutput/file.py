# jabber =open("C:/Zspark/Python/original.txt",'r')
# for line in jabber:
#     print(line)

# jabber.close()

# with open("original.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line,end='')

# with open("original.txt", 'r') as jabber:
#     lines = jabber.readline()               reads every single line 
# print(lines)

# with open("original.txt", 'r') as jabber:
#      lines = jabber.readlines()                  
#     # readlines() reads line as a string 
# print(lines)

with open("original.txt", 'r') as jabber:
     lines = jabber.read()                  
    # readlines() reads line as a string 
print(lines)