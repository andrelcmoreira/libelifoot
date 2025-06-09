from setuptools import setup, find_packages


setup(
    name='libelifoot',
    version='0.1.0',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='André L. C. Moreira',
    author_email='andrelcmoreira@disroot.org',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Unidecode',
        'BeautifulSoup4'
    ],
    license='LGPLv3',
    python_requires='>=3.7',
)
