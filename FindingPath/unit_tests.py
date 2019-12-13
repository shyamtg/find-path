import find_path
import unittest
import test_inputs


def test_run(test_case):
    """
    Supporting method to run unit test against the source code
    :param test_case:  Test case id
    :return: Test case output
    """
    print("Running test - {}".format(test_case["NAME"]))
    path, stops, duration = find_path.PathFinder().find_shortest_path(
        test_inputs.PATH_GRAPH, test_case["INPUT"][0], test_case["INPUT"][1])
    print("Test completed - {}".format(test_case["NAME"]))
    return [stops-1, duration]


class FindPathTests(unittest.TestCase):
    """
    To trigger list of unit test cases
    """

    def test(self):
        self.assertEqual(
            test_run(test_inputs.TEST_O1), test_inputs.TEST_O1["OUTPUT"],
            "Test failed - {}".format(test_inputs.TEST_O1["NAME"]))
        self.assertEqual(
            test_run(test_inputs.TEST_O2), test_inputs.TEST_O2["OUTPUT"],
            "Test failed - {}".format(test_inputs.TEST_O2["NAME"]))
        self.assertEqual(
            test_run(test_inputs.TEST_O3), test_inputs.TEST_O3["OUTPUT"],
            "Test failed - {}".format(test_inputs.TEST_O3["NAME"]))
        self.assertEqual(
            test_run(test_inputs.TEST_O4), test_inputs.TEST_O4["OUTPUT"],
            "Test failed - {}".format(test_inputs.TEST_O4["NAME"]))


if __name__ == '__main__':
    unittest.main()
