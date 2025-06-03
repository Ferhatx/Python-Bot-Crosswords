
# BOT CROSSWORDS

Extracting data from the web is becoming increasingly important every day. In this project, I used the Python BeautifulSoup library to parse the data under the "Across" and "Down" sections from the URL https://www.nytimes.com/crosswords/game/mini.

# Usage
- You can download and open the Python file with your preferred editor.

# Workflow
1. I examined the HTML page.  
2. I chose the `html.parser` parser to parse the HTML page (html5lib, lxml, html.parser).  
3. I created a BeautifulSoup object.  
4. I extracted the tags I needed.  
5. I saved the extracted tags into an array.  
6. Finally, I saved the extracted data as a JSON file.

# Libraries Used
```python
import requests  
from bs4 import BeautifulSoup  
import json  
```
