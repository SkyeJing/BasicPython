# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r,arg2: %r" % (arg1, arg2)
# ok, that *agrs is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
# this one takes no arguments
def print_none():
	print "I got nothing."
	
def two_number_add(num1,num2):
	print "%s + %s = %s" % (num1, num2, num1+num2)

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
two_number_add(5,7)