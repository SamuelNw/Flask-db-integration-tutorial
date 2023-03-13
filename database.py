from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


# load all jobs
def load_jobs():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM Jobs"))
    result_dicts = []
    for entry in result:
      result_dicts.append(entry._asdict())

  return result_dicts


# load specific job
def load_job(id):
  with engine.connect() as connection:
    if id == "1":
      result = connection.execute(text("SELECT * FROM Jobs WHERE id = 1"))
    elif id == "2":
      result = connection.execute(text("SELECT * FROM Jobs WHERE id = 2"))
    elif id == "3":
      result = connection.execute(text("SELECT * FROM Jobs WHERE id = 3"))
    else:
      return None

    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


print(load_job(3))
