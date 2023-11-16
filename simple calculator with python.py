def plus (x,y):
    return x+y
def minus(x,y):
    return x-y
def gun(x,y):
    return (x*y)
def division(x,y):
    return x/y

print('Calculetro')
print('1.plus')
print('2.minus')
print('3.Gun')
print('4.division')

while True:
    choice = input("Enter your choice:")
    if choice in ('1','2','3','4'):
        try:
            num1 = float (input("Enter youtr 1st number:"))
            num2 = float(input ("Enter your 2nd number:"))
        except ValueError:
            print("Invild choice")
            continue
        if choice == '1':
            print(num1,"+",num2,"=",plus(num1,num2))
        elif choice == '2':
            print(num1,"-",num2, "=", minus(num1,num2)) 
        elif choice == '3':
            print(num1, "*", num2 , "=", gun(num1, num2) ) 
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1,num2))
                   
        next_calculation = input("new calculation? (Yes/no)")
        

    
