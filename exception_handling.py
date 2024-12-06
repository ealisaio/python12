# try:
#     code to check
# except:
#     handling an exception
# finally:
#     running the code to be run after exception checking   
  
a = 1 
b = 0
try:
    print("resource open")
    print(a/b)
    print("resource closed")

except Exception as e:
    print(e)
    print("you cannot divide a number by zero")

finally:
    print("this is run after try catch block")        