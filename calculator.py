print("WELCOME TO BASIC CALCULATOR")
while True:
    A=int(input("ENTER FIRST OPERAND:"))
    B=int(input("ENTER SECOND OPERAND:"))
    print("[press \"A\" to add","\n","press \"B\" to subtract","\n",
    "press \"C\" to multiply","\n","press \"D\" to divide]")
    C=input("ENTER YOUR CHOISE:")
    if C=='A' or C=='a':
        print("ANSWER:",A+B)
    elif C=='B' or C=='b':
        print("ANSWER:",A-B)
    elif C=='C' or C=='c':
        print("ANSWER:",A*B)
    elif C=='D' or C=='d':
        print("ANSWER:",A/B)
    else:
        print("invalid selection")



