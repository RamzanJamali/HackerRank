from selenium import webdriver
from bs4 import BeautifulSoup
import time

# URL of the page containing the tables
url = "https://www.irishracing.com/trainer/Noel-Meade/229"

# Initialize Selenium webdriver
driver = webdriver.Chrome()  # You need to have chromedriver installed and in your PATH
driver.get(url)
time.sleep(5)  # Allowing time for the page to load

# Scraping the page source
page_source = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all tables on the page
tables = soup.find_all('div')
print(tables)
# Loop through each table and print its content
import csv

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['','']
    for table in tables:
       # Find all rows in the table
       rows = table.find_all('a')
       for row in rows:
           # Find all cells in the row
           cells = row.find_all(['div'])
           row_data = [cell.text.strip() for cell in cells]
           print(row_data)
           writer.writerow(row_data)
# Close the webdriver
driver.quit()
