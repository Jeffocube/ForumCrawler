# ForumCrawler(Centipede)

Forumcrawler is a web crawler based on Centipede library. It was made by UCR students to crawl any forums on specific contents in certain websites with job file. 

-------------
# Requirements

You need Python 2.7 to ForumCrawler. Also, here are additional required python libraries. 
 - Request (please use version under 2.10, recommend requests 2.9.1)
 - Awesome-slugify
 - Selenium
 - Centipede
 
You can install them via pip like this:
    
    $ pip install requests==2.9.1

Optional, you can install python packaged environment from Canopy. Most of required python libraries are included and ready to use. 
 https://store.enthought.com/downloads/ (please choose Canopy version 1.7.4 for requests version under 2.10)
 
-------------
# Quick start


After cloning repository, you can test running forum crawler with predefined job file for http://www.wilderssecurity.com:

    $ python crawler.py --debug --debug-level 2 -f wilder_job

There are multiple arguments needed to be specified for running a forum crawler. 

    $ python crawler.py <options> -f <path to job file> 

Here are available options. 
 - --debug; turn on debugging messages
 - --debug-level; detail of debugging messages [1,2,3] when --debug-level 3, it returns the most detailed information.
 - -c, --compress; archive the JSON result directory in compressed file
 - -f, --job; path to job file
    
-------------
# job file
Job file tells Forum crawler what job/site need to crawl for each run. You can put multiple job in a single job file. [wilder_job](https://github.com/JakapunTachaiya/ForumCrawler/blob/master/wilder_job) is template job file for http://www.wilderssecurity.com. A root URL and module file for each site should be speficied here. 
    
```
https://www.wilderssecurity.com/forums/mobile-device-security.141/ wildersecurity_thread
<root URLs_1> <root module_1>
<root URLs_2> <root module_2>
.
.
.
<root URLs_n> <root module_n>
```



