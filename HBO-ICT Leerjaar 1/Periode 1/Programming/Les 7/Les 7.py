#Opdracht 1
# def convert(celsius):
#     fahrenheit = celsius * 1.8 + 32
#     return fahrenheit
#
# def table():
#     print('F \t \t C')
#     for i in range (-30, 50, 10):
#         print(convert(float(i)), '\t' , float(i))
#
# table()

# Opdracht 2

# KN = open('Kaartnummers.txt', 'r')
# list = KN.readlines()
#
# for sentences in list:
#     kaartinfo = sentences.strip('\n')
#     new_list = kaartinfo.split(',')
#     print(new_list[1] + 'heeft kaartnummer: ' + new_list[0])

# Opdracht 3

# KN = open('Kaartnummers.txt', 'r')
# #todo, om regels te tellen
# Lines = sum(1 for line in open('Kaartnummers.txt'))
#
# data = KN.readlines()
# KN.close()
#
# #todo, om lines te stoppen in een list
# new_data = []
#
# for waarde in data:
#     x = waarde.strip('\n')
#     y = x.split(',')
#     new_data.append(y)
#
# max = max(new_data)
#
# #todo om line te zoeken bij data
# kaartnummer_index = new_data.index(max) + 1
#
# print('Deze file telt', Lines, 'regels.')
# print('Het grootste kaartnummer is:', max[0], 'en dat staat op regel', kaartnummer_index)

# opdracht 4

# import datetime
#
# vandaag = datetime.datetime.today()
# s = vandaag.strftime("%a %d %b %Y")
#
# tijd = datetime.datetime.now()
# x = tijd.strftime("%X")
#
# while True:
#     naam = input('Naam: ')
#     data = s + ' , ' + x + ' , ' + naam
#     text_file = open("Hardlopers.txt", "a") #todo, 'a' is append funtie voor file
#     text_file.write(data + '\n')
#     text_file.close()

# opdracht 5

# def gemiddelde():
#     zin = input('Voer een zin in: ')
#     alle_woorden = zin.split(' ')
#     aantal = 0
#     woorden = len(alle_woorden)
#
#     for i in alle_woorden: #todo, telt aantal letters in zin
#         for char in i:
#             aantal += 1
#
#     print(aantal / woorden)
#
#
# gemiddelde()