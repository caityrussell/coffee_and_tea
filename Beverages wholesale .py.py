# print("*** Welcome to the Bevrage Wholesale program ***")
 
 
# constants
 
TEA = "T"
COFFEE = "C"
 
# taxes stored as CONSTANTS
AB  = 5
BC = 5
ON = 13
OTHERS = 15
 
# -------------------------
#        CONSTANTS
# -------------------------
 
# Tea constants
BAGS_PER_BOX = 20
TEA_PRICE_PER_BAG = 0.45
TEA_DISCOUNT_THRESHOLD = 10
TEA_DISCOUNT_RATE = 0.15
 
# Coffee constants
COFFEE_PRICE_PER_KG = 18.50
COFFEE_DISCOUNT_THRESHOLD = 25
COFFEE_DISCOUNT_RATE = 0.10
 
# GST constant
GST_RATE = 0.05   # 5% GST
 
 
 
# Program begins from here !
 
print("*" * 50)
print("*** Welcome to the Bevrage Wholesale program ***")
print("*" * 50)
print("please select the type of purchase: ")
print("C: Coffee Beans")
print("T: Tea Boxes")
option = input("Enter your choice:")
 
if option == TEA:
   #  print(option)
    Province = input("Enter the 2-letter province abberivation: ")
    No_of_tea_boxes_kg = int(input("Enter the number of boxes of tea: "))
    price_before_discount = No_of_tea_boxes_kg * TEA_PRICE_PER_BAG  
    print(price_before_discount)
    print(TEA_PRICE_PER_BAG)
 
if No_of_tea_boxes_kg > TEA_DISCOUNT_THRESHOLD:
        Discount_amount = TEA_PRICE_PER_BAG * TEA_DISCOUNT_RATE
        final_price_after_discount = TEA_PRICE_PER_BAG - Discount_amount
        print(final_price_after_discount)
elif No_of_tea_boxes_kg <= TEA_DISCOUNT_THRESHOLD:
    print(price_before_discount)
 
# coffee
 
if option == COFFEE:
   COFFEE_DISCOUNT_THRESHOLD > 25
   total_value_coffee = COFFEE_PRICE_PER_KG * COFFEE_DISCOUNT_THRESHOLD
   Discount = total_value_coffee * COFFEE_DISCOUNT_RATE
   Coffee_After_discount = total_value_coffee - Discount
 
 
 
 
if Province == AB or BC:
   gst_calculated = TEA_PRICE_PER_BAG * GST_RATE
   print(gst_calculated + TEA_PRICE_PER_BAG)
 
elif option == COFFEE:
    gst_calculated = COFFEE_PRICE_PER_KG * GST_RATE
    print(gst_calculated + COFFEE_PRICE_PER_KG)
 
 
elif Province == ON:
   gst_calculated = TEA_PRICE_PER_BAG * (ON / 100)
   print(gst_calculated + TEA_PRICE_PER_BAG)
 
 
elif option == COFFEE:
    gst_calculated = COFFEE_PRICE_PER_KG * (ON/ 100)
    print(gst_calculated + COFFEE_PRICE_PER_KG)
 
elif Province == OTHERS:
   gst_calculated = TEA_PRICE_PER_BAG * (OTHERS / 100)
   print(gst_calculated + TEA_PRICE_PER_BAG)
 
 
elif option == COFFEE:
    gst_calculated = COFFEE_PRICE_PER_KG * (OTHERS/ 100)
    print(gst_calculated + COFFEE_PRICE_PER_KG)
 
 
 
 
 