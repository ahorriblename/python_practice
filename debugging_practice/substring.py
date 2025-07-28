def matching_substring(s, sub, a, b):
    '''Given a string s and a range contained by a & b, return True if sub is in that range of s'''
    return sub in s[a:b]

def fail_this_test():
    assert matching_substring("substring", "", 0, 8) == False


fail_this_test()