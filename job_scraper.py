import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

jobs = soup.find_all("div",class_="card-content")

print("total jobs found: ", len(jobs))
print("=" * 50)

for job in jobs:
    title = job.find("h2",class_="title").text.strip()
    company = job.find("h3",class_="company").text.strip()
    loction = job.find("p",class_="location").text.strip()

    link_tag = job.find("a",string="Apply")
    link = link_tag["href"] if link_tag else "No Link"

    print("title:", title)
    print("company:", company)
    print("Loction:", loction)
    print("Apply Link: ", link)
    print("-" * 50)




