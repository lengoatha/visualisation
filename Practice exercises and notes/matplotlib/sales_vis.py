import io
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data/jumta.csv')

# Streamlit app title and description
st.title("Jumta Sales Data Analysis")
st.write("""
This dashboard provides insights into the monthly sales data for Jumta over two years.
Below, are visualizations of:
- Monthly revenue trends
- Total number of orders per month
- Relationship between the number of orders and average order value
""")

# Display dataset in Streamlit
if st.checkbox("Show Raw Data"):
    st.write(df)

# 2. Display the first 10 rows of the dataset
st.header("First 10 Rows of the Dataset")
st.write(df.head(10))

    # 3. Display the shape and basic information about the dataset
st.header("Dataset Shape and Basic Information")
st.write(f"Shape of the dataset: {df.shape}")
st.write("Basic Information about the dataset:")
buffer = st.text("Loading data info...")
buffer.text(df.info())

    # 4. Check for missing data and handle it appropriately
st.header("Missing Data")
missing_data = df.isnull().sum()
st.write(missing_data)

    # Optionally handle missing data - drop rows with any missing data
df = df.dropna()
st.write("Missing data has been handled by dropping rows with any missing values.")

# Monthly Revenue Line Plot
st.subheader("Monthly Revenue Over Two Years")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Month', y='Revenue', data=df, marker='o', ax=ax)
ax.set_title('Monthly Revenue Over Two Years')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue')
plt.xticks(rotation=45)
st.pyplot(fig)

# Total Number of Orders Bar Plot
st.subheader("Total Number of Orders per Month")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Month', y='Orders', data=df, color='skyblue', ax=ax)
ax.set_title('Total Number of Orders per Month')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Orders')
plt.xticks(rotation=45)
st.pyplot(fig)

# Scatter Plot for Number of Orders vs. Average Order Value
st.subheader("Relationship between Number of Orders and Average Order Value")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Orders', y='Average_Order_Value', data=df, hue='Month', palette='viridis', ax=ax)
ax.set_title('Relationship between Number of Orders and Average Order Value')
ax.set_xlabel('Number of Orders')
ax.set_ylabel('Average Order Value')
st.pyplot(fig)

# Combined Subplot with All Visualizations
st.subheader("Combined Visualizations")
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Line plot for revenue
sns.lineplot(x='Month', y='Revenue', data=df, marker='o', ax=axs[0])
axs[0].set_title('Monthly Revenue Over Two Years')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Revenue')
axs[0].tick_params(axis='x', rotation=45)

# Bar plot for number of orders
sns.barplot(x='Month', y='Orders', data=df, color='skyblue', ax=axs[1])
axs[1].set_title('Total Number of Orders per Month')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Number of Orders')
axs[1].tick_params(axis='x', rotation=45)

# Scatter plot for orders vs. average order value
sns.scatterplot(x='Orders', y='Average_Order_Value', data=df, hue='Month', palette='viridis', ax=axs[2])
axs[2].set_title('Relationship between Number of Orders and Average Order Value')
axs[2].set_xlabel('Number of Orders')
axs[2].set_ylabel('Average Order Value')

# Adjust layout
plt.tight_layout()
st.pyplot(fig)

# Save the plot into an in-memory buffer
buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=300)
buffer.seek(0)  # Rewind the buffer to the beginning

# Save option for subplot
st.write("### Download Combined Visualization as High-Resolution Image")
st.download_button(
    label="Download Image",
    data=buffer,
    #data=plt.savefig('jumta_sales_analysis.png', dpi=300),
    file_name="jumta_sales_analysis.png",
    mime="image/png"
)
buffer.close()