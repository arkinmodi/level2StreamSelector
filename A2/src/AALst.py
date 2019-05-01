## @file AALst.py
#  @author Arkin Modi modia1
#  @brief Allocation Association List Module
#  @date 11/02/2019

from StdntAllocTypes import *


## @brief this class manages the allocation of students to a department list
class AALst:

    ## @brief initialized the state variable
    def init():
        AALst.s = {}    # set of AllocAssocListT
        for d in DeptT:
            AALst.s[d] = []

    ## @brief adds a student to a department
    #  @param dep the department
    #  @param dep the student
    @staticmethod
    def add_stdnt(dep, m):
        AALst.s[dep].append(m)

    ## @brief outputs the list of students allocated to a department
    #  @param the department
    #  @return the list of students allocated to the given department
    @staticmethod
    def lst_alloc(d):
        return AALst.s[d]

    ## @brief the number of allocated students in a department
    #  @param d the department
    #  @return the number of students allocaed to the given department
    @staticmethod
    def num_alloc(d):
        return len(AALst.s[d])
