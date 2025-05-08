def calculator():
    print("**************SIMPLE CALCULATOR**************************")
    
    num1=int(input("Enter number1:"))
    num2=int(input("Enter number2:"))
    op=input("Choose operator(+,-,*,/)")
    
    if op=='+':
        print("Result",num1+num2)
    elif op=='-':
        print("Result",num1-num2)
    elif op=='*':
        print("Result",num1*num2)
    elif op=='/':
        if num2 == 0:
            print("Zero Division Error")
        else:
            print("Result",num1/num2)
    else:
        print("Invalid input,try again")

calculator()