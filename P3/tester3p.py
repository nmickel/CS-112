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

#import subprocess

import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
    
REQUIRED_DEFNS = [  "how_odd",
                    "vibrate",
                    "is_combustible",
                    "biggest_combustible",
                    "any_oversized",
                    "any_adjacent_combustibles",
                    "get_combustibles",
                    "cheap_products",
                    "box_sort",
                    "packing_list",
                 ]

# for method names in classes that will be tested. They have to be here
# so that we don't complain about missing global function definitions.
# Really, any chosen name for test batches can go here regardless of actual
# method names in the code.
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = [ ]

# how many points are test cases worth?
weight_required     = 1
weight_extra_credit = 1

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


import inspect # for enforcing usage of an operator or function
import ast     # for enforcing usage of an operator or function

# checks if a call to the function is present in the code. Of course it 
# might not actually be used in their solution...
def enforce_func_usage(func, funcname):
    dumptext = ast.dump(ast.parse(inspect.getsource(func).strip()))
    batches = dumptext.split("value=Call")
    for batch in batches:
        parts = batch.split("attr=")
        for part in parts:
            if part.startswith("'"+funcname+"'"):
                return
    raise Exception("You're required to call "+funcname+" in your solution.")


# END SPECIALIZATION SECTION

################################################################################
################################################################################
################################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
        
    ############################################################################
    
    def test_how_odd_1(self): self.assertEqual(how_odd(11),2)
    def test_how_odd_2(self): self.assertEqual(how_odd(10),0)
    def test_how_odd_3(self): self.assertEqual(how_odd(47),4)
    def test_how_odd_4(self): self.assertEqual(how_odd(12341234),0)
    def test_how_odd_5(self): self.assertEqual(how_odd(7),3)
    def test_how_odd_6(self): self.assertEqual(how_odd(49),1)
    def test_how_odd_7(self): self.assertEqual(how_odd(95),5)
    def test_how_odd_8(self): self.assertEqual(how_odd(127),7)
    
    ########################################################################### 
    
    def test_vibrate_1(self): self.assertEqual(vibrate(1),0)
    def test_vibrate_2(self): self.assertEqual(vibrate(5),1)
    def test_vibrate_3(self): self.assertEqual(vibrate(7),3)
    def test_vibrate_4(self): self.assertEqual(vibrate(10),6)
    def test_vibrate_5(self): self.assertEqual(vibrate(81),4)
    def test_vibrate_6(self): self.assertEqual(vibrate(82),13)
    def test_vibrate_7(self): self.assertEqual(vibrate(20),4)
    def test_vibrate_8(self): self.assertEqual(vibrate(36),11)
    
    ########################################################################### 
    
    def test_is_combustible_1(self): self.assertEqual(is_combustible("battery",["battery","lighter","power bank"]),True)
    def test_is_combustible_2(self): self.assertEqual(is_combustible("battery",["power bank","lighter","battery"]),True)
    def test_is_combustible_3(self): self.assertEqual(is_combustible("battery",["power bank","lighter"]),False)
    def test_is_combustible_4(self): self.assertEqual(is_combustible("doll",["power bank","lighter"]),False)
    def test_is_combustible_5(self): self.assertEqual(is_combustible("x",['a','b','x','c','d','x','y']),True)
    def test_is_combustible_6(self): self.assertEqual(is_combustible("x",[]),False)
    def test_is_combustible_7(self): self.assertEqual(is_combustible("NO",['yes','no']),False)
    def test_is_combustible_8(self): self.assertEqual(is_combustible('c',['a','b','c','d','e']),True)
    
    ########################################################################### 
    
    def test_biggest_combustible_1(self): self.assertEqual(biggest_combustible(["doll","AA","AAA"], [15,5,4], ["AA","AAA","D"]),"AA")
    def test_biggest_combustible_2(self): self.assertEqual(biggest_combustible(["doll","bike"], [5,120], ["AA","AAA","D"]),None)
    def test_biggest_combustible_3(self): self.assertEqual(biggest_combustible([],[],["laptop"]),None)
    def test_biggest_combustible_4(self): self.assertEqual(biggest_combustible(["a","b","c"],[5,9,6],["a","b","c"]),"b")
    def test_biggest_combustible_5(self): self.assertEqual(biggest_combustible(["aa"],[1],["aa"]),"aa")
    def test_biggest_combustible_6(self): self.assertEqual(biggest_combustible(['a','b','c'],[5,5,5],[]),None)
    def test_biggest_combustible_7(self): self.assertEqual(biggest_combustible(["a","b","c"],[3,4,5],["x","y","a"]),"a")
    def test_biggest_combustible_8(self): self.assertEqual(biggest_combustible(["paper","samsungGalaxy","flexvolt20"],[150,5,13], ["flexvolt20","samsungGalaxy"]),"flexvolt20")
    
    ########################################################################### 
    
    def test_any_oversized_1(self): self.assertEqual(any_oversized([1,2,3,4,5,6,7],5),True)
    def test_any_oversized_2(self): self.assertEqual(any_oversized([50,100,200],101),True)
    def test_any_oversized_3(self): self.assertEqual(any_oversized([50,10,20],100),False)
    def test_any_oversized_4(self): self.assertEqual(any_oversized([],1),False)
    def test_any_oversized_5(self): self.assertEqual(any_oversized([6,7,8],5),True)
    def test_any_oversized_6(self): self.assertEqual(any_oversized([14,14,15],100000),False)
    def test_any_oversized_7(self): self.assertEqual(any_oversized([5,5,5,5,5,5,5,5,1,2,3,5,5,5,5,5],5),False)
    def test_any_oversized_8(self): self.assertEqual(any_oversized([3,4,5],4),True)
    
    ########################################################################### 
    
    def test_any_adjacent_combustibles_1(self): self.assertEqual(any_adjacent_combustibles(['a','b','c'],['a','b','d']),True)
    def test_any_adjacent_combustibles_2(self): self.assertEqual(any_adjacent_combustibles(['a','b','c'],['c','b']),True)
    def test_any_adjacent_combustibles_3(self): self.assertEqual(any_adjacent_combustibles(['a','b','c'],['a','c']),False)
    def test_any_adjacent_combustibles_4(self): self.assertEqual(any_adjacent_combustibles(['a','b','a'],['c','a']),False)
    def test_any_adjacent_combustibles_5(self): self.assertEqual(any_adjacent_combustibles([],['a','b','c']),False)
    def test_any_adjacent_combustibles_6(self): self.assertEqual(any_adjacent_combustibles(['a','b','c','d','e'],['d','b','e']),True)
    def test_any_adjacent_combustibles_7(self): self.assertEqual(any_adjacent_combustibles(['a','b','c','d','e'],['x','y','z']),False)
    def test_any_adjacent_combustibles_8(self): self.assertEqual(any_adjacent_combustibles(['AA','AAA'],['AAA','C','D','AA']),True)
    
    ########################################################################### 
    
    def test_get_combustibles_1(self): self.assertEqual(get_combustibles(["doll","AA","AAA"], ["AA","AAA","D"]),["AA","AAA"])
    def test_get_combustibles_2(self): self.assertEqual(get_combustibles(["doll","bike"], ["AA","AAA","D"]),[])
    def test_get_combustibles_3(self): self.assertEqual(get_combustibles(["AA","belt","AA"],["laptop","AA"]),["AA","AA"])
    def test_get_combustibles_4(self): self.assertEqual(get_combustibles(['a','x','b','y','z','d'],['x','z','y']),['x','y','z'])
    def test_get_combustibles_5(self): self.assertEqual(get_combustibles(['a','b','a','c','a','d','a'],['a','c']),['a','a','c','a','a'])
    def test_get_combustibles_6(self): self.assertEqual(get_combustibles(['a','x','y','z','b'],['z','y','x']),['x','y','z'])
    def test_get_combustibles_7(self): self.assertEqual(get_combustibles([],['a','aa']),[])
    def test_get_combustibles_8(self): self.assertEqual(get_combustibles(['q'],['a','aa']),[])
    
    ########################################################################### 
    
    def test_cheap_products_1(self): self.assertEqual(cheap_products(["a","b","c","d"],[1,5,10,15],10),["a","b","c"])
    def test_cheap_products_2(self): self.assertEqual(cheap_products(['a','b','c'],[7,8,9],5),[])
    def test_cheap_products_3(self): self.assertEqual(cheap_products(['x','y','z'],[5,5,5],5),['x','y','z'])
    def test_cheap_products_4(self): self.assertEqual(cheap_products(['a'],[10],15),['a'])
    def test_cheap_products_5(self): self.assertEqual(cheap_products([],[],20),[])
    def test_cheap_products_6(self): self.assertEqual(cheap_products(['apple','banana','carrot','date','elderberry','fig'],[8,2,12,6,15,3],10),['apple','banana','date','fig'])
    def test_cheap_products_7(self): self.assertEqual(cheap_products(['q','w','e','r','t','y'],[2,2,1,1,3,3],2),['q','w','e','r'])
    def test_cheap_products_8(self): self.assertEqual(cheap_products(['q','w','e','r','t','y'],[2,2,1,1,3,3],1),['e','r'])
    
    ########################################################################### 
    
    def test_box_sort_1(self): self.assertEqual(box_sort(['a','b','c','d'], [1,5,6,10]),[['a'],['b'],['c','d'],[]])
    def test_box_sort_2(self): self.assertEqual(box_sort(['a','b','c'], [49,50,51]),[[],[],[],['a','b']])
    def test_box_sort_3(self): self.assertEqual(box_sort(['one','two','three'],[1,2,3]),[['one','two'],['three'],[],[]])
    def test_box_sort_4(self): self.assertEqual(box_sort(['a','b','c','d','A','B','C','D','Q','W','E','R','q','w','e','r'], [2,  5, 25, 50,  1,  4, 24, 49, 100,200,51, 52, 26, 27, 28, 29]), [['a','A'],['b','B'],['c','C'],['d','D','q','w','e','r']])
    def test_box_sort_5(self): self.assertEqual(box_sort(['a','b','c','d'],[15,30,29,11]),[[],[],['a','d'],['b','c']])
    def test_box_sort_6(self): self.assertEqual(box_sort(['b','o','x','y','!','?'],[40,60,20,4,1,10]),[['!'],['y'],['x','?'],['b']])
    def test_box_sort_7(self): self.assertEqual(box_sort(['Q','R','S','T','U','V','W','X','Y','Z'],[1,2,3,4,5,6,7,8,9,10]),[['Q','R'],['S','T','U'],['V','W','X','Y','Z'],[]])
    def test_box_sort_8(self): self.assertEqual(box_sort(['only'],[21]),[[],[],['only'],[]])
    
    ########################################################################### 
    
    def test_packing_list_1(self): self.assertEqual(packing_list(['a','b','c','d'], [2,1,4,2],5),[['a','b'],['c'],['d']])
    def test_packing_list_2(self): self.assertEqual(packing_list(['a','b','c'], [2,10,3], 5),[['*b'],['a','c']])
    # some perfectly filled boxes
    def test_packing_list_3(self): self.assertEqual(packing_list(['a','b','c','x','y','z'],[1,4,2,7,5,2],10),[['a','b','c'],['x'],['y','z']])
    # extra space in a box
    def test_packing_list_4(self): self.assertEqual(packing_list(['m','o','n','k','e','y'],[8,3,6,2,9,1],10),[['m'],['o','n'],['k'],['e','y']])
    # oversized item sneaks in before second box is filled
    def test_packing_list_5(self): self.assertEqual(packing_list(['a','BIG','c','d'],[2,25,3,4],10),[['*BIG'],['a','c','d']])
    # many oversized
    def test_packing_list_6(self): self.assertEqual(packing_list(['a','b','c','x','y','z'],[2,20,3,21,4,100],10),[['*b'],['*x'],['*z'],['a','c','y']])
    # all oversized
    def test_packing_list_7(self): self.assertEqual(packing_list(['very','much','wow'],[100,200,300],15),[["*very"],["*much"],["*wow"]])
    def test_packing_list_8(self): self.assertEqual(packing_list(['x',"A",'y',"AA",'z'],[11,12,13,14,15],5),[['*x'],['*A'],['*y'],['*AA'],['*z']])
    
    ########################################################################### 
    
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
        
#       print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
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
        
#           print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
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
#       print(dirpath,dirnames,filez)
        if dirpath==".":
            continue
        for file in filez:
            if file==this_file:
                continue
            filenames.append(os.path.join(dirpath,file))
#       print(dirpath,dirnames,filez,"\n")
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
        print("\nScore based on test cases: %.2f / %d ( %d * %.2f + %d * %.2f) " % (
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
            for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
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
        
#           try:
#               print("\n |||||||||| scrupe: "+str(scruples))
#           except Exception as e:
#               print("NO SCRUPE.",e)
#           scruples = None
        
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
#           print("\n\n\nbegin attempt:")
            while True:
                try:
                    f = open("student.py","a")
                    f.close()
                    break
                except:
                    pass
#           print ("\n\nSUCCESS!")
                
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
            return((filename+"_IMPORT_ERROR_TRY_AGAIN   ",0,1)) 
        except Exception as e:
            print("Exception in loading"+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+str(e.__reduce__()[0]),0,1)
    
    # make a global for each expected definition.
    for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
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
