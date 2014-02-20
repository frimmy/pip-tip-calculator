from optparse import OptionParser #import the OptionParser object from this modulefinder

parser = OptionParser()
parser.add_option("-f", "--first", 
	dest="first_arg", help="the first argument",
	default="something")

parser.add_option("-s", "--second",
	dest="second_arg", help="the second argument",
	default=234, type=int)

(options, args) = parser.parse_args()

if not (options.first_arg and options.second_arg):
	parse.error("You need to supply an argument for -s")
	# if you want to require one or more of your arguments, and the if statement


print "The first argument is '{}'".format(options.first_arg)
print "The second argument is '{}'".format(options.second_arg)