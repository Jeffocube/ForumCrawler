

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
    'path': '//*[contains(@id, "thread")]',
    'attributes': {
        'title': {
            'path': './div/div[2]/div/h3/a/text()',
            'attrib': 'text',},
        'username': {
            'path': './div/div[4]/dl/dt/a/text()',
            'attrib': 'text',},
        'date': {
            'path': './div/div[4]/dl/dd/a/span/text()',
            'attrib': 'text',},
        'threadURL': {
            'path': './div/div[2]/div/h3/a',
            'attrib': 'href',},
        'threadID': {
            'attrib': 'id',
            'regex' : r'\d+'},
        'discussion': {
            'path': '/html/body/div[2]/div/div[3]/div/div/div[1]/nav/fieldset/span/span[3]/a/span/text()',
            'attrib': 'text',},
    }
}

new_jobs = [{
    #'path' : '//*[@id="content"]/div/div/div[4]/form/ol/li[contains(@id,"thread")]/div[2]/div/h3/a',
    'path' : '//*[contains(@id, "thread")]/div/div[2]/div/h3/a[last()]',
    'module': 'ubcbot_user',
    'prefix': 'https://forums.botanicalgarden.ubc.ca/',
}]
