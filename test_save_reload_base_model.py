#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

print("-- Storage objects after creating my_model --")
for obj_id, obj in storage.all().items():
    print(obj)

print("-- my_model attributes before saving --")
print(my_model.__dict__)

try:
    my_model.save()
except Exception as e:
    print("Error saving to file:", e)

print("-- Storage file path --")
print(storage._FileStorage__file_path)
