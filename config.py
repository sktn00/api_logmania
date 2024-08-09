from dotenv import load_dotenv
import os

load_dotenv()  # This line loads the variables from .env
DATABASE_URL = "sqlite:///./logs.db"
API_KEYS = {
    "service1": os.getenv("SERVICE1_API_KEY"),
    "service2": os.getenv("SERVICE2_API_KEY"),
    "service3": os.getenv("SERVICE3_API_KEY"),
}