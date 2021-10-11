# numbers_sets = {1, 2, 3, 4, (5, 6)}
# print(numbers_sets)

words_set = {"alpha", "bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)

if "feee" in words_set:
    print("Alpha in set")
else:
    print("NO no no no no")

words_set.add("Delta")
print(words_set)
words_set.discard("bravo")
print(words_set)
my_string = "Nucamp"
print(my_string[3:5])
