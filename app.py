from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")
    job_list = []

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        link_tag = job.find("a", string="Apply")
        link = link_tag["href"] if link_tag else "No Link"

        job_data = {
            "title": title,
            "company": company,
            "location": location,
            "link": link
        }

        job_list.append(job_data)

    return job_list


@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = scrape_jobs()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True)