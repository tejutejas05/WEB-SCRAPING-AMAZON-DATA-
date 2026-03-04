import requests
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd


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


    # this formart will be of json code 

    #with open("jobs.json" , "w", encoding="utf-8") as f:
    #    json.dump(job_list, f, indent=4)

    #below code will be of csv
    #with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    #    writer = csv.DictWriter(f, fieldnames = ["title" , "company" , "location" , "link"])
    #    writer.writeheader()
    #    writer.writerows(job_list)


# Now lets save this in the excel file

df = pd.DataFrame(job_list)
df.to_excel("jobs.xlsx", index=False)

print("saved as jobs.xlsx")


print("saved as jobs.csv file")

print("saved as jobs.json")

print("Toatal jobs collected:", len(job_list))






