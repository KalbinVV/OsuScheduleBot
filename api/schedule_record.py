from dataclasses import dataclass


@dataclass
class ScheduleRecord:
    class_id: int
    class_name: str
    class_room: str
    class_type: str
    teacher_name: str


def parse_as_schedule_records_dict(encoded_dict: dict) -> dict[str, list[ScheduleRecord]]:
    decoded_dict: dict[str, list[ScheduleRecord]] = dict()

    for date, obj in encoded_dict.items():
        decoded_dict[date] = parse_as_schedule_records_list(obj)

    return decoded_dict


def parse_as_schedule_records_list(encoded_list: list) -> list[ScheduleRecord]:
    decoded_list: list[ScheduleRecord] = list()

    for obj in encoded_list:
        decoded_list.append(ScheduleRecord(obj['class_id'],
                                           obj['class_name'],
                                           obj['class_room'],
                                           obj['class_type'],
                                           obj['teacher_name']))

    return decoded_list
