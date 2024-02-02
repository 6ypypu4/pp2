def reverseback(string):
    reversecentence = ""
    for i in range(0, len(sentence)):
        reversecentence = sentence[i] + " " + reversecentence
    return reversecentence

sentence = input().split(" ")
reversecentence = reverseback(sentence)
print(reversecentence)