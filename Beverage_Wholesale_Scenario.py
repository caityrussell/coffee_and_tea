# BEVERAGE WHOLESALE PROGRAM
# Description: This program calculates the cost of coffee or tea purchases
#              including discounts and GST based on province.

# Tea constants
BAGS_PER_BOX = 20
TEA_PRICE_PER_BAG = 0.45
TEA_DISCOUNT_THRESHOLD = 10
TEA_DISCOUNT_RATE = 0.15  

# Coffee constants
COFFEE_PRICE_PER_KG = 18.50
COFFEE_DISCOUNT_THRESHOLD = 25
COFFEE_DISCOUNT_RATE = 0.10  

# GST rates by province
GST_AB_BC = 0.05   
GST_ON = 0.13      #
GST_OTHER = 0.15   


# MAIN PROGRAM
def main():
    print("*** Welcome to Beverage Wholesale Program! ***")
    
    # Display menu
    print("Please select the type of purchase:")
    print("C: Coffee Beans")
    print("T: Tea Boxes")
    
    selection = input(">> ")
    
    if selection.lower() not c and selection,lower() not t:
        print("Invalid input, you should enter c/C or t/T")
        return  # Exit program
    
    if selection.lower() == 'c':
        # COFFEE PROCESSING
        # Get number of kilograms
        try:
            kg_coffee = float(input("Enter the number of kilograms of coffee: "))
        except ValueError:
            print("Error: Invalid input for kilograms")
            exit()
        
        if kg_coffee <= 0:
            print("Error: Number of coffee kg must be > 0")
            exit()
        
        province = input("Please enter the 2-letter province abbreviation: ")
        
        # Calculate coffee costs
        price_before_discount = kg_coffee * COFFEE_PRICE_PER_KG
        
        # Apply discount if applicable
        if kg_coffee > COFFEE_DISCOUNT_THRESHOLD:
            discount_amount = price_before_discount * COFFEE_DISCOUNT_RATE
            price_after_discount = price_before_discount - discount_amount
        else:
            price_after_discount = price_before_discount
        
        # Calculate GST based on province
        province_upper = province.upper()
        if province_upper in ['AB', 'BC']:
            gst_rate = GST_AB_BC
        elif province_upper == 'ON':
            gst_rate = GST_ON
        else:
            gst_rate = GST_OTHER
        
        gst_amount = price_after_discount * gst_rate
        total_price = price_after_discount + gst_amount
        
        print("\n" + "=" * 90)
        print(f"{'Product':<10} {'Qty (Bags/kg)':>14} {'Price Before Disc':>20} {'Price After Disc':>18} {'GST':>8} {'Total Price':>11}")
        print("-" * 90)
        
        print(f"{'Coffee':<10} {kg_coffee:>14.2f} {price_before_discount:>20.2f} {price_after_discount:>18.2f} {gst_amount:>8.2f} {total_price:>11.2f}")
        print("=" * 90)
        
    else:  
        try:
            boxes_tea = float(input("Enter the number of boxes of tea: "))
        except ValueError:
            print("Error: Invalid input for boxes")
            exit()
        
        if boxes_tea <= 0:
            print("Error: Number of tea boxes must be > 0")
            exit()
        
        province = input("Please enter the 2-letter province abbreviation: ")
        
        # Calculate tea costs
        total_bags = boxes_tea * BAGS_PER_BOX
        price_before_discount = total_bags * TEA_PRICE_PER_BAG
        
        # Apply discount if applicable
        if boxes_tea > TEA_DISCOUNT_THRESHOLD:
            discount_amount = price_before_discount * TEA_DISCOUNT_RATE
            price_after_discount = price_before_discount - discount_amount
        else:
            price_after_discount = price_before_discount
        
        # Calculate GST based on province
        province_upper = province.upper()
        if province_upper in ['AB', 'BC']:
            gst_rate = GST_AB_BC
        elif province_upper == 'ON':
            gst_rate = GST_ON
        else:
            gst_rate = GST_OTHER
        
        gst_amount = price_after_discount * gst_rate
        total_price = price_after_discount + gst_amount
        
        # Display results in tabular format
        print("\n" + "=" * 90)
        print(f"{'Product':<10} {'Qty (Bags/kg)':>14} {'Price Before Disc':>20} {'Price After Disc':>18} {'GST':>8} {'Total Price':>11}")
        print("-" * 90)
        
        # Format values with 2 decimal places
        print(f"{'Tea':<10} {total_bags:>14.2f} {price_before_discount:>20.2f} {price_after_discount:>18.2f} {gst_amount:>8.2f} {total_price:>11.2f}")
        print("=" * 90)
    
    # Goodbye message
    print("\nThanks for your business, Good Bye")

# =============================================================================
# RUN THE PROGRAM
# =============================================================================
if __name__ == "__main__":

    main()
