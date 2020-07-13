"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​""" 
O(1) - Constant Time
"""

# def print_animals(animal_list):
#     print(animal_list[0])

# def print_animals(animal_list):
#     for n in range(10000)
#         print(animal_list[0])
​
""" 
O(n) - Linear Time
"""
def print_animals(animal_list):
    for n in range(len(animal_list))
        print(animal_list[0])
​
"""
What about this one? What runtime complexity is this one?
"""

""" 
O(n^2) - Quadratic Time
"""​
def print_animals(animal_list): # This line is 0(n * (1 + 1 + 1 + (100000 * 1))) = O(n * 10003) = O(100003n) = O(n)
    for i in range(len(animal_list)): # This line is 0(n) - Linear
        print(animal_list[i]) # This line is 0(1) - Constant
        print(animal_list[i]) # This line is 0(1) - Constant --> (1 + 1) * n 
        # O(1+1) = ) = (2)

        my_number = 0 # This line is 0(1) - Constant
        for _ in range(100000): # This line is 0(100000) - Constant
            my_number += 1 # This line is 0(1) - Constant
​
​
"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""
​
​
"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# Print a list of all possible animal pairs
def print_animal_pairs(lst): ) #O(n*(n*1)) = O(n*n) = O(n^2)
    for animal_1 in lst: # O(n)
        for animal_2 in lst: # O(n)
            print(f"{animal_1} - {animal_2}") # O(1)
​
​
# Print a list of all possible animal triples O(n^3)
def print_animal_triples():
    for animal_1 in animals: # O(n)
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
# Print a list of all possible animal triples
def print_animal_triples():
    for animal in animals:
        print(animal)
​
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten"tuples?
"""
​
​
"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# free all the animals, half at a time
# (remove them from the array)
def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]
​
# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time
​
​
"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
"""

"""
-Linked Lists have O(1) appends
-Linked Lists have O(1) prepends
-Linked Lists have O(n) lookups

-Dynamic Arrays have O(n) appends
-Dynamic Arrays have O(n) prepends
-Dynamic Arrays have O(1) lookups
"""