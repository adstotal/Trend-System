import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def graficar_tendencia(df: pd.DataFrame, ticker: str) -> str:
    plt.figure(figsize=(10, 5))
    plt.plot(df["Close"], label="Precio")
    plt.plot(df["EMA_8"], label="EMA 8")
    plt.plot(df["EMA_21"], label="EMA 21")
    plt.title(f"Tendencia de {ticker}")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
