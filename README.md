# hydrogen2drumkv1.py v.1.3
Hydrogen to drumkv1 mass conversion tool

This script converts drumkit files for [Hydrogen](http://www.hydrogen-music.org/) into presets that can be loaded by [drumkv1](https://drumkv1.sourceforge.io/).

## Usage
```bash
hydrogen2drumkv1.py [-h] [-n NOTE] [-nv] source_dir dest_dir

positional arguments:
  source_dir          directory containing .h2drumkit files
  dest_dir            path to store resulting drumkv1 kits

optional arguments:
  -h, --help            show this help message and exit
  -n NOTE, --note NOTE  starting midi note (default: 35)
  -nv, --nonverbose     nonverbose output

```

If everything works, dest_dir (passed into the script) will now be populated with drumkv1 drumkits. Simply navigate these directories from drumkv1 and load the .drumkv1 file.


## Limitations
This tool can only processes uncompressed Hydrogen drumkits.  Since drumkv1 does not support multi-layered samples, drumkits containing these are partially supported - only the last layer (usually the loudest) is included in the output.

Tested with drumkv1 version 0.9.4.
