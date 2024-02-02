from itertools import permutations
def stringpermutations(string):
    perms = permutations(string)
    perm_strings = [''.join(perm) for perm in perms]
    for perm in perm_strings:
        print(perm)

stringa = str(input())
stringpermutations(stringa)