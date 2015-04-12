from enum import Enum


class ReversalMethods(Enum):
    slices = 1
    for_loop = 2


def reverse_string(s, reversal_method):
    if reversal_method == ReversalMethods.slices:
        #use slices to step through the string from end to beginning
        start_pos = -1 #the last position in s
        end_pos = -(len(s) + 1) #the first position in s
        step_size = -1 #negative for stepping in reverse order
        return s[start_pos:end_pos:step_size] #functionally equivalent to the commonly used shorthand s[::-1]
    
    if reversal_method == ReversalMethods.for_loop:
        s_reversed = ""
        for i in range(len(s)-1, -1, -1):
            s_reversed += s[i]
        return s_reversed


string_to_reverse = "palindrome"
print("Reversing string \"%s\":" % string_to_reverse)
print("Method 1 -- Using slices: %s" % reverse_string(string_to_reverse, ReversalMethods.slices))
print("Method 2 -- Using a for loop: %s" % reverse_string(string_to_reverse, ReversalMethods.for_loop))
print("Pretty cool, eh?")