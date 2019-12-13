import csv
import argparse


class Graph:
    """
    Handles generating graph in dict format by parsing the routes in CSV file
    """

    def __init__(self, routes_file):
        self.routes_file = routes_file

    def generate_graph_from_csv(self):
        """
        Read CSV File, parse and return the graph in python dictionary
        """
        path_dict = {}
        with open(self.routes_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if row[0] in path_dict:
                    path_dict[row[0]].append((row[1], row[2]))
                else:
                    path_dict[row[0]] = [
                        (row[1], row[2])
                    ]
                line_count += 1
        return path_dict


class PathFinder:
    """
    This class handles finding the path and framing the result
    """

    def find_shortest_path(self, path_dict, start, end, path=[]):
        """
        Method to find the shortest path for the given start and end points
        :param path_dict: Graph in python dict format
        :param start: Starting point
        :param end: Destination path
        :param path: Gets updated recursively
        :return: Path, Number of movements and Duration
        """
        shortest = None
        stops = 0
        duration = 0
        path = path + [start]
        if start == end:
            return path, stops, duration
        if not path_dict.__contains__(start):
            return None, stops, duration
        for node in path_dict[start]:
            if node[0] not in path:
                newpath, new_stops, new_duration = self.find_shortest_path(
                    path_dict, node[0], end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        stops = int(new_stops) + 1
                        shortest = newpath
                        duration = int(new_duration) + int(node[1])
        return shortest, stops, duration

    def get_result(self, path, start, end, stops, duration):
        """
        To frame the result based on inputs
        :param path: Path to reach destination from starting point
        :param start: Starting point
        :param end: Destination path
        :param stops: Number of stops
        :param duration: Time takes
        :return: Result
        """
        if not path:
            return "No routes from {0} to {1}".format(start, end)
        return "Your trip from {0} to {1} includes {2} stops and will take {3} minutes".format(
            start, end, stops, duration
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Enter file name')
    args = parser.parse_args()
    graph_instance = Graph(args.file)
    path_graph = graph_instance.generate_graph_from_csv()
    start = input('What station are you getting on the train?:')
    end = input('What station are you getting off the train?:')
    path_finder_instance = PathFinder()
    path, stops, duration = path_finder_instance.find_shortest_path(
        path_graph, start, end)
    result = path_finder_instance.get_result(
        path, start, end, stops-1, duration)
    print(result)
