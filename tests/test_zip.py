import zipfile
from zipfile import ZipFile
import os.path
from tests.conftest import tmp_directory_path

#путь к папке recourses
resources_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))

#путь к файлам для архивации
arch_files = os.listdir(resources_dir)

#путь к zip файлу
path_zip = os.path.abspath(os.path.join(tmp_directory_path, 'new_zip'))


def test_zip_arch(tmp_directory):
    with ZipFile(path_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zip_arch:
        for file in arch_files:
            add_file = os.path.join(resources_dir, file)
            zip_arch.write(add_file)
    with ZipFile(path_zip) as zip_arch:
        assert len(arch_files) == len(zip_arch.infolist())
