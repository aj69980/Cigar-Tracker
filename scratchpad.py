# god = "$6.50"
# fox = "$6.85"



# def price_as_float(x):
#     price = (float(x[1:5]))
#     price = str(price)
#     return price

# god_price = price_as_float(god)
# fox_price = price_as_float(fox)


# print(type(fox_price))


# if god_price < fox_price:
#     best_price = god_price
# else:
#     best_price = fox_price
    
# # print(best_price)

import datetime as dt
import time
import schedule

current_date = dt.date.today()
current_date = (str(current_date))
times_with_twos = {}  
 
def job():
    pulled_time = time.strftime("%I:%M:%S")
    if "2" in pulled_time:
       times_with_twos[current_date] = pulled_time
       print(times_with_twos)
    else:
        pass
    
    



schedule.every(1).seconds.until("18:00").do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
    
