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
    'path':'//*[@id="boardindex_table"]/table/tbody[contains(@class, "content")]/tr[contains(@id,"board")]',
    'attributes':{
        'subject':{
            'path': './td[contains(@class, "info")]/a/text()',
            'attrib': 'text'},
        'subtext':{
            'path': './td[contains(@class, "info")]/p[1]/text()',
            'attrib': 'text'},
        'posts':{
            'path': './td[contains(@class, "info")]/td[3]/p/text()',
            'attrib': 'text'},

    }
}
