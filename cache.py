from dijkstra import dijkstra
from MyTypes import Graph, NameMap, Cache


def add_to_cache(name: str, cache: Cache, graph: Graph, name_mapping: NameMap) -> None:
    terminal_id = name_mapping[name]
    distance, parent_map = dijkstra(graph, terminal_id)
    cache[terminal_id] = (distance, parent_map)