import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data
"""

customers_df = pd.read_csv("https://raw.githubusercontent.com/suryaadi45/Submision/refs/heads/main/Data/customers_dataset.csv")
customers_df.head()

orders_items_df = pd.read_csv("https://raw.githubusercontent.com/suryaadi45/Submision/refs/heads/main/Data/order_items_dataset.csv")
orders_items_df.head()

order_payments_df = pd.read_csv("https://raw.githubusercontent.com/suryaadi45/Submision/refs/heads/main/Data/order_payments_dataset.csv")
order_payments_df.head()

"""**Insight:**
- Pengambilan data Costumers
- Pengambilan data Order Items
- Pengambilan data Order Payments

### Assessing Data
"""

customers_df.info()

print("Jumlah duplikasi: ", customers_df.duplicated().sum())
customers_df.isna().sum()

orders_items_df.info()

orders_items_df.isna().sum()

print("Jumlah duplikasi: ", orders_items_df.duplicated().sum())
orders_items_df.describe()

order_payments_df.info()

order_payments_df.isna().sum()

print("Jumlah duplikasi: ", order_payments_df.duplicated().sum())
order_payments_df.describe()

"""**Insight:**
- Data costumers tidak ada keanehan
- Data orders_items terdapat nilai maksimal yang lebih tinggi dibanding lainnya di price
- Data orders_payments terdapat nilai maksimal yang lebih tinggi dibanding lainnya di payment value

### Cleaning Data
"""

orders_items_df[orders_items_df.price == orders_items_df.price.max()]

orders_items_df.groupby(by="price").agg({
    "order_item_id": "nunique",
    "price": ["max", "min", "mean", "std"]
})

orders_items_df.groupby(by="freight_value").agg({
    "order_id": "nunique",
    "freight_value": ["max", "min", "mean", "std"]
})

print("freight_value", "sum")

order_payments_df[order_payments_df.payment_value == order_payments_df.payment_value.max()]

order_payments_df.groupby(by="payment_value").agg({
    "order_id": "nunique",
    "payment_value": ["max", "min", "mean", "std"]
})

"""**Insight:**
- Pengecekan dan Perapian Data Orders Items
- Pengecekan dan Perapian Data Orders Payments

## Exploratory Data Analysis (EDA)

### Explore ...
"""

some_df = pd.merge(
    left=orders_items_df,
    right=order_payments_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
some_df.head()

some_df.groupby(by=["seller_id", "product_id"]).agg({
    "order_item_id": "sum",
    "price": "sum"
})

some_df.groupby(by=["payment_type", "order_id"]).agg({
        "payment_installments": "sum",
        "payment_value": "sum"
})

some_df.groupby(by=["payment_type"]).agg({
        "price": "sum",
        "payment_value": "sum"
})

some_df.to_csv("some_data.csv", index=False)

customers_df.describe(include="all")

customers_df.sample(5)

customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)

customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

orders_items_df.describe(include="all")

orders_items_df.sample(5)

orders_items_df.groupby(by="product_id").order_item_id.nunique().sort_values(ascending=False)

orders_items_df.groupby(by="seller_id").order_item_id.nunique().sort_values(ascending=False)

order_payments_df.describe(include="all")

order_payments_df.sample(5)

order_payments_df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False)

some_df.to_csv("some_data.csv", index=False)

"""**Insight:**
- Mendapatkan 5 costumer state dan costumer city terbanyak
- Mendapatkan produk yang terlaris dan penjual yang paling banyak pembeli
- Mendapatkan metode pembayaran terbanyak

## Visualization & Explanatory Analysis

### Pertanyaan 1:
"""

state_counts = customers_df.groupby('customer_state')['customer_unique_id'].nunique().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
colors = ["#3ED0ED", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x=state_counts.index, y=state_counts.values, palette=colors)
plt.title('Customer Distribution by State')
plt.xlabel('State')
plt.ylabel('Number of Customers')
_ = plt.xticks(rotation=45, ha='right')

state_counts = customers_df.groupby('customer_city')['customer_unique_id'].nunique().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x=state_counts.index, y=state_counts.values, palette=colors)
plt.title('Customer Distribution by City')
plt.xlabel('City')
plt.ylabel('Number of Customers')
_ = plt.xticks(rotation=45, ha='right')

"""### Pertanyaan 2:"""

state_counts = orders_items_df.groupby('product_id')['order_id'].nunique().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x=state_counts.index, y=state_counts.values, palette=colors)
plt.title('Product Sales Distribution')
plt.xlabel('Product ID')
plt.ylabel('Number of Orders')
_ = plt.xticks(rotation=45, ha='right')

"""### Pertanyaan 3:"""

state_counts = orders_items_df.groupby('seller_id')['order_id'].nunique().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x=state_counts.index, y=state_counts.values, palette=colors)
plt.title('TOP Saller Distribution')
plt.xlabel('Seller ID')
plt.ylabel('Number of Orders')
_ = plt.xticks(rotation=45, ha='right')

"""### Pertanyaan 4:"""

state_counts = order_payments_df.groupby('payment_type')['order_id'].nunique().sort_values(ascending=False).head(5)

plt.figure(figsize=(12, 6))
colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x=state_counts.index, y=state_counts.values, palette=colors)
plt.title('TOP Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Number of Payment')
_ = plt.xticks(rotation=45, ha='right')

"""**Insight:**
- Menampilkan 5 daerah dengan pembeli terbanyak
- Menampilkan 5 produk dengan pembelian terbanyak
- Menampilkan 5 ID penjual barang terbanyak
- Menampilkan 5 metode pembayaran

## Conclusion

- Costumer terbanyak berasal dari daerah SP yang paling banyak dari daerah Sao Paulo
- Produk ID 9571759451b1d780ee7c15012ea109d4 memiliki penjualan terbanyak
- Penjual dengan ID 2709af9587499e95e803a6498a5a56e9 memiliki penjualan terbanyak
- Metode yang digunakan terbanyak dalam pembayaran menggunakan Credit Card
"""
