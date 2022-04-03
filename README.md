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

Preconditions:
- make sure you've made your reading list public
- make sure you've changed username in url to yours

### Parse first 20 titles from your Medium reading list
```sh
python -m spider --url https://username.medium.com/list/reading-list
```
### Parse first 200 titles your Medium reading list
```sh
python -m spider --url https://username.medium.com/list/reading-list --page_count 10
```
### Classify titles using huggingface zero-shot learning pipeline
```sh
python -m classifier --data_path ./outputs/output.csv --predictions_output ./outputs/predictions.csv --num_of_titles 100 --output_path ./outputs/output.png
```
