# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1beta1/proto/asset_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.asset_v1beta1.proto import assets_pb2 as google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_assets__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/asset_v1beta1/proto/asset_service.proto',
  package='google.cloud.asset.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n4google/cloud/asset_v1beta1/proto/asset_service.proto\x12\x1agoogle.cloud.asset.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a-google/cloud/asset_v1beta1/proto/assets.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe9\x01\n\x13\x45xportAssetsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12-\n\tread_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x61sset_types\x18\x03 \x03(\t\x12=\n\x0c\x63ontent_type\x18\x04 \x01(\x0e\x32\'.google.cloud.asset.v1beta1.ContentType\x12?\n\routput_config\x18\x05 \x01(\x0b\x32(.google.cloud.asset.v1beta1.OutputConfig\"\x86\x01\n\x14\x45xportAssetsResponse\x12-\n\tread_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\routput_config\x18\x02 \x01(\x0b\x32(.google.cloud.asset.v1beta1.OutputConfig\"\xc4\x01\n\x1c\x42\x61tchGetAssetsHistoryRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x13\n\x0b\x61sset_names\x18\x02 \x03(\t\x12=\n\x0c\x63ontent_type\x18\x03 \x01(\x0e\x32\'.google.cloud.asset.v1beta1.ContentType\x12@\n\x10read_time_window\x18\x04 \x01(\x0b\x32&.google.cloud.asset.v1beta1.TimeWindow\"Z\n\x1d\x42\x61tchGetAssetsHistoryResponse\x12\x39\n\x06\x61ssets\x18\x01 \x03(\x0b\x32).google.cloud.asset.v1beta1.TemporalAsset\"d\n\x0cOutputConfig\x12\x45\n\x0fgcs_destination\x18\x01 \x01(\x0b\x32*.google.cloud.asset.v1beta1.GcsDestinationH\x00\x42\r\n\x0b\x64\x65stination\"\x1d\n\x0eGcsDestination\x12\x0b\n\x03uri\x18\x01 \x01(\t*I\n\x0b\x43ontentType\x12\x1c\n\x18\x43ONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08RESOURCE\x10\x01\x12\x0e\n\nIAM_POLICY\x10\x02\x32\xdf\x03\n\x0c\x41ssetService\x12\xc9\x01\n\x0c\x45xportAssets\x12/.google.cloud.asset.v1beta1.ExportAssetsRequest\x1a\x1d.google.longrunning.Operation\"i\x82\xd3\xe4\x93\x02\x63\")/v1beta1/{parent=projects/*}:exportAssets:\x01*Z3\"./v1beta1/{parent=organizations/*}:exportAssets:\x01*\x12\x82\x02\n\x15\x42\x61tchGetAssetsHistory\x12\x38.google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest\x1a\x39.google.cloud.asset.v1beta1.BatchGetAssetsHistoryResponse\"t\x82\xd3\xe4\x93\x02n\x12\x32/v1beta1/{parent=projects/*}:batchGetAssetsHistoryZ8\x12\x36/v1beta1/{parent=organizations/*}:batchGetAssetHistoryB\xb0\x01\n\x1e\x63om.google.cloud.asset.v1beta1B\x11\x41ssetServiceProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/asset/v1beta1;asset\xaa\x02\x1aGoogle.Cloud.Asset.V1Beta1\xca\x02\x1aGoogle\\Cloud\\Asset\\V1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_assets__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='google.cloud.asset.v1beta1.ContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTENT_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAM_POLICY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1028,
  serialized_end=1101,
)
_sym_db.RegisterEnumDescriptor(_CONTENTTYPE)

ContentType = enum_type_wrapper.EnumTypeWrapper(_CONTENTTYPE)
CONTENT_TYPE_UNSPECIFIED = 0
RESOURCE = 1
IAM_POLICY = 2



_EXPORTASSETSREQUEST = _descriptor.Descriptor(
  name='ExportAssetsRequest',
  full_name='google.cloud.asset.v1beta1.ExportAssetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.asset.v1beta1.ExportAssetsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_time', full_name='google.cloud.asset.v1beta1.ExportAssetsRequest.read_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_types', full_name='google.cloud.asset.v1beta1.ExportAssetsRequest.asset_types', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.cloud.asset.v1beta1.ExportAssetsRequest.content_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_config', full_name='google.cloud.asset.v1beta1.ExportAssetsRequest.output_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=465,
)


_EXPORTASSETSRESPONSE = _descriptor.Descriptor(
  name='ExportAssetsResponse',
  full_name='google.cloud.asset.v1beta1.ExportAssetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_time', full_name='google.cloud.asset.v1beta1.ExportAssetsResponse.read_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_config', full_name='google.cloud.asset.v1beta1.ExportAssetsResponse.output_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=602,
)


_BATCHGETASSETSHISTORYREQUEST = _descriptor.Descriptor(
  name='BatchGetAssetsHistoryRequest',
  full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_names', full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest.asset_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest.content_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_time_window', full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest.read_time_window', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=801,
)


_BATCHGETASSETSHISTORYRESPONSE = _descriptor.Descriptor(
  name='BatchGetAssetsHistoryResponse',
  full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='google.cloud.asset.v1beta1.BatchGetAssetsHistoryResponse.assets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=893,
)


_OUTPUTCONFIG = _descriptor.Descriptor(
  name='OutputConfig',
  full_name='google.cloud.asset.v1beta1.OutputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gcs_destination', full_name='google.cloud.asset.v1beta1.OutputConfig.gcs_destination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='destination', full_name='google.cloud.asset.v1beta1.OutputConfig.destination',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=895,
  serialized_end=995,
)


_GCSDESTINATION = _descriptor.Descriptor(
  name='GcsDestination',
  full_name='google.cloud.asset.v1beta1.GcsDestination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='google.cloud.asset.v1beta1.GcsDestination.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=997,
  serialized_end=1026,
)

_EXPORTASSETSREQUEST.fields_by_name['read_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPORTASSETSREQUEST.fields_by_name['content_type'].enum_type = _CONTENTTYPE
_EXPORTASSETSREQUEST.fields_by_name['output_config'].message_type = _OUTPUTCONFIG
_EXPORTASSETSRESPONSE.fields_by_name['read_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXPORTASSETSRESPONSE.fields_by_name['output_config'].message_type = _OUTPUTCONFIG
_BATCHGETASSETSHISTORYREQUEST.fields_by_name['content_type'].enum_type = _CONTENTTYPE
_BATCHGETASSETSHISTORYREQUEST.fields_by_name['read_time_window'].message_type = google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_assets__pb2._TIMEWINDOW
_BATCHGETASSETSHISTORYRESPONSE.fields_by_name['assets'].message_type = google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_assets__pb2._TEMPORALASSET
_OUTPUTCONFIG.fields_by_name['gcs_destination'].message_type = _GCSDESTINATION
_OUTPUTCONFIG.oneofs_by_name['destination'].fields.append(
  _OUTPUTCONFIG.fields_by_name['gcs_destination'])
_OUTPUTCONFIG.fields_by_name['gcs_destination'].containing_oneof = _OUTPUTCONFIG.oneofs_by_name['destination']
DESCRIPTOR.message_types_by_name['ExportAssetsRequest'] = _EXPORTASSETSREQUEST
DESCRIPTOR.message_types_by_name['ExportAssetsResponse'] = _EXPORTASSETSRESPONSE
DESCRIPTOR.message_types_by_name['BatchGetAssetsHistoryRequest'] = _BATCHGETASSETSHISTORYREQUEST
DESCRIPTOR.message_types_by_name['BatchGetAssetsHistoryResponse'] = _BATCHGETASSETSHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['OutputConfig'] = _OUTPUTCONFIG
DESCRIPTOR.message_types_by_name['GcsDestination'] = _GCSDESTINATION
DESCRIPTOR.enum_types_by_name['ContentType'] = _CONTENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExportAssetsRequest = _reflection.GeneratedProtocolMessageType('ExportAssetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTASSETSREQUEST,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """Export asset request.
  
  
  Attributes:
      parent:
          Required. The relative name of the root asset. Can only be an
          organization number (such as "organizations/123"), or a
          project id (such as "projects/my-project-id") or a project
          number (such as "projects/12345").
      read_time:
          Timestamp to take an asset snapshot. This can only be set to a
          timestamp in the past or of the current time. If not
          specified, the current time will be used. Due to delays in
          resource data collection and indexing, there is a volatile
          window during which running the same query may get different
          results.
      asset_types:
          A list of asset types of which to take a snapshot for.
          Example: "google.compute.disk". If specified, only matching
          assets will be returned.
      content_type:
          Asset content type. If not specified, no content but the asset
          name will be returned.
      output_config:
          Required. Output configuration indicating where the results
          will be output to. All results will be in newline delimited
          JSON format.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.ExportAssetsRequest)
  ))
_sym_db.RegisterMessage(ExportAssetsRequest)

ExportAssetsResponse = _reflection.GeneratedProtocolMessageType('ExportAssetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTASSETSRESPONSE,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """The export asset response. This message is returned by the
  [google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]
  method in the returned
  [google.longrunning.Operation.response][google.longrunning.Operation.response]
  field.
  
  
  Attributes:
      read_time:
          Time the snapshot was taken.
      output_config:
          Output configuration indicating where the results were output
          to. All results are in JSON format.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.ExportAssetsResponse)
  ))
_sym_db.RegisterMessage(ExportAssetsResponse)

BatchGetAssetsHistoryRequest = _reflection.GeneratedProtocolMessageType('BatchGetAssetsHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHGETASSETSHISTORYREQUEST,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """Batch get assets history request.
  
  
  Attributes:
      parent:
          Required. The relative name of the root asset. It can only be
          an organization number (such as "organizations/123"), or a
          project id (such as "projects/my-project-id")"or a project
          number (such as "projects/12345").
      asset_names:
          A list of the full names of the assets. See: https://cloud.goo
          gle.com/apis/design/resource\_names#full\_resource\_name
          Example: "//compute.googleapis.com/projects/my\_project\_123/z
          ones/zone1/instances/instance1".  The request becomes a no-op
          if the asset name list is empty, and the max size of the asset
          name list is 100 in one request.
      content_type:
          Required. The content type.
      read_time_window:
          Required. The time window for the asset history. The start
          time is required. The returned results contain all temporal
          assets whose time window overlap with read\_time\_window.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.BatchGetAssetsHistoryRequest)
  ))
_sym_db.RegisterMessage(BatchGetAssetsHistoryRequest)

BatchGetAssetsHistoryResponse = _reflection.GeneratedProtocolMessageType('BatchGetAssetsHistoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHGETASSETSHISTORYRESPONSE,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """Batch get assets history response.
  
  
  Attributes:
      assets:
          A list of assets with valid time windows.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.BatchGetAssetsHistoryResponse)
  ))
_sym_db.RegisterMessage(BatchGetAssetsHistoryResponse)

OutputConfig = _reflection.GeneratedProtocolMessageType('OutputConfig', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTCONFIG,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """Output configuration for export assets destination.
  
  
  Attributes:
      destination:
          Asset export destination.
      gcs_destination:
          Destination on Google Cloud Storage (GCS).
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.OutputConfig)
  ))
_sym_db.RegisterMessage(OutputConfig)

GcsDestination = _reflection.GeneratedProtocolMessageType('GcsDestination', (_message.Message,), dict(
  DESCRIPTOR = _GCSDESTINATION,
  __module__ = 'google.cloud.asset_v1beta1.proto.asset_service_pb2'
  ,
  __doc__ = """A Google Cloud Storage (GCS) location.
  
  
  Attributes:
      uri:
          The path of the GCS objects. It's the same path that is used
          by gsutil, for example: "gs://bucket\_name/object\_path". See:
          https://cloud.google.com/storage/docs/viewing-editing-metadata
          for more information.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.GcsDestination)
  ))
_sym_db.RegisterMessage(GcsDestination)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.google.cloud.asset.v1beta1B\021AssetServiceProtoP\001Z?google.golang.org/genproto/googleapis/cloud/asset/v1beta1;asset\252\002\032Google.Cloud.Asset.V1Beta1\312\002\032Google\\Cloud\\Asset\\V1beta1'))

_ASSETSERVICE = _descriptor.ServiceDescriptor(
  name='AssetService',
  full_name='google.cloud.asset.v1beta1.AssetService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1104,
  serialized_end=1583,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExportAssets',
    full_name='google.cloud.asset.v1beta1.AssetService.ExportAssets',
    index=0,
    containing_service=None,
    input_type=_EXPORTASSETSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002c\")/v1beta1/{parent=projects/*}:exportAssets:\001*Z3\"./v1beta1/{parent=organizations/*}:exportAssets:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='BatchGetAssetsHistory',
    full_name='google.cloud.asset.v1beta1.AssetService.BatchGetAssetsHistory',
    index=1,
    containing_service=None,
    input_type=_BATCHGETASSETSHISTORYREQUEST,
    output_type=_BATCHGETASSETSHISTORYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002n\0222/v1beta1/{parent=projects/*}:batchGetAssetsHistoryZ8\0226/v1beta1/{parent=organizations/*}:batchGetAssetHistory')),
  ),
])
_sym_db.RegisterServiceDescriptor(_ASSETSERVICE)

DESCRIPTOR.services_by_name['AssetService'] = _ASSETSERVICE

# @@protoc_insertion_point(module_scope)
