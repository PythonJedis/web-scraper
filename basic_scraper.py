# Well, first we need to import a couple modules
# Something to get the HTML from the website, and something to parse it with

# Requests will open the website and grab the HTML for us
# This is like better urllib2
import requests
# Now we need an HTML parser. BeautifulSoup does a wonderful job of this 
from bs4 import BeautifulSoup
# Lastly we need the sys module to do a couple things (like exit cleanly)
import sys

# If you don't have these modules you can install them by running
# pip install requests
# and
# pip install beautifulsoup4
# If you are on windows, you will need to navigate to C:\Python34\Scripts
# in order to run pip (Or your python install directory /Scripts)

# You can learn more about these modules/libraries 
# by reading their documentation
# Requests: http://docs.python-requests.org/en/latest/
# BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Now we ask the user for a URL
url = input('URL: ')

# Now I need to actually 'open' the site and get the html
# this is what we have the requests module for

try:
	r = requests.get(url)
# Use an except block to handle exceptions.
# This just cleanly tells you what the exception is
# We should have a different case for each exception
# Read more at http://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions
except requests.exceptions.RequestException as e:
	print(e)
	sys.exit(1)

# We need the text(html) from the page as opposed to headers and such
page = r.text

# Then we encode it with our stdout encoding (Usually UTF-8), 
# and replace any errors with a question mark. 
html = page.encode(sys.stdout.encoding, errors='replace')

# Now we make a BeautifulSoup Object (Essentially just parse the HTML)
soup = BeautifulSoup(html)

# Get all links
links = soup.find_all('a')

# Print all the links (just the href)
# For this we use a for loop and iterate over the links list 
# and then get the href of each one
for i in links:
	# Every link has something like <a href="blah" class="blah" target="blank"> 
	# soup.find_all lets you access all the html attributes
	# We could have done i.get('target') or i.text or similar 
	link = i.get('href')
	print(link)