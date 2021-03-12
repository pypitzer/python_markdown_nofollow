# python_markdown_nofollow

## about
a Python Markdown plugin used to add rel="external nofollow" and target="_blank" attribute to all <a> tags, can be uesed in django etc.

## Install

simply use this command to install 

```
pip install python-markdown-nofollow
```

if you use a different mirror of Pypi, you may got an error, you can specify the Pypi source to install:

```
pip install -i https://pypi.org/simple/ python-markdown-nofollow
```

## Requirements

**python markdown 3.x.x**

## Usage

this plugin is registered to `python-markdown` (version 3), so after installation, you just need to specify the name of this plugin:

```python
import markdown

def std_markdown(value):
    return markdown.markdown(value, extensions=[
        'python_markdown_nofollow',
     	....
    ])
```


package location: https://pypi.org/project/python-markdown-nofollow/0.0.1/

a more fundmental tutorial can be found here:[Adding rel="nofollow" and target="_blank" attributes to links in django project](https://stdworkflow.com/11/adding-rel-nofollow-and-target-blank-attributes-to-links-in-django-project/)


