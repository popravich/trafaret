from bson import ObjectId
from bson.errors import InvalidId

from .. import Trafaret, str_types


class MongoId(Trafaret):
    """ Trafaret type check & convert bson.ObjectId values
    """

    convertable = str_types + (ObjectId,)
    value_type = ObjectId

    def __init__(self, allow_blank=False):
        self.allow_blank = allow_blank

    def __repr__(self):
        return "<MongoId(blank)>" if self.allow_blank else "<MongoId>"

    def converter(self, value):
        try:
            return self.value_type(value)
        except InvalidId as e:
            self._failure(e.message)

    def check_and_return(self, value):

        if value is None:
            self._failure('value not provided')
        elif isinstance(value, self.convertable):
            return value
        elif len(value) is 0 and self.allow_blank:
            return value
        else:
            self._failure('value is not %s' % self.value_type.__name__)