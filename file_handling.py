"""open() function is used for file handling
read
create
write
delete
"""
"""text = input("enter a text:")
f = open("read.txt",'a')
f.write(text)
f.close()"""

f = open("read.txt",'r')
content = f.read()
print(content)
f.close()