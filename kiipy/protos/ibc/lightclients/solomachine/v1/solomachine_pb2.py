# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/solomachine/v1/solomachine.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1ibc/lightclients/solomachine/v1/solomachine.proto\x12\x1fibc.lightclients.solomachine.v1\x1a\'ibc/core/connection/v1/connection.proto\x1a!ibc/core/channel/v1/channel.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\x8d\x02\n\x0b\x43lientState\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x33\n\x0f\x66rozen_sequence\x18\x02 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:\"frozen_sequence\"\x12\x64\n\x0f\x63onsensus_state\x18\x03 \x01(\x0b\x32/.ibc.lightclients.solomachine.v1.ConsensusStateB\x1a\xf2\xde\x1f\x16yaml:\"consensus_state\"\x12K\n\x1b\x61llow_update_after_proposal\x18\x04 \x01(\x08\x42&\xf2\xde\x1f\"yaml:\"allow_update_after_proposal\":\x04\x88\xa0\x1f\x00\"\x7f\n\x0e\x43onsensusState\x12?\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x15\xf2\xde\x1f\x11yaml:\"public_key\"\x12\x13\n\x0b\x64iversifier\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04:\x04\x88\xa0\x1f\x00\"\xc4\x01\n\x06Header\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12G\n\x0enew_public_key\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyB\x19\xf2\xde\x1f\x15yaml:\"new_public_key\"\x12\x33\n\x0fnew_diversifier\x18\x05 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_diversifier\":\x04\x88\xa0\x1f\x00\"\x97\x02\n\x0cMisbehaviour\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x62\n\rsignature_one\x18\x03 \x01(\x0b\x32\x31.ibc.lightclients.solomachine.v1.SignatureAndDataB\x18\xf2\xde\x1f\x14yaml:\"signature_one\"\x12\x62\n\rsignature_two\x18\x04 \x01(\x0b\x32\x31.ibc.lightclients.solomachine.v1.SignatureAndDataB\x18\xf2\xde\x1f\x14yaml:\"signature_two\":\x04\x88\xa0\x1f\x00\"\xa0\x01\n\x10SignatureAndData\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12R\n\tdata_type\x18\x02 \x01(\x0e\x32).ibc.lightclients.solomachine.v1.DataTypeB\x14\xf2\xde\x1f\x10yaml:\"data_type\"\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04:\x04\x88\xa0\x1f\x00\"f\n\x18TimestampedSignatureData\x12\x31\n\x0esignature_data\x18\x01 \x01(\x0c\x42\x19\xf2\xde\x1f\x15yaml:\"signature_data\"\x12\x11\n\ttimestamp\x18\x02 \x01(\x04:\x04\x88\xa0\x1f\x00\"\xad\x01\n\tSignBytes\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x13\n\x0b\x64iversifier\x18\x03 \x01(\t\x12R\n\tdata_type\x18\x04 \x01(\x0e\x32).ibc.lightclients.solomachine.v1.DataTypeB\x14\xf2\xde\x1f\x10yaml:\"data_type\"\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c:\x04\x88\xa0\x1f\x00\"\x8a\x01\n\nHeaderData\x12\x41\n\x0bnew_pub_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x16\xf2\xde\x1f\x12yaml:\"new_pub_key\"\x12\x33\n\x0fnew_diversifier\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_diversifier\":\x04\x88\xa0\x1f\x00\"j\n\x0f\x43lientStateData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12\x43\n\x0c\x63lient_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:\"client_state\":\x04\x88\xa0\x1f\x00\"s\n\x12\x43onsensusStateData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12I\n\x0f\x63onsensus_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:\"consensus_state\":\x04\x88\xa0\x1f\x00\"d\n\x13\x43onnectionStateData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12\x39\n\nconnection\x18\x02 \x01(\x0b\x32%.ibc.core.connection.v1.ConnectionEnd:\x04\x88\xa0\x1f\x00\"U\n\x10\x43hannelStateData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12-\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x1c.ibc.core.channel.v1.Channel:\x04\x88\xa0\x1f\x00\"8\n\x14PacketCommitmentData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12\x12\n\ncommitment\x18\x02 \x01(\x0c\"B\n\x19PacketAcknowledgementData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61\x63knowledgement\x18\x02 \x01(\x0c\"(\n\x18PacketReceiptAbsenceData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\"U\n\x14NextSequenceRecvData\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12/\n\rnext_seq_recv\x18\x02 \x01(\x04\x42\x18\xf2\xde\x1f\x14yaml:\"next_seq_recv\"*\x8c\x04\n\x08\x44\x61taType\x12\x38\n#DATA_TYPE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUNSPECIFIED\x12&\n\x16\x44\x41TA_TYPE_CLIENT_STATE\x10\x01\x1a\n\x8a\x9d \x06\x43LIENT\x12,\n\x19\x44\x41TA_TYPE_CONSENSUS_STATE\x10\x02\x1a\r\x8a\x9d \tCONSENSUS\x12.\n\x1a\x44\x41TA_TYPE_CONNECTION_STATE\x10\x03\x1a\x0e\x8a\x9d \nCONNECTION\x12(\n\x17\x44\x41TA_TYPE_CHANNEL_STATE\x10\x04\x1a\x0b\x8a\x9d \x07\x43HANNEL\x12\x35\n\x1b\x44\x41TA_TYPE_PACKET_COMMITMENT\x10\x05\x1a\x14\x8a\x9d \x10PACKETCOMMITMENT\x12?\n DATA_TYPE_PACKET_ACKNOWLEDGEMENT\x10\x06\x1a\x19\x8a\x9d \x15PACKETACKNOWLEDGEMENT\x12>\n DATA_TYPE_PACKET_RECEIPT_ABSENCE\x10\x07\x1a\x18\x8a\x9d \x14PACKETRECEIPTABSENCE\x12\x36\n\x1c\x44\x41TA_TYPE_NEXT_SEQUENCE_RECV\x10\x08\x1a\x14\x8a\x9d \x10NEXTSEQUENCERECV\x12 \n\x10\x44\x41TA_TYPE_HEADER\x10\t\x1a\n\x8a\x9d \x06HEADER\x1a\x04\x88\xa3\x1e\x00\x42@Z>github.com/cosmos/ibc-go/v2/modules/core/02-client/legacy/v100b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.solomachine.v1.solomachine_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/cosmos/ibc-go/v2/modules/core/02-client/legacy/v100'
  _DATATYPE._options = None
  _DATATYPE._serialized_options = b'\210\243\036\000'
  _DATATYPE.values_by_name["DATA_TYPE_UNINITIALIZED_UNSPECIFIED"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_UNINITIALIZED_UNSPECIFIED"]._serialized_options = b'\212\235 \013UNSPECIFIED'
  _DATATYPE.values_by_name["DATA_TYPE_CLIENT_STATE"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_CLIENT_STATE"]._serialized_options = b'\212\235 \006CLIENT'
  _DATATYPE.values_by_name["DATA_TYPE_CONSENSUS_STATE"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_CONSENSUS_STATE"]._serialized_options = b'\212\235 \tCONSENSUS'
  _DATATYPE.values_by_name["DATA_TYPE_CONNECTION_STATE"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_CONNECTION_STATE"]._serialized_options = b'\212\235 \nCONNECTION'
  _DATATYPE.values_by_name["DATA_TYPE_CHANNEL_STATE"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_CHANNEL_STATE"]._serialized_options = b'\212\235 \007CHANNEL'
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_COMMITMENT"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_COMMITMENT"]._serialized_options = b'\212\235 \020PACKETCOMMITMENT'
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_ACKNOWLEDGEMENT"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_ACKNOWLEDGEMENT"]._serialized_options = b'\212\235 \025PACKETACKNOWLEDGEMENT'
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_RECEIPT_ABSENCE"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_PACKET_RECEIPT_ABSENCE"]._serialized_options = b'\212\235 \024PACKETRECEIPTABSENCE'
  _DATATYPE.values_by_name["DATA_TYPE_NEXT_SEQUENCE_RECV"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_NEXT_SEQUENCE_RECV"]._serialized_options = b'\212\235 \020NEXTSEQUENCERECV'
  _DATATYPE.values_by_name["DATA_TYPE_HEADER"]._options = None
  _DATATYPE.values_by_name["DATA_TYPE_HEADER"]._serialized_options = b'\212\235 \006HEADER'
  _CLIENTSTATE.fields_by_name['frozen_sequence']._options = None
  _CLIENTSTATE.fields_by_name['frozen_sequence']._serialized_options = b'\362\336\037\026yaml:\"frozen_sequence\"'
  _CLIENTSTATE.fields_by_name['consensus_state']._options = None
  _CLIENTSTATE.fields_by_name['consensus_state']._serialized_options = b'\362\336\037\026yaml:\"consensus_state\"'
  _CLIENTSTATE.fields_by_name['allow_update_after_proposal']._options = None
  _CLIENTSTATE.fields_by_name['allow_update_after_proposal']._serialized_options = b'\362\336\037\"yaml:\"allow_update_after_proposal\"'
  _CLIENTSTATE._options = None
  _CLIENTSTATE._serialized_options = b'\210\240\037\000'
  _CONSENSUSSTATE.fields_by_name['public_key']._options = None
  _CONSENSUSSTATE.fields_by_name['public_key']._serialized_options = b'\362\336\037\021yaml:\"public_key\"'
  _CONSENSUSSTATE._options = None
  _CONSENSUSSTATE._serialized_options = b'\210\240\037\000'
  _HEADER.fields_by_name['new_public_key']._options = None
  _HEADER.fields_by_name['new_public_key']._serialized_options = b'\362\336\037\025yaml:\"new_public_key\"'
  _HEADER.fields_by_name['new_diversifier']._options = None
  _HEADER.fields_by_name['new_diversifier']._serialized_options = b'\362\336\037\026yaml:\"new_diversifier\"'
  _HEADER._options = None
  _HEADER._serialized_options = b'\210\240\037\000'
  _MISBEHAVIOUR.fields_by_name['client_id']._options = None
  _MISBEHAVIOUR.fields_by_name['client_id']._serialized_options = b'\362\336\037\020yaml:\"client_id\"'
  _MISBEHAVIOUR.fields_by_name['signature_one']._options = None
  _MISBEHAVIOUR.fields_by_name['signature_one']._serialized_options = b'\362\336\037\024yaml:\"signature_one\"'
  _MISBEHAVIOUR.fields_by_name['signature_two']._options = None
  _MISBEHAVIOUR.fields_by_name['signature_two']._serialized_options = b'\362\336\037\024yaml:\"signature_two\"'
  _MISBEHAVIOUR._options = None
  _MISBEHAVIOUR._serialized_options = b'\210\240\037\000'
  _SIGNATUREANDDATA.fields_by_name['data_type']._options = None
  _SIGNATUREANDDATA.fields_by_name['data_type']._serialized_options = b'\362\336\037\020yaml:\"data_type\"'
  _SIGNATUREANDDATA._options = None
  _SIGNATUREANDDATA._serialized_options = b'\210\240\037\000'
  _TIMESTAMPEDSIGNATUREDATA.fields_by_name['signature_data']._options = None
  _TIMESTAMPEDSIGNATUREDATA.fields_by_name['signature_data']._serialized_options = b'\362\336\037\025yaml:\"signature_data\"'
  _TIMESTAMPEDSIGNATUREDATA._options = None
  _TIMESTAMPEDSIGNATUREDATA._serialized_options = b'\210\240\037\000'
  _SIGNBYTES.fields_by_name['data_type']._options = None
  _SIGNBYTES.fields_by_name['data_type']._serialized_options = b'\362\336\037\020yaml:\"data_type\"'
  _SIGNBYTES._options = None
  _SIGNBYTES._serialized_options = b'\210\240\037\000'
  _HEADERDATA.fields_by_name['new_pub_key']._options = None
  _HEADERDATA.fields_by_name['new_pub_key']._serialized_options = b'\362\336\037\022yaml:\"new_pub_key\"'
  _HEADERDATA.fields_by_name['new_diversifier']._options = None
  _HEADERDATA.fields_by_name['new_diversifier']._serialized_options = b'\362\336\037\026yaml:\"new_diversifier\"'
  _HEADERDATA._options = None
  _HEADERDATA._serialized_options = b'\210\240\037\000'
  _CLIENTSTATEDATA.fields_by_name['client_state']._options = None
  _CLIENTSTATEDATA.fields_by_name['client_state']._serialized_options = b'\362\336\037\023yaml:\"client_state\"'
  _CLIENTSTATEDATA._options = None
  _CLIENTSTATEDATA._serialized_options = b'\210\240\037\000'
  _CONSENSUSSTATEDATA.fields_by_name['consensus_state']._options = None
  _CONSENSUSSTATEDATA.fields_by_name['consensus_state']._serialized_options = b'\362\336\037\026yaml:\"consensus_state\"'
  _CONSENSUSSTATEDATA._options = None
  _CONSENSUSSTATEDATA._serialized_options = b'\210\240\037\000'
  _CONNECTIONSTATEDATA._options = None
  _CONNECTIONSTATEDATA._serialized_options = b'\210\240\037\000'
  _CHANNELSTATEDATA._options = None
  _CHANNELSTATEDATA._serialized_options = b'\210\240\037\000'
  _NEXTSEQUENCERECVDATA.fields_by_name['next_seq_recv']._options = None
  _NEXTSEQUENCERECVDATA.fields_by_name['next_seq_recv']._serialized_options = b'\362\336\037\024yaml:\"next_seq_recv\"'
  _globals['_DATATYPE']._serialized_start=2347
  _globals['_DATATYPE']._serialized_end=2871
  _globals['_CLIENTSTATE']._serialized_start=212
  _globals['_CLIENTSTATE']._serialized_end=481
  _globals['_CONSENSUSSTATE']._serialized_start=483
  _globals['_CONSENSUSSTATE']._serialized_end=610
  _globals['_HEADER']._serialized_start=613
  _globals['_HEADER']._serialized_end=809
  _globals['_MISBEHAVIOUR']._serialized_start=812
  _globals['_MISBEHAVIOUR']._serialized_end=1091
  _globals['_SIGNATUREANDDATA']._serialized_start=1094
  _globals['_SIGNATUREANDDATA']._serialized_end=1254
  _globals['_TIMESTAMPEDSIGNATUREDATA']._serialized_start=1256
  _globals['_TIMESTAMPEDSIGNATUREDATA']._serialized_end=1358
  _globals['_SIGNBYTES']._serialized_start=1361
  _globals['_SIGNBYTES']._serialized_end=1534
  _globals['_HEADERDATA']._serialized_start=1537
  _globals['_HEADERDATA']._serialized_end=1675
  _globals['_CLIENTSTATEDATA']._serialized_start=1677
  _globals['_CLIENTSTATEDATA']._serialized_end=1783
  _globals['_CONSENSUSSTATEDATA']._serialized_start=1785
  _globals['_CONSENSUSSTATEDATA']._serialized_end=1900
  _globals['_CONNECTIONSTATEDATA']._serialized_start=1902
  _globals['_CONNECTIONSTATEDATA']._serialized_end=2002
  _globals['_CHANNELSTATEDATA']._serialized_start=2004
  _globals['_CHANNELSTATEDATA']._serialized_end=2089
  _globals['_PACKETCOMMITMENTDATA']._serialized_start=2091
  _globals['_PACKETCOMMITMENTDATA']._serialized_end=2147
  _globals['_PACKETACKNOWLEDGEMENTDATA']._serialized_start=2149
  _globals['_PACKETACKNOWLEDGEMENTDATA']._serialized_end=2215
  _globals['_PACKETRECEIPTABSENCEDATA']._serialized_start=2217
  _globals['_PACKETRECEIPTABSENCEDATA']._serialized_end=2257
  _globals['_NEXTSEQUENCERECVDATA']._serialized_start=2259
  _globals['_NEXTSEQUENCERECVDATA']._serialized_end=2344
# @@protoc_insertion_point(module_scope)
