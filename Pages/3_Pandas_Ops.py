import streamlit as st
import pandas as pd
import numpy as np


st.title("Pandas Operations")

st.header("Part - A : Data Exploration")
with st.expander("Q-1 : Load the dataset into a DataFrame"):
    customers = pd.read_csv('D:/MCA/ML Ass/Data-Analysis-Using-ML/Datasets/Ecommerce_Purchases.csv')
    salaries = pd.read_csv('D:/MCA/ML Ass/Data-Analysis-Using-ML/Datasets/Salaries.csv')
    st.write(customers)
    st.write(salaries)

with st.expander("Q-2 : Display the first 5 rows of the DataFrame"):
    st.write("First 5 rows of the DataFrame:",customers.head())
    st.write("Last 5 rows of the DataFrame:",customers.tail())

with st.expander("Q-3 : Find Rows, Columns, Data Types, Missing Values and Duplicate Records"):
    st.write("Shape :", customers.shape)
    st.write("Rows :", customers.shape[0])
    st.write("Columns :", customers.shape[1])

    st.subheader("Data Types")
    st.write(customers.dtypes)

    st.subheader("Missing Values")
    st.write(customers.isnull().sum())

    st.write("Total Missing Values :", customers.isnull().sum().sum())

    st.subheader("Duplicate Records")
    st.write("Total Duplicate Records :", customers.duplicated().sum())


st.header("Part - B : Customer Analytics")

with st.expander("Q-1 : Average, Maximum and Minimum Purchase Price"):
    st.write("Average Purchase Price :", customers["Purchase Price"].mean())
    st.write("Maximum Purchase Price :", customers["Purchase Price"].max())
    st.write("Minimum Purchase Price :", customers["Purchase Price"].min())

with st.expander("Q-2 : Top 10 Most Expensive Purchases"):
    st.dataframe(customers.nlargest(10, "Purchase Price"))

with st.expander("Q-3 : Customers Preferred Language"):
    st.write("English :", (customers["Language"] == "en").sum())
    st.write("French :", (customers["Language"] == "fr").sum())
    st.write("German :", (customers["Language"] == "de").sum())

with st.expander("Q-4 : Customers by Credit Card Provider"):
    st.write("Visa :", (customers["CC Provider"] == "Visa").sum())
    st.write("MasterCard :", (customers["CC Provider"] == "Mastercard").sum())
    st.write("American Express :", (customers["CC Provider"] == "American Express").sum())

with st.expander("Q-5 : Five Most Common Job Titles"):
    st.dataframe(customers["Job"].value_counts().head(5))


st.header("Part - C : Business Insights")

with st.expander("Q-1 : Email Provider / Credit Card Provider Count"):
    st.dataframe(customers["CC Provider"].value_counts())

with st.expander("Q-2 : Total Sales, Average Sales and Median Purchase Price"):
    st.dataframe(customers["Purchase Price"].agg(["sum", "mean", "median"]))

with st.expander("Q-3 : Create Purchase Category"):
    def category(price):
        if price < 30:
            return "Low"
        elif price <= 60:
            return "Medium"
        else:
            return "High"

    customers["Purchase Category"] = customers["Purchase Price"].apply(category)
    st.dataframe(customers.head())

with st.expander("Q-4 : Percentage of Customers in Each Category"):
    st.dataframe(customers["Purchase Category"].value_counts(normalize=True) * 100)


st.header("Part - D : Advanced Pandas")

with st.expander("Q-1 : Company with Lowest Average Purchase Price"):
    company_avg = customers.groupby("Company")["Purchase Price"].mean().sort_values()
    st.dataframe(company_avg.head(1))

with st.expander("Q-2 : Credit Card Provider Revenue"):
    cc_revenue = customers.groupby("CC Provider")["Purchase Price"].sum().sort_values()
    st.dataframe(cc_revenue.head(1))

with st.expander("Q-3 : Browser Users Spending"):
    browser_spending = customers.groupby("Browser Info")["Purchase Price"].sum().sort_values()
    st.dataframe(browser_spending.head(1))


# --------------------- Salaries Dataset ---------------------

st.header("SF Employee Salary Analysis")

with st.expander("Q-1 : Display Head, Tail, Shape, Data Types and Summary"):
    st.write("Head")
    st.dataframe(salaries.head())

    st.write("Tail")
    st.dataframe(salaries.tail())

    st.write("Shape :", salaries.shape)

    st.write("Data Types")
    st.write(salaries.dtypes)

    st.write("Summary Statistics")
    st.dataframe(salaries.describe())


st.header("Part - B : Salary Analysis")

with st.expander("Q-1 : Highest Salary"):
    st.write(salaries["TotalPayBenefits"].max())

with st.expander("Q-2 : Lowest Salary"):
    st.write(salaries["TotalPayBenefits"].min())

with st.expander("Q-3 : Average BasePay"):
    st.write(salaries["BasePay"].mean())

with st.expander("Q-4 : Average OvertimePay"):
    st.write(salaries["OvertimePay"].mean())

with st.expander("Q-5 : Average TotalPayBenefits"):
    st.write(salaries["TotalPayBenefits"].mean())

with st.expander("Q-6 : Employee with Maximum TotalPayBenefits"):
    st.dataframe(
        salaries[salaries["TotalPayBenefits"] == salaries["TotalPayBenefits"].max()]
    )


st.header("Part - C : Employee Analytics")

with st.expander("Q-1 : Employees by Job Title"):
    st.dataframe(salaries["JobTitle"].value_counts())

with st.expander("Q-2 : Top 15 Highest Paid Employees"):
    st.dataframe(
        salaries.nlargest(15, "TotalPayBenefits")[
            ["EmployeeName", "JobTitle", "TotalPayBenefits"]
        ]
    )

with st.expander("Q-3 : Top 10 Job Titles by Average Salary"):
    st.dataframe(
        salaries.groupby("JobTitle")["TotalPayBenefits"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

with st.expander("Q-4 : Employees Earning More Than $100000"):
    st.write((salaries["TotalPayBenefits"] > 100000).sum())

with st.expander("Q-5 : Average Salary of Police Officers"):
    police = salaries[salaries["JobTitle"].str.contains("Police", case=False, na=False)]
    st.write(police["TotalPayBenefits"].mean())

with st.expander("Q-6 : Average Salary of Firefighters"):
    fire = salaries[salaries["JobTitle"].str.contains("Fire", case=False, na=False)]
    st.write(fire["TotalPayBenefits"].mean())


st.header("Part - D : Trend Analysis")

with st.expander("Q-1 : Employees Hired Each Year"):
    st.dataframe(salaries.groupby("Year").size())

with st.expander("Q-2 : Average Salary by Year"):
    st.dataframe(salaries.groupby("Year")["TotalPayBenefits"].mean())

with st.expander("Q-3 : Highest Average Salary Job Title by Year"):
    highest_avg = (
        salaries.groupby(["Year", "JobTitle"])["TotalPayBenefits"]
        .mean()
        .reset_index()
    )

    result = highest_avg.loc[
        highest_avg.groupby("Year")["TotalPayBenefits"].idxmax()
    ]

    st.dataframe(result)

with st.expander("Q-4 : Year with Highest Total Salary"):
    st.dataframe(
        salaries.groupby("Year")["TotalPayBenefits"]
        .sum()
        .sort_values(ascending=False)
    )

with st.expander("Q-5 : BasePay, OvertimePay and OtherPay Comparison"):
    comparison = salaries.groupby("Year")[
        ["BasePay", "OvertimePay", "OtherPay"]
    ].agg(["mean", "sum", "min", "max"])

    st.dataframe(comparison)


st.header("Part - E : Data Cleaning")

with st.expander("Q-1 : Replace Missing Values"):
    sal = salaries.copy()
    sal.fillna(0, inplace=True)
    st.dataframe(sal.head())

with st.expander("Q-2 : Convert Salary Columns to Numeric"):
    sal = salaries.copy()
    salary_columns = [
        "BasePay",
        "OvertimePay",
        "OtherPay",
        "Benefits",
        "TotalPay",
    ]

    for col in salary_columns:
        sal[col] = pd.to_numeric(sal[col], errors="coerce")

    st.dataframe(sal.head())

with st.expander("Q-3 : Remove Duplicate Rows"):
    sal = salaries.copy()
    sal.drop_duplicates(inplace=True)
    st.write("Rows after removing duplicates :", sal.shape[0])

with st.expander("Q-4 : Create Net Salary Column"):
    sal = salaries.copy()
    sal["Net Salary"] = sal["BasePay"] + sal["OvertimePay"] + sal["OtherPay"]
    st.dataframe(sal.head())