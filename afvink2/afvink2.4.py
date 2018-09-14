item1 = float(input('prijs van item 1'))
item2 = float(input('prijs van item 2'))
item3 = float(input('prijs van item 3'))
item4 = float(input('prijs van item 4'))
item5 = float(input('prijs van item 5'))

subtotaal = item1 + item2 + item3 + item4 + item5
print('de producten zonder belasting kosten',subtotaal, 'euro')

belasting = subtotaal * 0.07
print('de betaalde belasting is',belasting,'euro')

totaalbedrag = subtotaal + belasting
print('het totaal bedrag is', totaalbedrag, 'euro')
