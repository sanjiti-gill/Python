count=0
total=0

while True:
    num=int(input("enter a number:"))
    if (num<0):
        break
    elif (num%2!=0):
        count=count+1
        total=total+num
    else:
        continue

if count==0:
    print("no odd no was entered")

else:
    average=total/count
    print("count of odd nos", count)
    print("sum of odd nos", total)
    print("average of odd nos", average)
