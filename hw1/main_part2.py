import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the CSV file
df = pd.read_csv('result_data.csv')

missing_data = df.isnull()

print(missing_data)

# Convert 'Review' column to numeric values
df['Review'] = pd.to_numeric(df['Review'], errors='coerce')

# Sort the DataFrame by 'Review' column in descending order
sorted_df = df.sort_values(by='Review', ascending=False)

# Select the top 50 products with the highest review counts
top_50_products = sorted_df.head(50)

# Use .loc to avoid the warning when modifying the 'Price' column
top_50_products.loc[:, 'Price'] = top_50_products['Price'].replace('[\$,]', '', regex=True).astype(float)

# Calculate the mean, median, and standard deviation of the 'Review' column
average_review = top_50_products['Review'].mean()
median_review = top_50_products['Review'].median()
std_dev_review = top_50_products['Review'].std()

# Calculate the mean, median, and standard deviation of the 'Price' column
average_price_top_50 = top_50_products['Price'].mean()
median_price_top_50 = top_50_products['Price'].median()
std_dev_price_top_50 = top_50_products['Price'].std()

# Display the top 50 products, their average price, and plot bar graph for prices
print("Top 50 Products with Highest Review Counts:")
print(top_50_products[['Product', 'Review', 'Price']])
print("\nReview Statistics:")
print("  - Mean Review: {:.2f}".format(average_review))
print("  - Median Review: {:.2f}".format(median_review))
print("  - Standard Deviation of Review: {:.2f}".format(std_dev_review))

print("\nPrice Statistics:")
print("  - Mean Price: ${:.2f}".format(average_price_top_50))
print("  - Median Price: ${:.2f}".format(median_price_top_50))
print("  - Standard Deviation of Price: ${:.2f}".format(std_dev_price_top_50))

# Plot bar graph for prices
plt.figure(figsize=(15, 8))
bars = plt.bar(top_50_products['Product'], top_50_products['Price'], color='green')
plt.axhline(y=average_price_top_50, color='red', linestyle='--', label='Average Price')
plt.text(-1, average_price_top_50, '${:.2f}'.format(average_price_top_50), ha='right', va='center', color='red', fontweight='bold')
plt.title('Top 50 Products - Prices')
plt.xlabel('Product')
plt.ylabel('Price')
plt.xticks(rotation=45, ha='right')
plt.legend()

# Add values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, '${:.2f}'.format(yval), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Scatter plot for 'Review' and 'Price'
plt.figure(figsize=(10, 6))
plt.scatter(top_50_products['Review'], top_50_products['Price'], color='blue', alpha=0.7)
plt.title('Scatter Plot - Review vs. Price')
plt.xlabel('Review')
plt.ylabel('Price')
plt.grid(True)
plt.show()

