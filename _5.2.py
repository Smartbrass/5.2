Slovo = input("Введите слово:")
Count_Glasnie = 0
Count_Soglasnie = 0
Count_a = 0
Count_e = 0
Count_i = 0
Count_o = 0
Count_u = 0

Glasnie = set("aeiou")
Soglasnie = set("bcdfghjklmnpqrstvwxyz")
a = ("a")
e = ("e")
i = ("i")
o = ("o")
u = ("u")

for l in Slovo:
    if l in Glasnie:
        Count_Glasnie +=1
    if l in a:
            Count_a +=1
    if l in e:
            Count_e +=1
    if l in i:
            Count_i +=1
    if l in o:
            Count_o +=1
    if l in u:
            Count_u +=1  
    if l in Soglasnie:
        Count_Soglasnie +=1

print("Согласных Букв -", (Count_Soglasnie))
print("Гласных Букв -", (Count_Glasnie))
if Count_a > 0:
    print("Букв ""a"" -", (Count_a))
else:
    print("Букв ""a"" - нет")
if Count_e > 0:
    print("Букв ""e"" -", (Count_e))
else:
    print("Букв ""e"" - нет")
if Count_i > 0:
    print("Букв ""i"" -", (Count_i))
else:
    print("Букв ""i"" - нет")
if Count_o > 0:
    print("Букв ""o"" -", (Count_o))
else:
    print("Букв ""o"" - нет")
if Count_u > 0:
    print("Букв ""u"" -", (Count_u))
else:
    print("Букв ""u"" - нет")
