from flask import Flask, render_template, jsonify
from database import load_jobs

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobs = load_jobs()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
