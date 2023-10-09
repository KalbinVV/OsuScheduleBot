import json

import requests

import config
from api.schedule_record import ScheduleRecord, parse_as_schedule_records_list, parse_as_schedule_records_dict


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


def get_today_schedule(group_id: int) -> list[ScheduleRecord]:
    request = requests.get(f'{config.API_URL}/schedule_today',
                           params={'group_id': group_id})

    encoded_list = json.loads(request.json())

    schedule_list = parse_as_schedule_records_list(encoded_list)

    return schedule_list


def get_tomorrow_schedule(group_id: int) -> list[ScheduleRecord]:
    request = requests.get(f'{config.API_URL}/schedule_tomorrow',
                           params={'group_id': group_id})

    encoded_list = json.loads(request.json())

    schedule_list = parse_as_schedule_records_list(encoded_list)

    return schedule_list


def get_week_schedule(group_id: int) -> dict[str, list[ScheduleRecord]]:
    request = requests.get(f'{config.API_URL}/schedule_week',
                           params={'group_id': group_id})

    encoded_dict = json.loads(request.json())

    schedule_dict = parse_as_schedule_records_dict(encoded_dict)

    return schedule_dict
