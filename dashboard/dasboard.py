import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_customers_state_df(df):
    customers_state_df = df.groupby('customer_state')['customer_unique_id'].nunique().sort_values(ascending=False).head(5)

    return customers_state_df

def create_customers_city_df(df):
    customers_city_df = df.groupby('customer_city')['customer_unique_id'].nunique().sort_values(ascending=False).head(5)

    return customers_city_df

def create_orders_items_df(df):
    orders_items_df = df.groupby('product_id')['order_id'].nunique().sort_values(ascending=False).head(5)

    return orders_items_df

def create_orders_seller_df(df):
    orders_seller_df = df.groupby('seller_id')['order_id'].nunique().sort_values(ascending=False).head(5)

    return orders_seller_df

def create_orders_payments_df(df):
    orders_payments_df = df.groupby('payment_type')['order_id'].nunique().sort_values(ascending=False).head(5)

    return orders_payments_df


# Load cleaned data
df1 = pd.read_csv(r'https://raw.githubusercontent.com/suryaadi45/Submision/refs/heads/main/dasboard/some_data.csv')
df2 = pd.read_csv(r'https://raw.githubusercontent.com/suryaadi45/Submision/refs/heads/main/dasboard/customers_dataset.csv')

all_df = pd.concat([df1, df2])

# # Menyiapkan berbagai dataframe
customers_state_df = create_customers_state_df(all_df)
customers_city_df = create_customers_city_df(all_df)
orders_items_df = create_orders_items_df(all_df)
orders_seller_df = create_orders_seller_df(all_df)
orders_payments_df = create_orders_payments_df(all_df)

# Anggap customers_state_df adalah Series
customers_state_df = pd.DataFrame({'State': customers_state_df.index, 'Number of Customers': customers_state_df.values})
customers_city_df = pd.DataFrame({'City': customers_city_df.index, 'Number of Customers': customers_city_df.values})
orders_items_df = pd.DataFrame({'Product ID': orders_items_df.index, 'Number of Orders': orders_items_df.values})
orders_seller_df = pd.DataFrame({'Seller ID': orders_seller_df.index, 'Number of Orders': orders_seller_df.values})
orders_payments_df = pd.DataFrame({'Payment Type': orders_payments_df.index, 'Number of Payment': orders_payments_df.values})

st.title('SUBMISION')
 
with st.sidebar:
    
    st.text('First Project SAP')
    
    st.text('E-commerce-public-dataset')

    text = st.text_area('Please Comment About my project')
    st.write('Good comment: ', text)

tab1, tab2 = st.tabs(["State", "City"])
 
with tab1:
    st.header("5 Daerah dengan Pembeli Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#3ED0ED", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='State', y='Number of Customers', data=customers_state_df, palette=colors)
    plt.title('Customer Distribution by State')
    plt.xlabel('State')
    plt.ylabel('Number of Customers')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)
 
with tab2:
    st.header("5 Kota dengan Pembeli Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='City', y='Number of Customers', data=customers_city_df, palette=colors)
    plt.title('Customer Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Number of Customers')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)
 

with st.container():
    plt.figure(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]


    st.header("Top 5 Produk Terlaris")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='Product ID', y='Number of Orders', data=orders_items_df, palette=colors)
    plt.title('TOP Produk')
    plt.xlabel('Product ID')
    plt.ylabel('Number of Orders')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

with st.container():
    plt.figure(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]


    st.header("Top 5 ID Seller dengan Penjualan Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='Seller ID', y='Number of Orders', data=orders_seller_df, palette=colors)
    plt.title('TOP Saller Distribution')
    plt.xlabel('Seller ID')
    plt.ylabel('Number of Orders')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

with st.container():
    plt.figure(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]


    st.header("Top 5 Tipe Pembayaran Terbaik")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='Payment Type', y='Number of Payment', data=orders_payments_df, palette=colors)
    plt.title('TOP Payment Type')
    plt.xlabel('Payment Type')
    plt.ylabel('Number of Payment')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)


st.caption('Create by SAP')
