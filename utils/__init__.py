import types

def asbool(value):
    """Converts the value into a bool object or raises ValueError"""
    if type(value) in (types.StringType, types.UnicodeType):
        if not value.isalpha():
            value = int(value)
        elif value.lower() in ('true', 't'):
            return True
        else:
            return False
        
    if type(value) == types.IntType:
        return True if value >= 1 else False