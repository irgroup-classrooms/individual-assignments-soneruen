import re
from collections import Counter
from datetime import datetime

def main():
    # Define storage variables
    order_numbers = []
    product_names = []
    prices = []
    order_dates = []

    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.readlines()

    # Define regex patterns
    pattern = re.compile(r'Order #(\d+): Product: (.*?), Price: \$(\d+\.\d+), Date: (\d{4}-\d{2}-\d{2})')

    for line in text:
        match = pattern.match(line)
        if match:
            order_number, product_name, price, order_date = match.groups()
            order_numbers.append(order_number)
            product_names.append(product_name)
            prices.append(float(price))
            order_dates.append(order_date)

    # Process dates to change format
    formatted_dates = [datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y') for date in order_dates]

    # Filter prices over $500
    expensive_products = [price for price in prices if price > 500]

    # Product names with more than 6 characters
    long_product_names = [name for name in product_names if len(name) > 6]

    # Count the occurrence of each product
    product_count = Counter(product_names)

    # Orders with prices ending in .99
    prices_ending_in_99 = [price for price in prices if str(price).endswith('.99')]

    # Find the cheapest product
    cheapest_price = min(prices) if prices else None

    # Print the extracted information
    print("Order Numbers:", order_numbers)
    print("Product Names:", product_names)
    print("Prices:", prices)
    print("Formatted Dates:", formatted_dates)
    print("Expensive Products (>$500):", expensive_products)
    print("Product Names (>6 chars):", long_product_names)
    print("Product Occurrences:", product_count)
    print("Prices ending in .99:", prices_ending_in_99)
    print("Cheapest Price:", cheapest_price)

if __name__ == '__main__':
    main()