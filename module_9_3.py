first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = ((len(s1), len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))

second_result = (i == j for i, j in enumerate(len(s) for s in first) if i < len(second))

print(list(first_result))
print(list(second_result))