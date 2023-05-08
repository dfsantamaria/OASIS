import rdflib.collection
from rdflib import *


def __init__():
    # IRI
    oasis_iri = "https://raw.githubusercontent.com/dfsantamaria/OASIS/v2/OASIS-ontologies/oasis.owl"
    tbox_iri = "http://www.dmi.unict.it/oasis-tbox.owl"

    # Namespaces
    tbox = Namespace(tbox_iri+"#")
    oasis = Namespace("http://www.dmi.unict.it/oasis.owl"+"#")

    # Ontology
    ontology = Graph(base=tbox)
    ontology.namespace_manager.bind("base", tbox)
    ontology.namespace_manager.bind("oasis", oasis)

    ontology.add((URIRef(tbox), RDF.type, OWL.Ontology))

    # Classes
    actor = oasis.Actor
    #Restriction
    c = BNode()
    ontology.add((c, RDF.type, OWL.Class))
    rdflib.collection.Collection(ontology, c, [oasis.Behaviour, oasis.BehaviourThing])
    br1 = BNode()
    ontology.add((br1, RDF.type, OWL.Class))
    ontology.add((br1, OWL.intersectionOf, c))
    br = BNode()
    ontology.add((br, RDF.type, OWL.Restriction))
    ontology.add((br, OWL.onProperty, oasis.hasBehaviour))
    ontology.add((br, OWL.someValuesFrom, br1))
    ontology.add((actor, OWL.equivalentClass, br))

    # ObjectProperties

    # Imports
    # Remember to add manually the import
    ontology.add((URIRef(tbox), OWL.imports, URIRef(oasis_iri)))
    # ontology.add((URIRef(god_iri), OWL.imports, URIRef(geo_iri)))

    # Save
    file = open("oasis-tbox.owl", "w")
    file.write(ontology.serialize(format='pretty-xml'))


# end __init__

if __name__ == '__main__':
    __init__()
