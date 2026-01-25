from pyutils.inspect_util import *
from pyutils.json_util import *

heterogeneous_list = [1, "2", 3.0, True]
print(f"deep_type(heterogeneous_list) = {deep_type(heterogeneous_list)}")
print(to_json_pretty(json_schema(heterogeneous_list)))

heterogeneous_dict = {"a": 1, "b": "2", "c": 3.0, "d": True}
print(f"deep_type(heterogeneous_dict) = {deep_type(heterogeneous_dict)}")
print(to_json_pretty(json_schema(heterogeneous_dict)))

class HeterogeneousModel:
    def __init__(self, id, name, tags):
        self.id = id
        self.name = name
        self.tags = tags

m1 = HeterogeneousModel(1, "abc", ["a", 1.3])
print(f"deep_type(m1) = {deep_type(m1)}")
print(to_json_pretty(json_schema(m1)))

m2 = HeterogeneousModel(2, "def", ["c", True])
print(f"deep_type(m2) = {deep_type(m2)}")
print(to_json_pretty(json_objs_schema([m1, m2])))

m3 = HeterogeneousModel(2, "def", ["c", 10])
print(f"deep_type(m3) = {deep_type(m3)}")
print(to_json_pretty(json_objs_schema([m1, m2, m3])))


# ----

{
  "id": {
    "type": "integer"
  },
  "name": {
    "type": "string"
  },
  "tags": {
    "type": "array",
    "items": {
      "oneOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean"
        },
        {
          "type": "string"
        }
      ]
    }
  }
}
        