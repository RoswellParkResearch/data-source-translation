import pandas as pds
from rdflib import Graph, BNode, RDF, RDFS, OWL, Namespace, BNode, URIRef, Literal, XSD
from rdflib.namespace import NamespaceManager
from pprint import pprint


def make_iri_map_fn(iri_map):
    def fn(key):
        if key in iri_map:
            return URIRef(iri_map[key])
        else:
            return None
    return fn

if __name__ == "__main__":
    iri_map =\
        {
            'base': 'http://ex.com/',
            'entity_base': 'http://ex.com/entity/',
            'record': 'http://ex.com/dp_record',
            'field': 'http://ex.com/dp_field',
            'value': 'http://ex.com/dp_value'
         }
    miri = make_iri_map_fn(iri_map)
    # print(miri('record'))
    df = pds.read_excel('patients_1_eav.xlsx')

    g = Graph()
    for r in df.itertuples():
        # print(r.record)
        if "record_1" == str(r.record):
            b = BNode()        # create record as blank node
            g.add((b, miri('record'), Literal(r.record)))
            g.add((b, miri('field'), Literal(r.field)))
            g.add((b, miri('value'), Literal(r.value)))

    pprint(g.serialize(format='turtle'))


