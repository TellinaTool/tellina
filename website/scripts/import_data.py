import pickle

from website.models import URLTag
from website.utils import get_url


def load_urls(input_file_path):
    with open(input_file_path, 'rb') as f:
        urls = pickle.load(f)

    for utility in urls:
        for url in urls[utility]:
            url = get_url(url)

            if not URLTag.objects.filter(url=url, tag=utility):
                URLTag.objects.create(url=url, tag=utility)
                print("Add {}, {}".format(url, utility))


if __name__ == '__main__':
    load_urls()
