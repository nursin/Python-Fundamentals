numbers_set = {1, 2, 3, 4, 4, (9,8)}
print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)
if "Alpha" in words_set:
    print("Alpha in set")
else:
    print("Alpha not in set")

words_set.add("Delta")
print(words_set)
words_set.discard("Delta")
print(words_set)

