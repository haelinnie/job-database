import sqlite3
import internsupplyScraper

# db = sqlite3.connect('./database.sqlite')
# cursor = db.cursor()
# cursor.execute("""
#         CREATE TABLE jobs(name STRING , link STRING, jobType STRING, location STRING)
# """)
#
#
# db.commit()
# db.close()

result = internsupplyScraper.run()
jobs = result[0]
links = result[1]

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

#insertInformation(jobs, links, [], [])
