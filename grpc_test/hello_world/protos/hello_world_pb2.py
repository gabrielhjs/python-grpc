# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_test/hello_world/protos/hello_world.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.grpc_test/hello_world/protos/hello_world.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08response\x18\x01 \x01(\t28\n\x07Greeter\x12-\n\x08SayHello\x12\r.HelloRequest\x1a\x0e.HelloResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_test.hello_world.protos.hello_world_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=50
  _globals['_HELLOREQUEST']._serialized_end=78
  _globals['_HELLORESPONSE']._serialized_start=80
  _globals['_HELLORESPONSE']._serialized_end=113
  _globals['_GREETER']._serialized_start=115
  _globals['_GREETER']._serialized_end=171
# @@protoc_insertion_point(module_scope)
