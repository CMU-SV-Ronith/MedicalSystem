from enum import Enum

from status_codes.base_status_code import BaseStatusCode


class SuccessStatusCode(BaseStatusCode):
    PATIENT_RECORD_CREATION_SUCCESS = {"status_code": 1000, "status_message": "Successfully created patient record"}
    PATIENT_RECORD_UPDATE_SUCCESS = {"status_code": 1001, "status_message": "Successfully updated patient record"}
    PATIENT_RECORD_RETRIEVAL_SUCCESS = {"status_code": 1002,
                                        "status_message": "Successfully retrieved patient record(s)"}

    PRESCRIPTION_CREATION_SUCCESS = {"status_code": 1003, "status_message": "Successfully created prescription"}
    PRESCRIPTION_UPDATE_SUCCESS = {"status_code": 1004, "status_message": "Successfully updated prescription"}
    PRESCRIPTION_RETRIEVAL_SUCCESS = {"status_code": 1005, "status_message": "Successfully retrieved prescription(s)"}

    PATIENT_RECORD_EVENT_LOG_RETRIEVAL_SUCCESS = {"status_code": 1006,
                                                  "status_message": "Successfully retrieved patient record event log(s)"}

    PATIENT_CREATION_SUCCESS = {"status_code": 1007, "status_message": "Successfully created patient data"}
    PATIENT_UPDATE_SUCCESS = {"status_code": 1008, "status_message": "Successfully updated patient data"}
    RETRIEVED_PATIENT_DATA_SUCCESS = {"status_code": 1009, "status_message": "Successfully retrieved patient data"}
    PATIENT_ADDRESS_RETRIEVAL_SUCCESS = {"status_code": 1010, "status_message": "Patient address retrieval success"}

    DOCTOR_CREATION_SUCCESS = {"status_code": 1011, "status_message": "Successfully created doctor data"}
    DOCTOR_UPDATE_SUCCESS = {"status_code": 1012, "status_message": "Successfully updated doctor data"}
    RETRIEVED_DOCTOR_DATA_SUCCESS = {"status_code": 1013, "status_message": "Successfully retrieved doctor data"}

    DOCTOR_ADDRESS_RETRIEVAL_SUCCESS = {"status_code": 1014, "status_message": "Doctor address retrieval success"}
    DOCTOR_ADDRESS_UPDATE_SUCCESS = {"status_code": 1015, "status_message": "Doctor address update success"}

    DOCTOR_HOUR_CREATION_SUCCESS = {"status_code": 10016, "status_message": "Successfully created doctor hour"}
    DOCTOR_HOUR_UPDATE_SUCCESS = {"status_code": 1017, "status_message": "Successfully updated doctor hour"}
    DOCTOR_HOUR_RETRIEVAL_SUCCESS = {"status_code": 1018, "status_message": "Successfully retrieved doctor hour(s)"}
    DOCTOR_HOUR_DELETION_SUCCESS = {"status_code": 1019, "status_message": "Successfully deleted doctor hour"}

    DOCTOR_REVIEW_CREATION_SUCCESS = {"status_code": 1020, "status_message": "Successfully created doctor review"}
    DOCTOR_RATING_RETRIEVAL_SUCCESS = {"status_code": 1021, "status_message": "Successfully retrieved doctor rating"}
