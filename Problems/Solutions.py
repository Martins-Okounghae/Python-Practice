#Given a string and a non-negative int n,
#  return a larger string that is n copies of the original string.

def string_times(str, n):
    result = ""
    for i in range(n):
        result += str
    return result


print(string_times("Hello", 10))


