sign = 'sagitarrius'
file = "C:\\Users\\15134\\Astrology\\Astrology_Mapping\\doc\\comma_separated_astrology\\" + sign + ".txt"
f = open(file)
lis = list()
for l in f:
    spli = l.strip().split(', ')
    for i in spli:
        if i != "":
            lis.append(i)
from need_this.models import Individual, Zodiac
for item in lis:
    i = Individual.objects.create(name=item, 
                                  wiki="https://en.wikipedia.org/wiki/" + item.replace(" ", "_"), 
                                  zodiac=Zodiac.objects.filter(sign=sign.capitalize()).first())