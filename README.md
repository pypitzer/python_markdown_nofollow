# python_markdown_nofollow

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

