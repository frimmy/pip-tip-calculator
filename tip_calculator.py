meal = 20
tax = .12
tip = .20 

tax_value = meal*tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax*tip  #raw val of tip given meal_with_tax

total = tip_value + meal_with_tax #cost of meal_with_tax + tip_value

print "Base cost of meal: ${:.2f}".format(meal)  
print "Dollar value of tax on the meal: ${:.2f}".format(tax_value)
print "Dollar value given of tip(given tip %): ${:.2f}".format(tip_value)
print "Grand total for the meal(including tax & tip): ${:.2f}".format(total)