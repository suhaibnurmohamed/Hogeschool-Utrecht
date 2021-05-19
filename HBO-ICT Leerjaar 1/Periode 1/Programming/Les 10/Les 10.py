# opdracht 1

# bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Deurne', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond', 'Helmond Brouwhuis'}
# groen = {'Best', 'Boxtel', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
#
# print(bruin.intersection(groen))    # laat dezelfde gelijkheden zien
# print(groen.difference(bruin))      # laat verschil zien
# print(bruin.union(groen))           # bij elkaar

# opdracht 2

# import random
#
# def monopolyworp():
#     count = 0
#     while True:
#         vraag = input('Press enter to roll dice...')
#         worp1 = random.randrange(1, 7)
#         worp2 = random.randrange(1, 7)
#         som = worp1 + worp2
#         if len(vraag) == 0:
#             if worp1 == worp2 and count < 2:
#                 count += 1
#                 print(count)
#                 print('{} + {} = {} (dubbel)'.format(worp1, worp2, som))
#             elif count == 2 and worp1 == worp2:
#                 print('{} + {} = {} (direct naar gevangenis)'.format(worp1, worp2, som))
#                 break
#             else:
#                 print('{} + {} = {}'.format(worp1, worp2, som))
#         else:
#             print('Klaar')
#             break
#
# monopolyworp()

# opdracht 3

# def code(invoerstring):
#     tekens = []
#     vertaling = []
#     for letter in invoerstring:
#         nieuw = ord(letter) + 3
#         tekens.append(nieuw)
#     for waarde in tekens:
#         string = chr(waarde)
#         vertaling.append(string)
#         str = ''.join(vertaling)
#     print(str)
#
#
# code('RutteAlkmaarDen Helder')

# opdracht 4 INGELEVERD IN CANVAS
