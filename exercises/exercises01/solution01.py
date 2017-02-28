"""
Reference: https://codepad.remoteinterview.io/WDRGWBXXHO
Uploaded by: Kirsten Sison
"""
total_bill = float(input("What's your total bill?"))
payment_amount = float(input("Input payment:"))

change = payment_amount - total_bill

reply = 'Your change is {}'.format(change)
print(reply)
