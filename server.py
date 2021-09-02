import grpc
from concurrent import futures
import time
from cache import cache, cache_pb2, cache_pb2_grpc
from dataCRUD import dataCRUD, dataCRUD_pb2, dataCRUD_pb2_grpc
from metrics import cacheMetrics, cacheMetrics_pb2, cacheMetrics_pb2_grpc
from tableCRUD import tableCRUD, tableCRUD_pb2, tableCRUD_pb2_grpc
from CRUDquery import CRUDqry, CRUDqry_pb2, CRUDqry_pb2_grpc
print('All Modules Loaded')

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CacheServicer(cache_pb2_grpc.cacheServicer):

    def createCache(self, request, context):
        response = cache_pb2.createDelete_response()
        data = cache.createCache(request.cacheName)
        response.error = data['error']
        response.response = data['response']
        return response

    def deleteCache(self, request, context):
        response = cache_pb2.createDelete_response()
        data = cache.deleteCache(request.cacheName)
        response.error = data['error']
        response.response = data['response']
        return response


class MetricsServicer(cacheMetrics_pb2_grpc.metricsServicer):

    def cacheMetrics(self, request, context):
        response = cacheMetrics_pb2.metrics_response()
        data = cacheMetrics.cacheMetrics(request.cacheName)
        response.reads = data['response']['reads']
        response.writes = data['response']['writes']
        response.hits = data['response']['hits']
        response.misses = data['response']['misses']
        return response

    def getCache(self, request, context):
        response = cacheMetrics_pb2.metadata_response()
        data = cacheMetrics.cacheMetadata()
        response.status = data['status']
        response.error = str(data['error'])
        for items in data['metaData']:
            meta = cacheMetrics_pb2.metadata()
            meta.metadata_fields.update(items)
            response.metadata.append(meta)
        return response

    def showTables(self, request, context):
        response = cacheMetrics_pb2.show_response()
        data = cacheMetrics.showingTables(request)
        if data['table_names'] is not None:
            for items in data['table_names']:
                response.table_names.append(items[5])
        return response


class TableCRUDServicer(tableCRUD_pb2_grpc.tableCRUDServicer):

    def creatingTable(self, request, context):
        response = tableCRUD_pb2.createTable_response()
        data1 = tableCRUD.creatingTable(request)
        response.status = data1['status']
        response.error = str(data1['error'])
        if data1['data'] is not None:
            for items in data1['data']:
                response.data.append(str(items))
        if data1['schema'] is not None:
            for items in data1['schema']:
                schema_response = tableCRUD_pb2.table_schema()
                schema_response.metadata_fields.update(items)
                response.schema_data.append(schema_response)
        return response

    def deletingTable(self, request, context):
        response = tableCRUD_pb2.createTable_response()
        data1 = tableCRUD.deletingTable(request)
        response.status = data1['status']
        response.error = str(data1['error'])
        if data1['data'] is not None:
            for items in data1['data']:
                response.data.append(str(items))
        if data1['schema'] is not None:
            for items in data1['schema']:
                schema_response = tableCRUD_pb2.table_schema()
                schema_response.metadata_fields.update(items)
                response.schema_data.append(schema_response)
        return response


class DataCRUDServicer(dataCRUD_pb2_grpc.dataCRUDServicer):

    def insertingData(self, request, context):
        response = dataCRUD_pb2.readDelete_response()
        data1 = dataCRUD.insertingData(request)
        response.status = data1['status']
        for items in data1['data']:
            response.data.append(str(items))
        for items in data1['schema']:
            schema_response = dataCRUD_pb2.schema()
            schema_response.metadata_fields.update(items)
            response.schema_data.append(schema_response)
        return response

    def updatingData(self, request, context):
        response = dataCRUD_pb2.readDelete_response()
        data1 = dataCRUD.updatingData(request)
        response.status = data1['status']
        for items in data1['data']:
            response.data.append(str(items))
        for items in data1['schema']:
            schema_response = dataCRUD_pb2.schema()
            schema_response.metadata_fields.update(items)
            response.schema_data.append(schema_response)
        return response

    def readingData(self, request, context):
        response = dataCRUD_pb2.readDelete_response()
        data1 = dataCRUD.readingData(request)
        response.status = data1['status']
        for items in data1['data']:
            response.data.append(str(items))
        for items in data1['schema']:
            schema_response = dataCRUD_pb2.schema()
            schema_response.metadata_fields.update(items)
            # print(items)
            response.schema_data.append(schema_response)
        return response

    def deletingData(self, request, context):
        response = dataCRUD_pb2.readDelete_response()
        data1 = dataCRUD.deletingData(request)
        response.status = data1['status']
        for items in data1['data']:
            response.data.append(str(items))
        for items in data1['schema']:
            schema_response = dataCRUD_pb2.schema()
            schema_response.metadata_fields.update(items)
            response.schema_data.append(schema_response)
        return response


class CRUDqryServicer(CRUDqry_pb2_grpc.CRUDqryServicer):

    def crudQry(self, request, context):
        response = CRUDqry_pb2.CRUDqry_response()
        data1 = CRUDqry.qryTables(request)
        response.status = data1['status']
        response.error = str(data1['error'])
        if data1['metaData'] is not None:
            # for items in data1['metaData']:
            schema_response = CRUDqry_pb2.qry_metadata()
            schema_response.metadata_fields.update(data1['metaData'])
            response.metadata.append(schema_response)

        return response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_cacheServicer_to_server(CacheServicer(), server)
    cacheMetrics_pb2_grpc.add_metricsServicer_to_server(MetricsServicer(), server)
    tableCRUD_pb2_grpc.add_tableCRUDServicer_to_server(TableCRUDServicer(), server)
    dataCRUD_pb2_grpc.add_dataCRUDServicer_to_server(DataCRUDServicer(), server)
    CRUDqry_pb2_grpc.add_CRUDqryServicer_to_server(CRUDqryServicer(), server)
    print('Starting server. Listening on port 80.')
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
