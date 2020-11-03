http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },

    'stop' : lambda x: len(x.xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/nav/div[1]/a[contains(@class,"next")]')) == 0
     #'stop' : lambda x: True,
}
elements = {
    'path': '//*[contains(@class, "message message")]',
    'attributes': {
        'postID': {
            'path': './span',
            'attrib': 'id',
            'regex' : r'\d+'},
        'mainText': {
            'path': './div/div[2]/div/div/div[1]/article/div[1]/text()',
            'attrib': 'text',
            'regex' : '[^\n\t]+',},
        'mainTextLinks': {
            'path': './div/div[2]/div/div/div/article/div[1]/a[contains(@class,"link link--external")]',
            'attrib': 'href',},
        'username': {
            'path': './div/div[1]/section/div[2]/h4/a/text()',
            'attrib': 'text',},
        'dateTime': {
            'path': './div/div[2]/div/header/div/a/time',
            'attrib': 'title',},
        'quoteLink': {
            'path': './div/div[2]/div/div/div[1]/article/div[1]/blockquote/div[1]/a',
            'attrib': 'href',
            'regex' : r'[\d]+$',},
    }
}
