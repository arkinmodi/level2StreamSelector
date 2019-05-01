## @file testCalc.py
#  @author Arkin Modi
#  @brief This is a module that test CalcModule.py
#  @date 1/15/2019

from ReadAllocationData import *
from CalcModule import *

## @brief testCalc(stdnts, freeStdnts, dept) test the CalcModule.py file.
#  @param stdnts is the input file containing the students' information.
#  @param freeStdnts is the input file containing the list fo free choice 
#         students.
#  @param dept is the input file containing the capacities of each 
#         department.
#  @return a dictionary with a list of students (values) allocated to 
#          the respective departments (key).
def testCalc(stdnts, freeStdnts, dept):
    studentBody = readStdnts(stdnts)
    freeChoice = readFreeChoice(freeStdnts)
    deptCap = readDeptCapacity(dept)

    studentBodySort = sort(studentBody)
    
    maleAvg = average(studentBody, "male")
    femaleAvg = average(studentBody, "female")
    print("Male Average = " + str(maleAvg))
    print("Female Average = " + str(femaleAvg))

    result = allocate(studentBodySort, freeChoice, deptCap)
    print(result)
    print()
    return result

testCalc("src/test_files/stdnts_0.txt", "src/test_files/freeChoice_0.txt", "src/test_files/deptCap_0.txt")
testCalc("src/test_files/stdnts_0.txt", "src/test_files/freeChoice_0.txt", "src/test_files/deptCap_1.txt")
testCalc("src/test_files/stdnts_5.txt", "src/test_files/freeChoice_5.txt", "src/test_files/deptCap_0.txt")
testCalc("src/test_files/stdnts_5.txt", "src/test_files/freeChoice_5.txt", "src/test_files/deptCap_1.txt")
testCalc("src/test_files/stdnts_10.txt", "src/test_files/freeChoice_10.txt", "src/test_files/deptCap_0.txt")
testCalc("src/test_files/stdnts_10.txt", "src/test_files/freeChoice_10.txt", "src/test_files/deptCap_1.txt")