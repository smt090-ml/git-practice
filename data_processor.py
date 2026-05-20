# Moch data: Daily sales totals for the retail store
daily_sales = [1200, 1550, 980, 2100, 1750]

# Calculate total and average sales
total_sales = sum(daily_sales)
average_sales = total_sales/len(daily_sales)

print("-- Retail Data Summary--")
print(f"Total Weekly Sales: ${total_sales}")
print(f"Average Daily Sales: ${average_sales:.2f}")
