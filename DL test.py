import wget
import requests


def wget_test(url):
    wget.download(url)


def requests_test(url, name):
    r = requests.get(url, allow_redirects=True)
    open('dl\\' + name, 'wb').write(r.content)


def requests_head(url):
    h = requests.head(url)
    hs = h.headers
    hs_type = hs.get('content-type')
    return hs_type


def is_downloadable(url):
    h = requests.head(url)
    hs = h.headers
    hs_type = hs.get('content-type')
    if 'text' in hs_type.lower():
        return False, hs_type
    if 'html' in hs_type.lower():
        return False, hs_type
    return True, hs_type


def loop_test(c_max):
    i_locs = []

    for c in range(1, c_max + 1):
        c_comp = 1
        curr_url = 'https://cdn.readmanhwa.com/assets/images/134/chapter-' + str(c) + '/1.jpg'
        while is_downloadable(curr_url):
            curr_url = 'https://cdn.readmanhwa.com/assets/images/134/chapter-' + str(c) + '/' + str(c_comp) + '.jpg'
            i_locs.append(curr_url)
            print('chapter {}; image {}; num_URLs {}; URL: {}'.format(c, c_comp, len(i_locs), curr_url))
            c_comp += 1


if __name__ == '__main__':
    a, b = is_downloadable('http://www.rrachurch.com/wp-content/uploads/sermons/20190512 - Ruth 2-1 - 2-23 - Michael Steinwede.mp3')
    print(b)
    # chapter_max = 73
    # loop_test(chapter_max)

    # image_location = 'https://cdn.readmanhwa.com/assets/images/134/chapter-73/69.jpg'
    # mp3_location = 'http://www.rrachurch.com/wp-content/uploads/sermons/080320.MP3'
    # requests_head('https://cdn.readmanhwa.com/assets/images/134/chapter-73/70.jpg')
    # requests_test(image_location, 'TEST.jpg')
    # requests_head_test(mp3_location)
    # requests_test(mp3_location, 'TEST.mp3')
    # wget_test(mp3_location)