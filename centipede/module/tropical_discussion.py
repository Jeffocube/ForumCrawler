http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },

    #'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]//a[last()][contains(@class,"text")]')) == 0,
    #'stop' :  lambda x: int(x.xpath('//*[@id="content"]/div/div/div[3]//a[contains(@class,"currentPage")]/text()')[0]) == 1,
     'stop' : lambda x: True,
}
elements = {
    'path':'/html/body/div[5]/div/div/div/div[2]/table/tbody[contains(@id, "boards")]/tr[contains(@id, "board")]',
    'attributes':{
        'subject':{
            'path': './td[2]/a/text()',
            'attrib': 'text'},
        'subtext':{
            'path': './td[2]/p/text()',
            'attrib': 'text'},
        'posts':{
            'path': './td[3]/p/text()',
            'attrib': 'text'},

    }
}
new_jobs = [{
    #'path' : '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]/div[2]/div/h3/a',
    'path' : '//*[contains(@id,"board")]/td[2]/a',
    'module': 'tropical_thread',
    'prefix': 'http://www.tropicalfruitforum.com/',
}]
