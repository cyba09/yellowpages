# Yellow Pages  Data Scrapper

YPDS is a Python script for scraping emails and phone numbers from [Yellow Pages](https://www.yellowpages.ca/) onto excell file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install playwright bs4 requests pandas
```
Install playwright chromium webdriver
```bash
playwright install
```
## Usage
Change query and location in lines 8 and 9 in main.py
```python

# change here
What = 'Indian Restaurant'
Where = 'Mississauga ON'


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
