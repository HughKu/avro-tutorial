import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc").read())

writer = DataFileWriter(open("users_instance.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Cathy", "favorite_color": "blue"})
writer.append({"name": "Alyssa", "favorite_number": 255, "favorite_color": "blue"})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users_instance.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()