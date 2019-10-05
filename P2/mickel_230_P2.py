#------------------------------------------------------------------------------
# Name: Nathaniel Mickel
# Project 2
# Due Date: 22/9/2019
# -----------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# -----------------------------------------------------------------------------
# Refernces: Project 2 Guidelines
# -----------------------------------------------------------------------------
# Comments: N/A
# -----------------------------------------------------------------------------
# NOTE: width of the source code should be <= 80 characters readable on-screen.
# 23456789012345678901234567890123456789012345678901234567890123456789012345678
# 		10		  20		30		  40		50		  60		70		 80
# -----------------------------------------------------------------------------
def blood_pressure(systolic, diastolic):
	mean_pressure = (systolic + (2*diastolic))/3
	if systolic < 120 and diastolic < 80:
		risk_value = 1.0
		return round(risk_value*mean_pressure, 2)
	elif systolic in range(120, 130) and diastolic < 80:
		risk_value = 1.1
		return round(risk_value*mean_pressure, 2)
	elif systolic in range(130, 140) or diastolic in range(80, 90):
		risk_value = 1.2
		return round(risk_value*mean_pressure, 2)
	elif systolic >=140 or diastolic >= 90:
		risk_value = 1.3
		return round(risk_value*mean_pressure, 2)
	elif systolic > 180 or diastolic > 120:
		risk_value = 1.4
		return round(risk_value*mean_pressure, 2)
def standard_BMI(weight,height,ISU):
	if ISU == True:
		kg = weight/35
		m = height*0.025
		return round(kg/m**2, 2)
	if ISU == False:
		kg = weight
		m = height
		return round(kg/m**2, 2)
def BMI_chart(weight,height,age,gender):
	ISU = True
	BMI = standard_BMI(weight,height,ISU)
	if age >= 18:
		if 0 <= BMI < 18.5:
			return 'underweight'
		elif 18.5 <= BMI <= 25:
			return 'normal'
		elif 25 <= BMI <= 30:
			return 'overweight'
		elif 30 < BMI:
			return 'obese'
		elif age < 18:
			if gender == 'male':
				if 0 <= BMI <= 14:
					return 'underweight'
				elif 14 <= BMI <= 19:
					return 'normal'
				elif 19 <= BMI <= 22:
					return 'overweight'
				elif 22 < BMI:
					return 'obese'
			elif gender == 'female':
				if 0 <= BMI <= 15:
					return 'underweight'
				elif 15 <= BMI <= 20:
					return 'normal'
				elif 20 <= BMI <= 23:
					return 'overweight'
				elif BMI > 23:
					return 'obese'
def HCT(red_cells,total_cells,age,gender):
	if gender == "male":
		red_cells_percentage = (red_cells/total_cells)*100
		if age >= 18:
			if red_cells_percentage in range(40.7, 50.4):
				return 'True'
			else:
				return 'False'
	if gender == 'female':
		if age >= 18:
			if red_cells_percentage in range(36.1, 44.4):
				return 'True'
			else:
				return 'False'
	if age < 18:
		if red_cells_percentage in range(36, 41):
			return 'True'
		else:
			return 'False'
def LDL(total, HDL, trig, age, gender):
	if gender == 'male':
		if age >= 18:
			if trig in range(11.3, 43.6):
				LDL = total - HDL - (0*trig)
				if LDL < 120:
					return '0'
				elif LDL in range(120, 140):
					return '1'
				elif LDL in range(140, 160):
					return '2'
				elif LDL in range(160, 180):
					return '3'
				elif LDL in range(180, 200):
					return '4'
				elif LDL in range(200, 220):
					return '5'
		if age < 18:
			if trig in range(11.3, 43.6):
				LDL = total - HDL - (0*trig)
				if LDL < 100:
					return '0'
				if LDL in range(100, 115):
					return '1'
				if LDL in range(115, 130):
					return '2'
				if LDL in range(130, 145):
					return '3'
				if LDL in range(145, 150):
					return '4'
				if LDL in range(150, 165):
					return '5'
	if gender == 'female':
		if age >= 18:
			if trig in range(11.3, 43.6):
				LDL = total - HDL - (0*trig)
				if LDL < 120:
					return '0'
				elif LDL in range(120, 140):
					return '1'
				elif LDL in range(140, 160):
					return '2'
				elif LDL in range(160, 180):
					return '3'
				elif LDL in range(180, 200):
					return '4'
				elif LDL in range(200, 220):
					return '5'
		if age < 18:
			if trig in range(11.3, 43.6):
				LDL = total - HDL - (0*trig)
				if LDL < 100:
					return '0'
				if LDL in range(100, 115):
					return '1'
				if LDL in range(115, 130):
					return '2'
				if LDL in range(130, 145):
					return '3'
				if LDL in range(145, 150):
					return '4'
				if LDL in range(150, 165):
					return '5'