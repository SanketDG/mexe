# mexe

Convert any python script to an executable.

## Installation

```
pip install mexe
```

## Usage

```shell
usage: mexe [-h] [-p VERSION] [-v] [-r] FILE [FILE ...]

positional arguments:
  FILE                  file to be made executable

optional arguments:
  -h, --help            show this help message and exit
  -p VERSION, --python VERSION
                        python version (2 or 3)
  -v, --version         show version
  -r, --recursive       recursively iterate the directories
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