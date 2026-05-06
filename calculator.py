def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
print("please select operation-\n" "1.Add\n""2.subtract\n" "3.multiply\n" "4.division\n")
select=(int(input("select operation(1-4):"))
n1=int(input("enter first number:"))
n2=int(input("enter second number:))
if select==1:
             print(n1,"+",n2,"="add(n1,n2))
elif select==2:
             print(n1,"-",n2,"="sub(n1,n2))
elif select==3:
             print(n1,"*",n2"="mul(n1,n2))
elif  select==4:
             print(n1,"/",n2"=",div(n1,n2))
else :
             print("invalid input")
             
