# pywikiscraper
Pywikiscraper is a short library to scrape any Wikipedia page using just the url


## Installation - 

### Using pip
directly install using pypi repository
```
pip install pywikiscraper
```
link for project on pypi.org - https://pypi.org/project/pywikiscraper/

### cloning the repository from github

```
git clone 
```
got to the directory pywikiscrape>dist and run the following command

```
pip install pywikiscraper-*.*.*-py3-none-any.whl
```

## requirements 

these requirements will be downloaded automatically if you used a pip install
```
lxml,
requests,
regural expression.
```
Versions of the above will change with new releases but you can look it up on pywikiscraper>pywikiscraper.egg-info>requires.txt

## Usage

### scraping

```
import pywikiscraper as py
variable = py.scrape(url,printing=True)
```
 This scrapes the wikipedia page and prints the index on the page.you can set the printing false to not output index

### finding the text base 

```
variable.find_by_name(heading) 
#or
variable.find_by_key(index_key)
```
 this outputs the text in that section. for example you may want the text in References
```
variable.find_by_name('References')
```
 Headings and keys can be seen in index, and can be assesed using


```
variable.index

```

 All the text with respective key in index can be accesed using

```
variable.text_dict
```
 Dictionary with index headings and keys can be assesed using 
```
variable.index_dict
```

#### see the example.ipynb for implementation

## future improvements 

currently working on making the tables in wikipedia pages available and not loosing information in lists
