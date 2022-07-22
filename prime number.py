num=int(input("enter the number"))
if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0 and num%11!=0:
    print(num," prime number")
else:
    print(num,"not prime number")