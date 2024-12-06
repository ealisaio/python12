# x = 0
# while(x <= 10):
#     x += 1
#     if x == 3:
#         continue
#     print(x)

# pass example 
# def fun():
#     pass
# fun() 

# for loop

# list1 = [1,2,3,4,5]
# for i in list1:
#     print(i)

# total_ticket = 5
# print("welcome to the movie ticketing system")
# for ticket_number in range(1,total_ticket):
#     print(f"processing ticket {ticket_number}")
#     name = input("enter your name")
#     movie = input("enter your movie")
#     print(f"ticket booked for {name} to watch {movie} movie")

num = int(input("enter a number:"))
for x in range(1,num+1):
    if (x%2 == 0):
       print(x,end=' ')   

even_number = []
for n in range(1, num+1):
    if n%2 == 0:
        even_number .append(n)
print(even_number)               