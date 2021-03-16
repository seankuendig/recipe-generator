import json


def update(config_param):
    with open('config.json') as json_file:
        data = json.load(json_file)
        print(data)
        config_already_written = False
        for config in data['configs']:
            if config_param['user_id'] == config['user_id']:
                config['email'] = config_param['email']
                config['diet'] = config_param['diet']
                config['exclude'] = config_param['exclude']
                config['target_calories'] = config_param['target_calories']
                config_already_written = True
        if not config_already_written:
            data['configs'].append(config_param)
        print(data)
        dump_data(data)


def dump_data(data):
    with open('config.json', 'w') as json_file:
        json.dump(data, json_file)


def get_all_users():
    with open('config.json') as json_file:
        data = json.load(json_file)
        if data['configs']:
            return data['configs']
