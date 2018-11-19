import requests
from bs4 import BeautifulSoup


def get_webpage(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as e:
        print(e)
    return res

link = get_webpage('https://www.careerbuilder.com/jobs-computer-science-intern?page_number=1')
soup = BeautifulSoup(link.text, 'lxml')
pageCount = soup.find('span', attrs={'class':'page-count'}).text.strip()
pageNums = [int(char) for char in pageCount.split(' ') if char.isdigit()]
def findJobs():
    jobs, links, locations, jobTypes = [], [], [], []
    for i in range(pageNums[0], pageNums[1]):
        link = get_webpage('https://www.careerbuilder.com/jobs-computer-science-intern?page_number=' + str(i))
        soup = BeautifulSoup(link.text, 'lxml')
        for job in soup.findAll('div', class_='job-row'):
            a = job.findAll('a', href = True)
            jobTitle = a[0].text.strip()
            link = 'www.careerbuilder.com/' + str(a[0]['href']).strip()
            location = job.find('div', class_='columns end large-2 medium-3 small-12').text.strip()
            jobType = job.find('div', class_='columns medium-6 large-8').find('h4').text.strip()
            jobs.append(jobTitle)
            links.append(link)
            locations.append(location)
            jobTypes.append(jobType)
            print("Job title: %s " % jobTitle)
            print("Job type: %s " % jobType)
            print("Location: %s " % location)
            print("Link: %s " % link)
            print("\n")
    return jobs, links, locations, jobTypes
findJobs()
