'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

s = (
("Гитлер", 20, 2.1, "Сталинград"),
("Сталин", 21, 5, "Москва"),
("Наполеон", 19, 3.9, "Гроб"),
("Алина", 22, 4.7, "Новосибирск"),
("Дмитрий", 20, 3.8, "КАЗАХСТАН"),
("Зинаида", 21, 4.1, "Ростов-на-Дону"),
("Джигизмуд 1", 19, 1.9, "Волгоград")
)
t_g = sum([s[2] for s in s])
g_g = t_g / len(s)


g_s = [s[0] for s in s if s[2] >= g_g]


print("Ученики", ", ".join(g_s), "в этом семестре хорошо учатся!")


   


