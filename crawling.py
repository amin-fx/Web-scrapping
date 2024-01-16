# Calling important modules
import requests as req
from bs4 import BeautifulSoup as BS

# Define URL address and getting URL detail
URL = input("Enter URL address = ")
response = req.get(URL)

# Storing URL syntax as HTML
content = BS(response.text, "html.parser")

# Find head and title tag
head = content.find("head")
title = head.find("title").text
print(f"The title of the website = {title}")

print("===========================================\n")

# Finding all links in body

body = content.find("body")
aTag = body.find_all("a")

# Extract all links in <a> :
for link in aTag:
    href = link["href"]
    print(href)

print("===========================================\n")

# Finding all h tags eg, <h1>, <h2>, etc.
h1Tags = content.find_all("h1")
h1Text = [h1.get_text(strip=True) for h1 in h1Tags]
print(f"All <h1> tags :\n {h1Text}") if h1Text else print("There is no <h1> tag in this web page")
print("===========================================")
print("===========================================\n")

h2Tags = content.find_all("h2")
h2Text = [h2.get_text(strip=True) for h2 in h2Tags]
print(f"All <h2> tags :\n {h2Text}") if h2Text else print("There is no <h2> tag in this web page")
print("===========================================")
print("===========================================\n")

h3Tags = content.find_all("h3")
h3Text = [h3.get_text(strip=True) for h3 in h3Tags]
print(f"All <h3> tags :\n {h3Text}") if h3Text else print("There is no <h3> tag in this web page")
print("===========================================")
print("===========================================\n")

h4Tags = content.find_all("h4")
h4Text = [h4.get_text(strip=True) for h4 in h4Tags]
print(f"All <h4> tags :\n {h4Text}") if h4Text else print("There is no <h4> tag in this web page")
print("===========================================")
print("=========================================== \n")

h5Tags = content.find_all("h5")
h5Text = [h5.get_text(strip=True) for h5 in h5Tags]
print(f"All <h5> tags :\n {h5Text}") if h5Text else print("There is no <h5> tag in this web page")
print("===========================================")
print("=========================================== \n")

h6Tags = content.find_all("h6")
h6Text = [h6.get_text(strip=True) for h6 in h6Tags]
print(f"All <h6> tags :\n {h6Text}") if h6Text else print("There is no <h6> tag in this web page")
print("===========================================")
print("===========================================\n")
