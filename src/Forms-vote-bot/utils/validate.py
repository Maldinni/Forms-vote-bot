import re

def validate_url(url):
    URL_REGEX = re.compile(r'^(https?:\/\/)([\w-]+\.)+[\w-]{2,}(\/[^\s]*)?$')

    if not URL_REGEX.match(url):
        raise ValueError("URL inválida.")
    else:
        return url
