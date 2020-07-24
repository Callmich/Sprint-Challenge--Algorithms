'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Do I need a count? (revise)
    count = 0
    # Need to set a base case - in this case I think it would be best to be moving the string closer to 1 character as it cannot have a th if there is only one character
    if len(word)< 2: # need to account for an empty string
        return 0
    # if word begins with th we need to add one and recurse
    elif word.startswith("th"):
        return count_th(word[1:]) + 1
    # otherwise chop one off and run it again
    else:
        return count_th(word[1:])

    

        

word = "thhtthht"

count_th(word)
    
    
