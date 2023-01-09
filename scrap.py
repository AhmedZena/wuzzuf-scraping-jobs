
# first step is to import the libraries
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# second step is to get the url and save it in a variable
result = requests.get(
    "https://wuzzuf.net/search/jobs/?q=frontend&a=hpb")


# third step is to parse the html code and save it in a variable
src = result.content
# print(src)

# fourth step is to create a soup object
soup = BeautifulSoup(src, 'lxml')
# print(soup.prettify())

# fifth step is to get the elements that we want to scrap
# job title , job skills ,company name , job location , job description

# job title
job_titles = soup.find_all('h2', class_='css-m604qf')
# print(job_titles)

# company name
company_names = soup.find_all('a', class_='css-17s97q8')

# job location
job_locations = soup.find_all('span', class_='css-5wys0k')

# job description
# job_descriptions = soup.find_all('div', class_='css-y4udm8')

# job skills
job_skills = soup.find_all('div', class_="css-y4udm8")
# print(job_skills)

# sixth step is to get text from the elements
# job title
job_titles_text = []
for job_title in job_titles:
    job_titles_text.append(job_title.text)
print(job_titles_text)

# company name
company_names_text = []
for company_name in company_names:
    company_names_text.append(company_name.text)
print(company_names_text)

# job location
job_locations_text = []
for job_location in job_locations:
    job_locations_text.append(job_location.text)
print(job_locations_text)

# job description
# job_descriptions_text = []
# for job_description in job_descriptions:
#     job_descriptions_text.append(job_description.text)
# print(job_descriptions_text)

# job skills
job_skills_text = []
for job_skill in job_skills:
    job_skills_text.append(job_skill.text)
print(job_skills_text)

# seventh step is to save the data in a csv file
d = [job_titles_text, company_names_text,
     job_locations_text, job_skills_text]
export_data = zip_longest(*d, fillvalue='')
with open('G:\web scraping/job.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("job title", "company name",
                 "job location", "job skills"))
    wr.writerows(export_data)
# myfile.close()
# illustarte the above code
# d is array of arrays that contains the data
# export_data is a variable that contains the data in a zip format
# with open is a function that creates a csv file and save the data in it
# w is a parameter that means write
# encoding is a parameter that means the encoding of the file
# newline is a parameter that means the new line
# wr is a variable that contains the csv writer
# wr.writerow is a function that writes the first row in the csv file
# wr.writerows is a function that writes the rest of the rows in the csv file
# myfile.close() is a function that closes the csv file

# eighth step is to save the data in a json file
