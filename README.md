# mexe

A python script to make your Python files executable.

## Installation

```
pip install mexe
```

## Usage

```shell
usage: mexe [-h] [-p VERSION] [-v] FILE [FILE ...]

positional arguments:
  FILE                  file to be made executable

optional arguments:
  -h, --help            show this help message and exit
  -p VERSION, --pyversion VERSION
                        python version (2 or 3)
  -v, --version         show version
```

If `-p` or `--pyversion` is not specified, then the system default `python`
is used instead.

## Tests

To run tests:

```bash
./test_mexe.py
```

## License

MIT