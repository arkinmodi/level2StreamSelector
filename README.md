# Level 2 Stream Selector
Assignment 1 &amp; 2 for SFWRENG 2AA4 - Software Design I - Introduction to Software Development

## Overview
A python program to allocate engineering students from first year into their second year programs.

## How It Works
In the McMaster University Engineering Program, the first year is general engineering. In second year, the students get to specialize into 1 of 7 programs. Due to limited capacity of each stream, not all students can be allocated to their first choice.

This program used 3 factors to determine and allocate each student to their respective stream: Free Choice, GPA (12-Point Scale), and Top 3 Stream Preferences. Students who have free choice and a GPA > 4 will get their 1st choice. After that, the students with a GPA > 4 are ranked by their GPA, and are then allocated to their highest preference based on space of each stream. For students that are not allocated (due to either a GPA < 4 or all their top 3 preference got filled up) are handled by not assigning a level 2 stream.

## A1 vs A2
Both versions contain documentation using doxygen.

### A1
Assignment 1 was created with limited knowledge of object-oriented programming and no knowledge of any standardized/automated testing. The testing done is all manual testing. The specification was also provided in a natural language.

### A2
Assignment 2 was created with a basic understanding of object-oriented programming and unit testing. The version uses pytest (python unit testing) and has an implementation following an object-oriented programming style. The specification provided was also a formal specification.

## How To Run
To run the test:

    make test

To make the docs with doxygen:

    make doc

To removed the docs:

    make clean

## What I Learned
* Basic Object-Oriented Programming
* Manual Testing vs Automated Testing
    * Unit Testing
* Documenting Code
* Reading a Specification