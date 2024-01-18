


def make_change (total_charge, payment):
    #find difference
    difference = round(payment - total_charge, 2)
    difference_as_string = str(difference)
    parts = difference_as_string.split('.')
    bills = parts[0]
    # not to make coins go to 2 decimal places
    coins = parts[1]
   
    
    return count_bills(bills), count_coins(coins)
    
def count_bills(payment_in_bills):
    value= int(payment_in_bills)
    hundreds = value// 100
    value%= 100
    fifties = value//50
    value%= 50
    twenties = value//20
    value%= 20
    tens = value//10
    value%= 10
    fives = value//5
    value%= 5 
    singles = value//1
    value%= 1
    
    return(singles, fives, tens, twenties, fifties, hundreds)
    



def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)
    quarters = payment_in_coins // 25
    payment_in_coins %= 25
    dimes = payment_in_coins // 10
    payment_in_coins %= 10
    nickles = payment_in_coins //5
    payment_in_coins %= 5
    pennies = payment_in_coins //1
    payment_in_coins %= 1
   
    return(pennies, nickles, dimes, quarters)
    
def value_of_change(value):
    value = int(value)
    hundreds = value // 100
    value %= 100
    fifties = value//50
    value %= 50
    twenties = value//20
    value%= 20
    tens = value//10
    value%= 10
    fives = value//5
    value%= 5 
    singles = value//1
    value%= 1
    return(singles, fives, tens, twenties, fifties, hundreds)
    
  
print(make_change(148.60, 200))
print(value_of_change)