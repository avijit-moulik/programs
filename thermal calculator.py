def c_to_f():
    print(float(c * (9/5)+32))
    
def f_to_c():
    print(float((f-32) *(5/9)))
    
def k_to_c():
    print(float(k - 273.15))
def c_to_k():
    print(float(c + 273.15))
def k_to_f():
    print(float((k-273.15)* (9/5)+32))
def f_to_k():
    print(float((f-32) *(5/9)+273.15))

print("Thermal calculator\n choic scale\n1. celcius to farenheit\n2. farenheit to celcius\n3. farenheit to kelvin\n4. clecius to kelvin\n5. kelvin to celcius\n6. kelvin to farenheit")

print ("\nEnter Choose in intiger : ")
choice_input = int(input())

if choice_input == 1:
    print("Enter the value of celcius : \n")
    c = float(input())
    c_to_f()
elif choice_input == 2:
    print("Enter the value of farenheit : \n")
    f = float(input())
    f_to_c()
elif choice_input == 3:
    print("Enter the value of farenheit : \n")
    f = float(input())
    f_to_k()
elif choice_input == 4:
    print("Enter the value of celcius : \n")
    c = float(input())
    c_to_k()
elif choice_input == 5:
    print("Enter the value of kelvin : \n")

    k = float(input())
    k_to_c()
elif choice_input == 6:
    print("Enter the value of kelvin : \n")
    k = float(input())
    k_to_f()

else:
    print("Wrong input")







