from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# 🔹 Aquí colocas el import que me preguntaste
from app.core import obtener_datos, detectar_tendencia
from app.graficos import graficar_tendencia  # Si tienes esta parte

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:8080"] si usas http.server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔸 Inicializa la app
app = FastAPI()

# 🔸 Configura CORS (opcional pero útil para el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes. Cambia esto en producción.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔸 Endpoint principal
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
