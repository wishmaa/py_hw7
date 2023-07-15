import glob
import os
import pytest

tmp_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..tmp'))

@pytest.fixture(scope='function', autouse=False)
def tmp_directory():
    if not os.path.exists(tmp_directory_path):
        os.makedirs(tmp_directory_path)
    yield

    files = glob.glob(os.path.join(tmp_directory_path, '*'))
    for f in files:
        os.remove(f)
