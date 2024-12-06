# def college_info(cname,address,contact):#here name address and contact are called parameter
    # print(f"My college name is {cname} address is {address} and contact is {contact}")
# college_info("lumbini","rupandehi",9845672300) #here "lumbini","rupandehi"and 9845672300 are called arguments   
# college_info("Tillotama","Jaikuti",9845983445)



#ARBITARY ARGUMENTS
# def college_info(*args):
#     print(f"college name is:{args[0]} and address is {args[1]}")
# college_info("lumbini","Rupandehi")
# college_info("lumbini","Butawal")

#keyword arguments

# def college_info(**kargs):
#     print("college name is", kargs["name"],"and address is" kargs["address"])
# college_info(name="Lumbini",address="Rupandehi")


# default_funtion.py
# def car_brand(brand = "Toyota"):
#     print(brand)
# car_brand()
# car_brand("BMW")
# car_brand(brand = "Tata")

# def car_brand(carlist):
#     for i in carlist:
#         print(i)
# carlist = ["Toyota","BMW","Tata"]
# car_brand(carlist)


# return_function
# def add(a,b):
#     sum = a+b
#     return sum

# c = add(4,9)
# print(c)

"""boolean function"""
heart_rate = True
def blood_circulation(heart_measure):
    if heart_measure > 100:
        heart_rate = False
        print(heart_rate)
        print("you have high heart rate",heart_measure)
    elif heart_measure < 60:
        heart_rate = False
        print(heart_rate)
        print("you have low heart rate",heart_measure)
    else:
        heart_rate = True
        print(heart_rate)
        print("you are ok!")
heart_measure = int(input("enter your heart rate:"))
blood_circulation(heart_measure)            

