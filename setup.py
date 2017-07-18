from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
  name = 'pySkroutz',
  packages = ['pySkroutz'],
  version = '0.0.1.4',
  description = 'Unofficial Python SDK for Skroutz.gr API. This client library is designed to support the Skroutz API. You can read more about the Skroutz API by accessing its official documentation.',
  author = 'Panagiotis Simakis',
  license = 'GPL',
  author_email = 'simakis@autistici.org',
  url = 'https://github.com/sp1thas/pySkroutz',
  download_url = 'https://github.com/sp1thas/pySkroutz/archive/0.0.1.3.tar.gz',
  keywords = ['skroutz', 'python-sdk', 'sdk', 'api'],
  classifiers = [],
  install_requires=[
        'requests'
    ],
)
