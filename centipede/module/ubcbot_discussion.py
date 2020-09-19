

http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },
 'stop' : lambda x: True,
}
elements = {
    'path': '/html/body/div[2]/div/div[3]/div/div/div[1]/div/ol/li[not(contains(@class, "314"))]/ol/li',
    'attributes': {
        'discussion': {
            'path': './div/div/div[1]/h3/a/text()',
            'attrib': 'text',},
        'numPosts': {
            'path': './div/div/div[1]/div/dl[2]/dd/text()',
            'attrib': 'text',},
        'numThreads': {
            'path': './div/div/div[1]/div/dl[1]/dd/text()',
            'attrib': 'text',},
    }
}

new_jobs = [{
    'path' : '/html/body/div[2]/div/div[3]/div/div/div[1]/div/ol/li[not(contains(@class, "314"))]/ol/li/div/div/div[1]/h3/a',
    'module': 'ubcbot_thread',
    'prefix': 'https://forums.botanicalgarden.ubc.ca/',
}]
