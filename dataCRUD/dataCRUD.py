import time

import requests
# import time


def insertingData(input_data):
    url = 'http://localhost:8080/ignite?'
    # qry = 'insert into '+ input_data.tableName + ' values ( ' + str(input_data.column_1_id) + ')'
    # print(qry)

    params = {
        "cmd": 'qryfldexe',
        'pageSize': input_data.pageSize,
        'cacheName': input_data.cacheName,
        'qry': 'INSERT INTO %s VALUES(%d, \'%s\', \'%s\', \'%s\', %d);' % (input_data.tableName, input_data.column_1_id, input_data.column_2_date, input_data.column_3_string, input_data.column_4_string, input_data.column_5_int)
    }
    # print(params)
    x = requests.get(url, params).json()
    print(x)
    x_read = readingData(input_data)
    y = {
        # successStatus --- int value
        'status': x['successStatus'],
        # list of lists (here only only one list inside the data list)
        'data': x_read['data'],
        # list of dictionary
        'schema': x['response']['fieldsMetadata']
    }
    # print(y)
    return y


def updatingData(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": 'qryfldexe',
        'pageSize': "%d" % input_data.pageSize,
        'cacheName': '%s' % input_data.cacheName,
        'qry': 'UPDATE %s SET joining_date = \'%s\', full_name = \'%s\', designation = \'%s\', age = %d '
               'WHERE employee_ID = %d;'
               % (input_data.tableName, input_data.column_2_date, input_data.column_3_string,
                  input_data.column_4_string, input_data.column_5_int, input_data.column_1_id)
    }
    # print(params)
    x = requests.get(url, params).json()
    print(x)
    x_read = readingData(input_data)
    y = {
        # successStatus --- int value
        'status': x['successStatus'],
        # list of lists (here only only one list inside the data list)
        'data': x_read['data'],
        # list of dictionary
        'schema': x['response']['fieldsMetadata']
    }
    # print(y)
    return y


def readingData(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": 'qryfldexe',
        'pageSize': "%d" % input_data.pageSize,
        'cacheName': '%s' % input_data.cacheName,
        'qry': 'SELECT * FROM %s WHERE employee_ID = %d' % (input_data.tableName, input_data.column_1_id)
    }
    # print(params)
    x = requests.get(url, params).json()
    print(x)
    y = {
        # successStatus --- int value
        'status': x['successStatus'],
        # list of lists (here only only one list inside the data list)
        'data': x['response']['items'],
        # list of dictionary
        'schema': x['response']['fieldsMetadata']
    }
    # print(y)
    return y


def deletingData(input_data):
    url = 'http://localhost:8080/ignite?'
    params = {
        "cmd": 'qryfldexe',
        'pageSize': "%d" % input_data.pageSize,
        'cacheName': '%s' % input_data.cacheName,
        'qry': 'DELETE FROM %s WHERE employee_ID = %d' % (input_data.tableName, input_data.column_1_id)
    }
    # print(params)
    x_read = readingData(input_data)
    x = requests.get(url, params).json()
    print(x)
    y = {
        # successStatus --- int value
        'status': x['successStatus'],
        # list of lists (here only only one list inside the data list)
        'data': x_read['data'],
        # list of dictionary
        'schema': x['response']['fieldsMetadata']
    }
    # print(y)
    return y
