from forms_automation.automator import FormsAutomator


def main():
    automator = FormsAutomator(
        form_url="",
        checkbox_pos=(850, 620),
        submit_pos=(900, 780),
    )

    automator.run()


if __name__ == "__main__":
    main()
