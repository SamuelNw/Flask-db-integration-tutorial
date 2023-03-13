from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM Jobs"))
    result_dicts = []
    for entry in result:
      result_dicts.append(entry._asdict())

  return result_dicts
