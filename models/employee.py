from marshmallow import Schema, fields

class Employee(Schema):
    Name = fields.Str()
    Id   = fields.Str()