import requests
from bs4 import BeautifulSoup

page = requests.get("https://nytimes.com")

print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# Find and print the header
header = soup.find(class_="css-ahe4g0 e1suatyy1")

print(header.prettify())

# Find and print the date at the top
# Unfortunately, you can't statically grab the date!
date = header.find(class_="css-bpgv3s e1csuq9d0")
print(date.prettify())

# Who publishes the NYT?
publisher = soup.find(class_="css-jq1cx6")
print(publisher.prettify())

# aaaand just grab the text
print(publisher.get_text())

# thanks for coming to my ted talk