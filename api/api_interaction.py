import json

import requests

import config


def get_departments_dict() -> dict[str, int]:
    request = requests.get(f'{config.API_URL}/departments_dict')

    departments_dict: dict[str, int] = json.loads(request.text)

    return departments_dict


def get_streams_dict(department_id: int) -> dict[str, int]:
    request = requests.get(f'{config.API_URL}/departments_streams_dict',
                           params={'department_id': department_id})

    streams_dict: dict[str, int] = json.loads(request.text)

    return streams_dict


def get_groups_dict(department_id: int, stream_id: int) -> dict[str, int]:
    request = requests.get(f'{config.API_URL}/groups_dict',
                           params={'department_id': department_id,
                                   'stream_id': stream_id})

    groups_dict: dict[str, int] = json.loads(request.text)

    return groups_dict

