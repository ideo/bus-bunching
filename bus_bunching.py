import os
import csv
import time
from pathlib import Path
from dotenv import load_dotenv

from cta_bus_tracker import BusTracker


load_dotenv()


__DATA_DIR__ = Path("data/")


def stream_data(routes):
    while(True):
        get_bus_locations(routes)
        time.sleep(2 * 60)


def get_bus_locations(routes):
    """
    Get the locations of all buses currently on a route. Write those to a CSV.
    """
    tracker = BusTracker()
    for route in routes:
        create_csv_if_new_route(tracker, route)
        buses = tracker.get_vehicles(routes=[route])
        for bus in buses:
            write_csv_row(route, bus.values())


def create_csv_if_new_route(tracker, route):
    filename = make_filename(route)
    if not os.path.exists(__DATA_DIR__ / filename):
        print(f"Making new file: {filename}")
        # tracker = BusTracker()
        buses = tracker.get_vehicles(routes=[route])
        columns = buses[0].keys()
        write_csv_row(route, columns, first_row=True)


# def update_csv_file(route):
#     buses = get_bus_locations(route)
#     for bus in buses:
#         write_csv_row(route, bus.values())


def write_csv_row(route, data, first_row=False):
    filename = make_filename(route)
    filepath = __DATA_DIR__ / filename
    mode = "w" if first_row else "a"
    with open(filepath, mode) as file:
        writer = csv.writer(file)
        writer.writerow(data)


# def record_data(route):
#     create_csv(route)
#     while(True):
#         update_csv_file(route)
#         time.sleep(2*60)


def make_filename(route_designator):
    return Path(f"{route_designator}_bus.csv")



if __name__ == "__main__":
    routes = [66, 9, "X9"]
    stream_data(routes)

