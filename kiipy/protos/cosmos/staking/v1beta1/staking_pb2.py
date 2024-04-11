# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/staking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/staking.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x11\x61mino/amino.proto\x1a\x1ctendermint/types/types.proto\x1a\x1btendermint/abci/types.proto\"\x83\x01\n\x0eHistoricalInfo\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32\x18.tendermint.types.HeaderB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12<\n\x06valset\x18\x02 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x8e\x02\n\x0f\x43ommissionRates\x12J\n\x04rate\x18\x01 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12N\n\x08max_rate\x18\x02 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12U\n\x0fmax_change_rate\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"\xa8\x01\n\nCommission\x12P\n\x10\x63ommission_rates\x18\x01 \x01(\x0b\x32\'.cosmos.staking.v1beta1.CommissionRatesB\r\xc8\xde\x1f\x00\xd0\xde\x1f\x01\xa8\xe7\xb0*\x01\x12>\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"v\n\x0b\x44\x65scription\x12\x0f\n\x07moniker\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x18\n\x10security_contact\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"\xfd\x05\n\tValidator\x12\x32\n\x10operator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12H\n\x10\x63onsensus_pubkey\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x18\xca\xb4-\x14\x63osmos.crypto.PubKey\x12\x0e\n\x06jailed\x18\x03 \x01(\x08\x12\x32\n\x06status\x18\x04 \x01(\x0e\x32\".cosmos.staking.v1beta1.BondStatus\x12L\n\x06tokens\x18\x05 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x12V\n\x10\x64\x65legator_shares\x18\x06 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12\x43\n\x0b\x64\x65scription\x18\x07 \x01(\x0b\x32#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x18\n\x10unbonding_height\x18\x08 \x01(\x03\x12\x41\n\x0eunbonding_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x41\n\ncommission\x18\n \x01(\x0b\x32\".cosmos.staking.v1beta1.CommissionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12Y\n\x13min_self_delegation\x18\x0b \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x12#\n\x1bunbonding_on_hold_ref_count\x18\x0c \x01(\x03\x12\x15\n\runbonding_ids\x18\r \x03(\x04:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"E\n\x0cValAddresses\x12+\n\taddresses\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\x98\xa0\x1f\x00\x80\xdc \x01\"\x80\x01\n\x06\x44VPair\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"C\n\x07\x44VPairs\x12\x38\n\x05pairs\x18\x01 \x03(\x0b\x32\x1e.cosmos.staking.v1beta1.DVPairB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xc1\x01\n\nDVVTriplet\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x15validator_src_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x15validator_dst_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"N\n\x0b\x44VVTriplets\x12?\n\x08triplets\x18\x01 \x03(\x0b\x32\".cosmos.staking.v1beta1.DVVTripletB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xd2\x01\n\nDelegation\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12L\n\x06shares\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xdb\x01\n\x13UnbondingDelegation\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12L\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x30.cosmos.staking.v1beta1.UnbondingDelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xe2\x02\n\x18UnbondingDelegationEntry\x12\x17\n\x0f\x63reation_height\x18\x01 \x01(\x03\x12\x42\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12U\n\x0finitial_balance\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x12M\n\x07\x62\x61lance\x18\x04 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x12\x14\n\x0cunbonding_id\x18\x05 \x01(\x04\x12#\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"\xde\x02\n\x11RedelegationEntry\x12\x17\n\x0f\x63reation_height\x18\x01 \x01(\x03\x12\x42\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12U\n\x0finitial_balance\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x12P\n\nshares_dst\x18\x04 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12\x14\n\x0cunbonding_id\x18\x05 \x01(\x04\x12#\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\"\x8a\x02\n\x0cRedelegation\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x15validator_src_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x15validator_dst_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x45\n\x07\x65ntries\x18\x04 \x03(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xbc\x02\n\x06Params\x12@\n\x0eunbonding_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x16\n\x0emax_validators\x18\x02 \x01(\r\x12\x13\n\x0bmax_entries\x18\x03 \x01(\r\x12\x1a\n\x12historical_entries\x18\x04 \x01(\r\x12\x12\n\nbond_denom\x18\x05 \x01(\t\x12i\n\x13min_commission_rate\x18\x06 \x01(\tBL\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1ayaml:\"min_commission_rate\":(\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x1b\x63osmos-sdk/x/staking/Params\"\x98\x01\n\x12\x44\x65legationResponse\x12\x41\n\ndelegation\x18\x01 \x01(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x35\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xc2\x01\n\x19RedelegationEntryResponse\x12P\n\x12redelegation_entry\x18\x01 \x01(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12M\n\x07\x62\x61lance\x18\x04 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int:\x04\xe8\xa0\x1f\x01\"\xb2\x01\n\x14RedelegationResponse\x12\x45\n\x0credelegation\x18\x01 \x01(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12M\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x31.cosmos.staking.v1beta1.RedelegationEntryResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x04\xe8\xa0\x1f\x00\"\xee\x01\n\x04Pool\x12q\n\x11not_bonded_tokens\x18\x01 \x01(\tBV\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\x11not_bonded_tokens\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01\x12i\n\rbonded_tokens\x18\x02 \x01(\tBR\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\rbonded_tokens\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x01\xf0\xa0\x1f\x01\"P\n\x10ValidatorUpdates\x12<\n\x07updates\x18\x01 \x03(\x0b\x32 .tendermint.abci.ValidatorUpdateB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01*\xb6\x01\n\nBondStatus\x12,\n\x17\x42OND_STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12&\n\x14\x42OND_STATUS_UNBONDED\x10\x01\x1a\x0c\x8a\x9d \x08Unbonded\x12(\n\x15\x42OND_STATUS_UNBONDING\x10\x02\x1a\r\x8a\x9d \tUnbonding\x12\"\n\x12\x42OND_STATUS_BONDED\x10\x03\x1a\n\x8a\x9d \x06\x42onded\x1a\x04\x88\xa3\x1e\x00*]\n\nInfraction\x12\x1a\n\x16INFRACTION_UNSPECIFIED\x10\x00\x12\x1a\n\x16INFRACTION_DOUBLE_SIGN\x10\x01\x12\x17\n\x13INFRACTION_DOWNTIME\x10\x02\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.staking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _BONDSTATUS._options = None
  _BONDSTATUS._serialized_options = b'\210\243\036\000'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNSPECIFIED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNSPECIFIED"]._serialized_options = b'\212\235 \013Unspecified'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDED"]._serialized_options = b'\212\235 \010Unbonded'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDING"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDING"]._serialized_options = b'\212\235 \tUnbonding'
  _BONDSTATUS.values_by_name["BOND_STATUS_BONDED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_BONDED"]._serialized_options = b'\212\235 \006Bonded'
  _HISTORICALINFO.fields_by_name['header']._options = None
  _HISTORICALINFO.fields_by_name['header']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _HISTORICALINFO.fields_by_name['valset']._options = None
  _HISTORICALINFO.fields_by_name['valset']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _COMMISSIONRATES.fields_by_name['rate']._options = None
  _COMMISSIONRATES.fields_by_name['rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _COMMISSIONRATES.fields_by_name['max_rate']._options = None
  _COMMISSIONRATES.fields_by_name['max_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _COMMISSIONRATES.fields_by_name['max_change_rate']._options = None
  _COMMISSIONRATES.fields_by_name['max_change_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _COMMISSIONRATES._options = None
  _COMMISSIONRATES._serialized_options = b'\230\240\037\000\350\240\037\001'
  _COMMISSION.fields_by_name['commission_rates']._options = None
  _COMMISSION.fields_by_name['commission_rates']._serialized_options = b'\310\336\037\000\320\336\037\001\250\347\260*\001'
  _COMMISSION.fields_by_name['update_time']._options = None
  _COMMISSION.fields_by_name['update_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _COMMISSION._options = None
  _COMMISSION._serialized_options = b'\230\240\037\000\350\240\037\001'
  _DESCRIPTION._options = None
  _DESCRIPTION._serialized_options = b'\230\240\037\000\350\240\037\001'
  _VALIDATOR.fields_by_name['operator_address']._options = None
  _VALIDATOR.fields_by_name['operator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _VALIDATOR.fields_by_name['consensus_pubkey']._options = None
  _VALIDATOR.fields_by_name['consensus_pubkey']._serialized_options = b'\312\264-\024cosmos.crypto.PubKey'
  _VALIDATOR.fields_by_name['tokens']._options = None
  _VALIDATOR.fields_by_name['tokens']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _VALIDATOR.fields_by_name['delegator_shares']._options = None
  _VALIDATOR.fields_by_name['delegator_shares']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _VALIDATOR.fields_by_name['description']._options = None
  _VALIDATOR.fields_by_name['description']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATOR.fields_by_name['unbonding_time']._options = None
  _VALIDATOR.fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _VALIDATOR.fields_by_name['commission']._options = None
  _VALIDATOR.fields_by_name['commission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATOR.fields_by_name['min_self_delegation']._options = None
  _VALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _VALIDATOR._options = None
  _VALIDATOR._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _VALADDRESSES.fields_by_name['addresses']._options = None
  _VALADDRESSES.fields_by_name['addresses']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _VALADDRESSES._options = None
  _VALADDRESSES._serialized_options = b'\230\240\037\000\200\334 \001'
  _DVPAIR.fields_by_name['delegator_address']._options = None
  _DVPAIR.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DVPAIR.fields_by_name['validator_address']._options = None
  _DVPAIR.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DVPAIR._options = None
  _DVPAIR._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _DVPAIRS.fields_by_name['pairs']._options = None
  _DVPAIRS.fields_by_name['pairs']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DVVTRIPLET.fields_by_name['delegator_address']._options = None
  _DVVTRIPLET.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DVVTRIPLET.fields_by_name['validator_src_address']._options = None
  _DVVTRIPLET.fields_by_name['validator_src_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DVVTRIPLET.fields_by_name['validator_dst_address']._options = None
  _DVVTRIPLET.fields_by_name['validator_dst_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DVVTRIPLET._options = None
  _DVVTRIPLET._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _DVVTRIPLETS.fields_by_name['triplets']._options = None
  _DVVTRIPLETS.fields_by_name['triplets']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DELEGATION.fields_by_name['delegator_address']._options = None
  _DELEGATION.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DELEGATION.fields_by_name['validator_address']._options = None
  _DELEGATION.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DELEGATION.fields_by_name['shares']._options = None
  _DELEGATION.fields_by_name['shares']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _DELEGATION._options = None
  _DELEGATION._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _UNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
  _UNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _UNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
  _UNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _UNBONDINGDELEGATION.fields_by_name['entries']._options = None
  _UNBONDINGDELEGATION.fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _UNBONDINGDELEGATION._options = None
  _UNBONDINGDELEGATION._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _UNBONDINGDELEGATIONENTRY._options = None
  _UNBONDINGDELEGATIONENTRY._serialized_options = b'\230\240\037\000\350\240\037\001'
  _REDELEGATIONENTRY.fields_by_name['completion_time']._options = None
  _REDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _REDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
  _REDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _REDELEGATIONENTRY.fields_by_name['shares_dst']._options = None
  _REDELEGATIONENTRY.fields_by_name['shares_dst']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\322\264-\ncosmos.Dec'
  _REDELEGATIONENTRY._options = None
  _REDELEGATIONENTRY._serialized_options = b'\230\240\037\000\350\240\037\001'
  _REDELEGATION.fields_by_name['delegator_address']._options = None
  _REDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _REDELEGATION.fields_by_name['validator_src_address']._options = None
  _REDELEGATION.fields_by_name['validator_src_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _REDELEGATION.fields_by_name['validator_dst_address']._options = None
  _REDELEGATION.fields_by_name['validator_dst_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _REDELEGATION.fields_by_name['entries']._options = None
  _REDELEGATION.fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _REDELEGATION._options = None
  _REDELEGATION._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _PARAMS.fields_by_name['unbonding_time']._options = None
  _PARAMS.fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\230\337\037\001\250\347\260*\001'
  _PARAMS.fields_by_name['min_commission_rate']._options = None
  _PARAMS.fields_by_name['min_commission_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\362\336\037\032yaml:\"min_commission_rate\"'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000\350\240\037\001\212\347\260*\033cosmos-sdk/x/staking/Params'
  _DELEGATIONRESPONSE.fields_by_name['delegation']._options = None
  _DELEGATIONRESPONSE.fields_by_name['delegation']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DELEGATIONRESPONSE.fields_by_name['balance']._options = None
  _DELEGATIONRESPONSE.fields_by_name['balance']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DELEGATIONRESPONSE._options = None
  _DELEGATIONRESPONSE._serialized_options = b'\230\240\037\000\350\240\037\000'
  _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._options = None
  _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._options = None
  _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int'
  _REDELEGATIONENTRYRESPONSE._options = None
  _REDELEGATIONENTRYRESPONSE._serialized_options = b'\350\240\037\001'
  _REDELEGATIONRESPONSE.fields_by_name['redelegation']._options = None
  _REDELEGATIONRESPONSE.fields_by_name['redelegation']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _REDELEGATIONRESPONSE.fields_by_name['entries']._options = None
  _REDELEGATIONRESPONSE.fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _REDELEGATIONRESPONSE._options = None
  _REDELEGATIONRESPONSE._serialized_options = b'\350\240\037\000'
  _POOL.fields_by_name['not_bonded_tokens']._options = None
  _POOL.fields_by_name['not_bonded_tokens']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\352\336\037\021not_bonded_tokens\322\264-\ncosmos.Int\250\347\260*\001'
  _POOL.fields_by_name['bonded_tokens']._options = None
  _POOL.fields_by_name['bonded_tokens']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\352\336\037\rbonded_tokens\322\264-\ncosmos.Int\250\347\260*\001'
  _POOL._options = None
  _POOL._serialized_options = b'\350\240\037\001\360\240\037\001'
  _VALIDATORUPDATES.fields_by_name['updates']._options = None
  _VALIDATORUPDATES.fields_by_name['updates']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_BONDSTATUS']._serialized_start=4918
  _globals['_BONDSTATUS']._serialized_end=5100
  _globals['_INFRACTION']._serialized_start=5102
  _globals['_INFRACTION']._serialized_end=5195
  _globals['_HISTORICALINFO']._serialized_start=316
  _globals['_HISTORICALINFO']._serialized_end=447
  _globals['_COMMISSIONRATES']._serialized_start=450
  _globals['_COMMISSIONRATES']._serialized_end=720
  _globals['_COMMISSION']._serialized_start=723
  _globals['_COMMISSION']._serialized_end=891
  _globals['_DESCRIPTION']._serialized_start=893
  _globals['_DESCRIPTION']._serialized_end=1011
  _globals['_VALIDATOR']._serialized_start=1014
  _globals['_VALIDATOR']._serialized_end=1779
  _globals['_VALADDRESSES']._serialized_start=1781
  _globals['_VALADDRESSES']._serialized_end=1850
  _globals['_DVPAIR']._serialized_start=1853
  _globals['_DVPAIR']._serialized_end=1981
  _globals['_DVPAIRS']._serialized_start=1983
  _globals['_DVPAIRS']._serialized_end=2050
  _globals['_DVVTRIPLET']._serialized_start=2053
  _globals['_DVVTRIPLET']._serialized_end=2246
  _globals['_DVVTRIPLETS']._serialized_start=2248
  _globals['_DVVTRIPLETS']._serialized_end=2326
  _globals['_DELEGATION']._serialized_start=2329
  _globals['_DELEGATION']._serialized_end=2539
  _globals['_UNBONDINGDELEGATION']._serialized_start=2542
  _globals['_UNBONDINGDELEGATION']._serialized_end=2761
  _globals['_UNBONDINGDELEGATIONENTRY']._serialized_start=2764
  _globals['_UNBONDINGDELEGATIONENTRY']._serialized_end=3118
  _globals['_REDELEGATIONENTRY']._serialized_start=3121
  _globals['_REDELEGATIONENTRY']._serialized_end=3471
  _globals['_REDELEGATION']._serialized_start=3474
  _globals['_REDELEGATION']._serialized_end=3740
  _globals['_PARAMS']._serialized_start=3743
  _globals['_PARAMS']._serialized_end=4059
  _globals['_DELEGATIONRESPONSE']._serialized_start=4062
  _globals['_DELEGATIONRESPONSE']._serialized_end=4214
  _globals['_REDELEGATIONENTRYRESPONSE']._serialized_start=4217
  _globals['_REDELEGATIONENTRYRESPONSE']._serialized_end=4411
  _globals['_REDELEGATIONRESPONSE']._serialized_start=4414
  _globals['_REDELEGATIONRESPONSE']._serialized_end=4592
  _globals['_POOL']._serialized_start=4595
  _globals['_POOL']._serialized_end=4833
  _globals['_VALIDATORUPDATES']._serialized_start=4835
  _globals['_VALIDATORUPDATES']._serialized_end=4915
# @@protoc_insertion_point(module_scope)
