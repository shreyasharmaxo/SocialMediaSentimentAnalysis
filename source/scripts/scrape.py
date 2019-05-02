from bs4 import BeautifulSoup
import requests
import json


def get_info(first_name, last_name):
    query = first_name + " " + last_name
    profile = dict([])
    profile['name'] = query
    link = 'https://en.wikipedia.org/wiki/' + query
    page_response = requests.get(link)
    html = BeautifulSoup(page_response.content, "html.parser")  # yields page html
    infobox = html.find('table', {'class': 'infobox'})  # yields infobox html
    summary = ''
    for p in html.find_all('p'):
        if "signature" in str(p) or "Signature" in str(p):
            continue
        if last_name in str(p):
            summary = p
            break
    profile['image'] = infobox.find('img').get_attribute_list('src')[0]
    age_tag = infobox.find('span', {'class': 'noprint ForceAgeToShow'}).string  # finds html tag with actor age
    profile['age'] = age_tag.replace("(age", "").replace(")","").replace(" ","")[1:]  # cleans up extra html to yield age number
    profile['party'] = ''
    for a in infobox.find_all('a'):
        if a.string == 'Democratic' or a.string == 'Republican' or a.string == 'Independent':
            profile['party'] = a.string
            break

    profile['summary'] = str(summary).replace("<p>", "<p class=\"summary\">").replace("/wiki/", "https://en.wikipedia.org/wiki/")

    with open('../../data/profile.json', 'w') as fp:
        json.dump(profile, fp)


# get_info(given_name, surname)
