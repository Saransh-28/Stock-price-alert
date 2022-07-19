# import all required module
import yfinance as yf
from winotify import Notification , audio
import time

# make a list of all the stocks and the list of thershold stock price
stocks_list = ['TSLA','AAPL']
alert_val = [730,1000]

while True:
    # make a list of all the stocks that are below threshold
    alert_list= []
    for i , stock in enumerate(stocks_list):
        market_price = int(yf.Ticker(stock).info['regularMarketPrice'])

        # compare present price with given threshold price
        if market_price < alert_val[i]:
            alert_list.append(stock)

    # if any given stock is below threshold price then send notification
    if len(alert_list) > 0:
        all_stocks_names = ''
        if len(alert_list) == 1:
            # send notification
            notification = Notification(app_id='stock alert script' , 
                                    title='price alert',
                                    msg = f'{alert_list[0]} is below the set thershold',
                                    duration='long',
                                    icon=r'C:\Users\saran\Desktop\python\python\practice\random project\image.jpg')
            notification.set_audio(audio.Reminder,loop=False)
            notification.show() 

        else:
            # make all stocks names in one string
            for stock in alert_list:
                all_stocks_names += ', #' + stock

            # send notification
            notification = Notification(app_id='stock alert script' , 
                                    title='price alert',
                                    msg = f'{all_stocks_names} is below the set thershold',
                                    duration='long',
                                    icon=r'C:\Users\saran\Desktop\python\python\practice\random project\image.jpg')
            notification.set_audio(audio.Reminder,loop=False)
            notification.show() 

    # sleep for 10 minutes
    time.sleep(600)
