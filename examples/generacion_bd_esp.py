from faker import Faker
import csv, datetime, pandas, os

fake = Faker(['es_ES']) 
total= 10
today = datetime.date.today()
output="database-"+ str(today) + ".csv"

def create_csv(total):
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
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(data)
        print(data)

try:
    salidacsv = open(output, 'w')
    cabecera = ['count','name' ,'nif', 'address' , 'cp' , 'color' , 'phone' , 'ssn', 'count_bank' ]
    salida = csv.DictWriter(salidacsv, fieldnames=cabecera)
    salida.writeheader()
    with open(output,"w", encoding='UTF-8') as f:
        create_csv(total)
    print('Se ha creado el archivo: ' + output )

finally:
    salidacsv.close()