import os #allows us to access environment variables
from supabase import create_client
from dotenv import load_dotenv

load_dotenv() #reads the .env file and loads the environment variables into the system

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)#creates a client instance that we can use to interact with our Supabase database