import json


def write_json(dict):
    json_string = json.dumps(data)

    with open('hand_click_positions.json', 'w') as outfile:
        json.dump(json_string, outfile)

def load_json(json_file):
    with open('hand_click_positions.json') as json_file:
        data = json.load(json_file)
        json_dict = json.loads(data)
        return json_dict    