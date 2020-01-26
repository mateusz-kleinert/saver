#!/usr/bin/env python3

import os
import sys
import pycountry


USAGE_MSG = """
This script generates the following Enum classes:
    * Countries
    * Currencies

Example usage:

generate_enums.py saver/enums/enums.py
"""


def generate_enums(_path: str) -> None:
    with open(_path, "w") as f:
        f.write("#!/usr/bin/env python3\n\n")
        f.write("from enum import Enum\n\n\n")
        f.write("class Countries(Enum):\n")

        for country in pycountry.countries:
            f.write(f'    {country.alpha_2} = "{country.name}"\n')

        f.write("\n\nclass Currencies(Enum):\n")

        for currency in pycountry.currencies:
            f.write(f'    {currency.alpha_3} = "{currency.name}"\n')


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] == "help":
        print("Invalid number of arguments!")
        print(USAGE_MSG)
        sys.exit(1)

    _path = sys.argv[1]

    if not os.path.isdir(os.path.dirname(_path)):
        print(f"Provided directory doesn't exist: {os.path.dirname(_path)}")
        sys.exit(1)

    generate_enums(_path)
