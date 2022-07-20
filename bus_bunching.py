import csv
import time
from dotenv import load_dotenv

from cta_bus_tracker import BusTracker


load_dotenv()


def chicago_ave():
    """The 66 bus!"""
    tracker = BusTracker()
    buses = tracker.get_vehicles(routes=[66])
    return buses


def create_csv():
    buses = chicago_ave()
    columns = buses[0].keys()
    write_csv_row(columns, first_row=True)


def update_csv_file():
    buses = chicago_ave()
    for bus in buses:
        write_csv_row(bus.values())


def write_csv_row(data, first_row=False):
    filename = "data/66_bus.csv"
    mode = "w" if first_row else "a"
    with open(filename, mode) as file:
        writer = csv.writer(file)
        writer.writerow(data)



if __name__ == "__main__":
    create_csv()
    while(True):
        update_csv_file()
        time.sleep(2*60)
