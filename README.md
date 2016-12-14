# Ultra Chronic

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
@click.option('--reps', default=1, type=int, help='Number of repetitions')
def main(arg1, arg2, reps):
	repeat(do_something, reps, arg1=arg1, arg2=arg2)

if __name__ == '__main__':
	main()
```

Usage:

```sh
python do_something.py
python do_something.py --reps 10
python do_something.py --arg1 5 --reps 10
python do_something.py --arg2 hi --reps 10
```

## Authors

- Yoav Ram (@yoavram)
