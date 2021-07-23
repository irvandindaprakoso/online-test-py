def bonAppetit(bill, k, b):
    anna_paid = (sum(bill) - bill[k]) /2
    total_paid = b - anna_paid
    if total_paid<=0:
        print('Bon Appetit')
    else:
        print(int(total_paid))
