from pymodm import connect, MongoModel, fields

connect("mongodb+srv://lamelnyk:OstWQaHToQsUO1eK@bme547-lam.3ec0x.mongodb.net/hrdatabase?retryWrites=true&w=majority")


class User(MongoModel):
    name = fields.CharField()


x = User(name="Laryssa")
x.save()
