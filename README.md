# NASA API assignment

This code is designed to use the NASA API to make 3 distinct calls to their website  

## API Calls
1. Astronomy Picture of the Day
2. EPIC Earth Image Data
3. Asteroid data by date

## Setup

Install dependencies:
pip install -r requirements.txt

Create a .env file:
MY_API_KEY=your_api_key

Run the program:
python main.py

## Notes

- The API key is stored securely using a `.env` file.
- The program uses `os.getenv()` to access the API key.
- Do NOT upload your `.env` file to GitHub.
