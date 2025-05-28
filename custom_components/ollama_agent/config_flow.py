from homeassistant import config_entries

class OllamaAgentConfigFlow(config_entries.ConfigFlow, domain="ollama_agent"):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Ollama LLM Agent", data={})
        return self.async_show_form(step_id="user")
