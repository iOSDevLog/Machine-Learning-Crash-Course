#!/usr/bin/env python
from requests_html import HTMLSession
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://developers.google.com/machine-learning/crash-course/'

def course_info(course_url):
    session = HTMLSession()
    request = session.get(course_url)

    data_video_url = ''
    data_captions_url = ''
    # video_info = request.html.find('.devsite-vplus', first=True)
    # data_video_url = video_info.attrs['data-video-url']
    # data_captions_url = video_info.attrs['data-captions-url']

    next_url_info = request.html.find('div.devsite-steps-next > a.devsite-steps-link', first=True)
    next_url = next_url_info.attrs['href']

    return (data_video_url, data_video_url, next_url)

import urllib.request

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def saveHtml(file_name, file_content):
    dir = 'course_html/'
    file_name = file_name.replace('/','_')+'.html'
    path = os.path.join(dir, file_name)
    with open (path, 'wb') as f:
        f.write(file_content)

if __name__ == '__main__':
    next_url = 'https://developers.google.com/machine-learning/crash-course/framing/check-your-understanding'
    while next_url:
        try:
            (_, _, next_url) = course_info(next_url)
            filename = os.path.basename(next_url)
            html = getHtml(next_url)
            saveHtml(filename, html)
            print(next_url)
        except:
            sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
