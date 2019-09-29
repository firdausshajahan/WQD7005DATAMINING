import requests
import csv
from bs4 import BeautifulSoup

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'})

# Define URL and set Request
url = 'http://www.bnm.gov.my/index.php?ch=statistic&pg=stats_exchangerates&lang=en&StartMth=9&StartYr=2018&EndMth=9&EndYr=2019&sess_time=0900&pricetype=Buy&unit=rm'
req = requests.get(url, headers=headers)

#using beautifulSoup lets grab the whole from the URL
bnmContent = BeautifulSoup(req.content,"lxml")

#find the table that has the exchange rate
exchange_table = bnmContent.find(class_='Stats-table')

#grab the rows of table
exchange_table_list_items = exchange_table.find_all('tr',attrs={'class': None})

#set empty array to push later to write csv file
output_rows = []

#loop each row and column of the table to get the text
for table_row in exchange_table.findAll('tr',attrs={'class': None}):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.get_text())
    #push the row and column to generate csv
    output_rows.append(output_row)

#generate csv
with open('exchangeRate.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)