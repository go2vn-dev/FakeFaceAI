
def string_reverse(sentence):
    result = sentence.split(" ")
    revRes = result[::-1] # reverse the list
    return " ".join(revRes)

sent = input("Enter your sentence to reverse: ")
print(string_reverse(sent))
