import unittest
from src import verify_json
from src import load_json_test as load_json
from jsonschema import ValidationError


class TestVerify(unittest.TestCase):
    def test_example(self):
        data = load_json("example")
        self.assertFalse(verify_json(data))

    def test_asterisks(self):
        tests = [
            ("asterisk_1", True),
            ("asterisk_2", False),
            ("asterisk_3", True),
            ("asterisk_4", True),
        ]
        for name, result in tests:
            data = load_json(name)
            self.assertEqual(result, verify_json(data))

    def test_empty_resource(self):
        data = load_json("empty_resource")
        self.assertTrue(verify_json(data))

    def test_two_asterisks(self):
        data = load_json("two_asterisks")
        self.assertTrue(verify_json(data))

    def test_wrong_datatype(self):
        data = load_json("wrong_datatype")
        with self.assertRaises(ValidationError):
            verify_json(data)

    def test_statemet_different(self):
        data = load_json("statement_different")
        with self.assertRaises(ValidationError):
            verify_json(data)


if __name__ == "__main__":
    unittest.main()
