# bilka
scraping textual data for corpus building

## Build & run locally with `venv`

First, have `python3` installed and working locally. A very easy way to achieve this is to use [Anaconda](https://www.anaconda.com/docs/getting-started/getting-started) or even [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main), they are free for personal use.

* `$ python3 -m venv venv` creates a `venv` subdirectory (it is excluded by `.gitignore`)
* `$ source venv/bin/activate` will make `pip3` perform all installations in the virtual environment in `venv`
* `$ python3 setup.py install` installs this script and all its dependencies (once there are any)
* Then run with `$ vtc --help` to verify it works.
