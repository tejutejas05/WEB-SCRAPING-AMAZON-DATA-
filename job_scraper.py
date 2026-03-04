import requests
from bs4 import BeautifulSoup
import json


url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

jobs = soup.find_all("div",class_="card-content")

print("total jobs found: ", len(jobs))
print("=" * 50)

job_list =[]

for job in jobs:
    title = job.find("h2",class_="title").text.strip()
    company = job.find("h3",class_="company").text.strip()
    location = job.find("p",class_="location").text.strip()

    link_tag = job.find("a",string="Apply")
    link = link_tag["href"] if link_tag else "No Link"

    job_data = {
        "title":title,
        "company":company,
        "location":location,
        "link":link
    }

    job_list.append(job_data)

    with open("jobs.json" , "w", encoding="utf-8") as f:
        json.dump(job_list, f, indent=4)

print("saved as jobs.json")

print("Toatal jobs collected:", len(job_list))






