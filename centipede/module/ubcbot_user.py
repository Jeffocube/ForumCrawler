

http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },
    'stop' : lambda x: len(x.xpath('//*[@id="content"]/div/div/div[3]/div[2]/nav/a[last()][contains(@class,"text")]')) == 0
     #'stop' : lambda x: True,
}
elements = {
    'path': '//*[contains(@class, "message ")]',
    'attributes': {
        'postID': {
            'attrib': 'id',
            'regex' : r'\d+'},
        'mainText': {
            'path': './div[2]/div[1]/article/blockquote/text()',
            'attrib': 'text',
            'regex' : '[^\n\t]+',},
        'mainTextLinks': {
            'path': './div[2]/div[1]/article/blockquote/a',
            'attrib': 'href',},
        'username': {
            'path': './div[1]/div/h3/a/text()',
            'attrib': 'text',},
        'dateTime': {
            'path': './div[2]/div[contains(@class,"messageMeta")]/div[1]/span/a/span',
            'attrib': 'title',},
        'quoteLink': {
            'path': './div[1]/article/blockquote/a',
            'attrib': 'href',
            'regex' : r'[\d]+$',},
    }
}
