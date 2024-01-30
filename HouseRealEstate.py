current_price = int(input())
last_months_price = int(input())

print('This house is ${price}. The change is ${change} since last month.'.format(price = current_price, change = current_price - last_months_price))
print('The estimated monthly mortgage is ${mortgage:.2f}.'.format(mortgage = (current_price * 0.051) / 12))
   