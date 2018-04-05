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

# How ForumCrawler work?
When crawler starts, 
1. Run root URL in job file with specific module file
2. Save all elements of thread header in json format specified in module file 
3. Adding more jobs in the job running stacks if new_jobs is specified in module file.
4. check if stop condition is met in module file. typically, it will run till the last thread in that forum section.
5. After getting all possible threads,  it will start crawl all posts for each threads and save in JSON format.

For example,
crawler starts >> wildersecurity_thread.py(get all possible threads) >> wildersecurity_questions.py (crawl data for each threads.)

-------------
# Job file
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
-------------
# Module file
Module file are made in JSON format in order to tell crawler about rules and which content data should be creawled in each site. It consisted of 3 parts, http_rules, elements and new_jobs. Module file uses Xpath to get specific elements in from html format and use regular expression for extrating certain value. Here is an example of [wildersecurity_thread module](https://github.com/JakapunTachaiya/ForumCrawler/blob/master/centipede/models.py) file  

##### 1) http_rules - specify POST/GET html page & stop condition.
```
 'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },
    
    'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]//a[last()][contains(@class,"text")]')) == 0,
    # 'stop' :  lambda x: int(x.xpath('//*[@id="content"]/div/div/div[3]//a[contains(@class,"currentPage")]/text()')[0]) == 1,
    # 'stop' : lambda x: True,
```
'stop' value is used for stopping condition. If stop == true, it will stop at current page.
##### 2) elements - specify elements needed to save in JSON format with Xpath.
```
    'path': '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]',
    'attributes': {
        'title' : {
            'path'  : './div[2]/div/h3/a/text()', 
            'attrib': 'text'},
        'url' : {
            'path'  : './div[2]/div/h3/a', 
            'attrib': 'href'},
        'uid'    : {
            'path'  : './div[2]/div/div[contains(@class,"second")]/div[1]/a', 
            'attrib': 'href', 
            'regex' : r'\d+'},
        'user_fullname'  : {
            'path'  : './div[2]/div/div[contains(@class,"second")]/div[1]/a/text()', 
            'attrib': 'text',},
            .
            .
            .
        'last_posts_user'  : {
            'path'  : './div[4]/dl/dt/a/text()', 
            'attrib': 'text',},
        'last_posts_uid'  : {
            'path'  : './div[4]/dl/dt/a', 
            'attrib': 'href', 
            'regex' : r'\d+'},
```
'path' uses Xpath to get to specific element in html format. It consists of base path and extend path in 'attributes'. 
'attrib' uses to speficify type of input(plain text, href). Regular expression is used to help extracting part of string.
##### This 'attributes' in elements will later be save in JSON format as crawled data. 

##### 3) new_jobs - adding more jobs to running crawler stacks. Typically, it will point to another module file for each thread module file. 
```
    'path' : '//*[contains(@id,"thread")]/div[2]/div/h3/a',
    'module': 'wildersecurity_questions',
    'prefix': 'http://www.wilderssecurity.com/',
```

-------------
# How to create new module file with Xpath for specific site. 

There are at least 2 module files needed to be specified to crawl a simple site. ([thread module file](https://github.com/JakapunTachaiya/ForumCrawler/blob/master/centipede/module/wildersecurity_thread.py) and [post module file](https://github.com/JakapunTachaiya/ForumCrawler/blob/master/centipede/module/wildersecurity_questions.py))
This example is for crawling in https://www.wilderssecurity.com/forums/mobile-device-security.141/. (wilderssecurity in mobile-device-security.141 section)

<img src="https://github.com/JakapunTachaiya/ForumCrawler/blob/master/readme_image/1.jpg" width="500" height="600">
1) use browser (recommmended chrome) to get an Xpath of element. Right click on element and inspect. It will show html tag for that element on the right side.
<img src="https://github.com/JakapunTachaiya/ForumCrawler/blob/master/readme_image/2.jpg">
2) Then click on copy Xpath for specific element. You will get that element Xpath.
<img src="https://github.com/JakapunTachaiya/ForumCrawler/blob/master/readme_image/3.jpg">

Noted: Some results of copy Xpath is not shown to top level of DOM. You have to trace back to top level for prevent ambiguity when referring. For example on getting url,
```
From base Xpath  
//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]
[id==Content]
    -->div
        -->div
            -->div[0]
            .
            .
            .
            -->div[4]
                -->form
                    -->ol
                        -->li[contains(@id,"thread")]
            
From copy Xpath for url
//*[@id="thread-402211"]/div[2]/div/h3/a

[contains(@id,"thread")]
    -->div[0]
    -->div[1]
    -->div[2]
        -->div
            -->h3
                -->a


generalize to get all possible threads ( use '.' for relative from base path and use 'contain' to get lists which its id contain 'thread' )

'path': '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]'
'url' : {
            'path'  : './div[2]/div/h3/a', 
            'attrib': 'href'},
            
```
## Here is some tips and tricks for Xpath and other configurations

1) There are generally 3 types of data you can get from html tags. 
    - **plain text**, you can get by using text().
    ```
    'title' : {
            'path'  : './div[2]/div/h3/a/text()', 
            'attrib': 'text'}
    ```
    - **url**, you can get by using href.
    ```
    'url' : {
            'path'  : './div[2]/div/h3/a', 
            'attrib': 'href'}
    ```
    - **substring**, use regex to get part of string like numberm id. (r'\d+ = get only number)
    ```
    'uid'    : {
            'path'  : './div[2]/div/div[contains(@class,"second")]/div[1]/a', 
            'attrib': 'href', 
            'regex' : r'\d+'}    
    ```
2. use // (double slashes) to match any descendant node of the current node in the html tree which matches the locator.
    - you can use with [@id="container"] to excact match with id 
    - or, you can use with contains to match a substring(e.g.li[contains(@id,"post")])
    - result will return in list of possible match
3. new_jobs needs to be specified in order to crawl each posts inside threads. 
4. For stopping citeria/rules
    - when only you want to crawl only current page in job file.
    ```
    'stop' : lambda x: True
    ```
    - To crawl all possible threads in subsection (stop when no more thread to crawl). 
    <img src="https://github.com/JakapunTachaiya/ForumCrawler/blob/master/readme_image/5.jpg">
    
    This stop condition will check when there is no next link page on a last page
    ```
    'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]//a[last()][contains(@class,"text")]')) == 0 
    ```
    - To stop at certain page (stop by specific date). 
    This stop condition will check number of each page with current page.
    ```
    'stop' :  lambda x: int(x.xpath('//*[@id="content"]/div/div/div[3]//a[contains(@class,"currentPage")]/text()')[0]) == 1,
    ```
### Noted: Xpath and stopping condition might be different for each site. So, it needs modification accordingingly.    
    
    
    
    
    
    
    