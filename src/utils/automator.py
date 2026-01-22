import time
import webbrowser
import pyautogui

pyautogui.FAILSAFE = True


class FormsAutomator:
    def __init__(self, form_url, checkbox_pos, submit_pos):
        self.form_url = form_url
        self.checkbox_pos = checkbox_pos
        self.submit_pos = submit_pos

    def run(self):
        webbrowser.open(self.form_url)
        time.sleep(6)

        self._scroll(5)
        pyautogui.click(self.checkbox_pos)
        time.sleep(1)

        self._scroll(8)
        pyautogui.click(self.submit_pos)

    def _scroll(self, times, amount=-500):
        for _ in range(times):
            pyautogui.scroll(amount)
            time.sleep(0.4)
