# Diverse Transaction Dataset for Fraud Detection

## Overview
This repository contains a **diverse transaction dataset** generated for use in fraud detection projects. The dataset simulates real-world payment transactions with features like transaction amounts, IP geolocations, user behaviors, and fraud labels.

The dataset is particularly useful for:
- Building and testing fraud detection algorithms.
- Exploring behavioral patterns in transactions.
- Practicing machine learning workflows.

---

## Dataset Features
The dataset includes the following columns:
| Column              | Description                                               |
|---------------------|-----------------------------------------------------------|
| TransactionID       | Unique identifier for each transaction.                   |
| UserID              | Unique identifier for the user making the transaction.    |
| TransactionAmount   | The monetary amount of the transaction (in USD).          |
| IP                  | Simulated IP address of the user.                         |
| Location            | City associated with the transaction (or suspicious).     |
| TransactionStatus   | Status of the transaction (success, failed, disputed).    |
| IsFraud             | Binary label indicating if the transaction is fraudulent. |
| Timestamp           | The date and time of the transaction.                     |

---

## Data Generation
The dataset was generated using Python and the `Faker` library. Key steps include:
1. **Randomized Transaction Amounts**:
   - Transactions range from small purchases to high-value payments.
2. **Simulated Geolocations**:
   - Includes mismatched IP and location data for potential fraud cases.
3. **Randomized Transaction Statuses**:
   - Transactions may be successful, failed, disputed, or refunded.
4. **Fraud Labels**:
   - Fraudulent transactions are labeled based on high-risk patterns (e.g., large amounts, mismatched geolocation).

To regenerate the dataset, use the `generate_dataset.py` script included in this repository.

---

## Instructions for Use
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/diverse-transaction-dataset.git
