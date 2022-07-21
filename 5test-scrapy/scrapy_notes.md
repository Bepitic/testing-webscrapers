# Scrapy Notes
##### How scrapy works, high level.

Create a project:
`$scrapy startproject myProject`
structure:
```
path/to/project/
  scrapy.cfg           # deploy configuration file
  myProject/           # project's Python module, you'll import your code from here
      __init__.py
      items.py         # project items definition file
      middlewares.py   # project middlewares file
     pipelines.py      # project pipelines file
     settings.py       # project settings file
     spiders/          # a directory where you'll later put your spiders
        __init__.py
```

##### Main Questions:
- What is a xpath, and how to form it?
/route/to/the/node/miFavoriteDiv
//miFavoriteDiv
//miFavoriteDiv[@class='big_class']

`to get the text //div/text()`
- What is css and how to obtain properties?
route to the node miFavoriteDiv
miFavoriteDiv.big_class

`to get the text div::text`
`to get the href div::attr(href)`

- A cheatsheet: [xPath_CheatSheet](https://devhints.io/xpath)
- A xpath tutorial: [xPath_Tutorial](https://coderslegacy.com/python/scrapy-xpath-tutorial/)


