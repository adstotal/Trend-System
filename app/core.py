import yfinance as yf
import pandas as pd

def obtener_datos(ticker: str) -> pd.DataFrame:
    df = yf.download(ticker, interval="5m", period="1d")
    return df if not df.empty else None

def detectar_tendencia(df: pd.DataFrame) -> str:
    df["EMA_8"] = df["Close"].ewm(span=8).mean()
    df["EMA_21"] = df["Close"].ewm(span=21).mean()
    if df["EMA_8"].iloc[-1] > df["EMA_21"].iloc[-1]:
        return "Alcista"
    else:
        return "Bajista"
