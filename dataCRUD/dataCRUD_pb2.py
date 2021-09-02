# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataCRUD.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataCRUD.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64\x61taCRUD.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xc2\x01\n\x14insertUpdate_request\x12\x10\n\x08pageSize\x18\x01 \x01(\x05\x12\x11\n\tcacheName\x18\x02 \x01(\t\x12\x11\n\ttableName\x18\x03 \x01(\t\x12\x13\n\x0b\x63olumn_1_id\x18\x04 \x01(\x05\x12\x15\n\rcolumn_2_date\x18\x05 \x01(\t\x12\x17\n\x0f\x63olumn_3_string\x18\x06 \x01(\t\x12\x17\n\x0f\x63olumn_4_string\x18\x07 \x01(\t\x12\x14\n\x0c\x63olumn_5_int\x18\x08 \x01(\x05\"\x17\n\x15insertUpdate_response\"a\n\x12readDelete_request\x12\x10\n\x08pageSize\x18\x01 \x01(\x05\x12\x11\n\tcacheName\x18\x02 \x01(\t\x12\x11\n\ttableName\x18\x03 \x01(\t\x12\x13\n\x0b\x63olumn_1_id\x18\x04 \x01(\x05\"Q\n\x13readDelete_response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t\x12\x1c\n\x0bschema_data\x18\x03 \x03(\x0b\x32\x07.schema\":\n\x06schema\x12\x30\n\x0fmetadata_fields\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\x82\x02\n\x08\x64\x61taCRUD\x12>\n\rinsertingData\x12\x15.insertUpdate_request\x1a\x14.readDelete_response\"\x00\x12=\n\x0cupdatingData\x12\x15.insertUpdate_request\x1a\x14.readDelete_response\"\x00\x12:\n\x0breadingData\x12\x13.readDelete_request\x1a\x14.readDelete_response\"\x00\x12;\n\x0c\x64\x65letingData\x12\x13.readDelete_request\x1a\x14.readDelete_response\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INSERTUPDATE_REQUEST = _descriptor.Descriptor(
  name='insertUpdate_request',
  full_name='insertUpdate_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='insertUpdate_request.pageSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cacheName', full_name='insertUpdate_request.cacheName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tableName', full_name='insertUpdate_request.tableName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_1_id', full_name='insertUpdate_request.column_1_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_2_date', full_name='insertUpdate_request.column_2_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_3_string', full_name='insertUpdate_request.column_3_string', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_4_string', full_name='insertUpdate_request.column_4_string', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_5_int', full_name='insertUpdate_request.column_5_int', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=243,
)


_INSERTUPDATE_RESPONSE = _descriptor.Descriptor(
  name='insertUpdate_response',
  full_name='insertUpdate_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=268,
)


_READDELETE_REQUEST = _descriptor.Descriptor(
  name='readDelete_request',
  full_name='readDelete_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='readDelete_request.pageSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cacheName', full_name='readDelete_request.cacheName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tableName', full_name='readDelete_request.tableName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_1_id', full_name='readDelete_request.column_1_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=367,
)


_READDELETE_RESPONSE = _descriptor.Descriptor(
  name='readDelete_response',
  full_name='readDelete_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='readDelete_response.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='readDelete_response.data', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_data', full_name='readDelete_response.schema_data', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=450,
)


_SCHEMA = _descriptor.Descriptor(
  name='schema',
  full_name='schema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata_fields', full_name='schema.metadata_fields', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=510,
)

_READDELETE_RESPONSE.fields_by_name['schema_data'].message_type = _SCHEMA
_SCHEMA.fields_by_name['metadata_fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['insertUpdate_request'] = _INSERTUPDATE_REQUEST
DESCRIPTOR.message_types_by_name['insertUpdate_response'] = _INSERTUPDATE_RESPONSE
DESCRIPTOR.message_types_by_name['readDelete_request'] = _READDELETE_REQUEST
DESCRIPTOR.message_types_by_name['readDelete_response'] = _READDELETE_RESPONSE
DESCRIPTOR.message_types_by_name['schema'] = _SCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

insertUpdate_request = _reflection.GeneratedProtocolMessageType('insertUpdate_request', (_message.Message,), {
  'DESCRIPTOR' : _INSERTUPDATE_REQUEST,
  '__module__' : 'dataCRUD_pb2'
  # @@protoc_insertion_point(class_scope:insertUpdate_request)
  })
_sym_db.RegisterMessage(insertUpdate_request)

insertUpdate_response = _reflection.GeneratedProtocolMessageType('insertUpdate_response', (_message.Message,), {
  'DESCRIPTOR' : _INSERTUPDATE_RESPONSE,
  '__module__' : 'dataCRUD_pb2'
  # @@protoc_insertion_point(class_scope:insertUpdate_response)
  })
_sym_db.RegisterMessage(insertUpdate_response)

readDelete_request = _reflection.GeneratedProtocolMessageType('readDelete_request', (_message.Message,), {
  'DESCRIPTOR' : _READDELETE_REQUEST,
  '__module__' : 'dataCRUD_pb2'
  # @@protoc_insertion_point(class_scope:readDelete_request)
  })
_sym_db.RegisterMessage(readDelete_request)

readDelete_response = _reflection.GeneratedProtocolMessageType('readDelete_response', (_message.Message,), {
  'DESCRIPTOR' : _READDELETE_RESPONSE,
  '__module__' : 'dataCRUD_pb2'
  # @@protoc_insertion_point(class_scope:readDelete_response)
  })
_sym_db.RegisterMessage(readDelete_response)

schema = _reflection.GeneratedProtocolMessageType('schema', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMA,
  '__module__' : 'dataCRUD_pb2'
  # @@protoc_insertion_point(class_scope:schema)
  })
_sym_db.RegisterMessage(schema)



_DATACRUD = _descriptor.ServiceDescriptor(
  name='dataCRUD',
  full_name='dataCRUD',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=513,
  serialized_end=771,
  methods=[
  _descriptor.MethodDescriptor(
    name='insertingData',
    full_name='dataCRUD.insertingData',
    index=0,
    containing_service=None,
    input_type=_INSERTUPDATE_REQUEST,
    output_type=_READDELETE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updatingData',
    full_name='dataCRUD.updatingData',
    index=1,
    containing_service=None,
    input_type=_INSERTUPDATE_REQUEST,
    output_type=_READDELETE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='readingData',
    full_name='dataCRUD.readingData',
    index=2,
    containing_service=None,
    input_type=_READDELETE_REQUEST,
    output_type=_READDELETE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deletingData',
    full_name='dataCRUD.deletingData',
    index=3,
    containing_service=None,
    input_type=_READDELETE_REQUEST,
    output_type=_READDELETE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATACRUD)

DESCRIPTOR.services_by_name['dataCRUD'] = _DATACRUD

# @@protoc_insertion_point(module_scope)
