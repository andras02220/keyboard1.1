# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keyboard.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keyboard.proto',
  package='keyboardsender',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ekeyboard.proto\x12\x0ekeyboardsender\"\x18\n\tKeyStroke\x12\x0b\n\x03key\x18\x01 \x01(\t2Q\n\x08Keyboard\x12\x45\n\x0bGetKeyboard\x12\x19.keyboardsender.KeyStroke\x1a\x19.keyboardsender.KeyStroke0\x01\x62\x06proto3'
)




_KEYSTROKE = _descriptor.Descriptor(
  name='KeyStroke',
  full_name='keyboardsender.KeyStroke',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='keyboardsender.KeyStroke.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=58,
)

DESCRIPTOR.message_types_by_name['KeyStroke'] = _KEYSTROKE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyStroke = _reflection.GeneratedProtocolMessageType('KeyStroke', (_message.Message,), {
  'DESCRIPTOR' : _KEYSTROKE,
  '__module__' : 'keyboard_pb2'
  # @@protoc_insertion_point(class_scope:keyboardsender.KeyStroke)
  })
_sym_db.RegisterMessage(KeyStroke)



_KEYBOARD = _descriptor.ServiceDescriptor(
  name='Keyboard',
  full_name='keyboardsender.Keyboard',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=60,
  serialized_end=141,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeyboard',
    full_name='keyboardsender.Keyboard.GetKeyboard',
    index=0,
    containing_service=None,
    input_type=_KEYSTROKE,
    output_type=_KEYSTROKE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYBOARD)

DESCRIPTOR.services_by_name['Keyboard'] = _KEYBOARD

# @@protoc_insertion_point(module_scope)