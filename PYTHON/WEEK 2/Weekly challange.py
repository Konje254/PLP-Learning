"""
Task 1: Write a program that accepts user input to create a list of integers.
Then, compute the sum of all the integers in the list
"""




# creating an empty list
lst = []


# number of elements as input
n = int(input("Enter number of integers to get the sum: "))


# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)


print('The sum of the integer you have given is: ',sum(lst))


"""
Task 2: Create a tuple containing the names of five of your favorite books.
Then, a for loop prints each book name on a separate line.
"""


Books = ('Love is blind', 'The Great Gatsby', 'To Kill a Mockingbird', 'Frankenstein', 'Jane Eyre')


for book in Books:
    print(book)


"""
Task 3: Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color.
Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
"""


dict = {}


name = input('Enter your name:')
age = input('Enter your age:')
fav_col = input('Enter your favorite color:')


dict['name'] = name
dict['age'] = age
dict['fav_col'] = fav_col


print("Your name is ", dict['name'], " , age is ", dict['age'], ", and favourite color is", dict['fav_col'] )


"""
Task 4: Write a program that accepts user input to create two sets of integers.
Then, create a new set that contains only the elements that are common to both sets.


"""


# creating an empty list
set1, set2 = set(), set()


# number of elements as input
n = int(input("Enter the first range of numbers"))


for i in range(0, n):
    ele = int(input())
    # adding the element
    set1.add(ele)


# number of elements as input
n = int(input("Enter the Second range of numbers"))


for i in range(0, n):
    ele = int(input())
    # adding the element
    set2.add(ele)


u = set.intersection(set1, set2)


print("Intersection of lst and lst2 is", u)


"""
Task 5:Create a program that stores a list of words.
Then, use list comprehension to create a new list that
contains only the words that have an odd number of characters.
"""


lst = []


# number of elements as input
n = int(input("Enter number of words you want to input: "))


# iterating till the range
for i in range(0, n):
    ele = str(input())
    if len(ele)%2 != 0:
        # adding the element
        lst.append(ele)


print("Words of odd length are: ", lst)
