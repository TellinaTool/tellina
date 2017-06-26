import html
import os, sys
import pickle
import re
import sqlite3

from website.models import URL, URLTag
from website.utils import get_tag, get_command, get_url

learning_module_dir = os.path.join(os.path.dirname(__file__), '..', '..',
                                   "tellina_learning_module")
sys.path.append(learning_module_dir)

from bashlex import data_tools


CODE_REGEX = re.compile(r"<pre><code>([^<]+)<\/code><\/pre>")

def extract_code(text):
    for match in CODE_REGEX.findall(text):
        if match.strip():
            yield html.unescape(match.replace("<br>", "\n"))


def load_urls(input_file_path):
    with open(input_file_path, 'rb') as f:
        urls_by_utility = pickle.load(f)

    for utility in urls_by_utility:
        for url in urls_by_utility[utility]:
            if not URLTag.objects.filter(url__str=url, tag=utility):
                URLTag.objects.create(url__str=url, tag=utility)
                print("Add {}, {}".format(url, utility))


def import_commands_in_url(stackoverflow_dump_path):
    url_prefix = 'https://stackoverflow.com/questions/'

    with sqlite3.connect(stackoverflow_dump_path, detect_types=sqlite3.PARSE_DECLTYPES) as db:
        for url in URL.objects.all():
            print(url.str)
            if not url.html_content:
                for question_id, answer_body in db.cursor().execute("""
                        SELECT questions.Id, answers.Body FROM questions, answers
                        WHERE questions.Id = answers.ParentId AND questions.Id = {}
                        """, url.str[len(url_prefix):]):
                    url.html_content = answer_body
                    url.save()

            for cmd in extract_code(url.html_content):
                print(cmd)
                cmd = cmd.strip()
                command = get_command(cmd)
                url.commands.append(command)
                ast = data_tools.bash_parser(cmd)
                for utility in data_tools.get_utilities(ast):
                    command.tags.append(get_tag(utility))
                    command.save()
                    
            url.save()


if __name__ == '__main__':
    load_urls()