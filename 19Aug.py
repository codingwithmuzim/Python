// Write a program to gaussing a number with the help of while loop in 3 attempts if 3 attempts completed than you are game over or loss?
import random
count=1
while True:
    if count==1:
        gauss_no = int(input("gauss_no " + str(count) + " time "))
        k = random.randint(0,2)
        if(gauss_no==k):
            print("you are win with count " + str(count))
        else:
            print("try again")
        count=count+1
    elif count==2:
        gauss_no = int(input("gauss_no " + str(count) + " time "))
        k = random.randint(0, 2)
        if(gauss_no==k):
            print("you are win with count " + str(count))
        else:
            print("try again")
        count=count+1
    elif count==3:
        gauss_no = int(input("gauss_no " + str(count) + " time "))
        k = random.randint(0, 2)
        if(gauss_no==k):
            print("you are win with count " + str(count))
        else:
            count=count+1
    else:
        print(" you are lossed")
        break
