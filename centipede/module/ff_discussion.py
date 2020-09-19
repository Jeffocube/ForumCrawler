http_rules = {
    'method'  : 'GET',
    'page' : {
        'key'   : 'page',
        'value' : 1,
    },
 'stop' : lambda x: True,
}
elements = {
    'path': '//*[contains(@class, "depth2")]',
    'attributes': {
        'discussion': {
            'path': './div[1]/h3/a/text()',
            'attrib': 'text',},
        'numPosts': {
            'path': './div[1]/div/div/dl[2]/dd/text()',
            'attrib': 'text',},
        'numThreads': {
            'path': './div[1]/div/div/dl[1]/dd/text()',
            'attrib': 'text',},
    }
}
new_jobs = [{
    'path' : '//*[contains(@class, "depth2")]/div/div[1]/h3/a',
    'module': 'ff_thread',
    'prefix': 'https://thefarmingforum.co.uk/index.php',
}]
