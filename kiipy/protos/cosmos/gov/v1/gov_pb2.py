# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1/gov.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63osmos/gov/v1/gov.proto\x12\rcosmos.gov.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"_\n\x12WeightedVoteOption\x12)\n\x06option\x18\x01 \x01(\x0e\x32\x19.cosmos.gov.v1.VoteOption\x12\x1e\n\x06weight\x18\x02 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\"\x81\x01\n\x07\x44\x65posit\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x34\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xab\x04\n\x08Proposal\x12\n\n\x02id\x18\x01 \x01(\x04\x12&\n\x08messages\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x12-\n\x06status\x18\x03 \x01(\x0e\x32\x1d.cosmos.gov.v1.ProposalStatus\x12\x36\n\x12\x66inal_tally_result\x18\x04 \x01(\x0b\x32\x1a.cosmos.gov.v1.TallyResult\x12\x35\n\x0bsubmit_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12:\n\x10\x64\x65posit_end_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12;\n\rtotal_deposit\x18\x07 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\x11voting_start_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x39\n\x0fvoting_end_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x10\n\x08metadata\x18\n \x01(\t\x12\r\n\x05title\x18\x0b \x01(\t\x12\x0f\n\x07summary\x18\x0c \x01(\t\x12*\n\x08proposer\x18\r \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\xa5\x01\n\x0bTallyResult\x12!\n\tyes_count\x18\x01 \x01(\tB\x0e\xd2\xb4-\ncosmos.Int\x12%\n\rabstain_count\x18\x02 \x01(\tB\x0e\xd2\xb4-\ncosmos.Int\x12 \n\x08no_count\x18\x03 \x01(\tB\x0e\xd2\xb4-\ncosmos.Int\x12*\n\x12no_with_veto_count\x18\x04 \x01(\tB\x0e\xd2\xb4-\ncosmos.Int\"\x90\x01\n\x04Vote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x07options\x18\x04 \x03(\x0b\x32!.cosmos.gov.v1.WeightedVoteOption\x12\x10\n\x08metadata\x18\x05 \x01(\tJ\x04\x08\x03\x10\x04\"\xbb\x01\n\rDepositParams\x12M\n\x0bmin_deposit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x15min_deposit,omitempty\x12[\n\x12max_deposit_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB$\xea\xde\x1f\x1cmax_deposit_period,omitempty\x98\xdf\x1f\x01\"F\n\x0cVotingParams\x12\x36\n\rvoting_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\x98\xdf\x1f\x01\"x\n\x0bTallyParams\x12\x1e\n\x06quorum\x18\x01 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12!\n\tthreshold\x18\x02 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12&\n\x0eveto_threshold\x18\x03 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\"\xaf\x03\n\x06Params\x12\x39\n\x0bmin_deposit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\x12max_deposit_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\x98\xdf\x1f\x01\x12\x36\n\rvoting_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\x98\xdf\x1f\x01\x12\x1e\n\x06quorum\x18\x04 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12!\n\tthreshold\x18\x05 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12&\n\x0eveto_threshold\x18\x06 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12\x31\n\x19min_initial_deposit_ratio\x18\x07 \x01(\tB\x0e\xd2\xb4-\ncosmos.Dec\x12\x18\n\x10\x62urn_vote_quorum\x18\r \x01(\x08\x12%\n\x1d\x62urn_proposal_deposit_prevote\x18\x0e \x01(\x08\x12\x16\n\x0e\x62urn_vote_veto\x18\x0f \x01(\x08*\x89\x01\n\nVoteOption\x12\x1b\n\x17VOTE_OPTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fVOTE_OPTION_YES\x10\x01\x12\x17\n\x13VOTE_OPTION_ABSTAIN\x10\x02\x12\x12\n\x0eVOTE_OPTION_NO\x10\x03\x12\x1c\n\x18VOTE_OPTION_NO_WITH_VETO\x10\x04*\xce\x01\n\x0eProposalStatus\x12\x1f\n\x1bPROPOSAL_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1ePROPOSAL_STATUS_DEPOSIT_PERIOD\x10\x01\x12!\n\x1dPROPOSAL_STATUS_VOTING_PERIOD\x10\x02\x12\x1a\n\x16PROPOSAL_STATUS_PASSED\x10\x03\x12\x1c\n\x18PROPOSAL_STATUS_REJECTED\x10\x04\x12\x1a\n\x16PROPOSAL_STATUS_FAILED\x10\x05\x42-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
  _WEIGHTEDVOTEOPTION.fields_by_name['weight']._options = None
  _WEIGHTEDVOTEOPTION.fields_by_name['weight']._serialized_options = b'\322\264-\ncosmos.Dec'
  _DEPOSIT.fields_by_name['depositor']._options = None
  _DEPOSIT.fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DEPOSIT.fields_by_name['amount']._options = None
  _DEPOSIT.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _PROPOSAL.fields_by_name['submit_time']._options = None
  _PROPOSAL.fields_by_name['submit_time']._serialized_options = b'\220\337\037\001'
  _PROPOSAL.fields_by_name['deposit_end_time']._options = None
  _PROPOSAL.fields_by_name['deposit_end_time']._serialized_options = b'\220\337\037\001'
  _PROPOSAL.fields_by_name['total_deposit']._options = None
  _PROPOSAL.fields_by_name['total_deposit']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _PROPOSAL.fields_by_name['voting_start_time']._options = None
  _PROPOSAL.fields_by_name['voting_start_time']._serialized_options = b'\220\337\037\001'
  _PROPOSAL.fields_by_name['voting_end_time']._options = None
  _PROPOSAL.fields_by_name['voting_end_time']._serialized_options = b'\220\337\037\001'
  _PROPOSAL.fields_by_name['proposer']._options = None
  _PROPOSAL.fields_by_name['proposer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _TALLYRESULT.fields_by_name['yes_count']._options = None
  _TALLYRESULT.fields_by_name['yes_count']._serialized_options = b'\322\264-\ncosmos.Int'
  _TALLYRESULT.fields_by_name['abstain_count']._options = None
  _TALLYRESULT.fields_by_name['abstain_count']._serialized_options = b'\322\264-\ncosmos.Int'
  _TALLYRESULT.fields_by_name['no_count']._options = None
  _TALLYRESULT.fields_by_name['no_count']._serialized_options = b'\322\264-\ncosmos.Int'
  _TALLYRESULT.fields_by_name['no_with_veto_count']._options = None
  _TALLYRESULT.fields_by_name['no_with_veto_count']._serialized_options = b'\322\264-\ncosmos.Int'
  _VOTE.fields_by_name['voter']._options = None
  _VOTE.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DEPOSITPARAMS.fields_by_name['min_deposit']._options = None
  _DEPOSITPARAMS.fields_by_name['min_deposit']._serialized_options = b'\310\336\037\000\352\336\037\025min_deposit,omitempty'
  _DEPOSITPARAMS.fields_by_name['max_deposit_period']._options = None
  _DEPOSITPARAMS.fields_by_name['max_deposit_period']._serialized_options = b'\352\336\037\034max_deposit_period,omitempty\230\337\037\001'
  _VOTINGPARAMS.fields_by_name['voting_period']._options = None
  _VOTINGPARAMS.fields_by_name['voting_period']._serialized_options = b'\230\337\037\001'
  _TALLYPARAMS.fields_by_name['quorum']._options = None
  _TALLYPARAMS.fields_by_name['quorum']._serialized_options = b'\322\264-\ncosmos.Dec'
  _TALLYPARAMS.fields_by_name['threshold']._options = None
  _TALLYPARAMS.fields_by_name['threshold']._serialized_options = b'\322\264-\ncosmos.Dec'
  _TALLYPARAMS.fields_by_name['veto_threshold']._options = None
  _TALLYPARAMS.fields_by_name['veto_threshold']._serialized_options = b'\322\264-\ncosmos.Dec'
  _PARAMS.fields_by_name['min_deposit']._options = None
  _PARAMS.fields_by_name['min_deposit']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _PARAMS.fields_by_name['max_deposit_period']._options = None
  _PARAMS.fields_by_name['max_deposit_period']._serialized_options = b'\230\337\037\001'
  _PARAMS.fields_by_name['voting_period']._options = None
  _PARAMS.fields_by_name['voting_period']._serialized_options = b'\230\337\037\001'
  _PARAMS.fields_by_name['quorum']._options = None
  _PARAMS.fields_by_name['quorum']._serialized_options = b'\322\264-\ncosmos.Dec'
  _PARAMS.fields_by_name['threshold']._options = None
  _PARAMS.fields_by_name['threshold']._serialized_options = b'\322\264-\ncosmos.Dec'
  _PARAMS.fields_by_name['veto_threshold']._options = None
  _PARAMS.fields_by_name['veto_threshold']._serialized_options = b'\322\264-\ncosmos.Dec'
  _PARAMS.fields_by_name['min_initial_deposit_ratio']._options = None
  _PARAMS.fields_by_name['min_initial_deposit_ratio']._serialized_options = b'\322\264-\ncosmos.Dec'
  _globals['_VOTEOPTION']._serialized_start=2155
  _globals['_VOTEOPTION']._serialized_end=2292
  _globals['_PROPOSALSTATUS']._serialized_start=2295
  _globals['_PROPOSALSTATUS']._serialized_end=2501
  _globals['_WEIGHTEDVOTEOPTION']._serialized_start=234
  _globals['_WEIGHTEDVOTEOPTION']._serialized_end=329
  _globals['_DEPOSIT']._serialized_start=332
  _globals['_DEPOSIT']._serialized_end=461
  _globals['_PROPOSAL']._serialized_start=464
  _globals['_PROPOSAL']._serialized_end=1019
  _globals['_TALLYRESULT']._serialized_start=1022
  _globals['_TALLYRESULT']._serialized_end=1187
  _globals['_VOTE']._serialized_start=1190
  _globals['_VOTE']._serialized_end=1334
  _globals['_DEPOSITPARAMS']._serialized_start=1337
  _globals['_DEPOSITPARAMS']._serialized_end=1524
  _globals['_VOTINGPARAMS']._serialized_start=1526
  _globals['_VOTINGPARAMS']._serialized_end=1596
  _globals['_TALLYPARAMS']._serialized_start=1598
  _globals['_TALLYPARAMS']._serialized_end=1718
  _globals['_PARAMS']._serialized_start=1721
  _globals['_PARAMS']._serialized_end=2152
# @@protoc_insertion_point(module_scope)
