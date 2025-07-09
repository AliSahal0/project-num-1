import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Bikes with Their Company Names")

# Display a simple text
st.write("Best bikes suggested for you")

# Create a simple DataFrame with bike names and random prices
df = pd.DataFrame({
    'Bike Model': [
        "Yamaha YZF-R3", "Honda CB500F", "Suzuki Gixxer SF", "Kawasaki Ninja 400", "Royal Enfield Classic 350",
        "BMW G 310 R", "KTM Duke 390", "Yamaha MT-15", "TVS Apache RR 310", "Bajaj Pulsar NS200",
        "Hero Xpulse 200", "Ducati Scrambler", "Harley-Davidson Iron 883", "Triumph Trident 660", "Kawasaki Z650"
    ],
    'Price (USD)': [
        5300, 6800, 3200, 6100, 4200,
        6500, 5000, 4000, 4600, 3500,
        2900, 9500, 9800, 8900, 7700
    ]
})

# Display the full DataFrame
st.write("### Here is the list of bikes and their prices:")
st.dataframe(df)

# Recommended bikes (e.g. price under $6000)
recommended = df[df['Price (USD)'] <= 6000]

# Display recommended bikes
st.write("### 🏍️ Recommended Bikes for You (Price ≤ $6,000):")
st.dataframe(recommended)