t# Profile Builder

AI-powered psychological profile generator that analyzes user onboarding data from Supabase and generates structured personality profiles.

## Features

- 📥 Fetches user onboarding data from Supabase
- 🤖 Generates psychological profiles using AI (Groq/Llama)
- 💾 Saves profiles as JSON files
- 🆓 Uses free AI API (Groq)

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd profile_builder
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Add your API keys:
     - `SUPABASE_URL` - Your Supabase project URL
     - `SUPABASE_KEY` - Your Supabase service key
     - `GROQ_API_KEY` - Your Groq API key (get free at https://console.groq.com)

## Usage

Run the profile builder:
```bash
python main.py
```

Generated profiles are saved to the `profiles/` directory.

## Project Structure

```
profile_builder/
├── agent.py              # AI profile generation
├── fetch_user.py         # Supabase data retrieval
├── prepare_payload.py    # Data transformation
├── save_profile.py       # JSON file saving
├── supabase_client.py    # Database connection
├── main.py              # Main pipeline
├── list_tables.py       # Utility for listing tables
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (not in git)
```

## Technologies

- **Python 3.12+**
- **Supabase** - Cloud PostgreSQL database
- **Groq** - Fast, free AI inference
- **Llama 3.3 70B** - Large language model

## License

MIT
