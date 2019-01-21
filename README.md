# hydrogen2drumkv1.py v.1.3
Hydrogen to drumkv1 mass conversion tool

This script converts drumkit files for [Hydrogen](http://www.hydrogen-music.org/) into presets that can be loaded by [drumkv1](https://drumkv1.sourceforge.io/).

Many thanks goes to TuriSc for writing the original version over at https://github.com/TuriSc/hydrogen2drumkv1.py

This refactor was inspired by a desire for a somewhat different work-flow. Basically, I wanted a script that would convert a directory of .h2drumkit files into a directory of corresponding files (samples and map) that could be used by drumkv1.

Many thanks goes to the following sites for making the kits available:

 - http://www.skyehaven.net/blog/linux-multimedia-sprint/downloads/hydrogen-drumkits-v2/
 - https://sourceforge.net/projects/hydrogen/files/Sound%20Libraries/Main%20sound%20libraries/
 - https://freewavesamples.com/hydrogen-drum-kits

All of the above kits (and more) can be obtained via http://mtf8.info/hydrogen-kits.tar.gz. This collection is slightly improved as directory names have been cleaned up (to be easier on the eyes) and file permissions have been fixed in order to avoid errors when clobbering (like when re-running this script).

So onto the work-flow...

git clone this repo like it's hot and run hydrogen2drumkv1.py as shown below:

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

## Contribute

I really don't python so feel free to PR if you can improve this script.

## Limitations
This tool can only processes uncompressed Hydrogen drumkits.  Since drumkv1 does not (yet?) support multi-layered samples, drumkits containing these are partially supported - only the last layer (usually the loudest) is included in the output.

Tested with drumkv1 version 0.9.4.
