stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']

def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is je beginstation? ')
        if beginstation not in stations:
            print('Deze trein komt niet in {}'.format(beginstation))
        else:
            return beginstation

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation? ')
        if eindstation not in stations:
            print('Deze trein komt niet in {}'.format(eindstation))
        else:
            index1 = stations.index(eindstation)
            index2 = stations.index(beginstation)
            if index1 < index2:
                print('Deze trein is al voorbij dit station.')
            else:
                return eindstation

eindstation = inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    index1 = stations.index(eindstation)
    index2 = stations.index(beginstation)
    aantal = abs(index2 - index1)
    prijs = aantal * 5
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, index2))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, index1))
    print('De afstand bedraagt {} station(s).'.format(aantal))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('Jij stapt de trein in: {}'.format(beginstation))
    print('Jij stapt uit in: {}'.format(eindstation))

omroepen_reis(stations, beginstation, eindstation)