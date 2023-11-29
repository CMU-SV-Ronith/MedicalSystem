from flask import Flask
from flask_jwt_extended import JWTManager

from routes import patient_record_routes, prescription_routes, patient_record_event_log_routes, patient_routes, \
    patient_address_routes, doctor_routes, doctor_address_routes, doctor_hours_routes, doctor_review_routes, \
    session_routes

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

app.register_blueprint(patient_record_routes.blueprint, url_prefix='/patientRecord')
app.register_blueprint(prescription_routes.blueprint, url_prefix='/prescription')
app.register_blueprint(patient_record_event_log_routes.blueprint, url_prefix='/patientRecordEventLog')

app.register_blueprint(patient_routes.blueprint, url_prefix='/patient')
app.register_blueprint(patient_address_routes.blueprint, url_prefix='/address')

app.register_blueprint(doctor_routes.blueprint, url_prefix='/doctor')
app.register_blueprint(doctor_address_routes.blueprint, url_prefix='/address')
app.register_blueprint(doctor_hours_routes.blueprint, url_prefix='/doctorHours')
app.register_blueprint(doctor_review_routes.blueprint, url_prefix='/review')

app.register_blueprint(session_routes.blueprint, url_prefix='/session')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
