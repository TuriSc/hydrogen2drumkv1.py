#!/usr/bin/env python3

# ## hydrogen2drumkv1.py - v.1.1 ##
# Convert Hydrogen 2 drumkits to drumkv1.
# Usage: hydrogen2drumkv1.py uncompressed_hydrogen_drumkit.xml output.drumkv1
# Homepage: https://github.com/TuriSc/hydrogen2drumkv1.py
# Author: Turi Scandurra

import os
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

# argument parsing
if len(sys.argv) != 3:
    #TODO
    sys.exit(
        'Usage: %s uncompressed_hydrogen_drumkit.xml '
        'output.drumkv1' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    #TODO
    sys.exit('ERROR: File %s not found' % sys.argv[1])


# helper functions
def scale(value, to_min, to_max, from_min, from_max):
    return (to_max-to_min)*(value-from_min)/(from_max-from_min) + to_min


def pretty_print(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            pretty_print(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# append the correct extension if missing
if sys.argv[2].find('.drumkv1') == -1:
    output_file = sys.argv[2] + '.drumkv1'
else:
    output_file = sys.argv[2]

# read source file
input_xml = ET.parse(sys.argv[1]).getroot()

# strip namespace if present
namespace = '{http://www.hydrogen-music.org/drumkit}'
nsl = len(namespace)
for elem in input_xml.getiterator():
    if elem.tag.startswith(namespace):
        elem.tag = elem.tag[nsl:]

# throw error on malformed xml
if 'drumkit_info' not in input_xml.tag:
    print('ERROR: File %s not a valid Hydrogen drumkit' % sys.argv[1])
    sys.exit(1)

inst_list = input_xml.find('instrumentList')
if inst_list is None:
    print('ERROR: File %s not a valid Hydrogen drumkit' % sys.argv[1])
    sys.exit(1)

preset_name = input_xml.findtext('name')
preset_author = input_xml.findtext('author')
preset_info = input_xml.findtext('info')
preset_license = input_xml.findtext('license')

if preset_name is None:
    preset_name = 'Untitled'
root = ET.Element('preset', name=preset_name)
root.append(ET.Comment('Converted with hydrogen2drumkv1.py'))
if preset_author is not None:
    root.append(ET.Comment('Hydrogen preset author: ' + preset_author))
if preset_info is not None:
    root.append(ET.Comment('Hydrogen preset info: ' + preset_info))
if preset_license is not None:
    root.append(ET.Comment('Hydrogen preset license: ' + preset_license))
elements = ET.SubElement(root, 'elements')

# main loop
index = 35
for instrument in inst_list.findall('instrument'):
    # reset variables
    sample_pitch = None
    # create element node
    element = ET.SubElement(elements, 'element', index=str(index))
    sample = ET.SubElement(element, 'sample', name='GEN1_SAMPLE', index='0')
    inst_filename = instrument.find('filename')
    if inst_filename is None:
        # check if instrument is multilayered
        layer = instrument.findall('layer')
        if layer:
            layer_filename = layer[len(layer)-1].find('filename')
            if layer_filename is not None:
                sample.text = layer_filename.text
                sample_pitch = layer[len(layer)-1].find('pitch')
    else:
        sample.text = inst_filename.text
    # param_0 GEN1_SAMPLE
    params = ET.SubElement(element, 'params')
    param_0 = ET.SubElement(params, 'param', name='GEN1_SAMPLE', index='0')
    param_0.text = str(index)
    # param_1 GEN1_REVERSE - not supported
    # param_2 GEN1_GROUP
    inst_group = instrument.find('muteGroup')
    if inst_group is not None:
        param_2 = ET.SubElement(params, 'param', name='GEN1_GROUP', index='2')
        # Hydrogen's default is 1, drumkv1's is 0
        _group = int(inst_group.text) + 1
        param_2.text = str(_group)
    # param_3 GEN1_COARSE
    if sample_pitch is not None:
        param_3 = ET.SubElement(params, 'param', name='GEN1_COARSE', index='3')
        _pitch = float(sample_pitch.text)
        param_3.text = str(scale(_pitch, -2, 2, -24, 24))
    # param_4 GEN1_FINE - not supported
    # param_5 GEN1_ENVTIME - not supported
    # param_6 DCF1_CUTOFF
    inst_cutoff = instrument.find('filterCutoff')
    if inst_cutoff is not None:
        param_6 = ET.SubElement(params, 'param', name='DCF1_CUTOFF', index='6')
        _cutoff = float(inst_cutoff.text)
        param_6.text = str(scale(_cutoff, 0, 100, 0, 1))
    # param_7 DCF1_RESO
    inst_resonance = instrument.find('filterResonance')
    if inst_resonance is not None:
        param_7 = ET.SubElement(params, 'param', name='DCF1_RESO', index='7')
        _resonance = float(inst_resonance.text)
        param_7.text = str(scale(_resonance, 0, 100, 0, 1))
    # param_8 DCF1_TYPE - not supported
    # param_9 DCF1_SLOPE - not supported
    # param_10 DCF1_ENVELOPE - not supported
    # param_11 DCF1_ATTACK - not supported
    # param_12 DCF1_DECAY1 - not supported
    # param_13 DCF1_LEVEL2 - not supported
    # param_14 DCF1_DECAY2 - not supported
    # param_15-29 LFO1_* - not supported
    # param_30 DCA1_VOLUME - not supported
    # param_31 DCA1_ATTACK
    inst_attack = instrument.find('Attack')
    if inst_attack is not None:
        param_31 = ET.SubElement(
            params, 'param', name='DCA1_ATTACK', index='31')
        _attack = float(inst_attack.text)
        param_31.text = str(scale(_attack, 0, 100, 0, 1))
    # param_32 DCA1_DECAY1 - no direct conversion possible, harcoded value
    inst_decay = instrument.find('Decay')
    param_32 = ET.SubElement(params, 'param', name='DCA1_DECAY1', index='32')
    param_32.text = '100'
    # param_33 DCA1_LEVEL2 - no direct conversion possible, harcoded value
    param_33 = ET.SubElement(params, 'param', name='DCA1_LEVEL2', index='33')
    param_33.text = '100'
    # param_34 DCA1_DECAY2 - no direct conversion possible, harcoded value
    param_34 = ET.SubElement(params, 'param', name='DCA1_DECAY2', index='34')
    param_34.text = '100'
    # param_35 OUT1_WIDTH - not supported
    # param_36 OUT1_PANNING
    inst_pan_l = instrument.find('pan_L')
    inst_pan_r = instrument.find('pan_R')
    if inst_pan_l is not None and inst_pan_r is not None:
        param_36 = ET.SubElement(
            params, 'param', name='OUT1_PANNING', index='36')
        _pan = float(inst_pan_l.text) * -1 + float(inst_pan_r.text)
        param_36.text = str(_pan)
    # param_37 OUT1_FXSEND - not supported
    # param_38 OUT1_VOLUME
    inst_volume = instrument.find('volume')
    if inst_volume is not None:
        param_38 = ET.SubElement(
            params, 'param', name='OUT1_VOLUME', index='38')
        _volume = float(inst_volume.text)
        param_38.text = str(scale(_volume, 0, 1, 0, 2))

    # increment loop index
    index += 1

# preset-wide parameters
# param_39-41, 43-69 - not supported
# param_42 DEF1_VELOCITY - hardcoded value
preset_params = ET.SubElement(root, 'params')
param_42 = ET.SubElement(
    preset_params, 'param', name='DEF1_VELOCITY', index='42')
param_42.text = '1'

# add newlines and indentation
pretty_print(root)

# write file
try:
    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE drumkv1>')
        f.write(ET.tostring(root).decode("utf-8"))
except IOError, e:
    print 'ERROR:', e[0], e[1]
    sys.exit(1)
