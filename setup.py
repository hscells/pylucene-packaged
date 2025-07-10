import platform
import sys

from setuptools import setup, find_namespace_packages

package_name = 'lucene'
version = '10.10.0'
python_tags = [f'cp{sys.version_info.major}{sys.version_info.minor}' for _ in range(2)]
platform_name = platform.system().lower()
platform_version = platform.release()

# Super hacky mac stuff.
if platform_name == "darwin":
    platform_name = "macosx"
    platform_version = platform.mac_ver()[0].split('.')[0] + '_0'
    architecture = "universal"

architecture = platform.machine()
wheel_file_name = f'{package_name}-{version}-{"-".join(python_tags)}-{platform_name}_{platform_version}_{architecture}.whl'

setup(
    name='pylucene-packaged',
    version='2025.07.10.1',
    license='Apache License 2.0',
    url='https://github.com/hscells/pylucene-packaged',
    packages=find_namespace_packages(),
    install_requires=[f'lucene@https://github.com/hscells/pylucene-packaged/raw/main/dist/{wheel_file_name}'],
)
