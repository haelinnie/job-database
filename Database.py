import sqlite3

# db = sqlite3.connect('./database.sqlite')
# cursor = db.cursor()
# cursor.execute("""
#         CREATE TABLE jobs(name STRING , link STRING, jobType STRING, location STRING)
# """)
#
#
# db.commit()
# db.close()


# Have jobs/links/locations/jobTypes be of the same length and correspond essentially
# To one row of the database (for each i)
def insertInformation(jobs, links, locations, jobTypes):
    db = sqlite3.connect('./database.sqlite')
    cursor = db.cursor()
    for i in range(len(jobs)):
        cursor.execute('''INSERT INTO jobs(name, link, jobType, location) \
                            VALUES(?,?,?,?)''', (jobs[i], links[i], jobTypes[i], locations[i]))
    db.commit()
    db.close()
