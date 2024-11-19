import inspect
def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    module = getattr(obj, '__module__', None)
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }
    return info
class Value_show():
    def __init__(self, value):
        self.value = value

    def show(self):
        return f'Значение: {self.value}'

object_ = Value_show(10)
object_info = introspection_info(object_)
print(object_info)
number_info = introspection_info(47)
print(number_info)