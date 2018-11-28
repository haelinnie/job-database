import sqlite3

from airtable import Airtable

# db = sqlite3.connect('./database.sqlite')
# cursor = db.cursor()
# cursor.execute("""
#         CREATE TABLE jobs(name STRING , link STRING, jobType STRING, location STRING)
# """)
#
#
# db.commit()
# db.close()

# result = internsupplyScraper.run()
# jobs = result[0]
# links = result[1]

# kdnuggets = kdnuggetsScraper.run()
# jobs = kdnuggets[0]
# links = kdnuggets[1]
#
# result = webscraperHw2.jobsSearch()
# jobs = result[0]
# links = result[1]
# Have jobs/links/locations/jobTypes be of the same length and correspond essentially
# To one row of the database (for each i)
def insertInformation(jobs, links, locations, jobTypes):
    db = sqlite3.connect('./database.sqlite')
    cursor = db.cursor()
    for i in range(len(jobs)):
        if (i < len(jobTypes)):
            jobType = jobTypes[i]
        else:
            jobType = None
        if (i < len(locations)):
            location = locations[i]
        else:
            location = None
        cursor.execute('''INSERT INTO jobs(name, link, jobType, location) \
                            VALUES(?,?,?,?)''', (jobs[i], links[i], jobType, location))
    db.commit()
    db.close()

airtable = Airtable('appnr1wKI79xFb1zt', 'Table 1', api_key = 'keyP3vnNHkpql58kI')
# insertInformation(jobs, links, [], [])

db = sqlite3.connect('./database.sqlite')
cursor = db.cursor()

name = cursor.execute('''SELECT name FROM jobs''')
jobType = cursor.execute('''SELECT jobType FROM jobs''')
link = cursor.execute('''SELECT link FROM jobs''')
location = cursor.execute('''SELECT jobType FROM jobs''')

names = list(name.fetchall())
jobTypes = list(jobType.fetchall())
links = list(link.fetchall())
locations = list(location.fetchall())


db.commit()
db.close()

print(len(names), len(jobTypes), len(links), len(locations))
for i in range(len(names)):
    airtable.insert({"Jobs": names[i], "Links": links[i], "Job Type": jobTypes[i], "Location": locations[i]})
