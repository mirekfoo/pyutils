from pyutils.inspect_util import *
from pyutils.json_util import *

heterogeneous_list = [1, "2", 3.0, True]
heterogeneous_dict = {"a": 1, "b": "2", "c": 3.0, "d": True}

print(f"deep_type(heterogeneous_list) = {deep_type(heterogeneous_list)}")
print(f"json_schema(heterogeneous_list) = {to_json_pretty(json_schema(heterogeneous_list))}")

print(f"deep_type(heterogeneous_dict) = {deep_type(heterogeneous_dict)}")
print(f"json_schema(heterogeneous_dict) = {to_json_pretty(json_schema(heterogeneous_dict))}")

class HeterogeneousModel:
    def __init__(self, id, name, tags):
        self.id = id
        self.name = name
        self.tags = tags

m1 = HeterogeneousModel(1, "abc", ["a", 1.3])
m2 = HeterogeneousModel(2, "def", ["c", True])
m3 = HeterogeneousModel(2, "def", ["c", 10])

print(f"deep_type(m1) = {deep_type(m1)}")
print(f"json_schema(m1) = {to_json_pretty(json_schema(m1))}")

print(f"deep_type(m2) = {deep_type(m2)}")
print(f"json_objs_schema([m1, m2]) = {to_json_pretty(json_objs_schema([m1, m2]))}")

print(f"deep_type(m3) = {deep_type(m3)}")
print(f"json_objs_schema([m1, m2, m3]) = {to_json_pretty(json_objs_schema([m1, m2, m3]))}")

# ---

md1 = HeterogeneousModel(1, "abc", {"a": 1.3})
md2 = HeterogeneousModel(2, "def", {"a": True, "b": False})
md3 = HeterogeneousModel(2, "def", {"a": 10})

print(f"deep_type(md1) = {deep_type(md1)}")
print(f"json_schema(md1) = {to_json_pretty(json_schema(md1))}")

print(f"deep_type(md2) = {deep_type(md2)}")
print(f"json_objs_schema([md1, md2]) = {to_json_pretty(json_objs_schema([md1, md2]))}")

print(f"deep_type(md3) = {deep_type(md3)}")
print(f"json_objs_schema([md1, md2, md3]) = {to_json_pretty(json_objs_schema([md1, md2, md3]))}")


# ---- Output:

"""
deep_type(heterogeneous_list) = [bool | float | int | str]
json_schema(heterogeneous_list) = {
  "type": "array",
  "items": {
    "oneOf": [
      {
        "type": "boolean"
      },
      {
        "type": "number"
      },
      {
        "type": "string"
      }
    ]
  }
}
deep_type(heterogeneous_dict) = dict[str, float | bool | str | int]
json_schema(heterogeneous_dict) = {
  "type": "object",
  "properties": {
    "a": {
      "type": "integer"
    },
    "b": {
      "type": "string"
    },
    "c": {
      "type": "number"
    },
    "d": {
      "type": "boolean"
    }
  },
  "additionalProperties": {
    "oneOf": [
      {
        "type": "boolean"
      },
      {
        "type": "number"
      },
      {
        "type": "string"
      }
    ]
  }
}
deep_type(m1) = HeterogeneousModel{id: int, name: str, tags: [float | str]}
json_schema(m1) = {
  "type": "object",
  "title": "HeterogeneousModel",
  "properties": {
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
            "type": "string"
          }
        ]
      }
    }
  }
}
deep_type(m2) = HeterogeneousModel{id: int, name: str, tags: [bool | str]}
json_objs_schema([m1, m2]) = {
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
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ]
    }
  }
}
deep_type(m3) = HeterogeneousModel{id: int, name: str, tags: [int | str]}
json_objs_schema([m1, m2, m3]) = {
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
          "type": "boolean"
        },
        {
          "type": "number"
        },
        {
          "type": "string"
        }
      ]
    }
  }
}
deep_type(md1) = HeterogeneousModel{id: int, name: str, tags: dict[str, float]}
json_schema(md1) = {
  "type": "object",
  "title": "HeterogeneousModel",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "tags": {
      "type": "object",
      "properties": {
        "a": {
          "type": "number"
        }
      },
      "additionalProperties": {
        "type": "number"
      }
    }
  }
}
deep_type(md2) = HeterogeneousModel{id: int, name: str, tags: dict[str, bool]}
json_objs_schema([md1, md2]) = {
  "id": {
    "type": "integer"
  },
  "name": {
    "type": "string"
  },
  "tags": {
    "type": "object",
    "properties": {
      "a": {
        "oneOf": [
          {
            "type": "boolean"
          },
          {
            "type": "number"
          }
        ]
      },
      "b": {
        "type": "boolean"
      }
    },
    "additionalProperties": {
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        }
      ]
    }
  }
}
deep_type(md3) = HeterogeneousModel{id: int, name: str, tags: dict[str, int]}
json_objs_schema([md1, md2, md3]) = {
  "id": {
    "type": "integer"
  },
  "name": {
    "type": "string"
  },
  "tags": {
    "type": "object",
    "properties": {
      "a": {
        "oneOf": [
          {
            "type": "boolean"
          },
          {
            "type": "number"
          }
        ]
      },
      "b": {
        "type": "boolean"
      }
    },
    "additionalProperties": {
      "oneOf": [
        {
          "type": "boolean"
        },
        {
          "type": "number"
        }
      ]
    }
  }
}
"""

