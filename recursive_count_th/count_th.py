'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     # Do I need a count? (revise)
#     count = 0
#     # Need to set a base case - in this case I think it would be best to be moving the string closer to 1 character as it cannot have a th if there is only one character

#     def helper(x):
#         nonlocal count

#         if len(x) < 2: # need to account for an empty string
#             return 0

#     # if the first two characters of the string are th we can return 1
#         if x.startswith('th'):
#             count =+ 1

#     # Next I think I want to return the recursion. in this case I think it would be best to run the same function but just eliminating the first character of the string of the string
#         return count_th(x[1:])
    
#     helper(word)

#     return count


def count_th(word):
    count = 0
    if len(word) < 2: # need to account for an empty string
        return count + 0
    def helper(x):
        
        if x.startswith('th'):
            return count + 1
            
    
    count_th(word[1:])
    helper(word)
    return count

        

word = "thhtthht"

count_th(word)
    
    
