# Given 2 strings, a and b, return the number of the
#  positions where they contain the same length 2 substring.
#  So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az"
#  substrings appear in the same place in both strings.


def string_match(a,b):
    shortestString = min(len(a), len(b))

    count = 0

    for i in range(shortestString - 1):
        subStringA = a[i:i+2]
        subStringB = b[i:i+2]

        if subStringA == subStringB:
            count += 1
    return count

print(string_match("abc","abc"))

