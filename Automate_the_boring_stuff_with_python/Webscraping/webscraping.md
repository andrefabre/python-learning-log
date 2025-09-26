
**webbrowser** comes with python and opens a browser to a specific page
**requests** downloads files and web pages from the internet
**bs4** Parses HTML, the format that web pages are written in
**selenium** Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser

- The webbrowser module's open() function can launch a new browser to a specified URL
```python
>>> import webbrowser
>>> webbrowser.open("https://inventwithpython.com/")
```

#### Downloading Files from the Web with the requests Module
- Downloading a Webpage with the requests.get() Function
  - The requests.get() function takes a string of a URL to download. By calling type() on requests.get()'s return value, you can see that it returns a *Response* object, which contains the response that the webserver gave for your request