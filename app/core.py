import yfinance as yf
import pandas as pd

def obtener_datos(ticker: str, timeframe: str = "5m") -> pd.DataFrame:
    """
    Descarga los datos históricos del ticker desde Yahoo Finance usando yfinance.

    Parámetros:
        ticker (str): Símbolo bursátil (ej. 'AAPL', 'TSLA').
        timeframe (str): Intervalo de tiempo (ej. '1m', '5m', '15m').

    Retorna:
        pd.DataFrame con las columnas: Open, High, Low, Close, Volume.
    """
    df = yf.download(ticker, interval=timeframe, period="1d")
    return df if not df.empty else None


def detectar_tendencia(df: pd.DataFrame) -> str:
    """
    Detecta si la tendencia es alcista o bajista basada en cruce de EMAs.

    Reglas:
    - Tendencia Alcista: EMA 8 está por encima de EMA 21.
    - Tendencia Bajista: EMA 8 está por debajo de EMA 21.

    Parámetros:
        df (pd.DataFrame): DataFrame con los datos de velas.

    Retorna:
        str: 'Alcista' o 'Bajista'
    """
    df["EMA_8"] = df["Close"].ewm(span=8).mean()
    df["EMA_21"] = df["Close"].ewm(span=21).mean()

    if df["EMA_8"].iloc[-1] > df["EMA_21"].iloc[-1]:
        return "Alcista"
    else:
        return "Bajista"
