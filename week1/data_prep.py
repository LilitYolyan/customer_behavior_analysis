# Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import date

def data_preparation():
    
    # Data 
    data = pd.read_csv('data.csv', engine='python')

    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['CustomerID'] = data['CustomerID'].astype('O')

    # Remove NAs
    data.dropna(subset=['CustomerID'], inplace=True)

    filtered = data[data['Quantity'] >= 0]
    filtered = filtered[filtered['Quantity']<5000]

    vals = ['M', 'D', 'POST',  'DOT', 'CRUK']
    filtered = filtered[~filtered['StockCode'].isin(vals)]

    filtered = filtered[filtered['UnitPrice']<500]

    filtered['TotalPrice'] = filtered['Quantity'] * filtered['UnitPrice']
    filtered['OrderHour'] = filtered.InvoiceDate.dt.hour
    filtered['OrderMonth'] = filtered.InvoiceDate.dt.month
    filtered['OrderWeekday'] = filtered.InvoiceDate.dt.weekday_name
    
    return filtered


