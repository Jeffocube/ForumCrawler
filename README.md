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

There are multiple arguments needed to specify for running a forum crawler. 

    $ python crawler.py <options> -f <path to job file> 

Here are available options. 
 - -debug; turn on debugging messages
 - --debug-level; detail of debugging messages [1 , 3]'
 - -c, --compress; archive the JSON result directory in compressed file
 - -f, --job; path to job file
    


[statically typed parts]: http://mypy.readthedocs.io/en/latest/basics.html#function-signatures
