from openai import OpenAI
from config.keys import OPENAI_API_KEY
from config.config import LLM_MODEL, LLM_TEMPERATURE

from utils.prompts import system_prompt, user_prompt
from utils.models import SearchResult, ChatHistory, Interaction

from utils.textual import summarize

from utils.log import get_logger
logger = get_logger("LLM")

class LLM():

    def __init__(self) -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.history = ChatHistory(interactions=[])
        self.history_limit = 4
        logger.info("Initialized LLM.")
    
    def generate(self, prompt: str, search_result: SearchResult) -> str:
        logger.info(f"Generating response for prompt: {summarize(prompt)}")
        completion = self.client.chat.completions.create(
            model=LLM_MODEL,
            temperature=LLM_TEMPERATURE,
            messages=[
                {"role": "developer", "content": system_prompt()},
                {
                    "role": "user",
                    "content": user_prompt(user_query=prompt, search_result=search_result, history=self.history)
                }
            ]
        )
        
        response = completion.choices[0].message.content
        logger.info(f"Generated response: {summarize(response)}")
        
        self.history.interactions.append(Interaction(user=prompt, chatbot=response))
        if len(self.history.interactions) > self.history_limit:
            self.history.interactions.pop(0)
            
        for interaction in self.history.interactions:
            logger.debug(f"Interaction: User: {summarize(interaction.user)}, Chatbot: {summarize(interaction.chatbot)}")

        return response
