# PageRequestChecker
A Python script to take a large list or urls and check their response codes to see what is and isn't working

[![gif](/PageRequestChecker.gif)](/PageRequestChecker.gif)

# Requirements

This script uses ```requests```, to install you can run;

## OSX/Linux

Python 2: ```sudo pip install requests```

Python 3: ```sudo pip3 install requests```

if you have pip installed (pip is the package installer for python and should come by default with your python installation). If pip is installed but not in your path you can use ```python -m pip install requests``` (or ```python3 -m pip install requests``` for python3)

Alternatively you can use your systems package manager:

For centos: ```sudo yum install python-requests```

For Debian/Ubuntu Python2: ```sudo apt-get --reinstall install python-requests```

For Debian/Ubuntu Python3: ```sudo apt-get --reinstall install python3-requests```

--reinstall may fix this error, if package was already installed.

## Windows

Use ```pip install requests``` (or ```pip3 install requests``` for python3) if you have pip installed and Pip.exe added to the Path Environment Variable. If pip is installed but not in your path you can use ```python -m pip install requests``` (or ```python3 -m pip install requests``` for python3)

# Usage

* Place any large list of URLs you want to check in a file called 'urls.txt'
* Place 'urls.txt' and 'main.py' in the same directory
* Open a terminal window and navigate to that directory
* type ```python3 .\main.py``` and run the query. It will cycle through the list of domains

This program will visualy display it's results as well as create two new files, 'valid_urls.txt' and 'invalid_urls.txt'.

An example output for 'invalid_urls.txt':

```
https://nonexistentdomain.xyz - Error: HTTPConnectionPool(host='nonexistentdomain.xyz', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8b4d5a99d0>: Failed to establish a new connection: [Errno -2] Name or service not known')

https://anotherbrokenexample.com - 404

https://timedouturl.com - Error: HTTPSConnectionPool(host='timedouturl.com', port=443): Read timed out. (read timeout=10)
```

I decided to make invalid_urls output with a line between each result as this makes it easier to visually separate each invalid URL and its corresponding error or status code.

Any bugs or issues please submit a pull request or shout me on [twitter](https://x.com/ha3ks)
