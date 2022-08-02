from itertools import count

lista_zakupow = {'Piekarnia': ['Chleb','Pączek','Bułki'],
                'Warzywniak': ['Marchwew','Seler','Rukola']}
zakup = []

for miejsce, zakupy in lista_zakupow.items():
    zakup.append(len(zakupy))
    if miejsce == 'Piekarnia':
        print(f'Idę do {miejsce}, kupuję następujące rzeczy: {zakupy}')
    elif miejsce == 'Warzywniak':
        print(f'Idę do {miejsce}, kupuję następujące rzeczy: {zakupy}')
wszystko = sum(zakup)

print(f'Kupuję w sumie: {wszystko} przedmiotów')





