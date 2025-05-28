from homeassistant.components.conversation.agent import ConversationAgent, ConversationInput, ConversationResult

class OllamaAgent(ConversationAgent):
    def __init__(self, hass):
        self.hass = hass

    @property
    def supported_languages(self):
        return ["en"]

    @property
    def attribution(self):
        return "Powered by Ollama LLM"

    @property
    def name(self):
        return "Ollama LLM Agent"

    async def async_process(self, user_input: ConversationInput) -> ConversationResult:
        text = user_input.text
        response = f"Ollama response: You said '{text}'"
        return ConversationResult(response=response)
