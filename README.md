[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/viant/drone-gcloud/blob/master/LICENSE)

Script to remove `null` character from an audiofile

## Requirements

* Python3
* Mutagen https://github.com/quodlibet/mutagen


## Usage

```bash
usage: strip_null.py [-h] [-v] file

positional arguments:
  file           path to file

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase verbosity
```

## Example

```bash
find ./ -name "*.flac" | while read f; do ~/bin/strip_null.py -v "$f"; done
```
