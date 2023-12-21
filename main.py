import requests
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

all_jobs = []

response = requests.get(base_url)
soup = BeautifulSoup(
  response.content, 
  "html.parser", 
)

jobs = soup.find("section", 
class_="jobs").find_all("li")[1:-1]

for job in jobs:
  title = job.find("span", class_="title").text
  company, position, region = job.find_all("span", class_="company")
  url = job.find("div", class_="tooltip").next_sibling
  if url:
    url = url["href"]

  job_data = {
    "title": title, 
    "company": company.text,
    "position": position.text, 
    "region": region.text,
    "url": f"https://weworkremotely.com{url}",
  } 
  all_jobs.append(job_data)

print(all_jobs)

