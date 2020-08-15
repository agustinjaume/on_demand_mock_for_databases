from faker import Faker
fake = Faker(['es_ES']) 

print(fake.latitude())
print(fake.longitude())
