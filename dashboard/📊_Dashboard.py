import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="📊",
)

st.title("DASHBOARD E-COMMERCE CUSTOMER AND SALES ANALYSIS")

with st.sidebar:
    selected = option_menu(
        menu_title="DASHBOARD",
        options=["About Projects","Dataset Overview"],
    )

if selected == "About Projects":
    path = os.path.dirname(__file__)
    my_file = path+'/images/ds_back.png'
    image = Image.open(my_file)
    resized_image = image.resize((650, 350))
    st.image(resized_image, caption='E-Comerce Analysis Dashboard')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text("Projek ini adalah sebuah dashboard interaktif yang dibangun menggunakan Streamlit. Dataset Brazilian E-Commerce Public Dataset oleh Olis merupakan sumber data yang dipergunakan pada dashboard ini. Dataset ini berisi informasi tentang transaksi e-commerce di Brazil dan memberikan gambaran tentang tren dan pola pembelian online di negara tersebut.")


    with col2:
        st.text("Dalam dashboard ini, dibuat visualisasi data yang menarik. Visualisasi ini akan membantu untuk memahami berbagai aspek penjualan e-commerce di Brazil, termasuk informasi tentang kota dengan jumlah penjual terbanyak, kategori produk yang paling populer, dan tren pembelian selama periode waktu tertentu.")

    
    with col3:
        st.text("""Selain itu, dashboard ini juga dilengkapi dengan fitur interaktif, yang memungkinkan untuk mengeksplorasi data dengan cara yang lebih dalam.
        Tujuan dari projek ini adalah untuk memberikan dashboard yang interaktif dan informatif dalam mempelajari dan menggali informasi dari dataset E-Commerce Public Dataset.\n""")
    
    st.caption('&copy; 2024 intandwianggreini99@ds.student.pens.ac.id')

if selected == "Dataset Overview":

    st.text("""Dataset yang digunakan adalah E-Commerce Public Dataset.
    Dataset ini mencakup informasi yang dikumpulkan dari transaksi e-commerce di Brazil dalam rentang waktu tertentu. Dataset tersebut terdiri dari beberapa file yang terkait satu sama lain dan memberikan wawasan yang komprehensif tentang industri e-commerce di Brazil.\n\n\n
    Beberapa file utama dalam dataset ini termasuk:
    - Orders: File ini berisi informasi tentang pesanan, seperti ID pesanan, status pesanan, waktu pembelian, waktu persetujuan, dan waktu pengiriman pesanan.
    - Order Items: File ini berisi informasi terperinci tentang setiap item yang dibeli dalam pesanan, seperti ID produk, harga produk, jumlah yang dibeli, dan biaya pengiriman.
    - Products: File ini berisi informasi tentang produk, termasuk ID produk, kategori produk, dan nama produk.
    - Sellers: File ini berisi informasi tentang penjual, seperti ID penjual, nama penjual, dan lokasi penjual (kota dan negara bagian).
    - Customers: File ini berisi informasi tentang pelanggan, seperti ID pelanggan, nama pelanggan, dan lokasi pelanggan (kota dan negara bagian).
    - Geolocation: File ini menyediakan informasi geografis tentang kota dan negara bagian di Brazil. Ini membantu dalam analisis berdasarkan lokasi geografis. \n
    Dataset ini memungkinkan analisis yang luas tentang berbagai aspek e-commerce di Brazil. Kita dapat menganalisis tren penjualan berdasarkan waktu, kategori produk yang paling populer, preferensi pembelian pelanggan di berbagai wilayah, serta karakteristik dan lokasi penjual.
    Dengan memanfaatkan dataset ini dalam projek analisis visualisasi, Kita dapat menghasilkan pemahaman yang lebih dalam tentang pasar e-commerce di Brazil, memperoleh wawasan tentang perilaku pembelian, dan mengidentifikasi peluang atau tantangan di industri ini.\n\n\n""")

    st.caption('&copy; 2024 intandwianggreini99@ds.student.pens.ac.id')