import logging

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)

# Read env variables from .env file
load_dotenv()

app = App()
app_handler = SlackRequestHandler(app)
api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@app.event("app_mention")
def handle_app_mentions(body, say):
    say("What's up?")


@app.event("app_home_opened")
def handle_app_home_opened(say, event, body):
    try:
        say("that is my home")
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


def simple_sum(a, b):
    return a + b
