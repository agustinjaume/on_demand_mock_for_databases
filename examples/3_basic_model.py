from faker import Faker
fake = Faker()
import csv, datetime, os

fake = Faker(['es_ES']) 
total= 10
today = datetime.date.today()
output="database-"+ str(today) + ".csv"
data = []
count = 0


for _ in range(total):
        count +=1
        name = fake.name()
        address = fake.address()
        color = fake.color()
        phone = fake.phone_number()
        nif = fake.doi()
        ssn = fake.ssn()
        cp = "cp: " + fake.postcode()
        count_bank = "count_bank: " + fake.iban()
        data = [
                count, 
                name ,
                nif,
                address ,
                cp , 
                color , 
                phone , 
                ssn,
                count_bank 
                ]
        print(data)