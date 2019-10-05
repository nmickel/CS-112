# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
#   
#   MAC:
#   python3 <thisfile.py> <your_one_file.py>
# 
#   PC:
#   python <thisfile.py> <your_one_file.py>
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
#   python3 <thisfile.py> .					# current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong,   Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder,   June 2017.
#  Edited by Raven Russell, Spring 2018.
#  Edited by Mark Snyder,   Spring 2019. (imp deprecated; now uses importlib)
#  Edited by Raven Russell, Spring 2019. (fixed batch mode again)

import unittest
import shutil
import sys
import os
import time

import importlib.util
import traceback
import platform
import random
import io

random.seed(0)

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.

REQUIRED_DEFNS = ['chemical_strength', 'light_status']

# for method names in classes that will be tested. They have to be here
# so that we don't complain about missing global function definitions.
# Really, any chosen name for test batches can go here regardless of actual
# method names in the code.
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = [  ]

# how many points are test cases worth?
weight_required	 = 1
weight_extra_credit = 0

# this is auto-calculated based on all possible tests.
total_points_from_tests = -1

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1

# this gets set in main() for windows/mac/linux
python_command = ""

# warnings to display
warnings = []

# get file contents
def get_file_contents(file_name):
	f = open(file_name,"r", newline='\n')
	contents = f.read()
	f.close()
	
	# remove a newline character at end...
	if contents[-1] == '\n':
		contents = contents[:-1]
		
	return contents

# write file
def set_file_contents(file_name, contents):
	f = open(file_name,"w", newline='\n')
	f.write(contents)
	f.close()

# END SPECIALIZATION SECTION

################################################################################
################################################################################
################################################################################

# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))
BATCH_MODE_SUB = len(sys.argv)==3 and sys.argv[2] in ["BATCH"]

# This class contains multiple "unit tests" that each check
# various inputs to specifclear
# c functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
		
	############################################################################
	
	# bad measurements
	def test_chemical_strength_00(self): self.assertEqual(chemical_strength(-0.0234),'bad measurement')
	def test_chemical_strength_01(self): self.assertEqual(chemical_strength(14.023),'bad measurement')
	def test_chemical_strength_02(self): self.assertEqual(chemical_strength(112),'bad measurement')
	def test_chemical_strength_03(self): self.assertEqual(chemical_strength(-13.345),'bad measurement')
	def test_chemical_strength_04(self): self.assertEqual(chemical_strength(521.6752),'bad measurement')
	def test_chemical_strength_05(self): self.assertEqual(chemical_strength(-542.098),'bad measurement')
	def test_chemical_strength_06(self): self.assertEqual(chemical_strength(167894039839.98767890239805614),'bad measurement')

	# two plain & one neutral
	def test_chemical_strength_07(self): self.assertEqual(chemical_strength(4),'plain acid')
	def test_chemical_strength_08(self): self.assertEqual(chemical_strength(7),'neutral')
	def test_chemical_strength_09(self): self.assertEqual(chemical_strength(10),'plain base')

	# very strong acids
	def test_chemical_strength_10(self): self.assertEqual(chemical_strength(0),'very strong acid')	
	def test_chemical_strength_11(self): self.assertEqual(chemical_strength(0.03245),'very strong acid')	
	def test_chemical_strength_12(self): self.assertEqual(chemical_strength(0.1562),'very strong acid')	
	def test_chemical_strength_13(self): self.assertEqual(chemical_strength(0.764222),'very strong acid')
	def test_chemical_strength_14(self): self.assertEqual(chemical_strength(0.9998),'very strong acid')

	# strong acids
	def test_chemical_strength_15(self): self.assertEqual(chemical_strength(1.00001),'strong acid')
	def test_chemical_strength_16(self): self.assertEqual(chemical_strength(1.031),'strong acid')
	def test_chemical_strength_17(self): self.assertEqual(chemical_strength(1.7743),'strong acid')
	def test_chemical_strength_18(self): self.assertEqual(chemical_strength(2.8893),'strong acid')
	def test_chemical_strength_19(self): self.assertEqual(chemical_strength(3.995),'strong acid')

	# weak acids
	def test_chemical_strength_20(self): self.assertEqual(chemical_strength(4.075),'weak acid')
	def test_chemical_strength_21(self): self.assertEqual(chemical_strength(4.5553),'weak acid')
	def test_chemical_strength_22(self): self.assertEqual(chemical_strength(5),'weak acid')
	def test_chemical_strength_23(self): self.assertEqual(chemical_strength(5.888888),'weak acid')
	def test_chemical_strength_24(self): self.assertEqual(chemical_strength(5.98),'weak acid')

	# very weak acids
	def test_chemical_strength_25(self): self.assertEqual(chemical_strength(6),'very weak acid')
	def test_chemical_strength_26(self): self.assertEqual(chemical_strength(6.22),'very weak acid')
	def test_chemical_strength_27(self): self.assertEqual(chemical_strength(6.823),'very weak acid')
	def test_chemical_strength_28(self): self.assertEqual(chemical_strength(6.0032),'very weak acid')
	def test_chemical_strength_29(self): self.assertEqual(chemical_strength(6.99),'very weak acid')

	# very weak bases
	def test_chemical_strength_30(self): self.assertEqual(chemical_strength(7.05),'very weak base')
	def test_chemical_strength_31(self): self.assertEqual(chemical_strength(7.832),'very weak base')
	def test_chemical_strength_32(self): self.assertEqual(chemical_strength(7.234),'very weak base')
	def test_chemical_strength_33(self): self.assertEqual(chemical_strength(7.77777),'very weak base')
	def test_chemical_strength_34(self): self.assertEqual(chemical_strength(8),'very weak base')

	# weak bases
	def test_chemical_strength_35(self): self.assertEqual(chemical_strength(8.0325),'weak base')
	def test_chemical_strength_36(self): self.assertEqual(chemical_strength(8.8888),'weak base')
	def test_chemical_strength_37(self): self.assertEqual(chemical_strength(9.4245),'weak base')
	def test_chemical_strength_38(self): self.assertEqual(chemical_strength(9.54),'weak base')
	def test_chemical_strength_39(self): self.assertEqual(chemical_strength(9.9999),'weak base')

	# strong bases
	def test_chemical_strength_40(self): self.assertEqual(chemical_strength(10.2391),'strong base')
	def test_chemical_strength_41(self): self.assertEqual(chemical_strength(11.56424),'strong base')
	def test_chemical_strength_42(self): self.assertEqual(chemical_strength(12),'strong base')
	def test_chemical_strength_43(self): self.assertEqual(chemical_strength(12.77722333),'strong base')
	def test_chemical_strength_44(self): self.assertEqual(chemical_strength(12.9999435),'strong base')

	# very strong bases
	def test_chemical_strength_45(self): self.assertEqual(chemical_strength(13),'very strong base')
	def test_chemical_strength_46(self): self.assertEqual(chemical_strength(13.5),'very strong base')
	def test_chemical_strength_47(self): self.assertEqual(chemical_strength(13.99),'very strong base')
	def test_chemical_strength_48(self): self.assertEqual(chemical_strength(13.1111),'very strong base')
	def test_chemical_strength_49(self): self.assertEqual(chemical_strength(14),'very strong base')

	# invalid switches 
	def test_light_status_00(self): self.assertEqual(light_status(0,0), 'invalid switch')
	def test_light_status_01(self): self.assertEqual(light_status(154,8524), 'invalid switch')
	def test_light_status_02(self): self.assertEqual(light_status(0,99), 'invalid switch')
	def test_light_status_03(self): self.assertEqual(light_status(99,0), 'invalid switch')
	def test_light_status_04(self): self.assertEqual(light_status(23,-156), 'invalid switch')
	def test_light_status_05(self): self.assertEqual(light_status(-10,10), 'invalid switch')
	def test_light_status_06(self): self.assertEqual(light_status(-345,0), 'invalid switch')
	def test_light_status_07(self): self.assertEqual(light_status(45,-45), 'invalid switch')
	def test_light_status_08(self): self.assertEqual(light_status(101,51), 'invalid switch')
	def test_light_status_09(self): self.assertEqual(light_status(51,101), 'invalid switch')

	# off
	def test_light_status_10(self): self.assertEqual(light_status(1,1), 'off')
	def test_light_status_11(self): self.assertEqual(light_status(2,1), 'off')
	def test_light_status_12(self): self.assertEqual(light_status(1,2), 'off')
	def test_light_status_13(self): self.assertEqual(light_status(5,15), 'off')
	def test_light_status_14(self): self.assertEqual(light_status(49,49), 'off')
	def test_light_status_15(self): self.assertEqual(light_status(33,57), 'off')
	def test_light_status_16(self): self.assertEqual(light_status(48,51), 'off')
	def test_light_status_17(self): self.assertEqual(light_status(2,51), 'off')
	def test_light_status_18(self): self.assertEqual(light_status(88,48), 'off')
	def test_light_status_19(self): self.assertEqual(light_status(32,56), 'off')

	# on, both over 50
	def test_light_status_20(self): self.assertEqual(light_status(51,51), 'on')
	def test_light_status_21(self): self.assertEqual(light_status(52,51), 'on')
	def test_light_status_22(self): self.assertEqual(light_status(51,52), 'on')
	def test_light_status_23(self): self.assertEqual(light_status(63,67), 'on')
	def test_light_status_24(self): self.assertEqual(light_status(77,78), 'on')
	def test_light_status_25(self): self.assertEqual(light_status(89,55), 'on')
	def test_light_status_26(self): self.assertEqual(light_status(55,89), 'on')
	def test_light_status_27(self): self.assertEqual(light_status(99,93), 'on')
	def test_light_status_28(self): self.assertEqual(light_status(64,83), 'on')
	def test_light_status_29(self): self.assertEqual(light_status(100,100), 'on')

	# on, sum is 100
	def test_light_status_30(self): self.assertEqual(light_status(56,44), 'on')
	def test_light_status_31(self): self.assertEqual(light_status(44,56), 'on')
	def test_light_status_32(self): self.assertEqual(light_status(1,99), 'on')
	def test_light_status_33(self): self.assertEqual(light_status(98,2), 'on')
	def test_light_status_34(self): self.assertEqual(light_status(34,66), 'on')
	def test_light_status_35(self): self.assertEqual(light_status(78,22), 'on')
	def test_light_status_36(self): self.assertEqual(light_status(15,85), 'on')
	def test_light_status_37(self): self.assertEqual(light_status(45,55), 'on')
	def test_light_status_38(self): self.assertEqual(light_status(90,10), 'on')
	def test_light_status_39(self): self.assertEqual(light_status(43,57), 'on')


	# on, difference is 50
	def test_light_status_40(self): self.assertEqual(light_status(1,51), 'on')
	def test_light_status_41(self): self.assertEqual(light_status(11,61), 'on')
	def test_light_status_42(self): self.assertEqual(light_status(72,22), 'on')
	def test_light_status_43(self): self.assertEqual(light_status(80,30), 'on')
	def test_light_status_44(self): self.assertEqual(light_status(77,27), 'on')
	def test_light_status_45(self): self.assertEqual(light_status(98,48), 'on')
	def test_light_status_46(self): self.assertEqual(light_status(49,99), 'on')
	def test_light_status_47(self): self.assertEqual(light_status(34,84), 'on')
	def test_light_status_48(self): self.assertEqual(light_status(14,64), 'on')
	def test_light_status_49(self): self.assertEqual(light_status(93,43), 'on')


	#---------------------------------------------------------------------
	
	############################################################################
	
	# EC
#   def test_extra_credit_main_01(self):
#	   self.assertEqual(ec(),2)
		
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
					self.num_req += 1
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
					self.num_ec += 1
		
#	   print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test_extra_credit_".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				if str(func).startswith("test_extra_credit_"+w):
					fs.append(AllTests(str(func)))
					self.num_ec += 1
	
#	   print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
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
#	   print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#	   print(dirpath,dirnames,filez,"\n")
	return filenames

def test_main():
	global python_command
	if(platform.system() == 'Windows'):
		python_command = "python"
	else:
		python_command = "python3"

	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\""+python_command+" testerX.py gmason76_2xx_Px.py\"")
	
	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return
		
	else:
		want_all = len(sys.argv) <=2 or sys.argv[2] in ["BATCH"]
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.', "BATCH"] or os.path.isdir(want_candidates[i]):
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
	
	#wants = REQUIRED_DEFNS + SUB_DEFNS
	#extra_credits = EXTRA_CREDIT_DEFNS
	
	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0
	tag = ""
	
	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
	
	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed (worth %.2f each)" % (passed1,tried1,weight_required) )
		print("\nScore based on test cases: %.2f/%.2f (%d*%.2f) " % (
																passed1*weight_required, 
																total_points_from_tests,
																passed1,
																weight_required
															 ))
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %.2f each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %.2f each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %.2f each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %.2f ( %d * %.2f + %d * %.2f) " % (
																passed1*weight_required+passed2*weight_extra_credit, 
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if BATCH_MODE_SUB:
		print("( %d %d %d %d %.2f )\n%s" % (passed1,tried1,passed2,tried2,total_points_from_tests,tag))
	elif len(warnings) > 0:
		for warning in warnings:
			print("\nWARNING: "+warning)

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)
		
		results = []
		for filename in filenames:
			if filename[-3:] in [".py"]:
				command = python_command+" \""+sys.argv[0]+"\" \""+filename+"\" BATCH"
				print(" Batching on : " +filename + " (command: " + command + ")")
				# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
				lines = os.popen(command).readlines()
				
				# delay of shame...
				time.sleep(DELAY_OF_SHAME)
				
				name = os.path.basename(lines[-1])
				stuff = lines[-2].split(" ")[1:6]
				(passed_req, tried_req, passed_ec, tried_ec, total_points_from_tests) = stuff
				results.append((filename,int(passed_req), int(tried_req), int(passed_ec), int(tried_ec), float(total_points_from_tests)))
			
		print("\n\n\nGRAND RESULTS:\n")
		
		for (tag_req, passed_req, tried_req, passed_ec, tried_ec, total_points_from_tests) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			print("%20s : %3d / %3d = %6.2f %% (%d/%d*%.2f + %d/%d*%.2f)" % (
															name,
															earned,
															total_points_from_tests, 
															(earned/total_points_from_tests)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def import_student_code(filename):
	
	# get code as string.
	f = open(filename)
	code = f.read()
	f.close()
	
	# using importlib to read contents into brand new module
	module_spec = importlib.util.spec_from_file_location("student",filename)
	module = importlib.util.module_from_spec(module_spec)
	module_spec.loader.exec_module(module)
	
	# register the module so it can be imported.
	sys.modules["student"] = module
	
	return module
	
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

def try_remove(filename, numTries, message):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print(message)
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def try_remove_test_file(file_name, function_name):
	try:
		try_remove(file_name, 3, "Trying to remove " + file_name)
	except:
		print("Warning: file " + file_name + 
			" couldn't be removed (possibly because " +
			"it was never closed in " + function_name + "(). " +
			"Please delete this file manually.")

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
	global total_points_from_tests
	
	if wants==None:
		wants = []
	
	# create an object that can run tests.
	runner = unittest.TextTestRunner()
	
	# define the suite of tests that should be run.
	#suite = None
	if not checking_ec:
		suite = TheTestSuite(wants)
		total_points_from_tests = suite.num_req*weight_required
	else:
		# do the same for the extra credit.
		suite = TheExtraCreditTestSuite(wants)
	
	# check number of tests before importing student code
	num_tests = suite.num_req + suite.num_ec
	
	# move the student's code to a valid file.
	#if(not try_copy(filename,"student.py", 5)):
	#   print("Failed to copy " + filename + " to student.py.")
	#   quit()
	
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	
	try:
		import_student_code(filename)
		import student
	except SyntaxError as e:
		print("SyntaxError in "+filename+":\n"+str(e))
		print("Run your file without the tester to see the details")
		return(filename+"_SYNTAX_ERROR",0,num_tests)
	except NameError as e:
		print("NameError in "+filename+":\n"+str(e))
		print("Run your file without the tester to see the details")
		return((filename+"_Name_ERROR",0,num_tests))	
	except ValueError as e:
		print("ValueError in "+filename+":\n"+str(e))
		print("Run your file without the tester to see the details")
		return(filename+"_VALUE_ERROR",0,num_tests)
	except TypeError as e:
		print("TypeError in "+filename+":\n"+str(e))
		print("Run your file without the tester to see the details")
		return(filename+"_TYPE_ERROR",0,num_tests)
	except ImportError as e:			
		print("ImportError in "+filename+":\n"+str(e))
		print("Run your file without the tester to see the details or try again")
		return((filename+"_IMPORT_ERROR_TRY_AGAIN   ",0,num_tests)) 
	except Exception as e:
		#traceback.print_last()
		print("Exception in loading"+filename+":\n"+str(e))
		print("Run your file without the tester to see the details")
		return(filename+str(e.__reduce__()[0]),0,num_tests)
	
	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn) 
	
	ans = runner.run(suite)
	num_errors   = len(ans.__dict__['errors'])
	num_failures = len(ans.__dict__['failures'])
	num_passed   = ans.__dict__['testsRun'] - num_errors - num_failures
	# print(ans)
	
	# remove our temporary file.
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	
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
	test_main()