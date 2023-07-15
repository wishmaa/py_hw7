import os.path

import requests

from tests.conftest import tmp_directory_path

url = 'https://selenium.dev/images/selenium_logo_square_green.png'
path_to_file = os.path.abspath(os.path.join(tmp_directory_path, 'selenium_logo.png'))


def test_download_file_png(tmp_directory):
    response = requests.get(url)
    with open(path_to_file, 'wb') as file:
        file.write(response.content)

    assert os.path.exists(path_to_file)

    print(os.path.getsize(path_to_file))

    assert (os.path.getsize(path_to_file)) == 30803

    os.remove(path_to_file)