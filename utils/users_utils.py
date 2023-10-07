from typing import Type

from sqlalchemy.orm import Session

import db


def user_exists(user_id: int) -> bool:
    session = Session(bind=db.engine)

    query = session.query(db.User).filter(db.User.id == user_id)

    if not query.scalar():  # Если запись не существует
        session.close()
        return False

    user: type[db.User] = query.one()

    if user.department_id is None or user.stream_id is None or user.group_id is None:
        session.close()
        return False

    session.close()
    return True


def get_user(user_id: int) -> db.User:
    session = Session(bind=db.engine)

    user_record: Type[db.User] = session.query(db.User).filter(db.User.id == user_id).one()

    user = db.User(id=user_record.id,
                   department_id=user_record.department_id,
                   stream_id=user_record.stream_id,
                   group_id=user_record.group_id)

    session.close()

    return user
