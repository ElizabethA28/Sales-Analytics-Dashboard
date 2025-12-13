#import dependencies
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Analytics Dashboard")

#File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel file)", type=["csv", "xlsx"])


if uploaded_file is not None:
    # Read the file depending on the type
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")



    #Group by Category and calculate total sales
    sales_summary = df.groupby("Category")["$ Sales"].sum()

    #Plot bar chart using Matplotlib
    fig, ax = plt.subplots()
    sales_summary.plot(kind="bar", ax=ax, color=["blue", "green"])
    ax.set_title("Sales Performance: Juices vs Smoothies")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Sales ($)")
    ax.set_xticklabels(sales_summary.index, rotation=0)

   #Display chart in Streamlit
    st.pyplot(fig)



#Q2

    #Convert Date Ordered to datetime
    df["Date Ordered"] = pd.to_datetime(df["Date Ordered"])

    #Group by Date Ordered and compute total sales
    daily_sales = df.groupby("Date Ordered")["$ Sales"].sum()

    #Plot line chart using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(daily_sales.index, daily_sales.values, marker="o", linestyle="-", color="blue")
    ax.set_title("Daily Sales Trend")
    ax.set_xlabel("Date Ordered")
    ax.set_ylabel("Total Sales ($)")
    plt.xticks(rotation=45)

    #Display chart in Streamlit
    st.pyplot(fig)

#Q3

   #missing values (drop or fill)
    df = df.dropna(subset=["Service Satisfaction Rating"])

    #Count ratings (1–5)
    rating_counts = df["Service Satisfaction Rating"].value_counts().sort_index()

    #Plot bar chart
    fig, ax = plt.subplots()
    rating_counts.plot(kind="bar", color="blue", edgecolor="black")
    ax.set_title("Service Satisfaction Distribution")
    ax.set_xlabel("Satisfaction Rating (1-5)")
    ax.set_ylabel("Number of Customers")
    ax.set_xticklabels(rating_counts.index, rotation=0)

    #Display chart in Streamlit
    st.pyplot(fig) 

#Q4

    #Convert Date Ordered to datetime for time-series tab
    df["Date Ordered"] = pd.to_datetime(df["Date Ordered"], errors="coerce")

    #Create tabs
    tab1, tab2, tab3 = st.tabs(["Category Sales", "Sales Over Time", "Satisfaction Ratings"])

    #Tab 1: Category Sales Comparison
    with tab1:
        st.subheader("Category Sales Comparison")
        category_sales = df.groupby("Category")["$ Sales"].sum()
        fig1, ax1 = plt.subplots()
        category_sales.plot(kind="bar", ax=ax1, color=["orange", "green"])
        ax1.set_title("Sales Performance: Juices vs Smoothies")
        ax1.set_xlabel("Product Category")
        ax1.set_ylabel("Total Sales ($)")
        st.pyplot(fig1)

    #Tab 2: Sales Over Time
    with tab2:
        st.subheader("Sales Over Time")
        daily_sales = df.groupby("Date Ordered")["$ Sales"].sum()
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        ax2.plot(daily_sales.index, daily_sales.values, marker="o", linestyle="-", color="blue")
        ax2.set_title("Daily Sales Trend")
        ax2.set_xlabel("Date Ordered")
        ax2.set_ylabel("Total Sales ($)")
        plt.xticks(rotation=45)
        st.pyplot(fig2)


    #Tab 3: Satisfaction Ratings
    with tab3:
        st.subheader("Service Satisfaction Ratings")
        df = df.dropna(subset=["Service Satisfaction Rating"])
        rating_counts = df["Service Satisfaction Rating"].value_counts().sort_index()
        fig3, ax3 = plt.subplots()
        rating_counts.plot(kind="bar", ax=ax3, color="skyblue", edgecolor="black")
        ax3.set_title("Service Satisfaction Distribution")
        ax3.set_xlabel("Satisfaction Rating (1–5)")
        ax3.set_ylabel("Number of Customers")
        st.pyplot(fig3)