from urllib.request import urlopen


def request_url(url):
    try:
        with urlopen(url) as response:
            html = response.read()
            return html
    except ValueError:
        raise ValueError(f"Unreachable URL: {url}")


def count_i_occurrences(url):
    html = request_url(url)
    return str(html).count("i")


print(count_i_occurrences("https://example.com"))
