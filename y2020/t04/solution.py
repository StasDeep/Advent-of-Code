import re

from utils import read, p1, p2


def main():
    passports = [Passport(p) for p in "\n".join(read()).split("\n\n")]

    check1 = RequiredFieldsCheck()
    p1(sum(check1.is_valid(p) for p in passports))

    check2 = FieldFormatCheck()
    p2(sum(check2.is_valid(p) for p in passports))


class Passport:

    def __init__(self, passport_str):
        self.fields = dict(x.split(':') for x in passport_str.split())


class RequiredFieldsCheck:

    def __init__(self):
        self.required_fields = ["byr", "iyr", "eyr", "hcl", "ecl", "pid", "hgt"]

    def is_valid(self, passport: Passport):
        return all(f in passport.fields for f in self.required_fields)


class FieldFormatCheck:

    def __init__(self):
        self.validators = {
            "byr": NumRangeValidator(1920, 2002),
            "iyr": NumRangeValidator(2010, 2020),
            "eyr": NumRangeValidator(2020, 2030),
            "hcl": RegexValidator(r"^#[\da-f]{6}$"),
            "ecl": RegexValidator(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
            "pid": RegexValidator(r"^\d{9}$"),
            "hgt": validate_height,
        }

    def is_valid(self, passport: Passport):
        return all(
            f in passport.fields and validator(passport.fields[f])
            for f, validator in self.validators.items()
        )


class NumRangeValidator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __call__(self, val):
        if re.match(r'^\d+$', val):
            if self.start <= int(val) <= self.end:
                return True

        return False


class RegexValidator:

    def __init__(self, regex):
        self.regex = regex

    def __call__(self, val):
        return bool(re.match(self.regex, val))


def validate_height(val):
    if re.match(r'^\d+cm$', val):
        return NumRangeValidator(150, 193)(val[:-2])
    elif re.match(r'^\d+in$', val):
        return NumRangeValidator(59, 76)(val[:-2])
    return False
