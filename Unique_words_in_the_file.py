# Implementing the task - find the all unique words from the file and show their numbers of meeting in it
# Showing the result in order it occured in the initial string
# Reading the file and putting datato the string
string = ''
with open('dataset_50_12.txt') as inf:
    for line in inf:
        string += line.strip()
        string += ' '

# It is important to use split() in order to write the words in the string as separate elements but not the letters
string_check = string.split()  # Extra string for checking
string = string.split()
print(string)  # Checking if the string was created properly

# Creating a set and writing in it the string
# The repeated elements will not be written
s = set(string)  # Creating the set with elements from the string but it will not add repeated elements
print(s)  # Checking if the set was created properly

# Going through the elements of the set and creating the dictionary with frequency
d = {}
for x in s:
    d[x] = string.count(x)

# Showing the result in order it occured in the initial string
print(len(s))  # The number of unique elements
for i in range(len(string)):
    if string[i] != ' ':
        print(string[i], d[string[i]])
        
    for j in range(i, len(string)):
        if string[j] == string_check[i]:
            string[j] = ' '

