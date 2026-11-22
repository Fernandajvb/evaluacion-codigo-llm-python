import os

from lxml import etree

CONFIG_FILE = 'resources/config.xml'


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    if not os.path.isfile(CONFIG_FILE):
        raise FileNotFoundError('Configuration file not found: ' + CONFIG_FILE)

    parser = etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
        dtd_validation=False,
        huge_tree=False,
        recover=False,
    )

    with open(CONFIG_FILE, 'rb') as config_file:
        tree = etree.parse(config_file, parser)

    root = tree.getroot()

    if root is None:
        raise ValueError('The XML document does not contain a root element.')

    return root
