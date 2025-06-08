import yfinance as yf
import pandas as pd

def obtener_datos(ticker: str, timeframe: str = "5m") -> pd.DataFrame:
    import yfinance as yf
    import pandas as pd

    df = yf.download(ticker, interval=timeframe, period="1d")
    return df if not df.empty else None


@app.get("/tendencia/{ticker}")
def analizar_tendencia(ticker: str, timeframe: str = "5m"):
    df = obtener_datos(ticker, timeframe)  # Asegúrate que tu función lo reciba
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


def detectar_tendencia(df: pd.DataFrame) -> str:
    df["EMA_8"] = df["Close"].ewm(span=8).mean()
    df["EMA_21"] = df["Close"].ewm(span=21).mean()
    if df["EMA_8"].iloc[-1] > df["EMA_21"].iloc[-1]:
        return "Alcista"
    else:
        return "Bajista"
