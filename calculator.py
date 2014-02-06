import arithmetic

# TO DO Need to fix integer validation isdigit() so that it works with negative numbers
# QUESTION how check for real #'s and floats and negatives?

operations_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
two_arg_ops = ["square", "cube"]
three_arg_ops = ["+", "-", "*", "/", "pow", "mod"]

calcswitch ="on"

# creates function to validate user input includes valid operator
def validateOperator (num1):
    for i in range(len(operations_list)):
        if num1 == operations_list[i]:
           return "success"

print "select command from the following:"
print operations_list

# variable for while loop break
while calcswitch == "on":

    useraction = raw_input("Enter command followed by operators, separated by space >")
    calc_list = useraction.split(" ")

# validate valid operator is input by user
    if validateOperator(calc_list[0]) != "success":
        print "Invalid operator, please select from operator list: " + str(operations_list)

    else:
# allows user to enter "q" to quit
        if calc_list[0] == "q":
            print "Exiting the calculator"
            calcswitch = "off"

# checks for square and cube operators, then ensure 2 arguments and 2nd is integer
        elif calc_list[0] in two_arg_ops: 
            if len(calc_list) == 2 and calc_list[1].isdigit() == True:
                if calc_list[0] == "square":
                    print arithmetic.square(int(calc_list[1]))
                elif calc_list[0] == "cube":
                    print arithmetic.cube(int(calc_list[1]))
            else: 
                print "Sample correct input: '%s integer'" % calc_list[0]

# checks for other operators, then ensure 3 arguments and last 2 are integers
        elif calc_list[0] in three_arg_ops:
            if len(calc_list) == 3 and calc_list[1].isdigit() == True and calc_list[2].isdigit() == True:
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

# probably won't need this
        else: 
            print "I have no idea what you just typed"