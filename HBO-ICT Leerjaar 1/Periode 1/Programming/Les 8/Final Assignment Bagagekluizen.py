keuze1 = '1: Ik wil weten hoeveel kluizen nog vrij zijn '
keuze2 = '2: Ik wil een nieuwe kluis '
keuze3 = '3: Ik wil even iets uit mijn kluis halen '

print(keuze1)
print(keuze2)
print(keuze3)

keuze_input = int(input('Maak uw keuze: '))

kluizen = 12
alle_kluizen = []
for i in range(1, 13):
    alle_kluizen.append(i)


def toon_aantal_kluizen_vrij():
    bestand = open('kluizen.txt', 'r')
    aantal = len(bestand.readlines())
    bestand.close()
    vrij = kluizen - aantal
    print('Er zijn', vrij, 'kluizen vrij.')


def nieuwe_kluis():
    bestand = open('kluizen.txt', 'r')
    list = bestand.readlines()
    bestand.close()
    for kluis in list:
        waarde = kluis.split(';')
        alle_kluizen.remove(int(waarde[0]))
    if alle_kluizen == []:
        print('Er zijn geen kluizen beschikbaar.')
    else:
        pincode = input('Voor een wachtwoord in: ')
        bestand = open('kluizen.txt', 'a')
        bestand.write("\n{};{}".format(alle_kluizen[0], pincode))
        print('Dit is uw kluisnummer:', alle_kluizen[0])
        bestand.close()


def kluis_openen():
    bestand = open('kluizen.txt', 'r')
    checkwaarde = bestand.readlines()
    checklist = []
    for check in checkwaarde:
        check = check.strip('\n')
        checklist.append(check)
    kluisnummer = input('Voer uw kluisnummer in: ')
    wachtwoord = input('Voer uw wachtwoord in: ')
    combinatie = kluisnummer + ';' + wachtwoord
    if combinatie in checklist:
        print('Uw kluis is nu geopend.')
    else:
        print('De gegevens komen niet overeen.')


while True:
    if keuze_input == 1:
        toon_aantal_kluizen_vrij()
        break
    elif keuze_input == 2:
        nieuwe_kluis()
        break
    elif keuze_input == 3:
        kluis_openen()
        break
    else:
        print('Vul geldige waarde in.')
        break