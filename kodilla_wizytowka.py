from faker import Faker
fake = Faker('pl_PL')

class BaseContact:

    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.length = len(self.name) + len(self.last_name) + 1

    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone} {self.email}"

    def __repr__(self):
         return f"{self.name} {self.last_name} {self.phone} {self.email}"

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}"

    def length(self):
        return self.length

class BusinessContact(BaseContact):
    def __init__(self, posiiton, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = posiiton
        self.company = company
        self.business_phone = business_phone
        self.length = len(self.name) + len(self.last_name) + 1

    def __str__(self):
        return f"{self.name} {self.last_name} {self.phone} {self.email} {self.position} {self.company} {self.business_phone}"

    def __repr__(self):
         return f"{self.name} {self.last_name} {self.phone} {self.email} {self.position} {self.company} {self.business_phone}"

    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.last_name}"

    def length(self):
        return self.length

random_card = []

def create_contacts(card_type, quantity):

    if card_type == "BaseContact":
        for number in range(quantity):
            random_card.append(BaseContact(name=fake.name(), last_name=fake.last_name(), phone=fake.phone_number(), email=fake.email()))
    elif card_type == "BusinessContact":
        for number in range(quantity):
            random_card.append(BusinessContact(name=fake.name(), last_name=fake.last_name(), phone=fake.phone_number(),
                                               email=fake.email(), posiiton=fake.job(), company=fake.company(), business_phone=fake.phone_number()))
    else :
        print('Invalid contact type')
    return random_card


random_card = create_contacts("BusinessContact", 2)
single_card = random_card[0]
print(single_card.contact())