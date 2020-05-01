import os
import time
import sys
try:
    try:
        mode = sys.argv[2]
    except:
        mode="nondev"
    appid = sys.argv[1]
    while(1):
        pricepage = os.popen('curl https://store.steampowered.com/api/appdetails?appids='+appid).read()
        pricepos = pricepage.find('''"price_in_cents_with_discount":''')
        price=pricepage[pricepos+31:]
        priceendpos = price.find('''}''')
        price=price[:priceendpos]
        print("Price is",int(price)/100)
        startprice = price
        if startprice != price:
            if startprice > price:
                import tturtle
            else:
                import btturtle
        if mode == "-dev":
            time.sleep(2)
        else:
            time.sleep(120)
except:
    print('''
Usage:
================================================================================
python3 main.py [options] <appid>
    -dev    enable development mode(check the price more frequently)
================================================================================
Appid is the steam app id. For example PLAYERUNKNOWN'S BATTLEGROUNDS's steam url
is https://store.steampowered.com/app/578080. So PLAYERUNKNOWN'S BATTLEGROUNDS's
appid is 578080.
================================================================================
    ''')
