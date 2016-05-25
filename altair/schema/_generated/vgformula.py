# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class VgFormula(BaseObject):
    """
    
    Attributes
    ----------
    expr: Unicode
        A string containing an expression for the formula.
    field: Unicode
        The field in which to store the computed formula value.
    """
    expr = T.Unicode(allow_none=True, default_value=None, help="""A string containing an expression for the formula.""")
    field = T.Unicode(allow_none=True, default_value=None, help="""The field in which to store the computed formula value.""")
    

    def __init__(self, expr=None, field=None, **kwargs):
        kwds = dict(expr=expr, field=field, )
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(VgFormula, self).__init__(**kwargs)