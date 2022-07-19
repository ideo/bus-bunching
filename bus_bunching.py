from dotenv import load_dotenv

from cta_bus_tracker import BusTracker


load_dotenv()


if __name__ == "__main__":
    tracker = BusTracker()
    busses = tracker.get_vehicles(routes=[66])
    print(busses)