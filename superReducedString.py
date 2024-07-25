 
# I use the stack structure for practicality.

def reduce_string(s):
    stack = [] # I created an empty stack.

    for char in s:
        if stack and stack[-1] == char:
            stack.pop() # If the same character is found, it's remouved from the stack.
        else:
            stack.append(char) # Add different character to the stack.

    result = ''.join(stack) # Create the result string from the characters in the stack.
    return result if result else "Empty String"



if __name__ == '__main__': 
    s = input()
    print(reduce_string(s))
