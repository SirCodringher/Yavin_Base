# 1 Zadanie

lista_zakupow = {"Piekarnia": ['Chleb', 'Pączek','Bułki'],
                 "Warzywniak": ['Marchew','Seler','Rukola']}

count = 1

for miejsca, zakupy in lista_zakupow.items():
    if miejsca == 'Piekarnia':
        print(f'Idę do: {miejsca}, kupuję tu następujące przedmioty: {zakupy}')


    elif miejsca == 'Warzywniak':
        print(f'Idę do: {miejsca}, kupuję tu następujące przedmioty: {zakupy}')

    for element in zakupy:
        count = len(element)

print(f'W sumie kupuję: {count} produktów')

# 2 Zadanie

numerki = []
potegi = []
for i in range(0,100):
    if i % 5 == 0:
        numerki.append(i)
for pot in numerki:
    potegi.append(pot**3)

print(potegi)
