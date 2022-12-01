from collections import Counter

текст = input("Введіть текст: ")

split_it = текст.split()

Counter = Counter(split_it)


most_occur = Counter.most_common(5)

print(most_occur)
from collections import Counter

a = input("a:")
split_it = a.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(5)
print(most_occur)
my_str  = input("Введіть текст:")

words = [word.lower() for word in my_str.split()]

words.sort()


print("Посортовані слова :")
for word in words:
   print(word)