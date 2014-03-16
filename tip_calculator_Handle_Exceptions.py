from tip_calculator_as_functions import calculate_rate, calculate_meal_costs
import sys

def main():
	# calculate_meal_costs(argv[])
	base_info = {}
	try:
		base_info = dict(base_meal=float(sys.argv[1]), base_tax=sys.argv[2],
					base_tip=sys.argv[3])
	except ValueError:
		print "Sorry, you must supply numbers for all imput parameters to this script. Try again."
		base_info['base_meal'] = float(raw_input("Enter base meal cost: ")) 
		base_info['base_tax'] = float(raw_input("Enter base tax percentage as a decimal: "))
		base_info['base_tip'] = float(raw_input("Enter base tip percentage as a decimal: "))
	
		
	meal_info = calculate_meal_costs(base_info['base_meal'], base_info['base_tax'],
									base_info['base_tip'])

	print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
	print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
	print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
    									int(100*meal_info['tip_rate']),
    									meal_info['tax_value'])
	print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])

if __name__ == '__main__':
	main()

