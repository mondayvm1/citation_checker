from config.base_config import Config
from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from exceptions.custom_exceptions import ConfigurationException


class OpenAIClient:
    @staticmethod
    def validate_api_key():
        """
        Validate that the OpenAI API key is present in the environment variables.
        """
        if not Config.OPENAI_API_KEY:
            raise ConfigurationException("OPENAI_API_KEY not found in environment variables")

    @staticmethod
    def get_api_key():
        """
        Return the OpenAI API key from environment variables.
        """
        OpenAIClient.validate_api_key()
        return Config.OPENAI_API_KEY

    @staticmethod
    def initialize_llm():
        """
        Determine the appropriate OpenAI model based on the date and initialize ChatOpenAI object.
        """
        if not Config.LLM_NAME:
            raise ConfigurationException("LLM_NAME not found in environment variables")
        return ChatOpenAI(model_name=Config.LLM_NAME, temperature=0)
