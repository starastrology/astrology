from need_this.models import Individual, Zodiac

inds = Individual.objects.all()
for i in inds:
    if "," in i.name:
        print(i.name)
        i.name = i.name.replace(',','')
        i.wiki = i.wiki.replace(',','')
        i.save()