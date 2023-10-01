import itertools

# This function calculates the numerical value of a word based on a substitution dictionary.
# For example, if word="SEND" and substitution={'S': 9, 'E': 5, 'N': 6, 'D': 7}, it returns 9567.
def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

# This function solves the equation given as a string.
def solve2(equation):
    # Split the equation into the left and right sides based on the '=' sign,
    # convert it to lowercase, and remove spaces.
    left, right = equation.lower().replace(' ', '').split('=')
    
    # Split the left side into individual words based on the '+' sign.
    left = left.split('+')
    
    # Create a set of unique letters used in the equation.
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    
    # Generate all permutations of digits for the unique letters in the equation.
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))  # Create a dictionary to map letters to digits.
        
        # Calculate the numerical values for the left side words and the right side.
        left_values = [get_value(word, sol) for word in left]
        right_value = get_value(right, sol)
        
        # Check if the equation is satisfied by comparing the sum of left side values
        # with the right side value.
        if sum(left_values) == right_value:
            # Print the solution along with the mapping of letters to digits.
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(right_value, sol))

if __name__ == '__main__':
    # Call the solve2 function with the equation 'SEND + MORE = MONEY'.
    solve2('SEND + MORE = MONEY')
