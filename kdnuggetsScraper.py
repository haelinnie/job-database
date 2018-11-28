from selenium import webdriver

def run():

	options = webdriver.ChromeOptions()

	options.add_argument('headless')

	options.add_argument('window-size=1200x600')

	driver = webdriver.Chrome(chrome_options=options)

	driver.get('https://www.kdnuggets.com/jobs/index.html')

	driver.implicitly_wait(10)

	#driver.get_screenshot_as_file('job_page.png')

	all_links = driver.find_elements_by_xpath("//ul/li/b/a")

	job_position = []
	job_link = []

	for elem in all_links:
	  job_link.append(elem.get_attribute("href"))
	  job_position.append(elem.text)

	return [job_position, job_link]



