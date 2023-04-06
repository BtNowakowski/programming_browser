import webbrowser
import sys

websites = [
    'stackoverflow.com',
    'staclexchange.com',
    'medium.com'
]

url = "https://www.google.com/search?q="


def create_filter():
    filter = '('
    for index, website in enumerate(websites):
        filter += 'site:' + website
        if index == len(websites)-1:
            filter += ')'
        else:
            filter += ' OR '
    return filter


def get_query():
    query = sys.argv[1:]
    return " ".join(query)


if len(sys.argv[1:]) == 0:
    print("Error, not a valid query")
else:
    final_url = url + get_query() + " " + create_filter()
    webbrowser.open(final_url)
