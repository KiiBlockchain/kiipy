# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/types/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/types/params.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"\xdb\x01\n\x0f\x43onsensusParams\x12,\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x1d.tendermint.types.BlockParams\x12\x32\n\x08\x65vidence\x18\x02 \x01(\x0b\x32 .tendermint.types.EvidenceParams\x12\x34\n\tvalidator\x18\x03 \x01(\x0b\x32!.tendermint.types.ValidatorParams\x12\x30\n\x07version\x18\x04 \x01(\x0b\x32\x1f.tendermint.types.VersionParams\"7\n\x0b\x42lockParams\x12\x11\n\tmax_bytes\x18\x01 \x01(\x03\x12\x0f\n\x07max_gas\x18\x02 \x01(\x03J\x04\x08\x03\x10\x04\"~\n\x0e\x45videnceParams\x12\x1a\n\x12max_age_num_blocks\x18\x01 \x01(\x03\x12=\n\x10max_age_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tmax_bytes\x18\x03 \x01(\x03\"2\n\x0fValidatorParams\x12\x15\n\rpub_key_types\x18\x01 \x03(\t:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\"&\n\rVersionParams\x12\x0b\n\x03\x61pp\x18\x01 \x01(\x04:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\">\n\x0cHashedParams\x12\x17\n\x0f\x62lock_max_bytes\x18\x01 \x01(\x03\x12\x15\n\rblock_max_gas\x18\x02 \x01(\x03\x42\x39Z3github.com/cometbft/cometbft/proto/tendermint/types\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/cometbft/cometbft/proto/tendermint/types\250\342\036\001'
  _EVIDENCEPARAMS.fields_by_name['max_age_duration']._options = None
  _EVIDENCEPARAMS.fields_by_name['max_age_duration']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _VALIDATORPARAMS._options = None
  _VALIDATORPARAMS._serialized_options = b'\270\240\037\001\350\240\037\001'
  _VERSIONPARAMS._options = None
  _VERSIONPARAMS._serialized_options = b'\270\240\037\001\350\240\037\001'
  _globals['_CONSENSUSPARAMS']._serialized_start=106
  _globals['_CONSENSUSPARAMS']._serialized_end=325
  _globals['_BLOCKPARAMS']._serialized_start=327
  _globals['_BLOCKPARAMS']._serialized_end=382
  _globals['_EVIDENCEPARAMS']._serialized_start=384
  _globals['_EVIDENCEPARAMS']._serialized_end=510
  _globals['_VALIDATORPARAMS']._serialized_start=512
  _globals['_VALIDATORPARAMS']._serialized_end=562
  _globals['_VERSIONPARAMS']._serialized_start=564
  _globals['_VERSIONPARAMS']._serialized_end=602
  _globals['_HASHEDPARAMS']._serialized_start=604
  _globals['_HASHEDPARAMS']._serialized_end=666
# @@protoc_insertion_point(module_scope)
