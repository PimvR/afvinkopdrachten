suiker = 1.5 / 48
boter = 1 / 48
meel = 2.75 / 48

hoeveelcookies = float(input('hoeveel cookies wil je maken '))
totalesuiker = (hoeveelcookies * suiker)
totaleboter = (hoeveelcookies * boter)
totalemeel = (hoeveelcookies * meel)

print('je hebt ', totalesuiker, ' kopjes suiker nodig voor ', hoeveelcookies, ' cookies')
print('je hebt ', totaleboter, ' kopjes boter nodig voor ', hoeveelcookies, ' cookies')
print('je hebt ', totalemeel, ' kopjes meel nodig voor ', hoeveelcookies, ' cookies')
