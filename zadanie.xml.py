import xml.etree.ElementTree as ET

cube_colors = {'red': 0, 'green': 0, 'blue': 0}


def parse_cube(elem, deep_level=1):
    if elem.findall('cube'):
        for i in elem.findall('cube'):
            parse_cube(i, deep_level + 1)
    cube_colors[elem.attrib['color']] += deep_level


tree = ET.ElementTree(ET.fromstring(input()))
root = tree.getroot()
parse_cube(root)
print(cube_colors['red'], cube_colors['green'], cube_colors['blue'])