'''
Program name: beverage_wholesale.py
Names: Akbar Ali, Caitlyn Russell, Hoang Nam Bui, Mehakpreet Kaur
Description: Writing a code that calculates the cost of coffee and tea purchases with GST and discounts if applicable 
'''

#Display the menu and ask user to select between coffee or tea
print(f'''{'-'*45}\n***Welcome to Beverage Wholesale Program!***\n{'-'*45}\n
Please select the type of purchase:\nC: Coffee Beans\nT: Tea Boxes''')
product = str(input('>>>')).lower()

#Check to see if the input is valid

if product != 't' and product != 'c':
    print('Invalid input, you should enter c/C or t/T') and exit()
    
#Ask user to enter coffee kilograms or tea boxes
if product == 'c':
    coffee_kg = int(input('Enter number of kilograms (kg) of coffee:'))
    if coffee_kg <= 0:
        print('Quantity of coffee should be > 0') and exit()
    
    #Calucate coffee price before and after discount    
    price_before_discount = coffee_kg * 18.50
    price_after_discount = price_before_discount - (price_before_discount * .10)

if product == 't':
    tea_boxes = int(input('Enter the number of boxes of tea:'))
    if tea_boxes <= 0:
        print('Number of tea boxes should be > 0') and exit()
    
    #Calculate tea price before and after discount
    price_before_discount = float(tea_boxes * 20 * .45)
    price_after_discount = float(price_before_discount - (price_before_discount *.10))

#Calculate the GST 
prov_code = str(input('Please enter the 2-letter province abbreviation: ').lower())
if prov_code == 'ab' or prov_code == 'bc':
    gst = .05
elif prov_code == 'on':
    gst = .13
else:
    gst = .15

#Calculate the price after GST

price_after_gst_no_discount = float(price_before_discount + (price_before_discount * gst))
price_after_gst_with_discount = float(price_after_discount + (price_after_discount * gst))

#Diplay the output based on the users input
print(f'{'-'*100}')
print(f"{'Product':^10}"
      f"{'Qty (Bags/kg)':^15}"
      f"{'Price Before Disc':^20}"
      f"{'Price After Disc':^20}"
      f"{'GST':^10}"
      f"{'Total Price':^15}")

if product == 'c' and coffee_kg > 25:
    print(f"{'Coffee':^10}"
          f"{coffee_kg:^15.2f}"
          f"{price_before_discount:^20.2f}"
          f"{price_after_discount:^20.2f}"
          f"{gst:^10.2f}"
          f"{price_after_gst_with_discount:^15.2f}")
elif product == 'c' and coffee_kg <= 25:
    print(f"{'Coffee':^10}"
          f"{coffee_kg:^15.2f}"
          f"{price_before_discount:^20.2f}"
          f"{price_before_discount:^20.2f}"
          f"{gst:^10.2f}"
          f"{price_after_gst_no_discount:^15.2f}")

elif product == 't' and tea_boxes > 10:
    print(f"{'Tea':^10}"
          f"{tea_boxes:^15}"
          f"{price_before_discount:^20.2f}"
          f"{price_after_discount:^20.2f}"
          f"{gst:^10.2f}"
          f"{price_after_gst_with_discount}")
else:
    print(f"{'Tea':^10}"
          f"{tea_boxes:^15}"
          f"{price_before_discount:^20.2f}"
          f"{price_before_discount:^20.2f}"
          f"{gst:^10.2f}"
          f"{price_after_gst_no_discount:^10.2f}")
print(f'{'-'*100}')
print('Thanks for your business, Good Bye')





