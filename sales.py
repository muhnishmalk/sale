import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
try:
    df = pd.read_csv('sales_data.csv', sep='#')
except FileNotFoundError:
    print("Error: The 'sales_data.csv' file was not found. Please provide the correct file path.")
    exit()

# Step 2: Data Cleaning

# Check for missing values
if df.isnull().values.any():
    # Handle missing values (e.g., drop rows with missing data)
    df.dropna(inplace=True)
    print("Missing values were removed.")

# Data type conversion (if needed)
# In this example, we assume the data types are already correct.

# Step 3: Calculate Key Metrics

# Calculate total revenue
total_revenue = df['Revenue'].sum()

# Calculate average revenue per order
average_revenue_per_order = total_revenue / len(df)

# Find the top-selling product category
top_selling_category = df['Product Category'].value_counts().idxmax()

# Step 4: Create Visualizations

# Create a bar chart for total revenue by product category
category_revenue = df.groupby('Product Category')['Revenue'].sum()
plt.figure(figsize=(10, 6))
category_revenue.plot(kind='bar')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product Category')
plt.xticks(rotation=45)

# Save the chart as an image file
plt.savefig('revenue_by_category.png')

# Step 5: Save key metrics to a text file

with open('key_metrics.txt', 'w') as file:
    file.write(f"Total Revenue: ${total_revenue:.2f}\n")
    file.write(f"Average Revenue per Order: ${average_revenue_per_order:.2f}\n")
    file.write(f"Top Selling Product Category: {top_selling_category}\n")

# Display the chart (optional)
plt.show()

print("Data analysis and visualization completed.")
