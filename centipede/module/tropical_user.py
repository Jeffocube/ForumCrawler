http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },

    'stop' :  lambda x: (True if int(x.xpath('count(/html/body/div[5]/div/div/div/div[2]/div[3]/a)')) == 0 #End when there is only one page(the one strong is showing)
    else (True if 'All' in str(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/a[last()]/text()')[0]) #End if the page has an "All" button(happens only when there are 2 pages)
        and int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/strong/text()')[0]) == 2
    else (False if 'All' in str(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/a[last()]/text()')[0]) #Continuation of the last if
        and int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/strong/text()')[0]) == 1
    else int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/strong/text()')[0]) > int(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/a[last()]/text()')[0])))), #No "All button"
    #'stop' :  lambda x: True if 'All' in str(x.xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/a[last()]/text()')[0]) else False
}
elements={
    'path': '/html/body/div[5]/div/div/div/div[3]/form/div',
    'attributes': {
        'mainText': {
            'path': './div/div[2]/div[2]/div/text()',
            'attrib': 'text',},
        'mainTextLinks': {
            'path': './div/div[2]/div[2]/div/a',
            'attrib': 'href',},
        'username': {
            'path': './div/div[1]/h4/a/text()',
            'attrib': 'text',},

        'dateTime': {
            'path': './div/div[2]/div[1]/div/div[2]/text()[2]',
            'attrib': 'text',
            'regex' : '[^\n\t]+',},
        'postID': {
            'path': './div/div[2]/div[1]/div/h5',
            'attrib': 'id',
            'regex' : r'\d+',},
        'quoteLink': {
            'path': './div/div[2]/div[2]/div/div[1]/div/a',
            'attrib': 'href',
            'regex' : r'[\d]+$',},
        'parentLink': {
            'path': '/html/body/div[5]/div/div/div/div[1]/ul/li[4]/a',
            'attrib': 'href',},
    }
}
