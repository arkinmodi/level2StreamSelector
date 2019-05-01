## @file CalcModule.py
#  @author Arkin Modi
#  @brief This module consists of functions that will completes various 
#         calculations on the list of students
#  @date 1/13/2019

## @brief sort(S) sorted the list generated from readStdnts(s) in 
#                 decending order by gpa.
#  @param S is the list of dictionaries created by readStdnts(s).
#  @return the list of dictionaries in sorted decending order by gpa.
def sort(S):
    return sorted(S, key=lambda S: S["gpa"], reverse=True)

## @brief sort(S) sorted the list generated from readStdnts(s) in 
#                 decending order by gpa.
#  @param L a list of the dictionaries created by function 
#         readStdnts(s).
#  @param g a string representing the gender (male or female).
#  @return the average gpa of male or female students, with the 
#          choice depending on the value of g.
def average(L, g):
    if(len(L) == 0):
        return 0

    g = g.lower()
    if(g == "male"):
        genderSorted = sorted(L, key=lambda L: L["gender"], reverse=True)
    else:
        genderSorted = sorted(L, key=lambda L: L["gender"], reverse=False)

    i = 0
    genderAverages = []
    while(genderSorted[i]["gender"].lower() == g):
        genderAverages.append(genderSorted[i]["gpa"])
        i+=1

    if(len(genderAverages) == 0):
        return 0
    return sum(genderAverages)/len(genderAverages)

## @brief allocate(S, F, C) allocates all the students into their 
#         respective departments.
#  @detail allocate(S, F, C) allocates all the students with a gpa 
#          greater than 4.0 into their respective departments. 
#          Those with less than 4.0 will not be allocated. Students 
#          with free choice will be allocated to their first choice. 
#          All other students will be allocated in the order of gpa. 
#          Starting with the highest gpa, students are put into 
#          departments by their first choice, until the bin for a 
#          given department is full. From that point onward students 
#          that select that department are instead allocated to their 
#          second choice. If their second choice is full, then they 
#          are allocated to their third choice.
#  @param S a list of the dictionaries of students.
#  @param F a list of students with free choice.
#  @param C a dictionary of department capacities.
#  @return a dictionary with a list of students (values) allocated to 
#          the respective departments (key).
def allocate(S, F, C):
    for student in S:
        if((student["macid"] in F) and (student["gpa"] >= 4.0)):   # Assuming students with free choice are also listed in S
            student["gpa"] = 13.0   # Assuming students with free choice get allocated first
    S = sort(S)

    departments = {
        "civil":        [],
        "chemical":     [],
        "electrical":   [],
        "mechanical":   [],
        "software":     [],
        "materials":    [],
        "engphys":      []
    }

    i = 0
    while(i < len(S) and S[i]["gpa"] >= 4.0):  # Assuming students with GPA = 4.0 get allocated
        firstChoice = S[i]["choices"][0]
        secondChoice = S[i]["choices"][1]
        thirdChoice = S[i]["choices"][2]

        if(C[firstChoice]):
            departments[firstChoice].append(S[i])
            C[firstChoice]-=1
        elif(C[secondChoice]):
            departments[secondChoice].append(S[i])
            C[secondChoice]-=1
        elif(C[thirdChoice]):
            departments[thirdChoice].append(S[i])
            C[thirdChoice]-=1
        i+=1
    return departments


"""
Assumptions:
- sort(S)
    - correctly formated input

- average(L, g)
    - g will be correctly spelled (male or female)
    - correctly formated input L

- allocate(S, F, C)
    - correctly formated inputs
    - students with 4.0 GPA get allocated
    - students with free choice are also listed in S
    - students with free choice get allocated first
    - departments don't get filled up before all free choice students are allocated
"""

"""
Resources Used:
https://stackoverflow.com/questions/9542738/python-find-in-list
https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
"""