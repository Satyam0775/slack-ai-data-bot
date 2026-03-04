import logging
from slack_bolt import App
from app.config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from app.llm_sql import natural_language_to_sql
from app.database import execute_query
from app.formatter import format_results, format_error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

slack_app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)


@slack_app.command("/ask-data")
def handle_ask_data(ack, body, respond):
    ack()  # must acknowledge Slack within 3 seconds

    question = body.get("text", "").strip()

    if not question:
        respond(":warning: Please provide a question.\nUsage: `/ask-data show revenue by region for 2025-09-01`")
        return

    logger.info("Question: %s", question)

    # Step 1 — NL -> SQL
    try:
        sql = natural_language_to_sql(question)
        logger.info("SQL: %s", sql)
    except Exception as exc:
        respond(format_error("Failed to generate SQL: {}".format(exc)))
        return

    # Step 2 — Execute SQL
    try:
        rows, columns = execute_query(sql)
    except RuntimeError as exc:
        respond(format_error(str(exc), sql=sql))
        return

    # Step 3 — Reply
    respond(format_results(rows, columns, sql))