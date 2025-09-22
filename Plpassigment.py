# quick function to check discounts
def get_discounted_price(cost, percent_off):   
    if percent_off >= 20:   # only apply discount if it's above 20%
        cut = cost * (percent_off / 100)  
        final = cost - cut
        return final
    else:
        return cost   # no deal, just return the same price


def run_program():
    try:
        item_price = float(input("Enter item price (e.g. 99.99): $"))
        discount = float(input("Enter discount %: "))
        
        # call the function above
        new_price = get_discounted_price(item_price, discount)
        
        # result printout
        if discount >= 20:
            money_saved = item_price - new_price
            print("\nNice! Discount applied.")
            print(f"Original: ${item_price:.2f}")
            print(f"Discount rate: {discount}%")
            print(f"Savings: ${money_saved:.2f}")
            print(f"Now you pay: ${new_price:.2f}")
        else:
            print("\nSorry, discount wasn’t high enough.")
            print(f"Price stays at: ${new_price:.2f}")
            
    except ValueError as e:
        # just catch the obvious error here
        print("Oops, enter valid numbers please.")
        # print("Debug:", e)   # <- leaving this here in case I need it later

if __name__ == "__main__":
    run_program()
