import sys as s 

meal = float(s.argv[1])
tax = float(s.argv[2])
tip = float(s.argv[3])

tax_value = meal*tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax*tip  #raw val of tip given meal_with_tax

total = tip_value + meal_with_tax #cost of meal_with_tax + tip_value

print "Base cost of meal: ${:.2f}".format(meal)  
print "Dollar value of tax on the meal based on a tax rate of {:.2%}: ${:.2f}".format(tax, tax_value)
print "Dollar value given you tip {:.2%}: ${:.2f}".format(tip, tip_value)
print "Grand total for the meal(including tax & tip): ${:.2f}".format(total)