# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/proto/motion_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/proto/motion_service.proto',
  package='apollo.perception',
  syntax='proto2',
  serialized_pb=_b('\n-modules/perception/proto/motion_service.proto\x12\x11\x61pollo.perception\x1a!modules/common/proto/header.proto\"\xdc\x01\n\nMotionType\x12\x0b\n\x03m00\x18\x01 \x01(\x02\x12\x0b\n\x03m01\x18\x02 \x01(\x02\x12\x0b\n\x03m02\x18\x03 \x01(\x02\x12\x0b\n\x03m03\x18\x04 \x01(\x02\x12\x0b\n\x03m10\x18\x05 \x01(\x02\x12\x0b\n\x03m11\x18\x06 \x01(\x02\x12\x0b\n\x03m12\x18\x07 \x01(\x02\x12\x0b\n\x03m13\x18\x08 \x01(\x02\x12\x0b\n\x03m20\x18\t \x01(\x02\x12\x0b\n\x03m21\x18\n \x01(\x02\x12\x0b\n\x03m22\x18\x0b \x01(\x02\x12\x0b\n\x03m23\x18\x0c \x01(\x02\x12\x0b\n\x03m30\x18\r \x01(\x02\x12\x0b\n\x03m31\x18\x0e \x01(\x02\x12\x0b\n\x03m32\x18\x0f \x01(\x02\x12\x0b\n\x03m33\x18\x10 \x01(\x02\"\xe6\x01\n\rVehicleStatus\x12\x11\n\troll_rate\x18\x01 \x01(\x02\x12\x12\n\npitch_rate\x18\x02 \x01(\x02\x12\x10\n\x08yaw_rate\x18\x03 \x01(\x02\x12\x10\n\x08velocity\x18\x04 \x01(\x02\x12\x12\n\nvelocity_x\x18\x05 \x01(\x02\x12\x12\n\nvelocity_y\x18\x06 \x01(\x02\x12\x12\n\nvelocity_z\x18\x07 \x01(\x02\x12\x0f\n\x07time_ts\x18\x08 \x01(\x01\x12\x0e\n\x06time_d\x18\t \x01(\x01\x12-\n\x06motion\x18\n \x01(\x0b\x32\x1d.apollo.perception.MotionType\"q\n\x0eMotion_Service\x12\x38\n\x0evehicle_status\x18\x01 \x03(\x0b\x32 .apollo.perception.VehicleStatus\x12%\n\x06header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MOTIONTYPE = _descriptor.Descriptor(
  name='MotionType',
  full_name='apollo.perception.MotionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m00', full_name='apollo.perception.MotionType.m00', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m01', full_name='apollo.perception.MotionType.m01', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m02', full_name='apollo.perception.MotionType.m02', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m03', full_name='apollo.perception.MotionType.m03', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m10', full_name='apollo.perception.MotionType.m10', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m11', full_name='apollo.perception.MotionType.m11', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m12', full_name='apollo.perception.MotionType.m12', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m13', full_name='apollo.perception.MotionType.m13', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m20', full_name='apollo.perception.MotionType.m20', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m21', full_name='apollo.perception.MotionType.m21', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m22', full_name='apollo.perception.MotionType.m22', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m23', full_name='apollo.perception.MotionType.m23', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m30', full_name='apollo.perception.MotionType.m30', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m31', full_name='apollo.perception.MotionType.m31', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m32', full_name='apollo.perception.MotionType.m32', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='m33', full_name='apollo.perception.MotionType.m33', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=324,
)


_VEHICLESTATUS = _descriptor.Descriptor(
  name='VehicleStatus',
  full_name='apollo.perception.VehicleStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roll_rate', full_name='apollo.perception.VehicleStatus.roll_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch_rate', full_name='apollo.perception.VehicleStatus.pitch_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yaw_rate', full_name='apollo.perception.VehicleStatus.yaw_rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='apollo.perception.VehicleStatus.velocity', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity_x', full_name='apollo.perception.VehicleStatus.velocity_x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity_y', full_name='apollo.perception.VehicleStatus.velocity_y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity_z', full_name='apollo.perception.VehicleStatus.velocity_z', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_ts', full_name='apollo.perception.VehicleStatus.time_ts', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_d', full_name='apollo.perception.VehicleStatus.time_d', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motion', full_name='apollo.perception.VehicleStatus.motion', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=557,
)


_MOTION_SERVICE = _descriptor.Descriptor(
  name='Motion_Service',
  full_name='apollo.perception.Motion_Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle_status', full_name='apollo.perception.Motion_Service.vehicle_status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.perception.Motion_Service.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=672,
)

_VEHICLESTATUS.fields_by_name['motion'].message_type = _MOTIONTYPE
_MOTION_SERVICE.fields_by_name['vehicle_status'].message_type = _VEHICLESTATUS
_MOTION_SERVICE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['MotionType'] = _MOTIONTYPE
DESCRIPTOR.message_types_by_name['VehicleStatus'] = _VEHICLESTATUS
DESCRIPTOR.message_types_by_name['Motion_Service'] = _MOTION_SERVICE

MotionType = _reflection.GeneratedProtocolMessageType('MotionType', (_message.Message,), dict(
  DESCRIPTOR = _MOTIONTYPE,
  __module__ = 'modules.perception.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.MotionType)
  ))
_sym_db.RegisterMessage(MotionType)

VehicleStatus = _reflection.GeneratedProtocolMessageType('VehicleStatus', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLESTATUS,
  __module__ = 'modules.perception.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.VehicleStatus)
  ))
_sym_db.RegisterMessage(VehicleStatus)

Motion_Service = _reflection.GeneratedProtocolMessageType('Motion_Service', (_message.Message,), dict(
  DESCRIPTOR = _MOTION_SERVICE,
  __module__ = 'modules.perception.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.Motion_Service)
  ))
_sym_db.RegisterMessage(Motion_Service)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
