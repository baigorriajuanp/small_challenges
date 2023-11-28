"""Create Acronyms using Python
To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence. 
You can do this by splitting and indexing to get the first word and then combine it. Let’s see how to create an acronym using Python:"""

def acronyms(string):
    return ''.join([str(chain[0]) for chain in string.split()])


print(acronyms(input("Enter the phrase: ")))