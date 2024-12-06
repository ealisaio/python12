print("wlcome to the noteboook")
print("1.Add the npte")
print("2.to read a note")
print("3.to delete the note")
choice=int(input("enter your choices:"))
if choice==1:
    note=input("enter the note:")
    with open("file.txt",'w') as f:
        f.write(note)
        f.close()
elif choice==2:
    try:
        with open("file.txt",'r') as f:
            read_text=f.read()
            print(read_text)
            f.close()
    except Exception as e:
        print("you dont have the rfequired file")
else:
    print("sorry the choice is yours")

print("thank you")