import requests  # for accessing the websites
from bs4 import BeautifulSoup  # for capturing the relevant tags for downloading
from fake_useragent import UserAgent  # for generating user agents to access otherwise inaccessible sites


def get_user_agent():  # creates a user agent for requests to spoof
    ua = UserAgent()
    print(ua.firefox)  # I prefer Firefox agents
    return ua.firefox


def get_html(url, session):  # cuts the useless parts of the object, leaving only the content (the HTML)
    r = session.get(url)
    return r.content


def trim_rrac_mp3_url(url):
    url = url[url.find("file_name=") + 10:-4]  # trim for the content of file_name
    url = url.replace("+", "%20")  # fix the spaces
    url = "http://www.rrachurch.com/wp-content/uploads/sermons/" + url  # add the file_name to the right host
    return url


def get_sermons(url, file_name):
    # Downloads the supplied .mp3 site / page content
    with open(file_name, 'wb') as file:
        doc = sesh.get(url)
        file.write(doc.content)


if __name__ == '__main__':
    # Blank inits, because there's no such thing as a do_while loop in Python
    all_soups, new_soups, rrac_mp3s = [], [], []
    num = 0

    # Create a valid session with a usable user-agent
    agent = get_user_agent()
    sesh = requests.Session()
    sesh.headers.update({'User-Agent': str(agent)})

    # Get the pages' urls, adding them to a master list. Stop when a page is devoid of .mp3s
    while len(new_soups) != 0 or num == 0:
        num += 1
        new_url = 'http://www.rrachurch.com/bible-talks/?pagenum=' + str(num)
        html = get_html(new_url, sesh)

        new_soup = BeautifulSoup(html, 'html.parser')
        new_soups = new_soup.find_all(attrs={"type": "audio/mpeg"})
        for new_soup in new_soups:
            all_soups.append(new_soup)
        print("NUM = " + str(num) + "  ;  LEN_SOUPS = " + str(len(new_soups)))

    # Pull the content from the floating HTML tags / attributes and cleans them for downloading
    for soup in all_soups:
        rrac_mp3s.append(soup.get('src'))
    # print(rrac_mp3s)  # test code for retrieving the correct urls
    # print(len(rrac_mp3s))
    # print(trim_rrac_mp3_url(rrac_mp3s[0]))  # test code for trimming the url
