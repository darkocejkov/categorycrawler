# categorycrawler
A web crawler application meant for scraping the web and categorizing webpages via content and keywords

Ran using a script that uses BeautifulSoup to parse google queries and obtain their constituent result links, later requesting each link and writes it to it's own HTML file.

Automatically creates a ./dataset/ folder to contain all HTML files, and will also create sub-directories to organize each page by topic (query).