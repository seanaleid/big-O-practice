"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
def print_animals(animal_list):
    print(animal_list[0])
​
​
"""
What about this one? What runtime complexity is this one?
"""
​
​
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
        my_number = 0
        for _ in range(100000):
            my_number += 1
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
def print_animal_pairs():
    for animal_1 in animals:
        for animal_2 in animals:
            print(f"{animal_1} - {animal_2}")
​
​
# Print a list of all possible animal triples
def print_animal_triples():
    for animal_1 in animals:
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
