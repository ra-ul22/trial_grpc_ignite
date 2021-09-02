import requests


def qryTables(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": "qryfldexe",
        'cacheName': input_data.cacheName,
        'pageSize': input_data.pageSize,
        'qry': input_data.qry
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
