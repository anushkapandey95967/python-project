
def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer)+"\n")

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer)+"\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer)+"\n")

def div(a, b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer)+"\n")

while True:
    print("A.Addition")
    print("B.Substraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.Exit")

    choice=input("input your choice:")
    if choice== "a" or choice == "A":
      print("Addition")
      a=int(input("input first number:"))
      b=int(input("input second number:"))
      print(a,b)
      add(a ,b)
    elif choice =="b" or choice =="B":
       print("Substraction")
       a=int(input("input first number:"))  
       b=int(input("input second number:"))
       print(a,b)
       sub(a,b)
    elif choice =="c" or choice =="C":
       print("Multiplying")
       a=int(input("input first number:"))  
       b=int(input("input second number:"))
       print(a,b)
       mul(a,b)    
    elif choice =="d" or choice =="D":
       print("Division")
       a=int(input("input first number:"))  
       b=int(input("input second number:"))
       print(a,b)
       div(a,b)
    elif choice =="e" or choice =="E":
      print("program ended")
      quit()
    else:
       print("Invalid choice")
    

