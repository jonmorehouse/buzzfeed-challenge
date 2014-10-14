from method_missing import MethodMissingMetaClass
from exceptions import ParamMissing

class VideoActionValidations:

    __metaclass__ = MethodMissingMetaClass
    required_params = {
            "query": ["title"],
            "create": ["create"],
            "process_file": ["filepath"],
    }

    @classmethod
    def method_missing(kls, method_name, params, **kw):
        
        """ Handle validations that are not specifically defined. Assumes that params is an immutable dict """
        required_params = kls.required_params.get(method_name)
        if not required_params: return True

        for param in required_params:
            if not params.get(param):
                raise ParamMissing(param)
                return False

        return True


    # TODO - check and convert the duration / pub fields and cast them correctly


