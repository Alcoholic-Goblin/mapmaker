import csv
import os
width=int(input("Enter Width:"))
height=int(input("Enter Height:"))

print(width)
print(height)
height+=2
width+=1
lst=""
if os.path.isfile("seed.csv"):
    os.remove("seed.csv")
for i in range(height):
    for j in range(width):
          if j < width:
              lst=lst+"0,"
          if j == width-1:
              lst=lst+"0"
    print(lst)
    with open("seed.csv", "a") as myfile:
        myfile.write(lst)
    lst=""
    print("row ",i)
    with open("seed.csv", "a") as myfile:
        myfile.write("\n")
print(lst)


        
