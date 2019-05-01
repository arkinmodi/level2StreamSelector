## @file Read.py
#  @author Arkin Modi modia1
#  @brief Reads and parses the inputed files
#  @date 11/02/2019

from StdntAllocTypes import *
from DCapALst import *
from SALst import *


## @breif reads the inputed file for the data on students and parses the data
#         into SALst.py
#  @param s the filename for the student data
def load_stdnt_data(s):
    SALst.init()
    stdnt_data = open(s, 'r')

    for student in stdnt_data.readlines():
        student = student.rstrip('\n')
        student = student.replace(' ', '')
        student = student.replace('[', '')
        student = student.replace(']', '')
        student = student.split(',')

        dept = []
        for i in range(5, len(student) - 1):
            dept.append(DeptT[student[i]])

        sinfo = SInfoT(student[1], student[2], GenT[student[3]], float(student[4]),
                       SeqADT(dept), student[-1] == "True")
        SALst.add(student[0], sinfo)
    stdnt_data.close()


## @breif reads the inputed file for the data on the departments and parses the
#         data into DCapALst.py
#  @param s the filename for the department data
def load_dcap_data(s):
    DCapALst.init()
    dept_capacity = open(s, 'r')

    for dept in dept_capacity.readlines():
        dept = dept.rstrip('\n')
        dept = dept.replace(' ', '')
        dept = dept.split(',')
        DCapALst.add(DeptT[dept[0]], int(dept[1]))

    dept_capacity.close()
