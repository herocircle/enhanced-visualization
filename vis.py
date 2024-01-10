import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Title for your dashboard
st.title("Enhanced Payout Dashboard")

# Reading JSON data
json_file_path = 'payout.json'  # replace with your JSON file path
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Displaying basic JSON data in structured form
st.subheader("Basic Data")
st.write("Total Payouts:", data["totalPayouts"])
st.write("Total Commission:", data["totalCommission"])
st.write("Total Tax:", data["totalTax"])


# Displaying 'totalCirclePayouts' in a table with sorting
st.subheader("Total Circle Payouts")
circle_payouts_df = pd.DataFrame(
    data["totalCirclePayouts"].items(), columns=['Circle', 'Amount'])
st.write(circle_payouts_df)

# Plotting 'totalCirclePayouts' as a bar chart
st.subheader("Total Circle Payouts Chart")
fig = px.bar(circle_payouts_df, x='Circle', y='Amount', color='Circle')
st.plotly_chart(fig)

# Transforming and displaying 'mobilizerCirclePayouts' in a sortable table
mobilizer_list = []
for mobilizer, circles in data["mobilizerCirclePayouts"].items():
    for circle, amount in circles.items():
        mobilizer_list.append(
            {"Mobilizer": mobilizer, "Circle": circle, "Amount": amount})
mobilizer_df = pd.DataFrame(mobilizer_list)
st.subheader("Mobilizer Circle Payouts Table")
st.write(mobilizer_df)

# Converting 'breakdown' to a DataFrame and displaying it with sorting
st.subheader("Detailed Breakdown")
breakdown_df = pd.DataFrame(data["breakdown"])
st.write(breakdown_df)
