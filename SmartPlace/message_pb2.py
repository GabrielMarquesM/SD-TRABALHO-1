# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"9\n\x07Request\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0f\n\x07request\x18\x03 \x01(\t\"\"\n\x06\x44\x65vice\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"&\n\nDeviceList\x12\x18\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x07.Device\"\x1c\n\x08Response\x12\x10\n\x08response\x18\x01 \x01(\t')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=17
  _REQUEST._serialized_end=74
  _DEVICE._serialized_start=76
  _DEVICE._serialized_end=110
  _DEVICELIST._serialized_start=112
  _DEVICELIST._serialized_end=150
  _RESPONSE._serialized_start=152
  _RESPONSE._serialized_end=180
# @@protoc_insertion_point(module_scope)