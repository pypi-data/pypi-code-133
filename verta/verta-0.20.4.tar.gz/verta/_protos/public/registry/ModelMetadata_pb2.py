# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registry/ModelMetadata.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='registry/ModelMetadata.proto',
  package='ai.verta.registry',
  syntax='proto3',
  serialized_options=b'P\001Z?github.com/VertaAI/modeldb/protos/gen/go/protos/public/registry',
  serialized_pb=b'\n\x1cregistry/ModelMetadata.proto\x12\x11\x61i.verta.registry\x1a\x1cgoogle/api/annotations.proto\"=\n\x11ModelLanguageEnum\"(\n\rModelLanguage\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06Python\x10\x01\"\\\n\rModelTypeEnum\"K\n\tModelType\x12\n\n\x06\x43ustom\x10\x00\x12\x16\n\x12StandardVertaModel\x10\x01\x12\x1a\n\x16UserContainerizedModel\x10\x02\x42\x43P\x01Z?github.com/VertaAI/modeldb/protos/gen/go/protos/public/registryb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MODELLANGUAGEENUM_MODELLANGUAGE = _descriptor.EnumDescriptor(
  name='ModelLanguage',
  full_name='ai.verta.registry.ModelLanguageEnum.ModelLanguage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Python', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=102,
  serialized_end=142,
)
_sym_db.RegisterEnumDescriptor(_MODELLANGUAGEENUM_MODELLANGUAGE)

_MODELTYPEENUM_MODELTYPE = _descriptor.EnumDescriptor(
  name='ModelType',
  full_name='ai.verta.registry.ModelTypeEnum.ModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Custom', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StandardVertaModel', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserContainerizedModel', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_MODELTYPEENUM_MODELTYPE)


_MODELLANGUAGEENUM = _descriptor.Descriptor(
  name='ModelLanguageEnum',
  full_name='ai.verta.registry.ModelLanguageEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODELLANGUAGEENUM_MODELLANGUAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=142,
)


_MODELTYPEENUM = _descriptor.Descriptor(
  name='ModelTypeEnum',
  full_name='ai.verta.registry.ModelTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODELTYPEENUM_MODELTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=236,
)

_MODELLANGUAGEENUM_MODELLANGUAGE.containing_type = _MODELLANGUAGEENUM
_MODELTYPEENUM_MODELTYPE.containing_type = _MODELTYPEENUM
DESCRIPTOR.message_types_by_name['ModelLanguageEnum'] = _MODELLANGUAGEENUM
DESCRIPTOR.message_types_by_name['ModelTypeEnum'] = _MODELTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelLanguageEnum = _reflection.GeneratedProtocolMessageType('ModelLanguageEnum', (_message.Message,), {
  'DESCRIPTOR' : _MODELLANGUAGEENUM,
  '__module__' : 'registry.ModelMetadata_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.registry.ModelLanguageEnum)
  })
_sym_db.RegisterMessage(ModelLanguageEnum)

ModelTypeEnum = _reflection.GeneratedProtocolMessageType('ModelTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _MODELTYPEENUM,
  '__module__' : 'registry.ModelMetadata_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.registry.ModelTypeEnum)
  })
_sym_db.RegisterMessage(ModelTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
