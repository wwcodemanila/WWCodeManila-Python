""" Aling Nena's Receipt Challenge
Author:
Description: Just like in grocery stores where items where scanned one by one and the
total amount due is summed, please help Aling Nena's Sari-sari store
to compute a customer's total order amount and print the receipt by:
* Input the customer's products
* The product dictionary contains Aling Nena's products and maps it's price.
* If the product name is NOT in her list, just print 'Item <product name> void!'
  and skip it from the computation of total amount due.
* If the product is in the list, please print current purchased products and
  their quantity.
* If done punching the items:
    - Print each purchased products, it's quantity, price, total price (quantity * price)
    - Print the total items and total amount due.

@example
Item name:  sunsilk
{'sunsilk': 1}
Are you done? Press y to finish: n
Item name:  SUNsilk
{'sunsilk': 2}
Are you done? Press y to finish: n
Item name:  ligo
{'sunsilk': 2, 'ligo': 1}
Are you done? Press y to finish: n
Item name:  Spam
{'sunsilk': 2, 'ligo': 1, 'spam': 1}
Are you done? Press y to finish: n
Item name:  test
Item test void!
Are you done? Press y to finish: n
Item name:  ligo
{'sunsilk': 2, 'ligo': 2, 'spam': 1}
Are you done? Press y to finish: y
***** PRINTING YOUR RECEIPT *****
sunsilk 7.5 * 2 = 15.0
ligo 12.0 * 2 = 24.0
spam 115.25 * 1 = 115.25
5 items --------- 154.25
"""

products = {
    'sunsilk': 7.50,
    'dove': 8.00,
    'tide': 12.50,
    'coke': 45.75,
    'sprite': 45.75,
    'spam': 115.25,
    'ligo': 12.00
}

# Let's punch the customer's items!
is_done = 'n'
while is_done != 'y':
    item = input('Item name: ').lower()
    # Check if done punching items
    is_done = input('Are you done? Press y to finish:').lower()
