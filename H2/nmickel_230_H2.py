
def chemical_strength(pH):
	if pH >= float(0) and pH <= float(14):
		if pH < 7:
			if pH <= 1:
				one = 'very strong acid'
				return one
			elif pH > 1 and pH < 4:
				two = 'strong acid'
				return two
			elif pH == 4:
				pa = 'plain acid'
				return pa
			elif pH > 4 and pH < 6:
				three = 'weak acid'
				return three
			elif pH >= 6:
				four = 'very weak acid'
				return four
		elif pH == 7:
			five = 'neutral'
			return five
		elif pH > 7:
			if pH <= 8:
				six = 'very weak base'
				return six
			elif pH > 8 and pH < 10:
				seven = 'weak base'
				return seven
			elif pH == 10:
				eight = 'plain base'
				return eight
			elif pH > 10 and pH < 13:
				nine ='strong base'
				return nine
			elif pH >= 13:
				ten ='very strong base'
				return ten
	else:
		bad = "bad measurement"
		return bad
def light_status(s1, s2):
	if s1 & s2 in range(0,101):
		if s1 >= 50:
			return "on"
		if s2 >= 50:
			return "on"
		elif s2 >= s1:
	 		return "on"
		elif s2 <= s1:
	 		return "off"
		elif s1 - s2 == (s1+s2)/2:
	  		return "on"
		elif s1 - s2 != (s1+s2)/2:
	  		return "off"
	else:
 		return "invalid switch"