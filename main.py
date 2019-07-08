import os
import time
from random import randint as rand
while(1):
    pricepage = os.popen('curl https://store.steampowered.com/api/appdetails?appids=821800').read()
    pricepos = pricepage.find('''"price_in_cents_with_discount":''')
    price=pricepage[pricepos+31:]
    priceendpos = price.find('''}''')
    price=price[:priceendpos]
    print(int(price)/100)
    startprice = price
    if startprice != price:
        if startprice > price:
            import tturtle
        else:
            import btturtle
    time.sleep(2)
