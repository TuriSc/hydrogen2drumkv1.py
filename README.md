# hydrogen2drumkv1.py
Hydrogen to drumkv1 drumkit conversion tool

This script converts drumkit files for [Hydrogen](http://www.hydrogen-music.org/) into presets that can be loaded by [drumkv1](https://drumkv1.sourceforge.io/).

## Usage
```bash
python hydrogen2drumkv1.py /path/to/uncompressed_hydrogen_drumkit.xml /path/to/output.drumkv1
```
Since the paths to the audio samples are relative to the input drumkit.xml index file, make sure to export the output file to the same directory.

## Limitations
This tool can only processes uncompressed Hydrogen drumkits. So if your source is a compressed .h2drumkit file, make sure you extract its content first (it's a tarball).
Multi-layered drumkits are partially supported - only the first layer (usually the quietest) is included in the output.

Tested with drumkv1 version 0.8.6.

