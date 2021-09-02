import requests


def creatingTable(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": 'qryfldexe',
        'pageSize': "%d" % input_data.pageSize,
        'cacheName': '%s' % input_data.cacheName,
        'qry': 'CREATE TABLE %s (%s int PRIMARY KEY, %s datetime, %s varchar(20), %s varchar(20), %s int);'
               % (input_data.tableName, input_data.column_1_primarykey_int, input_data.column_2_date,
                  input_data.column_3_string, input_data.column_4_string, input_data.column_5_int)
    }
    # print(params)
    x = requests.get(url, params).json()
    print(x)
    y = {
        # successStatus --- int value
        'status': int(x['successStatus']),
        # list of lists (here only only one list inside the data list)
        'data': None,
        # list of dictionary
        'schema': None,
        # error
        'error': x['error']
    }
    if x['response'] is not None:
        # list of lists (here only only one list inside the data list)
        y['data'] = x['response']['items']
        # list of dictionary
        y['schema'] = x['response']['fieldsMetadata']
    # print(y)
    return y


def deletingTable(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": 'qryfldexe',
        'cacheName': input_data.cacheName,
        'qry': 'DROP TABLE ' + input_data.tableName + ';',
        'pageSize': input_data.pageSize
    }
    print(params)
    x = requests.get(url, params).json()
    print(x)
    y = {
        # successStatus --- int value
        'status': x['successStatus'],
        # list of lists (here only only one list inside the data list)
        'data': None,
        # list of dictionary
        'schema': None,
        # error
        'error': x['error']
    }
    if x['response'] is not None:
        # list of lists (here only only one list inside the data list)
        y['data'] = x['response']['items']
        # list of dictionary
        y['schema'] = x['response']['fieldsMetadata']
    # print(y)
    return y
