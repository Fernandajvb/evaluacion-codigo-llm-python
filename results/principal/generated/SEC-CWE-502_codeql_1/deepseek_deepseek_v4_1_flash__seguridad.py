from django.conf.urls import url
import pickle
import io

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        raise pickle.UnpicklingError("Deserialization of arbitrary objects is not allowed")

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    if not isinstance(pickled, (bytes, bytearray)):
        raise TypeError("pickled data must be bytes or bytearray")
    return SafeUnpickler(io.BytesIO(pickled)).load()
