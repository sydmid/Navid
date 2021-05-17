from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta:
        # it only loads this field and wont dump it (for get for example for request)
        load_only = ('password',)
        # it only dumps this field and wont load it (we don't want it from the user)
        dump_only = ('id',)
    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
