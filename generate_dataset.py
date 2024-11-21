import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()


# Helper functions for diverse data
def generate_transaction_amount():
    return round(random.choice([
        random.uniform(100, 1000),  # Small amounts
        random.uniform(10000, 20000)  # High amounts
    ]), 2)


def generate_geolocation():
    ip_address = fake.ipv4()
    location = fake.city()
    fraud = random.choice([0, 1])  # Simulate mismatch as fraud
    if fraud:
        location = "Suspicious Location"
    return ip_address, location, fraud


def generate_transaction_status():
    return random.choice(["success", "failed", "disputed", "refunded"])


def generate_fraud_label(amount, geolocation_fraud, fraud_ratio=0.2):
    # Ensure fraud proportion aligns with dataset requirements
    if random.random() < fraud_ratio or amount > 10000 or geolocation_fraud == 1:
        return 1  # Fraudulent
    return 0  # Non-fraudulent


def generate_diverse_transactions(num_transactions=1000, fraud_ratio=0.2):
    data = []
    for _ in range(num_transactions):
        ip, location, geolocation_fraud = generate_geolocation()
        amount = generate_transaction_amount()
        status = generate_transaction_status()
        fraud = generate_fraud_label(amount, geolocation_fraud, fraud_ratio)

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


if __name__ == "__main__":
    # Generate dataset
    num_transactions = 1000
    fraud_ratio = 0.2  # 20% of transactions should be fraudulent
    output_path = "diverse_transactions.csv"

    print(f"Generating {num_transactions} transactions...")
    transactions = generate_diverse_transactions(num_transactions, fraud_ratio)

    # Save dataset to specified path
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    transactions.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
