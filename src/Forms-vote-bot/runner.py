import time
import webbrowser

from utils.automator import _scroll, _click, open_browser
from utils.validate import validate_url
from utils.position import get_checkbox_position, get_submit_position
from config.settings import IMAGE_DIR


def main():
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdXRtcx9G24a6_ccvbjwQyP3bcWHiOWZs4etGuSEyY_UF28Lg/viewform"

    url = validate_url(form_url)

    open_browser(url)

    _scroll(7)

    time.sleep(1)

    checkbox_pos = get_checkbox_position(IMAGE_DIR)

    _click(checkbox_pos)

    _scroll(22)

    time.sleep(1)

    submit_pos = get_submit_position(IMAGE_DIR)

    _click(submit_pos)

if __name__ == "__main__":
    main()
