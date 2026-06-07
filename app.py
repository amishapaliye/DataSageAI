import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="DataSage AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataSage AI")
st.caption("AI-Powered Business Analytics Dashboard")

# Sidebar
st.sidebar.title("📊 DataSage AI")
st.sidebar.success("Hackathon Edition")

st.sidebar.info("""
✅ Analytics Dashboard
✅ AI Insights
✅ Business Reports
✅ Data Quality Check
✅ Recommendations
""")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Dataset Preview
    st.subheader("📄 Dataset Preview")
    st.dataframe(df)

    st.subheader("📑 Dataset Summary")
    st.dataframe(df.describe())

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Calculations
    total_sales = df["Sales"].sum()
    max_sales = df["Sales"].max()
    min_sales = df["Sales"].min()

    best_product = df.loc[df["Sales"].idxmax(), "Product"]
    lowest_product = df.loc[df["Sales"].idxmin(), "Product"]

    average_sales = df["Sales"].mean()

    below_avg = df[df["Sales"] < average_sales]

    # Business Insights
    st.subheader("📈 Business Insights")

    st.write("📊 Total Sales:", total_sales)
    st.write("🏆 Best Product:", best_product)
    st.write("📉 Lowest Product:", lowest_product)
    st.write("📈 Average Sales:", round(average_sales, 2))

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Sales", total_sales)

    with col2:
        st.metric("Best Product Sales", max_sales)

    with col3:
        st.metric("Average Sales", round(average_sales, 2))

    # Bar Chart
    st.subheader("📊 Sales Bar Chart")
    st.bar_chart(df.set_index("Product")["Sales"])

    # Pie Chart
    st.subheader("🥧 Sales Distribution")

    fig, ax = plt.subplots()

    ax.pie(
        df["Sales"],
        labels=df["Product"],
        autopct="%1.1f%%"
    )

    ax.set_title("Sales Distribution")

    st.pyplot(fig)

    # AI Insights
    st.subheader("🤖 AI Insights")

    st.success(
        f"{best_product} is the top performing product with sales of {max_sales}."
    )

    st.warning(
        f"{lowest_product} is the lowest performing product with sales of {min_sales}."
    )

    st.info(
        "Some products are performing above average. Focus on high-performing products for growth."
    )

    # Recommendations
    st.subheader("📋 Recommendations")

    st.write(
        f"Increase inventory for {best_product} because it is performing strongly."
    )

    st.write(
        f"Consider promotions or discounts for {lowest_product} to improve sales."
    )

    # Risk Alert
    st.subheader("🚨 Risk Alerts")

    if min_sales < average_sales:
        st.error(
            f"{lowest_product} is underperforming and may require immediate business attention."
        )

    # Products Below Average
    st.subheader("⚠ Products Below Average")
    st.dataframe(below_avg)

    # Health Score
    st.subheader("📊 Data Health Score")

    health_score = 100

    if df.isnull().sum().sum() > 0:
        health_score -= 20

    if len(df) < 5:
        health_score -= 10

    st.metric("Health Score", f"{health_score}/100")

    # Missing Values Analysis
    st.subheader("🔍 Missing Values Analysis")

    missing_values = df.isnull().sum()

    st.dataframe(
        missing_values.reset_index().rename(
            columns={
                "index": "Column",
                0: "Missing Values"
            }
        )
    )

    # Ask DataSage AI
    st.subheader("💬 Ask DataSage AI")

    question = st.text_input("Ask DataSage AI")

    if question:

        q = question.lower()

        if "best" in q or "top" in q:
            st.success(
                f"{best_product} is the best selling product with sales of {max_sales}."
            )

        elif "total" in q:
            st.success(
                f"Total sales are {total_sales}."
            )

        elif "average" in q:
            st.success(
                f"Average sales are {average_sales:.2f}."
            )

        elif "improve" in q or "low" in q:
            st.warning(
                f"{lowest_product} needs attention because its sales are only {min_sales}."
            )

        elif "recommend" in q:
            st.info(
                f"Focus on {best_product} and improve marketing for {lowest_product}."
            )

        else:
            st.warning(
                "I do not understand that question yet."
            )

    # AI Business Report
    st.subheader("🧠 AI Business Analyst")

    analysis = f"""
BUSINESS REPORT

Total Sales: {total_sales}

Best Product: {best_product}

Lowest Product: {lowest_product}

Average Sales: {average_sales:.2f}

RECOMMENDATIONS

1. Increase stock of {best_product}
2. Improve marketing for {lowest_product}
3. Focus on products above average sales
"""

    st.text_area(
        "AI Generated Business Report",
        analysis,
        height=250
    )

    st.download_button(
        label="📥 Download Report",
        data=analysis,
        file_name="datasage_report.txt",
        mime="text/plain"
    )