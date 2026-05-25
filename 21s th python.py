#random module
#to generate random number in python, randint function is used this function is defined in randome module
#python defines a set of functions that are used to generate or manupilate random numbers through the random module
#random module
'''import random
a = random.sample(range(10,40),5)
print(a)'''

#randint()
'''import random
a = random.randint(30,50)
print(a)'''

#choice()
'''import random
a = [10,20,30,40,50,60]
b = random.choice(a)
print(b)'''
# my task
'''import random
a = ["name","veerendra","idno","date"]
b = random.choice(a)
print(b)'''

#task
'''import random
while True:
    input("enter the roll of dice")
    a = random.randint(1,6)
    print(a)
    option = input("roll again?(y/n)")
    if option=="y":
        continue
    if option=="n":
        break
    else:
        print("invalid option")'''
#calendar
'''import calendar
year = 2026
month = 5
print(calendar.month(year,month)'''

'''import calendar
year = 2026
print(calendar.calendar(year))'''

'''import calendar
year = int(input("Year:"))
month = int(input("Month:"))
print(calendar.month(year, month))'''


#date and time
'''from datetime import date
a = date.today()
print(a)'''

'''while True: 
    import datetime
    a = datetime.datetime.now()
    print(a)'''

'''import time
a= time.time()
print(a)#epoch time
b =time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}/{b.tm_mon}/{b.tm_year}")'''


'''import time
a= time.time()
print(a)
b =time.localtime(a)
print(b)
print(f"today date is {b.tm_yday}/{b.tm_wday}/{b.tm_sec}")'''


'''import random
import time
for i in range(1,11):
    num = random.randint(1,100)
    print(num)
    time.sleep(2)'''

'''import calendar
import random
import time
count = 0
while count<10:
    year = random.randint(1900, 2050)
    if calendar.isleap(year):
        print(year, "is a leap year")
        count += 1
        time.sleep(2)'''

    
        




        
    
        
