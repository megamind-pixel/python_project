def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it's 20% or higher.
    :param price: Original price of the item.
    :param discountPercent: Discount percentage to be applied.
    :return: Final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
