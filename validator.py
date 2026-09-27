def validate(sql):

    sql = sql.strip().upper()

    if not sql.startswith("SELECT"):
        return False

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "ALTER",
        "INSERT",
        "CREATE",
        "TRUNCATE"
    ]

    for word in blocked:

        if word in sql:
            return False

    return True