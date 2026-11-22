from lxml import etree
from pathlib import Path

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    config_path = Path("resources/config.xml")

    if not config_path.exists():
        raise FileNotFoundError("Configuration file not found: resources/config.xml")

    if not config_path.is_file():
        raise IsADirectoryError("Configuration path is not a file: resources/config.xml")

    parser = etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        dtd_validation=False,
        load_dtd=False,
        huge_tree=False,
    )

    with config_path.open("rb") as xml_file:
        tree = etree.parse(xml_file, parser)

    return tree.getroot()
