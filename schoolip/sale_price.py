# Program to calculate sale price of a product after discount

initial_price = float(input("Enter price of the products in Rupees: "))
discount = float(input("Enter discount in percentage: ").strip().replace("%", ''))

# Calculate discount

perc = (initial_price * discount) / 100
final_price = initial_price - perc

# Show final price 

print(f"The final price of the product is: Rs. {final_price}")