from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
import logging

from .conversation import OllamaAgent
from homeassistant.components.conversation.agent import async_register_agent

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.info("Setting up Ollama Conversation Agent from config entry")
    async_register_agent(hass, OllamaAgent(hass), "ollama_agent")
    return True
