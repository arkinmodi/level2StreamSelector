## @file DCapALst.py
#  @author Arkin Modi, modia1
#  @brief Department Capacity Association List Module
#  @date 11/02/2019


## @brief this class manages the department capacity association list
class DCapALst:

    ## @brief initialized the state variable
    @staticmethod
    def init():
        DCapALst.s = {}  # set of tupple of (dept: DeptT, cap: Natural)

    ## @brief adds the capacity of the department to the state vairable
    #  @param d the department
    #  @param n the capacity of the department
    @staticmethod
    def add(d, n):
        if(d in DCapALst.s):
            raise(KeyError)
        DCapALst.s[d] = n

    ## @brief removes a department from the state vairable
    #  @param d the department to be removed
    @staticmethod
    def remove(d):
        if not (d in DCapALst.s):
            raise(KeyError)
        del DCapALst.s[d]

    ## @brief checks if a department is in the state vairable
    #  @param d the department
    #  @return bool representing if the department exists
    @staticmethod
    def elm(d):
        return d in DCapALst.s

    ## @brief check the capacity of a department
    #  @param d the department
    #  @return an int representing the capacity
    @staticmethod
    def capacity(d):
        if not (d in DCapALst.s):
            raise(KeyError)
        return DCapALst.s[d]
