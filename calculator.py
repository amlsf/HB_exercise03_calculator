import arithmetic

#Need to comment more!!
# Need to fix warnings to be more specific

def validateOperator (num1):
    operatorlist = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
    for i in range(len(operatorlist)):
        if num1 == operatorlist[i]:
           return "success"

calcswitch ="on"

operations_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
print "select command from the following:"
print operations_list

two_arg_ops = ["square", "cube"]
three_arg_ops = ["+", "-", "*", "/", "pow", "mod"]

while calcswitch == "on":

    useraction = raw_input("Enter command followed by operators, separated by space >")
    calc_list = useraction.split(" ")

    if validateOperator(calc_list[0]) != "success":
        print "invalid operator, please select from operator list: " + str(operations_list)
    else:
        if calc_list[0] == "q":
            print "Exiting the calculator"
            calcswitch = "off"

# fix the IN function to check for two argument operations
        elif calc_list[0] in two_arg_ops and len(calc_list) == 2 and calc_list[1].isdigit() == True:
            if calc_list[0] == "square":
                print arithmetic.square(int(calc_list[1]))
            elif calc_list[0] == "cube":
                print arithmetic.cube(int(calc_list[1]))
            else: 
                print "Sample correct input: '%s integer'" % calc_list[0]

# fix the IN function to check for three argument operations
        elif calc_list[0] in three_arg_ops and len(calc_list) == 3 and calc_list[1].isdigit() == True and calc_list[2].isdigit() == True:
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
                print "Sample correct input: '%s integer integer'" % calc_list[0]

        else: 
            print "I have no idea what you just typed"