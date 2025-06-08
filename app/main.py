from fastapi import FastAPI
from app.core import obtener_datos, detectar_tendencia
from app.graficos import graficar_tendencia
import io
import base64
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Agrega CORS después de crear la app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar * por tu dominio si deseas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tendencia/{ticker}")
def analizar_tendencia(ticker: str):
    df = obtener_datos(ticker)
    if df is None:
        return JSONResponse(content={"error": "No se pudieron obtener datos."}, status_code=400)

    tendencia = detectar_tendencia(df)
    img_data = graficar_tendencia(df, ticker)

    return {
        "ticker": ticker,
        "tendencia": tendencia,
        "grafico_base64": img_data
    }
