import socket
import ssl
import sys
import urllib

from django.core.exceptions import ObjectDoesNotExist
from website.models import NL, Command, URL


def get_nl(nl_str):
    try:
        nl = NL.objects.get(str=nl_str)
    except ObjectDoesNotExist:
        nl = NL.objects.create(str=nl_str)
    return nl


def get_command(command_str):
    try:
        cmd = Command.objects.get(str=command_str)
    except ObjectDoesNotExist:
        cmd = Command.objects.create(str=command_str)
    return cmd


def get_url(url_str):
    try:
        url = URL.objects.get(str=url_str)
    except ObjectDoesNotExist:
        html = extract_html(url_str)
        if html is None:
            url = URL.objects.create(str=url_str)
        else:
            url = URL.objects.create(str=url_str, html_content=html)
    return url


def extract_html(url):
    hypothes_prefix = "https://via.hypothes.is/"
    try:
        html = urllib.request.urlopen(hypothes_prefix + url, timeout=2)
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
