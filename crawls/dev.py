import requests

url = "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dev_guide.htm"
html = requests.get(url, timeout=20).text

print(html)