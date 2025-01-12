import os
import dotenv

dotenv.load_dotenv()

# LLM
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')