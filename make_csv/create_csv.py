import csv
from faker import Faker
import random
import string

fake = Faker()

# Create the first CSV file with 100 records
with open('workers.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'last_name', 'birth_date', 'height_cm', 'weight_kg']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(0, 100):
        writer.writerow({
            'id': i,
            'name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.date_of_birth(minimum_age=16, maximum_age=34).strftime('%Y-%m-%d'),
            'height_cm': random.uniform(150, 200),
            'weight_kg': random.uniform(50, 120)
        })

# Create the second CSV file with related information
with open('workers_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['company', 'job', 'worker_id', 'registration_date', 'id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(0, 100):
        writer.writerow({
            'company': fake.company(),
            'job': fake.job(),
            'worker_id': ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
            'registration_date': fake.date_this_century().strftime('%Y-%m-%d'),
            'id': i
        })
