# Assessment_Test
Assessment Test For Software Engineer (Python)

Ques: Tell us about one thing you are proud of in your career. It could be a difficult technical problem you had to solve in your work or a personal project. There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine.
-----------------------------------------------------------------------------------------------------
**Ans:** Comment: docx file is added Achievements_in _previous_project.docx

Ques: Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.
-----------------------------------------------------------------------------------------------------------
**Ans:** There are three files in the Print_the_number_folder

a) __init__file.py (empty file)

b) print_numbers.py file : This file contains the function name display_the_nos which puts the logic for printing as mentioned in Question 2

c) test_case.py file : This file consists of class TestCaseToCheckTheReturnValue to check that the return value for display_the_nos is Generator type or not.

**Ques:** Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. The API that this library provides is your choice.--

Postcodes API is available at http://postcodes.io/

**Ans:** Here we are validating and formating the Postcode with the api i.e http://postcodes.io/

There is a file validate_format_PostCode.py (module)

It consists of below functions

a) loadJsonResponse

b) validatePostcode--- Function to validate the post code

c) randomPostcode--- Function to generate random post code

d) queryPostcode--- Function to query the post code

e) getAutoCompletePostcode--- Function to get auto complete post code

**Next file is the test case file i.e test_cases.py**

It consists of below Test classes.

a) TestToValidateThePostCode--- Test for valid postcode

b) TestToQueryPostcode--- Test for query with valid postcode

c) TestToGetAutoCompletePostcode--- Test to get auto complete with valid postcode
