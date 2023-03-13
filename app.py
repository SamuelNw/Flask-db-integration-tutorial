from flask import Flask, render_template, jsonify, request
from database import load_jobs, load_job, store_applications

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  jobs = load_jobs()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs()
  return jsonify(jobs)


@app.route("/job/<id>")
def list_job(id):
  job = load_job(id)

  if not job:
    return "Not Found", 404

  return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["post"])
def apply_job(id):
  data = request.form
  job = load_job(id)

  #store data
  store_applications(id, data)
  return render_template("application_submitted.html",
                         application=data,
                         job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
