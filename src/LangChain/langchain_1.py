import getpass
import os
from langchain.chat_models import init_chat_model

class LangChainDemo_1:

    def __init__(self, model_name, model_provider):
        self.model_name = model_name
        self.model_provider = model_provider
        self.set_up_api_key()
    

    @staticmethod
    def set_up_api_key():
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("")


    def init_chat_model(self):
        model = init_chat_model(self.model_name, model_provider=self.model_provider)
        model.invoke("Hello, world!")



# model = init_chat_model("gpt-4o-mini", model_provider="openai")