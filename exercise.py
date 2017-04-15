print "Please select what conversion do you want:"
print "------------------------------------------"
print "1-Fahrenheit to Celcius"
print "2-Celcius to Fahrenheit"
print "------------------------------------------"
x = input()
if x == 1:
    from_temperature = "Fahrenheit"
    to_temperature = "Celcius"
elif x == 2:
    from_temperature = "Celcius"
    to_temperature = "Fahrenheit"
else:
    print "Insert a valid option!"
    exit()

print "Insert a temperature in %s to be converted in %s" % (from_temperature,to_temperature)
calc = input()

if from_temperature == "Fahrenheit":
    result = (calc - 32) / 1.8
elif from_temperature == "Celcius":
    result = (calc * 1.8) + 32


print "------------------------------------------"
print "Converting  %s %s" %  (calc,from_temperature)
print "The Result is: %s %s" %  (result,to_temperature)
print "------------------------------------------"
