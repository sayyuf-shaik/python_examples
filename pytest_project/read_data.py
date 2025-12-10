import json

import pytest


@pytest.skip
def test_read_pass_students():
    with open("records.json") as fp:
        data = json.load(fp)
    for key, value in data.items():
        if value['result'] == "pass":
            print(key, value)


