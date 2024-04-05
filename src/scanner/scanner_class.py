# word = input("enter numbers").split(",")
# result = []
# for i in word:
#     result.append(int(i)*int(i))
# print(result)

def convert(word):
    result = []
    for i in word.split(","):
        result.append(int(i)*int(i))
    return result
