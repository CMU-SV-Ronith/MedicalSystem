from status_codes.base_status_code import BaseStatusCode


class ErrorStatusCode(BaseStatusCode):
    PATIENT_RECORD_CREATION_FAILED = {"status_code": 4010, "status_message": "patient record creation failed"}
    PATIENT_RECORD_UPDATE_FAILED = {"status_code": 4011, "status_message": "patient record data update failed"}
    PATIENT_RECORD_DATA_RETRIEVAL_FAILED = {"status_code": 4012,
                                            "status_message": "Patient record data retrieval failed"}

    PRESCRIPTION_CREATION_FAILED = {"status_code": 4013, "status_message": "prescription creation failed"}
    PRESCRIPTION_UPDATE_FAILED = {"status_code": 4014, "status_message": "prescription update failed"}
    PRESCRIPTION_DATA_RETRIEVAL_FAILED = {"status_code": 4014, "status_message": "prescription retrieval failed"}

    PATIENT_RECORD_EVENT_LOG_RETRIEVAL_FAILED = {"status_code": 4015,
                                                 "status_message": "patient record event log(s) retrieval failed"}

    DOCTOR_CREATION_FAILED = {"status_code": 4016, "status_message": "doctor creation failed"}
    DOCTOR_UPDATE_FAILED = {"status_code": 4017, "status_message": "doctor data update failed"}
    DOCTOR_DATA_RETRIEVAL_FAILED = {"status_code": 4018, "status_message": "Doctor data retrieval failed"}

    DOCTOR_ADDRESS_UPDATE_FAILED = {"status_code": 4019, "status_message": "Doctor address update failed"}
    DOCTOR_ADDRESS_RETRIEVAL_FAILED = {"status_code": 4020, "status_message": "Doctor address retrieval failed"}

    DOCTOR_HOUR_CREATION_FAILED = {"status_code": 4021, "status_message": "doctor hour creation failed"}
    DOCTOR_HOUR_UPDATE_FAILED = {"status_code": 4022, "status_message": "doctor hour update failed"}
    DOCTOR_HOUR_RETRIEVAL_FAILED = {"status_code": 4023, "status_message": "doctor hour(s) retrieval failed"}
    DOCTOR_HOUR_DELETION_FAILED = {"status_code": 4024, "status_message": "doctor hour deletion failed"}

    DOCTOR_REVIEW_CREATION_FAILED = {"status_code": 4025, "status_message": "doctor hour creation failed"}
    DOCTOR_RATING_RETRIEVAL_FAILED = {"status_code": 4025, "status_message": "doctor rating retrieval failed"}

    PATIENT_CREATION_FAILED = {"status_code": 4026, "status_message": "patient creation failed"}
    PATIENT_UPDATE_FAILED = {"status_code": 4027, "status_message": "patient data update failed"}
    PATIENT_DATA_RETRIEVAL_FAILED = {"status_code": 4028, "status_message": "Patient data retrieval failed"}
    PATIENT_ADDRESS_UPDATE_FAILED = {"status_code": 4029, "status_message": "Patient address update failed"}
    PATIENT_ADDRESS_RETRIEVAL_FAILED = {"status_code": 4030, "status_message": "Patient address retrieval failed"}

    SESSION_CREATE_FAILED = {"status_code": 4031, "status_message": "session creation failed"}
