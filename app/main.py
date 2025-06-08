# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core import obtener_datos, detectar_tendencia
from app.graficos import graficar_tendencia

# 🔹 1. Define la app
app = FastAPI()

# 🔹 2. Agrega el middleware CORS si usas frontend separado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 3. Endpoint principal
@app.get("/tendencia/{ticker}")
def analizar_tendencia(ticker: str, timeframe: str = "5m"):
    df = obtener_datos(ticker, timeframe)
    if df is None:
        return JSONResponse(content={"error": "No se pudieron obtener datos."}, status_code=400)

    tendencia = detectar_tendencia(df)
    img_data = graficar_tendencia(df, ticker)

    return {
        "ticker": ticker,
        "timeframe": timeframe,
        "tendencia": tendencia,
        "grafico_base64": img_data
    }
