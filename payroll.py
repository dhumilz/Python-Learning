hours = raw_input('Enter Hours:')
try:
	hours = float(hours)
	rate =  raw_input ('Enter Rate:')
	try:
		rate = float(rate)
		overtime = 0
		if hours > 40 :
			overtime = hours-40
			hours = 40
			pay = (hours * rate)
		else:
			pay = (hours * rate) + (overtime * rate * 1.5)
		print 'Pay:', pay 
	except:
		print ' Please enter a number'
	
except:
	print ' Please enter a number'


	
	
	
