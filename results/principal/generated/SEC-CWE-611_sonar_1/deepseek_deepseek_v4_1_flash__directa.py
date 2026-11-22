def get_root():
    parser = etree.XMLParser()
    tree = etree.parse('resources/config.xml', parser)
    return tree.getroot()
