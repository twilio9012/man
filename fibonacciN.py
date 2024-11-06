n=int(input("Enter the number: "))
print("Fibonachi Series")
n1=0
n2=1
n3=n1+n2
print(n1,n2,end=" ")
for i in range(n-2):
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2



    



# def fibo(n):
#     if(n<=1):
#         return n
#     else:
#         return(fibo(n-1)+fibo(n-2))
    
# n=int(input("Enter the number: "))
# print("Fibonachi Series")
# for i in range(n):
#     print(fibo(i))