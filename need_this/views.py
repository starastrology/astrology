from django.http import HttpResponse
from django.urls import reverse
from .models import Zodiac, Individual

def Index(self):
    z = Zodiac.objects.all().order_by('value')
    html = "<html><head><style>ul{color:orange;}li{display:inline; padding: 0 5px;} \
    body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} div{text-align: center; margin-top: 600px;}</style></head><body> \
    <a href='" + reverse('splash') + "'>Back</a><h1>Celebrity Astrology</h1><ul>"
    for v in z:
        html += "<li><a href='" + reverse('individuals', kwargs={'zodiac_value': v.value}) + "'>" + v.sign + "</a></li>"
    html += "</ul></body></html>"
    return HttpResponse(html)

def Individuals(self, zodiac_value):
    inds = Individual.objects.filter(zodiac=Zodiac.objects.filter(value=zodiac_value).first()).order_by('name')
    html = "<html><head><style>ul{color:orange;}li:nth-child(even){padding:0 !important;}li{display:inline; padding: 0 5px;}body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} a{font-size: 9px;} div{text-align: center; margin-top: 600px;}</style></head><body> \
    <a href='" + reverse('index') + "'>Back</a><h1>" + Zodiac.objects.filter(value=zodiac_value).first().sign + "</h1><ul>"
    for i in inds:
        html += "<li><a target=_blank href='" + i.wiki + "'>" + i.name + "</a></li>"
    html += "</ul></body></html>"
    return HttpResponse(html)

def Splash(self):
    html = "<style>body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} h1{text-align:center;}div{text-align: center; margin-top: 500px;}</style>"
    html += "<body><h1>Star Astrology!</h1><div><button><a href='" + reverse('index') + "'>Celebrity Astrology</a></button> \
    <button><a href='" + reverse('calculator') + "'> \
    Find Your Sign</a></button></div>"
    html += "</body>"
    return HttpResponse(html)

def Calculator(self):
    html = "<html><head><style>body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} form,h3{text-align: center;}</style></head><body>"
    html += "<a href='" + reverse('splash') + "'>Back</a><h3>Your birthday</h3><form action='calculate' method='POST'><select name=month><option value=01>January</option> \
    <option value=02>February</option> \
    <option value=03>March</option> \
    <option value=04>April</option> \
    <option value=05>May</option> \
    <option value=06>June</option> \
    <option value=07>July</option> \
    <option value=08>August</option> \
    <option value=09>September</option> \
    <option value=10>October</option> \
    <option value=11>November</option> \
    <option value=12>December</option> \
    </select><select name=day>"
    for i in range(1, 32):
        if i >= 10:
            html += "<option value=" + str(i) + ">" + str(i) + "</option>"
        else:
            html += "<option value=0" + str(i) + ">" + str(i) + "</option>"
    html += "</select><select name=year>"
    for i in range(1900, 2022):
        html += "<option>" + str(i) + "</option>"
    html += "</select></br></br><input type=submit />"
    import django.middleware.csrf
    token = django.middleware.csrf.get_token(self)
    html += "<input type=hidden name=csrfmiddlewaretoken value='" + token + "'></form></body></html>"
    return HttpResponse(html)

def get_astro(sum):
    astro = 0
    rem = sum % 12
    sum /= 12
    sum = int(sum)
    if rem == 0:
        astro = (sum + 1) % 12
    elif rem == 1:
        if sum % 2 == 0:
            astro = int(sum / 2)
        elif sum < 6:
            astro = int(sum * 2)
        else:
            astro = sum - 6
    elif rem == 2:
        astro = ((sum - 4) + 12) % 12
    elif rem == 3:
        astro = (sum + 4) % 12
    elif rem == 4:
        astro = ((sum - 1) + 12) % 12
    elif rem == 5:
        astro = ((sum - 2) + 12) % 12
    elif rem == 6:
        astro = (sum + 6) % 12
    elif rem == 7:
        astro = ((sum - 5) + 12) % 12
    elif rem == 8:
        astro = (sum + 2) % 12
    elif rem == 9:
        if sum != 7:
            astro = sum
        else:
            astro = 1
    elif rem == 10:
        astro = (sum + 3) % 12
    else:
        astro = ((sum - 3) + 12) % 12
    if astro == 0:
        astro = 12
    return astro

def Calculate(self):
    month = self.POST.get('month')
    day = self.POST.get("day")
    year = self.POST.get('year')

    from flatlib.datetime import Datetime
    from flatlib.geopos import GeoPos
    from flatlib.chart import Chart
    from flatlib import const
    from flatlib import props
    
    date = Datetime(str(year) + '/' + str(month) + '/' + str(day), '12:00', '+00:00')
    pos = GeoPos('38n32', '8w54')
    lis = const.LIST_OBJECTS
    if "Chiron" in lis:
        lis.remove('Chiron')
    chart = Chart(date, pos, IDs=lis)
    numbers = props.sign().number
    sun = chart.get(const.SUN).sign
    sun = (numbers.get(sun) + 3) % 12
    if sun == 0:
        sun = 12
    moon = chart.get(const.MOON).sign
    moon = (numbers.get(moon) + 3) % 12
    if moon == 0:
        moon = 12
    mercury = chart.get(const.MERCURY).sign
    mercury = (numbers.get(mercury) + 3) % 12
    if mercury == 0:
        mercury = 12
    venus = chart.get(const.VENUS).sign
    venus = (numbers.get(venus) + 3) % 12
    if venus == 0:
        venus = 12
    mars = chart.get(const.MARS).sign
    mars = (numbers.get(mars) + 3) % 12
    if mars == 0:
        mars = 12
    jupiter = chart.get(const.JUPITER).sign
    jupiter = (numbers.get(jupiter) + 3) % 12
    if jupiter == 0:
        jupiter = 12
    saturn = chart.get(const.SATURN).sign
    saturn = (numbers.get(saturn) + 3) % 12
    if saturn == 0:
        saturn = 12
    uranus = chart.get(const.URANUS).sign
    uranus = (numbers.get(uranus) + 3) % 12
    if uranus == 0:
        uranus = 12
    neptune = chart.get(const.NEPTUNE).sign
    neptune = (numbers.get(neptune) + 3) % 12
    if neptune == 0:
        neptune = 12
    pluto = chart.get(const.PLUTO).sign
    pluto = (numbers.get(pluto) + 3) % 12
    if pluto == 0:
        pluto = 12
    north_node = chart.get(const.NORTH_NODE).sign
    north_node = (numbers.get(north_node) + 3) % 12
    if north_node == 0:
        north_node = 12

    if int(day) < 10:
        day = day[1]
    if int(month) < 10:
        month = month[1]

    import requests
    response = requests.get('https://widgets.astro-seek.com/calculate-lilith/',\
                         params={'muz_narozeni_den': day,\
                               'muz_narozeni_mesic': month,\
                               'muz_narozeni_rok': year,\
                               'muz_narozeni_hodina': '12',\
                               'muz_narozeni_minuta': '00',\
                               'muz_narozeni_city': 'Seattle, USA, Washington',\
                                 'muz_narozeni_mesto_hidden': 'Seattle',\
                                 'muz_narozeni_stat_hidden': 'US',\
                                 'muz_narozeni_podstat_hidden': 'Washington'})
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    td = soup.find_all('td')[4]
    import re
    lilith = 1
    for i, k in enumerate(list(numbers.keys())):
        if k in td.img['alt']:
            lilith = (i + 4) % 12
            if lilith == 0:
                lilith == 12
            break
    sum = sun + moon + mercury + venus + mars \
      + jupiter + saturn + uranus + neptune \
      + pluto + north_node + lilith
    astro = (get_astro(sum) - 3) % 12
    if astro == 0:
        astro = 12

    sign = list(numbers.keys())[list(numbers.values()).index(astro)]

    html = "<html><head><style>body{background: lightblue url('/static/starastro.png') no-repeat fixed center; \
    background-size: 500px;} div{text-align: center;}</style> </head><body>"
    html += "<div><h1>The sign for the birthday, </h1><blockquote>" + self.POST.get('month') + "/" + self.POST.get('day') + "/" + self.POST.get('year') + "</blockquote>"
    html += "<h2>is</h2>"
    html += "<blockquote><u>" + sign + "</u></blockquote><a href='" + reverse('calculator') + "'>Back</a></body></div></html>"
    return HttpResponse(html) 