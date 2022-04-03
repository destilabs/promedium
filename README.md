# Promedium
## _Repository of tools to improve medium user experience_

## Features

- Parsing of reading list
- Zero-shot learning classification of reading list titles

## Installation

Promedium requires Python3.9 and [Selenium Chrome Driver](https://chromedriver.chromium.org/downloads) to be installed.

Create virtual environment and install requirements.txt

```sh
python3.9 -m pip install virtualenv
python3.9 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

After completion run like this:
- make sure you've made your reading list public
- make sure you've changed username in url to yours

```sh
python -m spider --url https://username.medium.com/list/reading-list
```
