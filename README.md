# Ultra Chronic

[![PyPI version](https://badge.fury.io/py/ultrachronic.svg)](https://badge.fury.io/py/ultrachronic)
[![Build Status](https://travis-ci.org/yoavram/ultrachronic.svg?branch=master)](https://travis-ci.org/yoavram/ultrachronic)
[![codecov](https://codecov.io/gh/yoavram/ultrachronic/branch/master/graph/badge.svg)](https://codecov.io/gh/yoavram/ultrachronic)

Run parallel jobs and save results to json.gz files.

## Install

Stable:

```sh
pip install ultrachronic
```

Latest:

```sh
pip install git+https://github.com/yoavram/ultrachronic.git
```

Supports Python 3.4 and 3.5.

## Test

Requirements:

```sh
pip install nose click
```

Run:

```sh
nosetests tests
```

## Example

Code in `do_something.py`:

```py
from ultrachronic import jsonify_result, repeat

import click

@jsonify_result
def do_something(arg1, arg2):
	a = 1
	b = 2
	# must return a dict!
	return dict(a=a, b=b)

@click.command()
@click.option('--arg1', default=1, type=int, help='Argument 1')
@click.option('--arg2', default='a', type=str, help='Argument 2')
@click.option('--reps', default=1, type=click.IntRange(1, None), help='Number of repetitions')
@click.option('--cpus', default=1, type=int, help='Number of CPUs to use (<1 for all available)')
def main(arg1, arg2, reps, cpus):
	repeat(do_something, reps, cpus, arg1=arg1, arg2=arg2)

if __name__ == '__main__':
	main()
```

Usage:

```sh
python do_something.py
python do_something.py --reps 10 --cpus 2
python do_something.py --arg1 5 --reps 10 --cpus 1
python do_something.py --arg2 hi --reps 10 --cpus 0
```

## Authors

- Yoav Ram (@yoavram)
