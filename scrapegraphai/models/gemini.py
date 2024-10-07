
    

from langchain_google_genai import ChatGoogleGenerativeAI as gemini
class Gemini(gemini):
    """
    A wrapper for the OneApi class that provides default configuration
    and could be extended with additional methods if needed.

    Args:
        llm_config (dict): Configuration parameters for the language model.
    """

    def __init__(self, **llm_config):
        if 'api_key' in llm_config:
            llm_config['GOOGLE_API_KEY'] = llm_config.pop('api_key') 
        llm_config["convert_system_message_to_human"] = True
        super().__init__(**llm_config)

    
        

