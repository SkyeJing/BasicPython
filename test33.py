def num_list(max,step=1):
	i = 0
	numbers = []
	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += step
		print "Numbers now :",numbers
		print "At the bottom i is %d" % i
		
	print "The numbers:"

	for num in numbers:
		print num

num_list(10,5)