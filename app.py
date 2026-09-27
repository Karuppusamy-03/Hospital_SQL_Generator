from flask import Flask, render_template, request
from database import get_connection
from prompt import generate_sql
from validator import validate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    sql = ""
    results = []
    error = ""

    if request.method == "POST":

        question = request.form["question"]

        print(f"\nQuestion: {question}")

        try:
            sql = generate_sql(question)

            print(f"Generated SQL: {sql}")

            if sql and validate(sql):

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(sql)

                results = cursor.fetchall()

                conn.close()

            else:
                error = "Generated SQL is not valid."

        except Exception as e:
            error = str(e)
            print("Error:", e)

    return render_template(
        "index.html",
        sql=sql,
        results=results,
        error=error
    )

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)