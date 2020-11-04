
http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },
    # 'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]//a[last()][contains(@class,"text")]')) == 0,
    'stop' :  lambda x: (True if int(x.xpath('count(/html/body/div[5]/div/div/div/div[2]/div/a)')) == 0
    else (True if int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div/strong/text()')[0]) == 2
        and 'All' in x.xpath('/html/body/div[5]/div/div/div/div[2]/div/a[last()]/text()')[0]
    else(False if 'All' in x.xpath('/html/body/div[5]/div/div/div/div[2]/div/a[last()]/text()')[0]
        and int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div/strong/text()')[0]) == 1
    else int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div/strong/text()')[0]) > int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div/a[last()]/text()')[0])))),
     #'stop' : lambda x: True,
}
elements = {
    'path': '//*[@id="messageindex"]/table/tbody/tr',
    'attributes': {
        'title': {
            'path': './td[3]/div/span/a/text()',
            'attrib': 'text',},
        'username': {
            'path': './td[3]/div/p/a/text()',
            'attrib': 'text',},
        'dateTime': {
            'path': './td[5]/text()[2]',
            'attrib': 'text',
            'regex' : '[^\n\t]+',},
        'url': {
            'path': './td[3]/div/span/a',
            'attrib': 'href',},
        'discussion': {
            'path': '/html/body/div[5]/div/div/div/div[1]/ul/li[3]/a[1]/span/text()',
            'attrib': 'text',},
    }
}
'''
new_jobs = [{
    #'path' : '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]/div[2]/div/h3/a',
    'path' : '//*[contains(@id,"msg")]/a',
    'module': 'tropical_user',
    'prefix': 'http://www.tropicalfruitforum.com/',
}]
'''
