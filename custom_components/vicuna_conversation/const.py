"""Constants for the Custom OpenAI Conversation integration."""

import logging

DOMAIN = "vicuna_conversation"
LOGGER = logging.getLogger(__package__)

CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODELS = [
    "gpt-3.5-turbo",
    "google/gemini-2.5-flash",
]
RECOMMENDED_CHAT_MODEL = RECOMMENDED_CHAT_MODELS[0]
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 1.0
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 1.0
CONF_STREAMING = "streaming"

CONF_BASE_URL = "base_url"
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_API_KEY = "sk-0000000000000000000"
