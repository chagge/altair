# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T


class HorizontalAlign(T.Enum):
    def __init__(self, default_value=T.Undefined, **metadata):
        super(HorizontalAlign, self).__init__(['left', 'right', 'center', ],
                                       default_value=default_value,
                                       **metadata)