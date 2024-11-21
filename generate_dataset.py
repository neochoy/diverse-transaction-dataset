import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_transaction_amount():
    return round(random.choice([
        random.uniform(1, 50),
        random.uniform(100, 1000),
        random.uniform(10000, 20000)
    ]), 2)

def generate_diverse_transactions(num_transactions=1000):
    data = []
    for _ in range(num_transactions):
        ip, location, geolocation_fraud = generate_geolocation()
        amount = generate_transaction_amount()
        status = generate_transaction_status()
        fraud = generate_fraud_label(amount, geolocation_fraud)
        
        data.append({
            "TransactionID": fake.uuid4(),
            "UserID": fake.uuid4(),
            "TransactionAmount": amount,
            "IP": ip,
            "Location": location,
            "TransactionStatus": status,
            "IsFraud": fraud,
            "Timestamp": fake.date_time_this_year()
        })
    return pd.DataFrame(data)
