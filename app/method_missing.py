class MethodMissingMetaClass(type):

    def __getattr__(cls, attr_name):

        try:
            attr = cls.__getattribute__(cls, attr_name)
        except Exception as e:
            attr = getattr(cls, "method_missing")
        
        return attr

