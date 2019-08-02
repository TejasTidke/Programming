# 1.  If the length is even, every unique character in the input has to occur a multiple of 2 times.
# 2.  If the length is odd, every unique character except one has to occur a multiple of 2 times and
#       Only 1 character is allowed to not occur a multiple of 2 times.


def can_permutation_palindrome(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    odd_count = 0
    for count in counter.values():
        odd_count += count % 2
    return odd_count in [0, 1]


result1 = can_permutation_palindrome("amamd")   # madam is palindrome
result2 = can_permutation_palindrome("mmo")     #omo is palindrome
result3 = can_permutation_palindrome("zakka")   #akzka is palindrome
result4 = can_permutation_palindrome("tejas")   #no palindrome
result5 = can_permutation_palindrome("ttyt")    #no palindrome

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
