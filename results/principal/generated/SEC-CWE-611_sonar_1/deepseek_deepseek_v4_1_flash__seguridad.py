from lxml import etree

def get_root():
    parser = etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
        dtd_validation=False,
        huge_tree=False,
        recover=False,
    )
    tree = etree.parse('resources/config.xml', parser)
    return tree.getroot()
