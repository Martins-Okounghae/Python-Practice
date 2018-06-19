# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front;

def front_times(str, n):

    frontchar = 3

    if frontchar < 3:
        frontchar = str

    front = str[:frontchar]

    copies = ""

    for i in range(n):
        copies = copies + front
    return copies


print( front_times( "Good", 10))
