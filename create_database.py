import sqlite3
import pandas as pd

conn = sqlite3.connect("hospital.db")

tables = {
    "patients": "patients.csv",
    "doctors": "doctors.csv",
    "appointments": "appointments.csv",
    "billing": "billing.csv",
    "treatments": "treatments.csv"
}

for table, file in tables.items():
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table} imported successfully.")

conn.close()

print("\nHospital Database Created Successfully!")