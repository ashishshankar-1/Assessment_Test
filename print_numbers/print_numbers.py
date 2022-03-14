#!/usr/bin/env python3

def display_the_nos(number):
    """
    Fucntion will check the number: 
    1. Multiple by 3
    2. Multiple by 5
    3. Multiple by 3 and 5 both
    args: int
    return : iterator
    """
    # Using the generator to reduce memory consumption.
    # If suppose number is not 100 its 1 million
    for element in range(1, number+1):
        value = ''
        if element % 3 == 0:
            value = value + 'Three'
        if element % 5 == 0:
            value = value + 'Five'
        if value == '':
            value = element
        yield value

# Main method starts here
if __name__ == '__main__':
    # Displaying for 1-100 numbers
    for element in display_the_nos(100):
        print(element)

