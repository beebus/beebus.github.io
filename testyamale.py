"""Import the yamale library and make a schema object. Create a Data object. Validate data against the schema. Throws a ValueError if data is invalid."""
import yamale
def testyamle():
    schema = yamale.make_schema('./schema.yaml')
    data = yamale.make_data('./_pages/')
    for datum in data:
        yamale.validate(schema, datum)
