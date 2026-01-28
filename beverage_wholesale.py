'''
Program name: beverage_wholesale.py
Names: Akbar Ali, Caitlyn Russell, Hoang Nam Bui
Description: Writing a code that calculates the cost of coffee and tea purchases with GST and discounts if applicable 
'''

#Display the menu and ask user to select between coffee or tea
print(f'''{'-'*45}\n***Welcome to Beverage Wholesale Program!***\n{'-'*45}\n
Please select the type of purchase:\nC: Coffee Beans\nT: Tea Boxes''')
product = str(input('>>>')).lower()

#Check to see if the input is valid

if product != 't' and product != 'c':
    print('Invalid input, you should enter c/C or t/T')
    
#Ask user to enter coffee kilograms or tea boxes
if product == 'c':
    coffee_kg = int(input('Enter number of kilograms (kg) of coffee:'))
    if coffee_kg <= 0:
        print('Quantity of coffee should be > 0')

if product == 't':
    tea_boxes = int(input('Enter the number of boxes of tea:'))
    if tea_boxes <= 0:
        print('Number of tea boxes should be > 0')