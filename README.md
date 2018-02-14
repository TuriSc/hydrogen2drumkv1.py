# hydrogen2drumkv1.py v.1.2
Hydrogen to drumkv1 drumkit conversion tool

This script converts drumkit files for [Hydrogen](http://www.hydrogen-music.org/) into presets that can be loaded by [drumkv1](https://drumkv1.sourceforge.io/).

## Usage
```bash
hydrogen2drumkv1.py [-h] [-p PREFIX] [-n NOTE] [-nv] infile outfile

positional arguments:
  infile                path to source xml
  outfile               path to output drumkv1

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        prefix to sample path
  -n NOTE, --note NOTE  starting midi note (default: 35)
  -nv, --nonverbose     nonverbose output

```

## Limitations
This tool can only processes uncompressed Hydrogen drumkits. So if your source is a compressed .h2drumkit file, make sure you extract its content first (it's a tarball).
Multi-layered drumkits are partially supported - only the last layer (usually the loudest) is included in the output.

Tested with drumkv1 version 0.8.6.
