http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },

    # 'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]//a[last()][contains(@class,"text")]')) == 0,

    #'stop' : lambda x: len(x.xpath('//*[@id="main_content_section"]/div[2]/div/strong')) == 1,
     'stop' : lambda x: True,
}
elements={
    'path': '//*[@id="quickModForm"]/div[5]/div',
    'attributes': {
        'mainText': {
            'path': './div[2]/div[2]/div/text()',
            'attrib': 'text',},
        'username': {
            'path': './div[1]/h4/a/text()',
            'attrib': 'text',},
        'dateTime': {
            'path': './div[2]/div[1]/div/div[2]/text()[2]',
            'attrib': 'text',
            'regex' : '[^\n\t]+',},
        'postID': {
            'path': './div[2]/div[1]/div/h5',
            'attrib': 'id',
            'regex' : r'\d+',},
        'quoteLink': {
            'path': './div[2]/div[2]/div/div[1]/div/a',
            'attrib': 'href',
            'regex' : r'[\d]+$',},
    }
}
