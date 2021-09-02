import requests


def createCache(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": "getorcreate",
        'cacheName': '%s' % input_data
    }
    print(params)
    print(input_data)
    x = requests.get(url, params).json()
    x['error'] = '' if x['error'] is None else x['error']
    x['response'] = '' if x['response'] is None else x['response']
    print(x)
    return x


def deleteCache(input_data):
    url = 'http://localhost:8080/ignite?cmd=destcache&cacheName=%s' % input_data
    x = requests.delete(url).json()
    x['error'] = '' if x['error'] is None else x['error']
    x['response'] = '' if x['response'] is None else x['response']
    print(x)

    return x


