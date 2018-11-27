import requests
import bs4

def run():
    res = requests.get("https://www.intern.supply/")
    try:
        res.raise_for_status()
    except Exception as e:
        print(e)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    companyNames = []
    companyLinks = []
    for companyDiv in soup.find_all("div", "box company-row"):
        companyName = companyDiv.find("p", "title is-5")
        if companyName is None: #some companies like Amazon/Facebook/Microsoft have a different format for name
            companyName = companyDiv.find("p", "title is-5 badge")
        name = companyName.string
        for link in companyDiv.find_all("a"):
            if 'href' in link.attrs:
                companyNames.append(name)
                companyLinks.append(link['href'])

    return [companyNames, companyLinks]
