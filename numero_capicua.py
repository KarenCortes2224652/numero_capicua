# QUIZ: Leer un número de 5 dígitos y determinar si es capicúa.

#input
num = int(input("Ingrese un número entero de cinco dígitos:"))

#processing
if num <= 99999 and num>9999:
    A_digit = num//10000
    B_digit = (num//1000)-((A_digit*10))
    C_digit = (num//100)-((A_digit*100)+(B_digit*10))
    D_digit = (num//10)-((A_digit*1000)+(B_digit*100)+(C_digit*10))
    E_digit = num - ((A_digit*10000)+(B_digit*1000)+(C_digit*100)+(D_digit*10))

    invert_num = (E_digit*10000)+(D_digit*1000)+(C_digit*100)+(B_digit*10)+A_digit
    if num == invert_num:
        print(" Es capicúa")
    else:
        print("No es capicúa")
else:
    print("El número que digita no es de 5 dígitos: ")

#output
