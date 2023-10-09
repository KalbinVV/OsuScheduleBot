from python:3.11.6-alpine

copy ./ $HOME/app/

WORKDIR $HOME/app/

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "start-bot.sh"]