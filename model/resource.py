import os

import tests


def path(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../tests/images/{file_name}')
    )
