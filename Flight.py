from dataclasses import dataclass
from datetime import datetime

from MyTypes import Graph, NameMap, Cache
from dijkstra import dijkstra
# used when the start or end points are not found
from config import DEFAULT_DISTANCE


@dataclass
class Flight:
    def __init__(self, flight_id: int, date: datetime, flight_type: str, terminal_name: str, airline_code: str,
                 airline_number: int, airport_code: str, airport_name: str, aircraft_type: str, parking_number: str,
                 gate_number: str, passengers_count: int) -> None:
        self.id: int = flight_id
        self.date: datetime = date
        self.flight_type: str = flight_type
        self.terminal_name: str = terminal_name
        self.airline_code: str = airline_code
        self.airline_number: int = airline_number
        self.airport_code: str = airport_code
        self.airport_name: str = airport_name
        self.aircraft_type: str = aircraft_type
        self.parking_number: str = parking_number
        self.gate_number: str = gate_number
        self.passengers_count: int = passengers_count

    def __str__(self):
        return f"{self.airline_code}-{self.airline_number}"

    def __lt__(self, other: "Flight") -> bool:
        return self.date < other.date

    def __gt__(self, other: "Flight") -> bool:
        return self.date > other.date

    def get_distance(self, g: Graph, cache: Cache, mapping: NameMap) -> float:
        if self.flight_type == "A":
            start = mapping.get(self.gate_number, None)
            stop = mapping.get(self.parking_number, None)
        elif self.flight_type == "D":
            start = mapping.get(self.parking_number, None)
            stop = mapping.get(self.gate_number, None)
        else:
            raise ValueError(f"bad flight type: {self.flight_type}")

        if start is None or stop is None:
            return DEFAULT_DISTANCE

        return dijkstra(g, start, stop, cache)[stop]
