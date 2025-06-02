def discreteIntegrate(coeff_list):
	''' reverse of forward difference see README'''
	coeff = coeff_list[:] # make a copy that will be changed in-place
	dim = len(coeff)
	for i in range(dim - 1, -1, -1):
		hgterm = coeff[i] # binoimial term factors count down/up on numerator, and on denominator
		#print("hgterm =", hgterm, end=" ")
		coeff[i] = coeff[i]//(i + 1)
		for j in range(i - 1, -1, -1):
			#print("coeff[", j, "] = ", coeff[j], end = " ")
			hgterm = hgterm*(j + 1)//(1 + i - j) # starts at 2 for j = i - 1, counts down by j, 2 = k - j for j = i - 1, k = 2 + i - 1
			coeff[j] = coeff[j] - hgterm
			#print(", hgterm =", hgterm, " new coeff[", j, "]=", coeff[j], end=" -- ")
		#print(" ")
	return [0] + coeff # the first term is the constant term thus is anything really, here return 0 for that

def polyFromShift(coeff_list, s):
	 ''' uses in-place synthetic division to get the new poly coefficients 
			 if self is y and f is the shift then y(x) = f(x - s) and f(x) = y(x + s)
	 '''
	 coeff = coeff_list[:] # if self.dim truncates this doesn't care...
	 dim = len(coeff)
	 for i in range(dim): # need to do synthetic division from the high coefficient first
		 c = 0
		 for j in range(dim - 1, i - 1, -1):
			 c = c*s + coeff[j]
			 coeff[j] = c # the result is the last term of the diminishing length, basically a pascal's triangle recurrence
	 return coeff
