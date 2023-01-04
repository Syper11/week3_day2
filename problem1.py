# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:						
# Input: ‘Joel’
# Output: ‘Jl’
# Input: ‘Shoha’
# Output: ‘Shh’

def vowels(st):
    empty = []

    vowels = ("a","e","u","i","o")
    for char in st.lower():
        if char not in vowels:
            empty.append(char)
    print(''.join(empty))

vowels('joeL')