# Ollama LLM Agent for Home Assistant

A custom conversation agent integration for Home Assistant that connects to Ollama LLM models via local API.

## Features
- Adds a new Assist conversation agent
- Connects to your Ollama server
- Configurable via UI (config flow)
- Example response handler

## Installation

1. Copy `custom_components/ollama_agent/` to your Home Assistant `config/custom_components/` directory.
2. Restart Home Assistant.
3. Go to **Settings → Devices & Services → Add Integration** and search for **Ollama LLM Agent**.
4. Set up your voice assistant pipeline with this agent.

## HACS Installation

1. In HACS → Integrations, add this repository as a custom repository.
2. Install and restart Home Assistant.
3. Add integration as above.

## Author
- [Your Name](https://github.com/yourgithub)
