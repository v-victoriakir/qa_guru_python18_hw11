import os


class PracticeFormPage:
    def __init__(self, browser):
        self.browser = browser
        self.base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources')
        )

    def upload_picture(self, picture):
        file_path = os.path.join(self.base_path, picture)
        self.browser.element('#uploadPicture').send_keys(file_path)

        return self