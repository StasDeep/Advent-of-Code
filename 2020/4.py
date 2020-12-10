import re

from utils import read


def create_number_validation(start, end):
    def validate(val):
        if re.match(r"^\d+$", val):
            if start <= int(val) <= end:
                return True

        return False

    return validate


def create_regex_validation(regex):
    def validate(val):
        if re.match(regex, val):
            return True
        return False

    return validate


def validate_height(val):
    if re.match(r"^\d+cm$", val):
        return create_number_validation(150, 193)(val[:-2])
    elif re.match(r"^\d+in$", val):
        return create_number_validation(59, 76)(val[:-2])
    return False


def main():
    lines = read("4_1.txt")
    passports = "\n".join(lines).split("\n\n")

    fields_meta = {
        "byr": {"validator": create_number_validation(1920, 2002)},
        "iyr": {"validator": create_number_validation(2010, 2020)},
        "eyr": {"validator": create_number_validation(2020, 2030)},
        "hgt": {"validator": validate_height},
        "hcl": {"validator": create_regex_validation(r"^#[\da-f]{6}$")},
        "ecl": {"validator": create_regex_validation(r"^(amb|blu|brn|gry|grn|hzl|oth)$")},
        "pid": {"validator": create_regex_validation(r"^\d{9}$")},
    }

    c = 0
    for passport in passports:
        fields = [x.split(":")[0] for x in passport.split()]
        if all(f in fields for f in fields_meta):
            c += 1

    print(c)

    c = 0
    for passport in passports:
        values = dict([x.split(":") for x in passport.split()])
        if all(f in values and fields_meta[f]["validator"](values[f]) for f in fields_meta):
            c += 1

    print(c)


if __name__ == '__main__':
    main()
