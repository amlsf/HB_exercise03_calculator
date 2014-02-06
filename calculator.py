import arithmetic
operations_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
print "select command from the following:"
print operations_list

useraction = raw_input("Enter command followed by operators, separated by space >")

calc_list = useraction.split(" ")

if calc_list[0] == "+":
    print arithmetic.add(int(calc_list[1]), int(calc_list[2]))
elif calc_list[0] == "-":
    print arithmetic.subtract(int(calc_list[1]), int(calc_list[2]))
elif calc_list[0] == "*":
    print arithmetic.multiply(int(calc_list[1]), int(calc_list[2]))
elif calc_list[0] == "/":
    print arithmetic.divide(int(calc_list[1]), int(calc_list[2]))
elif calc_list[0] == "square":
    print arithmetic.square(int(calc_list[1]))
elif calc_list[0] == "cube":
    print arithmetic.cube(int(calc_list[1]))
elif calc_list[0] == "power":
    print arithmetic.power(int(calc_list[1]), int(calc_list[2]))    
elif calc_list[0] == "mod":
    print arithmetic.mod(int(calc_list[1]), int(calc_list[2]))
elif calc_list[0] == "q":
    print "Exiting the calculator"
else: 
    print "Incorrect input"