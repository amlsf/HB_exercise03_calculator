import arithmetic
print "Welcome to our Calculator Program"
operations_list = ["+", "-", "*", "/", "square", "pow", "mod", "q"]
print "select command from the following:"
print operations_list

useraction = raw_input("Enter command followed by operators, separated by space >")
print "Your command is %s" % useraction

calc_list = useraction.split(" ")
print calc_list

if calc_list[0] == "power":
    arithmetic.power(calc_list[1], calc_list[2])    




#check for "pow" in first string
#check for integer in second string
#check for inte
