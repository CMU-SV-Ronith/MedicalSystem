import json
from datetime import datetime


class BaseClass:
    def __init__(self):
        self._id = None

    def to_dict(self):
        # return {k: v for k, v in self.__dict__.items() if v is not None and k != '_id'}
        # return {k: v for k, v in self.__dict__.items() if v is not None}
        # return {k: (v.to_dict() if hasattr(v, 'to_dict') else v) for k, v in self.__dict__.items() if v is not None}
        return {k: self._json_serialize(v) for k, v in self.__dict__.items() if v is not None}

    @classmethod
    def from_dict(cls, attributes_dict):
        return cls(**attributes_dict)

    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id

    def to_json(self):
        return json.dumps(self, default=self._json_serialize)

    def _json_serialize(self, obj):
        """
        Custom serialization for objects not serializable by default json code.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, list):
            # Process each item in the list
            return [self._json_serialize(item) for item in obj]
        elif hasattr(obj, 'to_dict'):
            # If the object has a to_dict method, use it
            return obj.to_dict()
        elif hasattr(obj, '__dict__'):
            # Serialize objects with a __dict__ attribute
            return {k: self._json_serialize(v) for k, v in obj.__dict__.items() if v is not None}
        else:
            # Fallback to string representation
            return str(obj)
