#import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

#create data
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
df1 = pd.read_csv('dashboard/customers_data.csv')
df2 = pd.read_csv('dashboard/some_data.csv')

all_df = pd.concat([df1, df2])

# Menyiapkan berbagai dataframe
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

# menampilkan sidebar
with st.sidebar:
    st.text('First Project SAP')
    st.text('E-commerce-public-dataset')
    option = st.selectbox(
        label="Data Apa yang ingin ditampilkan : ",
        options=('Daerah dengan pembelian terbanyak', 
                'Kota dengan pembelian terbanyak',
                'Produk yang banyak terjual',
                'Penjual dengan penjualan terbanyak',
                'Metode pembayaran yang sering digunakan'
                )
    )
        
    text = st.text_area('Please Comment About my project')
    st.write('Good comment: ', text)

 #opsi yang ada pada sidebar beserta logikanya   
if option == 'Daerah dengan pembelian terbanyak':
    
    st.header("Top 5 Daerah dengan Pembeli Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#3ED0ED", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='State', y='Number of Customers', data=customers_state_df, palette=colors)
    plt.title('Customer Distribution by State')
    plt.xlabel('State')
    plt.ylabel('Number of Customers')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa pembeli terbayak berasal dari daerah SP sebanyak 41746 pelanggan.")

#opsi yang ada pada sidebar beserta logikanya   
if option == 'Kota dengan pembelian terbanyak':
    
    st.header("Top 5 Kota dengan pembelian terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#13C7EB", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x='City', y='Number of Customers', data=customers_city_df, palette=colors)
    plt.title('Customer Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Number of Customers')
    _ = plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)
    
    # menambah keterangan
    st.write("Kota dengan pembelian terbanyak didominasi oleh kota Sao Paulo sebanyak 16% dari total kota lainnya yang membuat kota tersebut mendominasi dalam pembelian produk")

 #opsi yang ada pada sidebar beserta logikanya   
if option == 'Produk yang banyak terjual':
    
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
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa produk yang paling banyak terjual adalah yang memiliki kode 99a4788cb24856965c36a24e339b6058 sebanyak 467 item.")

 #opsi yang ada pada sidebar beserta logikanya   
if option == 'Penjual dengan penjualan terbanyak':
    
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
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa penjual terbanyak memiliki id 6560211a19b47992c3666cc44a7e94c0 sebanyak 1854 item.")

 #opsi yang ada pada sidebar beserta logikanya   
if option == 'Metode pembayaran yang sering digunakan':
    
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
    
    # menambah keterangan
    st.write("Dari diagram diatas dapat disimpulkan bahwa  metode pembayaran terbanyak menggunakan credit_card sebanyak 76505 kali.")

st.caption('Create by SAP')
