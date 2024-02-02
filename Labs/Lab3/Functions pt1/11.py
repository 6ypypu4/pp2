def is_palindrome(sentence):
    revsentence = "".join(reversed(sentence))
    if sentence == revsentence:
        return True
    return False

sentence = str(input())
is_palindrome(sentence)