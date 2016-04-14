"""
http://stackoverflow.com/questions/36199100/python-1-to-100-using-while-statement-in-10-rows
"""
"""
1 to 100 using While statement in 10 rows
"""
def solution_01(n):
	index = 0
	row = ''
	while index <=n:
		index+=1
		row += ' '+str(index) 
		if index%10 == 0:
			print row
			row = ''

solution_01(100)
