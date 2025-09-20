import os
import time
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API key tidak ditemukan. Pastikan file .env berisi GEMINI_API_KEY")

# Buat client GenAI
client = genai.Client(api_key=API_KEY)
# Kalau kamu pakai Vertex AI, bisa seperti:
# client = genai.Client(vertexai=True, project="YOUR_PROJECT_ID", location="YOUR_LOCATION")

MODEL_NAME = "gemini-2.5-pro"  

INPUT_CSV = "data_input.csv"
OUTPUT_CSV = "data_labeled.csv"
TEXT_COLUMN = "text"
SENTIMENT_COLUMN = "sentiment"
DELAY_BETWEEN_CALLS = 0.5

def get_sentiment(text: str) -> str:
    prompt = f"""Klasifikasikan sentiment dari teks berikut ke dalam kategori: Positif, Negatif, atau Netral.

Teks: "{text}"

Jawab hanya salah satu: Positif, Negatif, atau Netral."""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.0)
        )
        ans = response.text.strip()
        low = ans.lower()
        if "positif" in low or "positive" in low:
            return "Positive"
        elif "negatif" in low or "negative" in low:
            return "Negative"
        elif "netral" in low or "neutral" in low:
            return "Neutral"
        else:
            # fallback
            return "Neutral"
    except Exception as e:
        print(f"Error saat memproses teks: {text}\n{e}")
        return "Error"

def main():
    df = pd.read_csv(INPUT_CSV)
    if TEXT_COLUMN not in df.columns:
        raise ValueError(f"Kolom '{TEXT_COLUMN}' tidak ditemukan di {INPUT_CSV}")

    sentiments = []
    for idx, row in df.iterrows():
        text = str(row[TEXT_COLUMN])
        sent = get_sentiment(text)
        print(f"Row {idx}: {sent}")
        sentiments.append(sent)
        time.sleep(DELAY_BETWEEN_CALLS)

    df[SENTIMENT_COLUMN] = sentiments
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Selesai. Hasil disimpan ke {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
