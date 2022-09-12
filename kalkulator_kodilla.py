import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calc.log")


def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    return x / y

print("Wybierz działanie.")
print("1.Dodaj")
print("2.Odejmij")
print("3.Podziel")
print("4.Pomnóż")

while True:
    choice = input("Twój wybór(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            logging.info("Dodaj")
            def x():
                x.x = int(input("Ile liczb ma być do siebie dodanych?: "))
                logging.info(x.x)

            x()

            i = 0
            nums = []
            while i != x.x:
                liczby_dod = float(input("Napisz kolejne liczby, które mają zostać dodane: "))
                logging.info(liczby_dod)
                nums.append(liczby_dod)
                i += 1
            index = 0
            ans = 0
            while index != len(nums):
                num = nums[index]
                ans = ans + num
                index += 1
            print(f"Dodaję do siebie {nums}")
            print("\nSuma liczb to: ", ans)

        elif choice == '2':
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
            logging.info("Odejmij")
            logging.info((num1, num2))
            print(f"Odejmuję: {num1} od {num2}")
            print(num1, "-", num2)
            print("Wynik = ", odejmij(num1, num2))

        elif choice == '3':
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
            logging.info("Podziel")
            logging.info((num1, num2))
            if num2 == 0:
                logging.info(ZeroDivisionError)
                print("Nie wolno dzielić przez 0")
                break
            else:
                print(f"Dzielę: {num1} przez {num2}")
                print(num1, "/", num2)
                print("Wynik = ", podziel(num1, num2))

        elif choice == '4':
            logging.info("Pomnóż")

            def y():
                y.y = int(input("Ile liczb ma być przez siebie pomnożonych?: "))
                logging.info(y.y)
            y()

            j = 0
            nums = []
            while j != y.y:
                liczby_mnoz = float(input("Napisz kolejne liczby, które mają być przez siebie mnożone: "))
                logging.info(liczby_mnoz)
                nums.append(liczby_mnoz)
                j += 1
            index = 0
            ans = 1
            while index != len(nums):
                num = nums[index]
                ans = ans * num
                index += 1

            print(f"Mnożę przez siebie: {nums}" )
            print("\nIloczyn liczb to: ", ans)

    else:
        print("Niewłaściwy wybór")
    break
