'''
Program name: beverage_wholesale.py
Authorss: Akbar Ali, Caitlyn Russell, Hoang Nam Bui, Mehakpreet Kaur
Date: February 4, 2026
Description: Calculates the cost of coffee or tea purchases with GST and discounts.
'''

# Calculate the Constants
BAGS_PER_BOX = 20
TEA_PRICE_PER_BAG = 0.45
TEA_DISCOUNT_THRESHOLD = 10
TEA_DISCOUNT_RATE = 0.15

COFFEE_PRICE_PER_KG = 18.50
COFFEE_DISCOUNT_THRESHOLD = 25
COFFEE_DISCOUNT_RATE = 0.10

GST_AB_BC = 0.05
GST_ON = 0.13
GST_OTHER = 0.15

# Display the Menu and ask user to input coffee or tea
print(f"{'-'*47}")
print("*** Welcome to Beverage Wholesale Program! ***")
print(f"{'-'*47}")
print("Please select the type of purchase:")
print("C: Coffee Beans")
print("T: Tea Boxes")

product = input(">>> ").lower()

# Check if the product is valid
if product != "c" and product != "t":
    exit("Invalid input, you should enter c/C or t/T")

# Process cost of coffee
if product == "c":
    coffee_kg = int(input("Enter number of kilograms (kg) of coffee: "))
    if coffee_kg <= 0:
        exit("Quantity of coffee should be > 0")

    price_before_discount = coffee_kg * COFFEE_PRICE_PER_KG

    if coffee_kg > COFFEE_DISCOUNT_THRESHOLD:
        price_after_discount = price_before_discount - (price_before_discount * COFFEE_DISCOUNT_RATE)
    else:
        price_after_discount = price_before_discount

# Process cost of tea
if product == "t":
    tea_boxes = int(input("Enter the number of boxes of tea: "))
    if tea_boxes <= 0:
        exit("Number of tea boxes should be > 0")

    total_bags = tea_boxes * BAGS_PER_BOX
    price_before_discount = total_bags * TEA_PRICE_PER_BAG

    if tea_boxes > TEA_DISCOUNT_THRESHOLD:
        price_after_discount = price_before_discount - (price_before_discount * TEA_DISCOUNT_RATE)
    else:
        price_after_discount = price_before_discount

# GST Calculation
province = input("Please enter the 2-letter province abbreviation: ").lower()

if province == "ab" or province == "bc":
    gst_rate = GST_AB_BC
elif province == "on":
    gst_rate = GST_ON
else:
    gst_rate = GST_OTHER

gst_amount = price_after_discount * gst_rate
total_price = price_after_discount + gst_amount

# Output
print("-" * 90)
print(f"{'Product':^10}{'Qty (Bags/kg)':^15}{'Price Before Disc':^20}"
      f"{'Price After Disc':^20}{'GST':^10}{'Total Price':^15}")

if product == "c":
    print(f"{'Coffee':^10}{coffee_kg:^15.2f}{price_before_discount:^20.2f}"
          f"{price_after_discount:^20.2f}{gst_amount:^10.2f}{total_price:^15.2f}")

if product == "t":
    print(f"{'Tea':^10}{total_bags:^15.2f}{price_before_discount:^20.2f}"
          f"{price_after_discount:^20.2f}{gst_amount:^10.2f}{total_price:^15.2f}")

print("-" * 90)

print("Thanks for your business, Good Bye")
