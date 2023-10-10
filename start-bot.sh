#!/bin/bash

alembic revision --autogenerate -m "initial"
alembic upgrade head
python ./main.py