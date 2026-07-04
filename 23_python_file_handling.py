#file handling
# write()

'''a= open("Veerendra.txt", "w")
a.write("codegnan IT solutions")
a.close()'''


'''a= open("Veerendra.txt", "w")
a.write("python")
a.close()'''

'''a= open("Veerendra.txt", "a")
a.write("\tpython")
a.close()'''

'''a = input()
b = open("Veerendra.txt", "a")
b.write(a)
b.close()'''

#read()

'''a = open("Veerendra.txt","w")
a.write(input("data"))
a.close()'''

'''a = open("Veerendra.txt")
print(a.read())#it will display entrie content
print(a.readline())#it will display first line
print(a.readines())#it will display with \n(when ever there is a second line
print(a.read(9))#it will display no of charcters(if we gave index number then it will print upto that number index)
#we cannot use the multiple prints in a singlecode'''

#writelines()-> it makes every object side by side
'''a = ["nani","bobby","chinni"]
b = open("bobby.txt","w")
b.writelines(a)
b.close'''

'''a = ["nani","bobby","chinni"]
b = open("Veerendra.txt","w")
b.writelines("\n".join(a))
b.close()'''

a = open(input(" File Name: ))
print(a.read())


