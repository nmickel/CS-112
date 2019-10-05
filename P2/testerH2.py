# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time


############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["blood_pressure",
                  "standard_BMI",
                  "BMI_chart",
                  "HCT",
                  "LDL"
                  ]

# for method names in classes that will be tested
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 80

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
	
		
	############################################################################

	# blood_pressure tests - 15pts
	def test_blood_pressure_1  (self):self.assertEqual(blood_pressure(97, 75), 82.33)
	def test_blood_pressure_2  (self):self.assertEqual(blood_pressure(108, 80), 107.2)
	def test_blood_pressure_3  (self):self.assertEqual(blood_pressure(119, 90), 129.57)
	def test_blood_pressure_4  (self):self.assertEqual(blood_pressure(120, 79), 101.93)
	def test_blood_pressure_5  (self):self.assertEqual(blood_pressure(127, 80), 114.8)
	def test_blood_pressure_6  (self):self.assertEqual(blood_pressure(129, 79), 105.23)
	def test_blood_pressure_7  (self):self.assertEqual(blood_pressure(130, 62), 101.6)
	def test_blood_pressure_8  (self):self.assertEqual(blood_pressure(133, 89), 124.4)
	def test_blood_pressure_9  (self):self.assertEqual(blood_pressure(139, 90), 138.23)
	def test_blood_pressure_10  (self):self.assertEqual(blood_pressure(140, 80), 130)
	def test_blood_pressure_11  (self):self.assertEqual(blood_pressure(155, 89), 144.3)
	def test_blood_pressure_12  (self):self.assertEqual(blood_pressure(172, 120), 178.53)
	def test_blood_pressure_13  (self):self.assertEqual(blood_pressure(180, 121), 196.93)
	def test_blood_pressure_14  (self):self.assertEqual(blood_pressure(181, 89), 167.53)
	def test_blood_pressure_15  (self):self.assertEqual(blood_pressure(195, 131), 213.27)
     
	# standard_BMI tests - 10pts
	def test_standard_BMI_1  (self):self.assertEqual(standard_BMI(75, 1.76, True), 24.21)
	def test_standard_BMI_2  (self):self.assertEqual(standard_BMI(82, 1.99, True), 20.71)
	def test_standard_BMI_3  (self):self.assertEqual(standard_BMI(41, 1.37, True), 21.84)
	def test_standard_BMI_4  (self):self.assertEqual(standard_BMI(97, 1.68, True), 34.37)
	def test_standard_BMI_5  (self):self.assertEqual(standard_BMI(106, 2, True), 26.5)
	def test_standard_BMI_6  (self):self.assertEqual(standard_BMI(3500, 79, False), 25.64)
	def test_standard_BMI_7  (self):self.assertEqual(standard_BMI(701, 33, False), 29.43)
	def test_standard_BMI_8  (self):self.assertEqual(standard_BMI(1049, 41.1, False), 28.39)
	def test_standard_BMI_9  (self):self.assertEqual(standard_BMI(1647, 47.9, False), 32.82)
	def test_standard_BMI_10  (self):self.assertEqual(standard_BMI(4199, 90.33, False), 23.53)
     
	# BMI_chart tests - 20pts
	def test_BMI_chart_1  (self):self.assertEqual(BMI_chart(57, 1.7556, 18, 'female'), 'underweight')
	def test_BMI_chart_2  (self):self.assertEqual(BMI_chart(43, 1.525, 44, 'male'), 'underweight')
	def test_BMI_chart_3  (self):self.assertEqual(BMI_chart(51, 1.909, 17, 'male'), 'underweight')
	def test_BMI_chart_4  (self):self.assertEqual(BMI_chart(30, 1.4145, 11, 'female'), 'underweight')
	def test_BMI_chart_5  (self):self.assertEqual(BMI_chart(25, 1.2914, 6, 'female'), 'underweight')
	def test_BMI_chart_6  (self):self.assertEqual(BMI_chart(75, 1.732, 18, 'male'), 'normal')
	def test_BMI_chart_7  (self):self.assertEqual(BMI_chart(49, 1.6276, 76, 'female'), 'normal')
	def test_BMI_chart_8  (self):self.assertEqual(BMI_chart(18, 1.134, 3, 'male'), 'normal')
	def test_BMI_chart_9  (self):self.assertEqual(BMI_chart(32, 1.4602, 7, 'female'), 'normal')
	def test_BMI_chart_10  (self):self.assertEqual(BMI_chart(46, 1.556, 11, 'male'), 'normal')
	def test_BMI_chart_11  (self):self.assertEqual(BMI_chart(100, 1.9997, 83, 'male'), 'overweight')
	def test_BMI_chart_12  (self):self.assertEqual(BMI_chart(70, 1.5274, 18, 'female'), 'overweight')
	def test_BMI_chart_13  (self):self.assertEqual(BMI_chart(73, 1.9101, 17, 'female'), 'overweight')
	def test_BMI_chart_14  (self):self.assertEqual(BMI_chart(41, 1.335, 12, 'female'), 'overweight')
	def test_BMI_chart_15  (self):self.assertEqual(BMI_chart(28, 1.1281, 5, 'male'), 'overweight')
	def test_BMI_chart_16  (self):self.assertEqual(BMI_chart(70, 1.5273, 18, 'female'), 'obese')
	def test_BMI_chart_17  (self):self.assertEqual(BMI_chart(80, 1.6328, 19, 'male'), 'obese')
	def test_BMI_chart_18  (self):self.assertEqual(BMI_chart(93, 2.0106, 17, 'female'), 'obese')
	def test_BMI_chart_19  (self):self.assertEqual(BMI_chart(114, 2.2761, 16, 'male'), 'obese')
	def test_BMI_chart_20  (self):self.assertEqual(BMI_chart(107, 2.1566, 15, 'female'), 'obese')
     
	# HCT tests - 15pts
	def test_HCT_1  (self):self.assertEqual(HCT(18505386, 45467778, 18, 'male'), True)
	def test_HCT_2  (self):self.assertEqual(HCT(22869000, 45467778, 89, 'male'), True)
	def test_HCT_3  (self):self.assertEqual(HCT(626888, 1540267, 54, 'male'), False)
	def test_HCT_4  (self):self.assertEqual(HCT(774755, 1540267, 43, 'male'), False)
	def test_HCT_5  (self):self.assertEqual(HCT(123456, 999999, 31, 'male'), False)
	def test_HCT_6  (self):self.assertEqual(HCT(2741678682, 7594677789, 67, 'female'), True)
	def test_HCT_7  (self):self.assertEqual(HCT(3364442260, 7594677788, 51, 'female'), True)
	def test_HCT_8  (self):self.assertEqual(HCT(87906802, 243509147, 34, 'female'), False)
	def test_HCT_9  (self):self.assertEqual(HCT(107874553, 243509148, 19, 'female'), False)
	def test_HCT_10  (self):self.assertEqual(HCT(987654, 999999, 18, 'female'), False)
	def test_HCT_11  (self):self.assertEqual(HCT(3555556, 9876543, 17, 'female'), True)
	def test_HCT_12  (self):self.assertEqual(HCT(3950616, 9876542, 16, 'female'), True)
	def test_HCT_13  (self):self.assertEqual(HCT(2510284282, 6973011895, 12, 'male'), False)
	def test_HCT_14  (self):self.assertEqual(HCT(2789204759, 6973011896, 8, 'female'), False)
	def test_HCT_15  (self):self.assertEqual(HCT(789234, 999999, 5, 'male'), False)
     
	# LDL tests - 20pts
	def test_LDL_1  (self):self.assertEqual(LDL(170, 50, 11.3, 67, 'female'), 0)
	def test_LDL_2  (self):self.assertEqual(LDL(202, 62, 43.5, 23, 'male'), 1)
	def test_LDL_3  (self):self.assertEqual(LDL(199, 40, 11.2, 18, 'male'), 2)
	def test_LDL_4  (self):self.assertEqual(LDL(251, 69, 43.6, 23, 'female'), 3)
	def test_LDL_5  (self):self.assertEqual(LDL(260, 70, 43.6, 18, 'female'), 4)
	def test_LDL_6  (self):self.assertEqual(LDL(290, 70, 51.2, 45, 'male'), 5)
	def test_LDL_7  (self):self.assertEqual(LDL(141, 42, 11.3, 17, 'male'), 0)
	def test_LDL_8  (self):self.assertEqual(LDL(173, 51, 43.5, 8, 'female'), 1)
	def test_LDL_9  (self):self.assertEqual(LDL(182, 56, 11.2, 11, 'female'), 2)
	def test_LDL_10  (self):self.assertEqual(LDL(208, 64, 43.6, 14, 'female'), 3)
	def test_LDL_11  (self):self.assertEqual(LDL(251, 83, 43.6, 17, 'male'), 4)
	def test_LDL_12  (self):self.assertEqual(LDL(299, 79, 43.6, 5, 'male'), 5)
	def test_LDL_13  (self):self.assertEqual(LDL(161, 39, 11.3, 18, 'male'), 1)
	def test_LDL_14  (self):self.assertEqual(LDL(219, 31, 43.5, 26, 'male'), 4)
	def test_LDL_15  (self):self.assertEqual(LDL(188, 49, 11.2, 39, 'female'), 2)
	def test_LDL_16  (self):self.assertEqual(LDL(177, 37, 43.6, 44, 'female'), 3)
	def test_LDL_17  (self):self.assertEqual(LDL(289, 41, 71.9, 78, 'female'), 5)
	def test_LDL_18  (self):self.assertEqual(LDL(188, 71, 43.6, 58, 'female'), 0)
	def test_LDL_19  (self):self.assertEqual(LDL(236, 82, 43.6, 69, 'male'), 1)
	def test_LDL_20  (self):self.assertEqual(LDL(259, 77, 11.3, 21, 'male'), 2)
     
	
	############################################################################
	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]
				
				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
		
#		print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))
		
#			print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	this_file = __file__
	if dir==".":
		dir = os.getcwd()
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
	
	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return
		
	else:
		want_all = len(sys.argv) <=2
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
				del want_candidates[i]
	
		# set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
		wants = []
		extra_credits = []
		if not want_all:
			for w in want_candidates:
				if w in REQUIRED_DEFNS:
					wants.append(w)
				elif w in SUB_DEFNS:
					wants.append(w)
				elif w in EXTRA_CREDIT_DEFNS:
					extra_credits.append(w)
				else:
					raise Exception("asked to limit testing to unknown function '%s'."%w)
		else:
			wants = REQUIRED_DEFNS + SUB_DEFNS
			extra_credits = EXTRA_CREDIT_DEFNS
		
		# now that we have parsed the function names to test, run this one file.	
		run_one(wants,extra_credits)	
		return
	return # should be unreachable!	

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
	
	has_reqs = len(wants)>0
	has_ec   = len(extra_credits)>0
	
	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0
	
	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
	
	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
																passed1*weight_required, 
																total_points_from_tests,
																passed1,
																weight_required
															 ))
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
																passed1*weight_required+passed2*weight_extra_credit, 
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if CURRENTLY_GRADING:
		print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			print(" Batching on : " +filename)
			# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
			lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
			
			# delay of shame...
			time.sleep(DELAY_OF_SHAME)
			
			name = os.path.basename(lines[-1])
			stuff =lines[-2].split(" ")[1:-1]
			print("STUFF: ",stuff, "LINES: ", lines)
			(passed_req, tried_req, passed_ec, tried_ec) = stuff
			results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
			continue
		
		print("\n\n\nGRAND RESULTS:\n")
		
			
		for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))
# only used for batch mode.
def run_all_orig():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS
		
		results = []
		for filename in filenames:
			# wipe out all definitions between users.
			for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
				globals()[fn] = decoy(fn)
				fn = decoy(fn)
			try:
				name = os.path.basename(filename)
				print("\n\n\nRUNNING: "+name)
				(tag_req, passed_req, tried_req) = run_file(filename,wants,False)
				(tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
				results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
				print(" ###### ", results)
			except SyntaxError as e:
				tag = filename+"_SYNTAX_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except NameError as e:
				tag =filename+"_Name_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ValueError as e:
				tag = filename+"_VALUE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except TypeError as e:
				tag = filename+"_TYPE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ImportError as e:
				tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except Exception as e:
				tag = filename+str(e.__reduce__()[0])
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
		
# 			try:
# 				print("\n |||||||||| scrupe: "+str(scruples))
# 			except Exception as e:
# 				print("NO SCRUPE.",e)
# 			scruples = None
		
		print("\n\n\nGRAND RESULTS:\n")
		for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req)
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible, 
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)
			
			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False
				
			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
		except BaseException as e:
			print("\n\n\n\n\n\ntry-copy saw: "+e)
	
	if(i == numTries):
		return False
	return True

def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
	if wants==None:
		wants = []
	
	# move the student's code to a valid file.
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	count = 0
	while True:
		try:
# 			print("\n\n\nbegin attempt:")
			while True:
				try:
					f = open("student.py","a")
					f.close()
					break
				except:
					pass
# 			print ("\n\nSUCCESS!")
				
			import student
			importlib.reload(student)
			break
		except ImportError as e:
			print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
			time.sleep(0.5)
			while not os.path.exists("student.py"):
				time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_SYNTAX_ERROR",None, None, None)
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",0,1))	
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",0,1)
		except ImportError as e:			
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),0,1)
	
	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn)	
	
	if not checking_ec:
		# create an object that can run tests.
		runner = unittest.TextTestRunner()
	
		# define the suite of tests that should be run.
		suite = TheTestSuite(wants)
	
	
		# let the runner run the suite of tests.
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		# print(ans)
	
	else:
		# do the same for the extra credit.
		runner = unittest.TextTestRunner()
		suite = TheExtraCreditTestSuite(wants)
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		#print(ans)
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	if(not try_remove("student.py", 5)):
		print("Failed to remove " + filename + " to student.py.")
	
	tag = ".".join(filename.split(".")[:-1])
	
	
	return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
		# this can accept any kind/amount of args, and will print a helpful message.
		def failyfail(*args, **kwargs):
			return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
		return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()