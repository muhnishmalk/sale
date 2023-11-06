import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path, sep='#')

def clean_data(df):
    df.dropna(inplace=True)
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
    return df

def calculate_metrics(df):
    total_revenue = df['Revenue'].sum()
    average_revenue_per_order = df['Revenue'].mean()
    top_product_category = df['Product Category'].value_counts().idxmax()
    return total_revenue, average_revenue_per_order, top_product_category

def visualize_discount_status(df):
    plt.figure(figsize=(8, 6))
    discount_counts = df['Discount Rate'].apply(lambda x: 'With Discount' if x > 0 else 'Without Discount').value_counts()
    discount_counts.plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title('Products with and Without Discounts')
    plt.xlabel('Discount Status')
    plt.ylabel('Quantity')
    plt.savefig('discount_status_bar_chart.png')
    plt.close()

def visualize_product_category(df):
    plt.figure(figsize=(8, 8))
    category_counts = df['Product Category'].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.title('Product Category Distribution')
    plt.savefig('product_category_pie_chart.png')
    plt.close()

def visualize_revenue_by_category(df):
    plt.figure(figsize=(10, 6))
    colors = plt.cm.Paired(range(len(df['Product Category'].unique())))
    revenue_by_category = df.groupby('Product Category')['Revenue'].sum()
    revenue_by_category.plot(kind='bar', color=colors)
    plt.title('Revenue by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Total Revenue')
    plt.savefig('revenue_by_product_category_bar_chart.png')
    plt.close()

def visualize_top_selling_products(df):
    plt.figure(figsize=(10, 6))
    top_products = df.groupby('Product Category')['Quantity Sold'].sum().sort_values(ascending=False).head(3)
    top_products.plot(kind='bar', color='skyblue')
    plt.title('Top 3 Selling Products')
    plt.xlabel('Product Category')
    plt.ylabel('Total Quantity Sold')
    plt.savefig('top_selling_products_bar_chart.png')
    plt.close()

def visualize_monthly_revenue(df):
    plt.figure(figsize=(12, 6))
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    monthly_revenue.plot(kind='bar', color='lightcoral')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.savefig('monthly_revenue_bar_chart.png')
    plt.close()

def main():
    data_file = 'sales_data.csv'
    df = load_data(data_file)
    df = clean_data(df)
    total_revenue, average_revenue_per_order, top_product_category = calculate_metrics(df)
    
    visualize_discount_status(df)
    visualize_product_category(df)
    visualize_revenue_by_category(df)
    visualize_top_selling_products(df)
    visualize_monthly_revenue(df)
    
    print("Total Revenue:", total_revenue)
    print("Average Revenue per Order:", average_revenue_per_order)
    print("Top Selling Product Category:", top_product_category)

if __name__ == "__main__":
    main()