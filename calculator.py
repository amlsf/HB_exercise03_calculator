import arithmetic

calcswitch ="on"

operations_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
print "select command from the following:"
print operations_list

while calcswitch == "on":

    useraction = raw_input("Enter command followed by operators, separated by space >")
    calc_list = useraction.split(" ")

    if calc_list[0] == "q":
        print "Exiting the calculator"
        calcswitch = "off"

    elif len(calc_list) == 2 and calc_list[1].isdigit() == True:
        if calc_list[0] == "square":
            print arithmetic.square(int(calc_list[1]))
        elif calc_list[0] == "cube":
            print arithmetic.cube(int(calc_list[1]))
        else: 
            print "Invalid input"

    elif len(calc_list) == 3 and calc_list[1].isdigit() == True and calc_list[2].isdigit() == True:
        if calc_list[0] == "+":
            print arithmetic.add(int(calc_list[1]), int(calc_list[2]))
        elif calc_list[0] == "-":
            print arithmetic.subtract(int(calc_list[1]), int(calc_list[2]))
        elif calc_list[0] == "*":
            print arithmetic.multiply(int(calc_list[1]), int(calc_list[2]))
        elif calc_list[0] == "/":
            print arithmetic.divide(int(calc_list[1]), int(calc_list[2]))
        elif calc_list[0] == "power":
            print arithmetic.power(int(calc_list[1]), int(calc_list[2]))    
        elif calc_list[0] == "mod":
            print arithmetic.mod(int(calc_list[1]), int(calc_list[2]))
        else: 
            print "Invalid input"

    else: 
        print "Invalid input"