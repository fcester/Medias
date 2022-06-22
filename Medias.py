import pandas as pd
from openpyxl import Workbook
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import sys
from mplfinance.original_flavor import candlestick_ohlc

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

stock = ["MELI"]
today = date.today()
first_day = "2018-01-01"
#Descarga de precios, cambia los nombres de las columnas de adj close por price
for activos in stock:
    df = yf.download(stock,start=first_day, end=today)

investment = pd.DataFrame()
investment["Price"] = df["Adj Close"]
investment["Return"] = investment["Price"].pct_change()


ma_day = [50,100,200]
#aca crea las medias para 50, 100 y 200 ruedas
for period in ma_day:
    column_name = f"{period}d MA"
    investment[column_name] = investment["Price"].rolling(period).mean()
    #plt.pyplot(investment)
    #plt.title("Grafico" + stock)
    #plt.show()
#precio maximo y minimo dentro de 52 semanas
investment["52W Max"] = investment["Price"].rolling(250).max()
investment["52W Min"] = investment["Price"].rolling(250).min()

pd.options.display.float_format = "{:.2f}".format
investment.dropna(inplace=True)
investment.tail()

#Opcion para graficar la inversion

investment.plot(grid=True)
plt.title(activos)
plt.show()
# filtro para busquedas dentro del dataframe
# print(investment.loc[investment.Return < -0.15])
#print(investment.loc[investment.Return < -0.15])


"""df = df[(df['fecha']>'2016-01-01')]
plt.figure(figsize=(15,10))
plt.plot(df['fecha'], df['cierre'])
plt.gcf().autofmt_xdate()
plt.show()"""



#print(investment)


#ebitdaMargins
#profitMargins
#revenueGrowth
#debtToEquity
#revenuePerShare
#enterpriseToEbitda
#trailingEps
#forwardEps
#beta
#pegRatio
#trailingPegRatio