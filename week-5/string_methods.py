sentence = "Python is my favorite programming language!"

print(sentence)

for i in range(len(sentence)):
    if sentence[i].isalpha() and sentence[i] == sentence[i].upper():
        print(sentence[i])

count=0

for i in range(len(sentence)):
    if sentence[i].lower() == 'o':
        count+=1

print(count)

print(sentence.replace("my", "everyone's"))

print(sentence.isalpha())

print(sentence.isascii())

print(sentence.isdigit())
