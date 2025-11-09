from rdflib import Graph

def run_sparql(graph: Graph, query: str):
    """Jalankan SPARQL query pada graph RDF."""
    return list(graph.query(query))
