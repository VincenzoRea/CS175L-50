#Stock Transaction Program
#COMMISSION_RATE = 0.0
#NUM_SHARES = 0
#PURCHASE_PRICE = 0.0
#SELLING_PRICE = 0.0
COMMISSION_RATE = float(input('What was the commission rate?:'))
NUM_SHARES = int(input('How many shares were bought?:'))
PURCHASE_PRICE = float(input('What price were the shares bought for?:'))
SELLING_PRICE = float(input('What was the selling price?:'))

amountPaidForStock = (NUM_SHARES * PURCHASE_PRICE)
purchaseCommission = (COMMISSION_RATE * amountPaidForStock)
totalPaid = (amountPaidForStock + purchaseCommission)
stockSoldFor = (NUM_SHARES * SELLING_PRICE)
sellingCommission = (COMMISSION_RATE * stockSoldFor)
totalReceived = (stockSoldFor - sellingCommission)
profitOrLoss = (totalReceived - totalPaid)
totalCommissionPaid = (purchaseCommission + sellingCommission)




print (f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print (f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print (f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print (f'Commission paid on the sale: ${sellingCommission:,.2f}')
print (f'Total commission paid: ${totalCommissionPaid:,.2f}')
print (f'Profit/Loss made: ${profitOrLoss:,.2f}')



