#Program to get input between 0.0 and 1.0 If the score is out of range print an error message. Or else print Grading table depending on score input

grade = raw_input('Enter score: ')
try:
		grade = float(grade)
		if grade > 0 and grade < 1.0:
			if grade >= 0.9:
				print ('A')
			elif grade >= 0.8:
				print ('B')
			elif grade >= 0.7:
				print ('C')
			elif grade >= 0.6:
				print ('D')
			elif grade < 0.6:
				print ('F')	
		else:
			print ('Bad score')
except:
	print ('Bad score')