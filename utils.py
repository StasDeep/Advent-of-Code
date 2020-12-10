import inspect
from pathlib import Path


def read():
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])

    with Path(mod.__file__).with_suffix(".txt").open() as fh:
        return [line.strip() for line in fh.readlines() if line]
