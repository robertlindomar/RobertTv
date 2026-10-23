#!/usr/bin/env python3
"""Use the user-selected vector artwork; never regenerate its lettering."""
from copy import deepcopy
from pathlib import Path
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'branding'
SOURCE = BRAND / 'originals'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

for original, output in (
    ('Robert_TV_claro.svg', 'robert-tv.svg'),
    ('Robert_TV_claro.svg', 'robert-tv-transparent.svg'),
    ('Robert_TV_escuro.svg', 'robert-tv-dark.svg'),
    ('Robert_TV_simbolo.svg', 'robert-tv-mark.svg'),
):
    shutil.copyfile(SOURCE / original, BRAND / output)

for original, output in (
    ('Robert_TV_claro.svg', 'robert-tv-light.svg'),
    ('Robert_TV_escuro.svg', 'robert-tv-dark.svg'),
):
    shutil.copyfile(SOURCE / original, ROOT / 'web/icons' / output)

# Rearrange the supplied paths for the square launcher without stretching
# the horizontal artwork or replacing the user's symbol and typography.
source = ET.parse(SOURCE / 'Robert_TV_escuro.svg').getroot()
square = ET.Element(f'{{{NS}}}svg', {
    'width': '512', 'height': '512', 'viewBox': '0 0 512 512',
})
ET.SubElement(square, f'{{{NS}}}title').text = 'Robert Tv'
square.append(deepcopy(source.find(f'{{{NS}}}defs')))
ET.SubElement(square, f'{{{NS}}}rect', {
    'width': '512', 'height': '512', 'fill': '#141419',
})
for element_id, transform in (
    ('simbolo-robert-tv', 'translate(95 42) scale(.51)'),
    ('logotipo-tipografia', 'translate(69 440) scale(.036 -.036)'),
    ('televisao-tv', 'translate(339 440) scale(.036 -.036)'),
):
    element = deepcopy(source.find(f"{{{NS}}}g[@id='{element_id}']"))
    element.set('transform', transform)
    square.append(element)
ET.ElementTree(square).write(BRAND / 'robert-tv-square.svg', encoding='utf-8', xml_declaration=True)
subprocess.run(['rsvg-convert', '-w', '1024', '-h', '1024', str(BRAND / 'robert-tv-square.svg'),
                '-o', str(ROOT / 'tizen/robert-tv.png')], check=True)
print('Logo escolhida importada; versões clara, escura e ícone quadrado gerados.')
