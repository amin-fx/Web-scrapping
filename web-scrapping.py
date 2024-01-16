# Calling important modules

import requests as req

# Define URL address

URL = input("Please enter your website address = ")

# Getting url address status code

webPage = req.get(URL)
webRequests = req.delete(URL)
statusCode = webPage.status_code
reason = webPage.reason

# Checking problem in status code
if statusCode == 200:
    print(f"The response of this website is {statusCode} and there is no problem. So the reason of the response is {reason}.")

else:
    print(f"The response of this website is {statusCode} and there is some problems. So the reason of the response is {reason}.")

print("=============================================================================")

# Taking header of the requests

headers = webRequests.request.headers
print(headers)
print("=============================================================================")

# All syntax of website page:
allSyntax = webPage.text
print(allSyntax)
