import ollama

SCHEMA = """
patients(
patient_id,
first_name,
last_name,
gender,
date_of_birth,
contact_number,
address,
registration_date,
insurance_provider,
insurance_number,
email
)

doctors(
doctor_id,
first_name,
last_name,
specialization,
phone_number,
years_experience,
hospital_branch,
email
)

appointments(
appointment_id,
patient_id,
doctor_id,
appointment_date,
appointment_time,
reason_for_visit,
status
)

treatments(
treatment_id,
appointment_id,
treatment_type,
description,
cost,
treatment_date
)

billing(
bill_id,
patient_id,
treatment_id,
bill_date,
amount,
payment_method,
payment_status
)
"""

def generate_sql(question):

    prompt = f"""
You are an expert SQLite SQL generator.

Database Schema:

{SCHEMA}

Rules:

1. Generate only SQLite SELECT statements.
2. Do not generate INSERT.
3. Do not generate UPDATE.
4. Do not generate DELETE.
5. Do not generate DROP.
6. Do not explain anything.
7. Return only SQL.

Question:

{question}
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"].strip()