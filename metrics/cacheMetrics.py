import requests


def cacheMetrics(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": "cache",
        'cacheName': '%s' % input_data
    }
    print(params)
    print(input_data)
    x = requests.get(url, params).json()
    print(x)

    return x


def cacheMetadata():
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": "metadata",
    }
    print(params)
    x = requests.get(url, params).json()
    print(x)
    # x['response'] = '' if x['response'] == None else x['response']
    y = {
        'status': x['successStatus'],
        'error': x['error'],
        'metaData': x['response']
    }

    return y


def showingTables(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": "qryfldexe",
        'pageSize': input_data.pageSize,
        'cacheName': input_data.cacheName,
        'qry': 'SELECT * FROM SYS.tables;'
    }
    print(params)
    x = requests.get(url, params).json()
    print(x)
    # x['response'] = '' if x['response'] == None else x['response']
    y = {
        'table_names': x['response']['items']
    }

    return y
