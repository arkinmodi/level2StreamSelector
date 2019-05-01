## @file ReadAllocationData.py
#  @author Arkin Modi
#  @brief This module consists of functions that will read the data
#  @date 1/12/2019

## @brief readStdnts(s) parses the inputed file (csv) into a list of dictionaries.
#  @detail readStdnts(s) parses the inputed file (csv) into a list of dictionaries. 
#          Each dictionary in the list corresponds to one student. The 
#          dictionary for each student will have the following form: 
#          {’macid’: string, ’fname’: string, ’lname’: string, 
#          ’gender’: string, ’gpa’: float, ’choices’: [string, string, 
#          string] }. Assumed that the input file is correctly formated.
#  @param s corresponding to a filename.
#  @return studentBody is a list of dictionaries of student information.
def readStdnts(s):
    infile = open(s, 'r')
    fileFormat = infile.readline()   # skip the first line
    
    studentData = infile.readlines()
    infile.close()

    studentBody = []

    for student in studentData:
        student = student.rstrip('\n')    # removes the \n at the end of the string
        student = student.split(',')
        
        studentBody.append({
            "macid":    student[0],
            "fname":    student[1],
            "lname":    student[2],
            "gender":   student[3],
            "gpa":      float(student[4]),
            "choices":  [student[5], student[6], student[7]]
        })
    
    return studentBody

## @brief readFreeChoice(s) parses the inputed file (csv) into a list.
#  @detail readStdnts(s) parses the inputed file (csv) into a list. 
#          The list contains the madic of all the students with free 
#          choice. Assumed that the input file is correctly formated.
#  @param s corresponding to a filename.
#  @return students is a list of students with free choice.
def readFreeChoice(s):
    infile = open(s, 'r')
    fileFormat = infile.readline()
    students = infile.readlines()
    infile.close()
    return students

## @brief readDeptCapacity(s) parses the inputed file (csv) into a dictionary.
#  @detail readStdnts(s) parses the inputed file (csv) into a dictionary. 
#          The dictionary contains all the departments with their capacity's.
#          Assumed that the input file is correctly formated.
#  @param s corresponding to a filename.
#  @return deptCapacity is a dictionary with the key being the name of the 
#          department and the value being the capacity of the respective 
#          department.
def readDeptCapacity(s):
    infile = open(s, 'r')
    fileFormat = infile.readline()
    rawData = infile.readlines()
    infile.close()

    deptCapacity = {}
    for data in rawData:
        data = data.split(',')
        deptCapacity[data[0]] = int(data[1])
    return deptCapacity

"""
Assumptions:
- All files are formated correctly
"""