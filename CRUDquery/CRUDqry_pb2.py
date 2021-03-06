# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CRUDqry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CRUDqry.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rCRUDqry.proto\x1a\x1cgoogle/protobuf/struct.proto\"C\n\x0f\x43RUDqry_request\x12\x10\n\x08pageSize\x18\x01 \x01(\x05\x12\x11\n\tcacheName\x18\x02 \x01(\t\x12\x0b\n\x03qry\x18\x03 \x01(\t\"R\n\x10\x43RUDqry_response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x1f\n\x08metadata\x18\x03 \x03(\x0b\x32\r.qry_metadata\"@\n\x0cqry_metadata\x12\x30\n\x0fmetadata_fields\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2;\n\x07\x43RUDqry\x12\x30\n\x07\x63rudQry\x12\x10.CRUDqry_request\x1a\x11.CRUDqry_response\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CRUDQRY_REQUEST = _descriptor.Descriptor(
  name='CRUDqry_request',
  full_name='CRUDqry_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='CRUDqry_request.pageSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cacheName', full_name='CRUDqry_request.cacheName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qry', full_name='CRUDqry_request.qry', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=47,
  serialized_end=114,
)


_CRUDQRY_RESPONSE = _descriptor.Descriptor(
  name='CRUDqry_response',
  full_name='CRUDqry_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='CRUDqry_response.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='CRUDqry_response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='CRUDqry_response.metadata', index=2,
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
  serialized_start=116,
  serialized_end=198,
)


_QRY_METADATA = _descriptor.Descriptor(
  name='qry_metadata',
  full_name='qry_metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata_fields', full_name='qry_metadata.metadata_fields', index=0,
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
  serialized_start=200,
  serialized_end=264,
)

_CRUDQRY_RESPONSE.fields_by_name['metadata'].message_type = _QRY_METADATA
_QRY_METADATA.fields_by_name['metadata_fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['CRUDqry_request'] = _CRUDQRY_REQUEST
DESCRIPTOR.message_types_by_name['CRUDqry_response'] = _CRUDQRY_RESPONSE
DESCRIPTOR.message_types_by_name['qry_metadata'] = _QRY_METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CRUDqry_request = _reflection.GeneratedProtocolMessageType('CRUDqry_request', (_message.Message,), {
  'DESCRIPTOR' : _CRUDQRY_REQUEST,
  '__module__' : 'CRUDqry_pb2'
  # @@protoc_insertion_point(class_scope:CRUDqry_request)
  })
_sym_db.RegisterMessage(CRUDqry_request)

CRUDqry_response = _reflection.GeneratedProtocolMessageType('CRUDqry_response', (_message.Message,), {
  'DESCRIPTOR' : _CRUDQRY_RESPONSE,
  '__module__' : 'CRUDqry_pb2'
  # @@protoc_insertion_point(class_scope:CRUDqry_response)
  })
_sym_db.RegisterMessage(CRUDqry_response)

qry_metadata = _reflection.GeneratedProtocolMessageType('qry_metadata', (_message.Message,), {
  'DESCRIPTOR' : _QRY_METADATA,
  '__module__' : 'CRUDqry_pb2'
  # @@protoc_insertion_point(class_scope:qry_metadata)
  })
_sym_db.RegisterMessage(qry_metadata)



_CRUDQRY = _descriptor.ServiceDescriptor(
  name='CRUDqry',
  full_name='CRUDqry',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=266,
  serialized_end=325,
  methods=[
  _descriptor.MethodDescriptor(
    name='crudQry',
    full_name='CRUDqry.crudQry',
    index=0,
    containing_service=None,
    input_type=_CRUDQRY_REQUEST,
    output_type=_CRUDQRY_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRUDQRY)

DESCRIPTOR.services_by_name['CRUDqry'] = _CRUDQRY

# @@protoc_insertion_point(module_scope)
