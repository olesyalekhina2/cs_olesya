from setuptools import setup

import pyvcs

AUTHOR = "Olesya Alekhina"
AUTHOR_EMAIL = "ale_um@inbox.ru"
HOME_PAGE = "https://github.com/olesyalekhina2/cs_olesya"

setup(
    name="pyvcs",
    version=pyvcs.__version__,
    description="The stupid content tracker",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=["pyvcs"],
    entry_points={"console_scripts": ["pyvcs = pyvcs.__main__:main"]},
    url=HOME_PAGE,
    license="GPLv3",
    python_requires=">=3.6.0",
)
