import requests
import json


while True:
    sehir = input("Lütfen hava durumunu istediğiniz şehri giriniz:")

    apikey = "201df92efbc519310133bc9a8dcdd12b"

    adres = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apikey)

    baglan = requests.get(adres)

    sorgu= baglan.json()
    
    havadurumu = sorgu["weather"][0]["description"]
    havasicaklik = sorgu["main"]["temp"]
    hissedilensicaklik = sorgu["main"]["feels_like"]
    minsicaklik = sorgu["main"]["temp_min"]
    maxsicaklik = sorgu["main"]["temp_max"]
    
    print("{} için Hava durumu bilgileri aşağıdaki gibidir.\n\nSıcaklık: {} derecedir.\nDurum: {}\nHissedilen Sıcaklık: {}\nEn düşük sıcaklık: {}\nEn yüksek sıcaklık: {}".format(sehir,havasicaklik,havadurumu,hissedilensicaklik,minsicaklik,maxsicaklik))   