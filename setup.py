from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'botv',
  packages = ['botv'],
  version = '2.3.1',
  license='MIT',
  description = 'Easy to use dict constructor for botv.io usage',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Chemss Eddine Ben Hassine',
  author_email = 'bhchemss@gmail.com',
  url = 'https://github.com/chemsseddine/',
  download_url = 'https://github.com/chemsseddine/botv/archive/v2.3.1.tar.gz',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
