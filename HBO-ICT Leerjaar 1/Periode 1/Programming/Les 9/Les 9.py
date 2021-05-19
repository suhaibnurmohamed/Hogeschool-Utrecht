# Opdracht 1

# count = 0
# som = 0
#
# while True:
#     geef_getal = int(input('Geef een getal: '))
#     if geef_getal != 0:
#         som += geef_getal
#         count += 1
#     else:
#         print('Er zijn {} getallen ingevoerd, de som is: {}'.format(count, som))
#         break

# opdracht 2

# while True:
#     invoer = str(input('Geef een string van vier letters: '))
#     lengte = len(invoer)
#     if lengte != 4:
#         print('{} heeft {} letters.'.format(invoer, lengte))
#     else:
#         print('Inlezen van correcte string: {} is geslaagd.'.format(invoer))
#         break

# opdracht 3

# cijfers = {
#     'Henk': 8,
#     'Adrie': 9,
#     'Bastiaan': 5,
#     'Michelle': 6,
#     'Pieter-Jan': 7.4,
#     'Anne': 9.0,
#     'Ankje': 9.3,
#     'Ligje': 4
# }
#
# for item in cijfers.values():
#     if item >= 9.0:
#         print(item)

# opdracht 4

# def ticker(filename):
#     ticker = open(filename)
#     checkwaarde = ticker.readlines()
#     lijst = {}
#     for key in checkwaarde:
#         bedrijf, afkorting = key.split(':')
#         lijst[bedrijf] = afkorting.strip('\n')
#     return lijst
#
#
# tickerdict = ticker('ticker.txt')
#
# print(tickerdict)
#
# keuze = str(input('Voer een bedrijfsnaam of Ticker in: '))
#
#
# keys = tickerdict.keys()
# values = tickerdict.values()
#
# if keuze in keys:
#     for key in keys:
#         if keuze == key:
#             x = tickerdict.get(key)
#             print(x)
# elif keuze in values:
#     for bedrijf, afkorting in tickerdict.items():
#         if afkorting == keuze:
#             print(bedrijf)

# opdracht 5

# def namen():
#     lijst = {}
#
#     while True:
#         invoer = str(input('Voer een naam in: '))
#         if len(invoer) != 0:
#             if invoer not in lijst:
#                 lijst[invoer] = 1
#             else:
#                 lijst[invoer] = lijst[invoer] + 1
#
#         else:
#             for waarde in lijst:
#                 if lijst[waarde] == 1:
#                     print('Er is ' + str(lijst[waarde]) + ' student met de naam ' + waarde)
#                 else:
#                     print('Er zijn ' + str(lijst[waarde]) + ' studenten met de naam ' + waarde)
#
#             print(lijst)
#             break
#
# namen()