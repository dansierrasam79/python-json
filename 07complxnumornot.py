# check if complex num or not
import json

def encode_complex(object):
    # check using isinstance method
    if isinstance(object, complex):
        return [object.real, object.imag]
    else:
        return "not JSON serialized"

complex_obj = json.dumps(8 + 1j, default=encode_complex)
print(complex_obj)
