import uuid
from datetime import datetime


class MyClass:
    """A test clasS"""
    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4()
        class_name = self.__class__.__name__
        print (class_name)


a = MyClass()
print (a)
