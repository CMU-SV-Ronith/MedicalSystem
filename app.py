from flask import Flask

from routes import patient_record_routes, prescription_routes, patient_record_event_log_routes, patient_routes, \
    patient_address_routes, doctor_routes, doctor_address_routes, doctor_hours_routes, doctor_review_routes

app = Flask(__name__)

app.register_blueprint(patient_record_routes.blueprint, url_prefix='/patientRecord')
app.register_blueprint(prescription_routes.blueprint, url_prefix='/prescription')
app.register_blueprint(patient_record_event_log_routes.blueprint, url_prefix='/patientRecordEventLog')

app.register_blueprint(patient_routes.blueprint, url_prefix='/patient')
app.register_blueprint(patient_address_routes.blueprint, url_prefix='/address')


app.register_blueprint(doctor_routes.blueprint, url_prefix='/doctor')
app.register_blueprint(doctor_address_routes.blueprint, url_prefix='/address')
app.register_blueprint(doctor_hours_routes.blueprint, url_prefix='/doctorHours')
app.register_blueprint(doctor_review_routes.blueprint, url_prefix='/review')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
