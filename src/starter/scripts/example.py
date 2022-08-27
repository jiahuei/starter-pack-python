"""
A simple example script.

Usage:

```shell
$ python3 src/starter/scripts/example.py
```
"""
import argparse

import starter


def main(x_var: int, y_var: bool):
    print(f"version = {starter.__version__}")
    print(f"starter.utils.io.read_yaml.__doc__ = \n'''\n{starter.utils.io.read_yaml.__doc__}\n'''")
    print(f"x_var = {x_var}")
    print(f"y_var = {y_var}")


def main_cli():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--x_var",
        "-x",
        type=int,
        default=0,
        help=f"int: Something.",
    )
    parser.add_argument(
        "--y_var",
        "-y",
        action="store_true",
        help="bool: If specified (True), do something.",
    )
    args = parser.parse_args()
    main(**vars(args))


if __name__ == "__main__":
    main_cli()
