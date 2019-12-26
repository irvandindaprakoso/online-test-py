# online-test-py

------------------------------------------------------------------------------
### Cofee Promo
------------------------------------------------------------------------------

in order to celebrate birthday

coffee menu 

| Coffee & drinks | Price |
| :---: | :---: |
| Coffee Latte (L) | Rp. 20.000 |
| Coffee Americano (A) | Rp. 20.000 |
| Coffee Cappucino (C) | Rp. 25.000 |
| Water (W) | Rp. 5.000 |

Note:
-Minimum order to get Discount is Rp.50.000
-1 cup of coffee at the most expensive price is enough to pay a price of Rp.3.000
-promo only applies to latte, cappuccino and Americano coffee drinks

example:

| input | output |
| :---: | :---: |
| 1 | Rp. 20.000 |
| L | |
| 3 | Rp. 28.000 |
| L | |
| C | |
| W | |
| 3 | Rp. 43.000 |
| L | |
| A | |
| L | |

------------------------------------------------------------------------------
### Ice Cream Meter
------------------------------------------------------------------------------

Our squad want to implement an "ice cream meter" for everyone who late on each warking day. We will count the total late after every 2 weeks (10 working days) and these people need to pay the ice cream meter penalty so we can gather it and buy ice cream for the whole team :D.

the late fee will be incremental and the incremental base fee will be based on team agreement, bellow is the example for increment base fee = Rp.5.000:

| Total late | incremental fee | ice cream meter |
| :---: | :---: | :---: |
| 1 | 5.000 | 5.000 |
| 2 | 5.000 + 10.000 | 15.000 |
| 1 | 5.000 + 10.000 + 15.000 | 30.000 |

u are being asked to create a helper to calculate the total of ice cream meter penalty one person needs to pay every 2 weeks. the input will be the total late (in integer) with maximum 10 times late and incremental fee with minimum fee of 1000 and maximum incremental fee of 10000 separated by a space. the output will be the total ice cream meter penalty to pay 

example:

input : 1 3500
output: 3500

input : 3 7000
output: 42000

input : 11 5000
output: Invalid input

------------------------------------------------------------------------------
### Net Caffe
------------------------------------------------------------------------------

net caffe want to open an internet cafe. customer will pay the service hourly, and the more hour the customer spends, the price will get cheaper. Bellow the price table.

| Time (hour) | Price |
| :---: | :---: |
| 1 | Rp. 4.000 |
| 5 | Rp. 18.000 |

U're being asked to create a helper to calculate the price for using a computer in the internet cafe. the input will be in hours (int) and the output in rupiah (int).

example:

input: 1

output: 4000

input: 7

output: 26000 (18000 + 8000)


