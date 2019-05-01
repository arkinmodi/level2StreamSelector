## @file SALst.py
#  @author Arkin Modi, modia1
#  @brief Student Association List Module
#  @date 11/02/2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *


## @brief the class manages the students and their information
class SALst:

    ## @brief initialized the state variable
    @staticmethod
    def init():
        SALst.s = {}

    ## @brief adds a student to the state variable
    #  @param m the macid of the student
    #  @param i the information of the student
    @staticmethod
    def add(m, i):
        if(m in SALst.s):
            raise(KeyError)
        SALst.s[m] = i

    ## @brief removes a student from the state variable
    #  @param m the macid of the student
    @staticmethod
    def remove(m):
        if not (m in SALst.s):
            raise(KeyError)

    ## @brief checks is a student is in the list
    #  @param m the macid of the student
    #  @return a bool representing if the student exists
    @staticmethod
    def elm(m):
        return m in SALst.s

    ## @breif outputs the information of the student
    #  @param m the macid of the student
    #  @return the information of the student
    @staticmethod
    def info(m):
        if not (m in SALst.s):
            raise(KeyError)
        return SALst.s[m]

    ## @brief sorts the students based on their GPA and removes students who
    #         do no pass the filter
    #  @param f the filter for which students are included
    #  @return the list of students that pass the filter sorted by decreasing
    #          order of GPA
    @staticmethod
    def sort(f):
        students = []
        sort_stdt = sorted(SALst.s, key=lambda x: SALst.s[x].gpa, reverse=True)
        for t in sort_stdt:
            if(f(SALst.s[t])):
                students.append(t)
        return students

    ## @brief outputs the average of the students' GPA that pass the filter
    #  @param f the filter for which the students are included
    #  @return the average GPA of the students that passed the filter
    @staticmethod
    def average(f):
        grades = []
        for x in SALst.s:
            if(f(SALst.s[x])):
                grades.append(SALst.s[x].gpa)
        if not len(grades):
            raise(ValueError)
        return sum(grades) / len(grades)

    ## @breif allocated the students into the repsective departments
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)

        s = SALst.sort(lambda t: (not t.freechoice) and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while (not alloc) and (not ch.end()):
                d = ch.next()
                if(AALst.num_alloc(d) < DCapALst.capacity(d)):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not (alloc):
                raise(RuntimeError)
