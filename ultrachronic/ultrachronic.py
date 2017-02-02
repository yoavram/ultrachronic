from datetime import datetime 
from uuid import uuid4
import gzip
import json
from functools import wraps
import warnings

try:
    import click
except ImportError:
    pass
else:
    print = click.echo


time_format = '%Y-%m-%d-%H-%M-%s'


def jsonify_result(f):
    @wraps(f)
    def wrapper(**kwargs):
        result = f(**kwargs)
        filename = '{}_{}.json.gz'.format(
            datetime.now().strftime(time_format),
            str(uuid4()).partition('-')[0]
        )
        print("Writing results to {}".format(filename))
        kwargs.update(result)
        kwargs['filename'] = filename
        with gzip.open(filename, 'wt') as output:
            json.dump(
                kwargs,
                output,
                sort_keys=True, indent=4, separators=(',', ': ')
            )
        return result
    return wrapper


def repeat(f, reps, cpus, **kwargs):
    if reps == 1:
        f(**kwargs)
        return
    fname = f.__name__
    print("Starting {} {} times with:".format(fname, reps))
    print(kwargs)
    if cpus == 1:
        for _ in range(reps):
            try:
                f(**kwargs)
            except Exception as e:
                warnings.warn(str(e))
    else:
        from multiprocessing import cpu_count
        from concurrent.futures import ProcessPoolExecutor, as_completed
        if cpus < 1:
            cpus = cpu_count()
        with ProcessPoolExecutor(cpus) as executor:
            futures = [executor.submit(f, **kwargs) for _ in range(reps)]
        for fut in as_completed(futures):
            if fut.exception():
                warnings.warn(str(fut.exception()))
    print("Finished")
