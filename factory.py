from validator import (
    FilenameValidator,
    HeaderValidator,
    DuplicateBatchValidator,
    ReadingValidator
)

class ValidatorFactory:
    @staticmethod
    def get_validator(validator_type):
        if validator_type == "filename":
            return FilenameValidator()
        elif validator_type == "header":
            return HeaderValidator()
        elif validator_type == "duplicate":
            return DuplicateBatchValidator()
        elif validator_type == "readings":
            return ReadingValidator()
        else:
            raise ValueError("Unknown validator type")
factory = ValidatorFactory()

v1 = factory.get_validator("filename")
print(v1.validate("MED_DATA_20240101120000.csv"))

v2 = factory.get_validator("readings")
print(v2.validate(["1.2"] * 10))
