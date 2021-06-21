
sentence = ["Python", "is", "the", "most", "powerful", "programming", "language."]

final = ''

for word in sentence:
    final += word + ' '
print(final)

# Alternatively,
final2 = ' '.join(sentence)
print(final2)