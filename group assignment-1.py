'''Program header
   program name: group assignment-1.py
   author: Caitlyn, Nam, Mehakpreet, Ali (Group )
   date: 04-Feb-26
   description: program to take input from user 
                to check coffee or tea and calculate 
                according to order requirment and province
'''
from typing import Final
tea_box_cost: Final = 20 * 0.45  #tea cost per box
coffee_cost: Final = 18.50       #coffee cost per bag
tea_discount: Final = 0.15       #tea discount for <10 bags
coffee_discount: Final = 0.10    #coffee discount for <25 boxes

print('----------------------------------------------')
print('*** Welcome to Beverage Wholesale Program! ***')
print('----------------------------------------------')
print("Please select the type of purchase:")
print('C: Coffee Beans\nT: Tea Boxes')
product_name = input('>>>  ').lower()
#to check either the option selected is coffee or tea
if(product_name == 'c' or product_name == 't'):
    
    #if coffee is  selected
    if(product_name == 'c'):
        coffee_quantity = float(input('Enter the number of kilograms (kg) of coffee: '))
        if coffee_quantity > 0 and coffee_quantity <= 25:
            province_name = input('Please enter the 2-letter province abbreviation: ').upper()
            price_before_discount = coffee_quantity * coffee_cost 
            price_after_discount =  price_before_discount #using only one value for calculating GST

        elif coffee_quantity > 25:
            province_name = input('Please enter the 2-letter province abbreviation: ').upper()
            price_before_discount = coffee_quantity* coffee_cost
            total_discount = price_before_discount * coffee_discount
            price_after_discount = price_before_discount - total_discount
        else:
            print('Quantity of coffee should be > 0')
        product_name = 'coffee'
        qty = coffee_quantity
            #if tea is selected
    elif(product_name == 't'):
          tea_boxes = int(input('Enter the number of boxes of tea: '))
          
          if (tea_boxes > 0 and tea_boxes <= 10):
            province_name = input('Please enter the 2-letter province abbreviation: ').upper()
            price_before_discount = tea_boxes * tea_box_cost
            price_after_discount =  price_before_discount
          elif (tea_boxes >10):
            province_name = input('Please enter the 2-letter province abbreviation: ').upper()
            price_before_discount = tea_boxes * tea_box_cost
            total_discount = price_before_discount * tea_discount
            price_after_discount = price_before_discount - total_discount
          else:
              print('Quantity of tea should be > 0')
    
          product_name = 'Tea'
          qty = tea_boxes * 20
else:
         print('Invalid input, you should enter c/C or t/T')
         #calculation for GST
if(province_name == 'AB' or province_name == 'BC'):
    GST = price_after_discount * 0.05     
elif(province_name == 'ON'):
    GST = price_after_discount * 0.13
elif(province_name == 'SK','NS'):
    GST = price_after_discount * 0.15

total_price = price_after_discount + GST
print('-------------------------------------------------------------',end='')
print('-------------------------------------------------------------')
print("Product \tQty bags/kg\tPrice Before Disc\t",end='')
print("Price After Disc\tGST\tTotal Price")
print(f'{product_name:>7s}{qty:>19.2f}{price_before_discount:>17.2f}',end='')
print(f'{price_after_discount:>24.2f}{GST:>16.2f}{total_price:>13.2f}')
print('-------------------------------------------------------------',end='')
print('-------------------------------------------------------------')
print('Thanks for your business, Good Bye')




            