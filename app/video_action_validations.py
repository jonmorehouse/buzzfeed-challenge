import os

from method_missing import MethodMissingMetaClass
from exceptions import ParamMissing


class VideoActionValidations:

    __metaclass__ = MethodMissingMetaClass
    required_params = {
            "find": ["search"],
            "create": ["pub", "title", "duration"],
    }

    @classmethod
    def method_missing(kls, method_name, **kw):
        
        """ Handle validations that are not specifically defined. Assumes that params is an immutable dict """
        required_params = kls.required_params.get(method_name)
        if not required_params: return True

        for param in required_params:
            if not kw.get(param):
                raise ParamMissing(param)
                return False

        return True

    @classmethod
    def load_from_file(kls, params, **kw):

        return os.path.exists(kw.get("filepath"))






