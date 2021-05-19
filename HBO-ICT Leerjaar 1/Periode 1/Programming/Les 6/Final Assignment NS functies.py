def standaardprijs(afstandKM):
    if afstandKM < 50:
        return afstandKM * 0.80
    else:
        return (afstandKM - 50) * 0.60 + 15

# print(round(standaardprijs(3), 2))

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == False:
        if leeftijd > 12 and leeftijd < 65:
            return standaardprijs(afstandKM)
        if leeftijd < 12 or leeftijd >= 65:
            return standaardprijs(afstandKM) * 0.7
    elif weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardprijs(afstandKM) * 0.65
        elif leeftijd >= 12 and leeftijd <= 65:
            return standaardprijs(afstandKM) * 0.60
    else:
        return standaardprijs(afstandKM)

print(round(ritprijs(13, False, standaardprijs(50)), 2))


