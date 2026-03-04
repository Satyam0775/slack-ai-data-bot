MAX_PREVIEW = 10


def format_results(rows: list, columns: list, sql: str) -> str:
    if not rows:
        return "*No rows returned.*\n```{}```".format(sql)

    preview = rows[:MAX_PREVIEW]
    total_rows = len(rows)

    widths = {col: len(col) for col in columns}

    # calculate correct column widths
    for row in preview:
        for col in columns:
            value = row.get(col, "")

            if isinstance(value, float):
                value = f"{value:.2f}"

            widths[col] = max(widths[col], len(str(value)))

    # format rows
    def fmt(data):
        formatted = []
        for col in columns:
            value = data.get(col, "")

            if isinstance(value, float):
                value = f"{value:.2f}"

            formatted.append(str(value).ljust(widths[col]))

        return "  ".join(formatted)

    header = "  ".join(col.ljust(widths[col]) for col in columns)
    separator = "  ".join("-" * widths[col] for col in columns)
    body = "\n".join(fmt(row) for row in preview)

    table = "\n".join([header, separator, body])

    note = (
        "_(showing {} of {} rows)_".format(MAX_PREVIEW, total_rows)
        if total_rows > MAX_PREVIEW
        else "_{} row(s) returned_".format(total_rows)
    )

    return "*Query Results* {}\n```{}```\n*SQL:*\n```{}```".format(note, table, sql)


def format_error(error: str, sql: str = "") -> str:
    sql_block = "\n*Generated SQL:*\n```{}```".format(sql) if sql else ""
    return ":x: *Query failed*\n```{}```{}".format(error, sql_block)