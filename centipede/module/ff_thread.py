

http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },

    'stop' : lambda x: len(x.xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[1]/div/nav/div[1]/a[contains(@class,"next")]')) == 0
     #'stop' : lambda x: True,
}
elements = {
    'path': '//*[@id="top"]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div/div',
    'attributes': {
        'title': {
            'path': './div[2]/div[1]/a/text()',
            'attrib': 'text',},
        'username': {
            'path': './div[2]/div[2]/ul/li[1]/a/text()',
            'attrib': 'text',},
        'date': {
            'path': './html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/ul/li[2]/a/time',
            'attrib': 'data-date-string',},
        'time': {
            'path': './html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/ul/li[2]/a/time',
            'attrib': 'data-time-string',},
        'threadURL': {
            'path': './html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/ul/li[2]/a',
            'attrib': 'href',},
        'threadID': {
            'attrib': 'class',
            'regex' : r'\d+'},
        'discussion': {
            'path': '/html/body/div[1]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[1]/div[1]/h1/text()',
            'attrib': 'text',},
    }
}
'''
new_jobs = [{
    #'path' : '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]/div[2]/div/h3/a',
    'path' : '//*[contains(@id, "thread")]/div/div[2]/div/h3/a[last()]',
    'module': 'ubcbot_user',
    'prefix': 'https://forums.botanicalgarden.ubc.ca/',
}]
'''
