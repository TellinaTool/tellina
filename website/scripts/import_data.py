import pickle
import socket
import ssl
import sys
import urllib

from django.core.exceptions import MultipleObjectsReturned
from website.models import URL, URLTag

def extract_html(url):
    hypothes_header = "https://via.hypothes.is/"
    try:
        html = urllib.request.urlopen(hypothes_header + url, timeout=2)
    except urllib.error.URLError:
        print("Error: extract_text_from_url() urllib2.URLError")
        # return "", randomstr(180)
        return None, None
    except socket.timeout:
        print("Error: extract_text_from_url() socket.timeout")
        # return "", randomstr(180)
        return None, None
    except ssl.SSLError:
        print("Error: extract_text_from_url() ssl.SSLError")
        # return "", randomstr(180)
        return None, None

    return html.read()


def load_urls(input_file_path):
    with open(input_file_path, 'rb') as f:
        urls = pickle.load(f)

    for utility in urls:
        for url in urls[utility]:
            if not URL.objects.filter(str=url):
                html = extract_html(url)
                if html is None:
                    url_obj = URL.objects.create(str=url)
                else:
                    url_obj = URL.objects.create(str=url, html_content=html)
            else:
                try:
                    url_obj = URL.objects.get(str=url)
                except MultipleObjectsReturned:
                    for url_obj in URL.objects.filter(str=url):
                        break

            if not URLTag.objects.filter(url=url_obj, tag=utility):
                URLTag.objects.create(url=url_obj, tag=utility)
                print("Add {}, {}".format(url, utility))


if __name__ == '__main__':
    load_urls()
