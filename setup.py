from setuptools import setup

setup(
    name="python_markdown_nofollow",
    version='1.0',
    py_modules=['python_markdown_nofollow'],
    install_requires=['markdown>=3.0'],
    description='a Python Markdown plugin used to add rel="external nofollow" '
                'and target="_blank" attribute to all <a> tags',
    autor='lyp',
    autor_email='gsyipingliu@gmail.com',
    url='https://stdworkflow.com',
    download_url='https://github.com/stdworkflow/python_markdown_nofollow.git',
    keywords=['nofollow', 'SEO'],
)
