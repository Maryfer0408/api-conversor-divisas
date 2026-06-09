from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Servicio Web de Conversión de Divisas",
    description="API para la asignatura de Aplicaciones Web Orientadas a Servicios - UPP",
    version="1.0.0"
)

# Configuración de CORS para permitir la conexión desde tu cliente JavaScript local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que cualquier origen (como tu index.html local) se conecte
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (POST, GET, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Tasas de cambio fijas para la simulación
# 1 Euro = 19.50 MXN, 1 USD = 18.00 MXN, 1 CAD = 13.20 MXN, 1 GBP = 23.00 MXN
TASAS = {
    "EUR_TO_MXN": 19.50,
    "USD_TO_MXN": 18.00,
    "CAD_TO_MXN": 13.20,
    "GBP_TO_MXN": 23.00,
}

# Modelo de datos para recibir la cantidad a convertir
class RequestModel(BaseModel):
    cantidad: float

# --- SECCIÓN 1: MÉTODOS DE OTRA MONEDA A PESOS MXN ---

@app.post("/convertir/eur-mxn")
def eur_a_mxn(data: RequestModel):
    resultado = data.cantidad * TASAS["EUR_TO_MXN"]
    return {"moneda_origen": "EUR", "moneda_destino": "MXN", "cantidad": data.cantidad, "resultado": round(resultado, 2)}

@app.post("/convertir/usd-mxn")
def usd_a_mxn(data: RequestModel):
    resultado = data.cantidad * TASAS["USD_TO_MXN"]
    return {"moneda_origen": "USD", "moneda_destino": "MXN", "cantidad": data.cantidad, "resultado": round(resultado, 2)}

@app.post("/convertir/cad-mxn")
def cad_a_mxn(data: RequestModel):
    resultado = data.cantidad * TASAS["CAD_TO_MXN"]
    return {"moneda_origen": "CAD", "moneda_destino": "MXN", "cantidad": data.cantidad, "resultado": round(resultado, 2)}

@app.post("/convertir/gbp-mxn")
def gbp_a_mxn(data: RequestModel):
    resultado = data.cantidad * TASAS["GBP_TO_MXN"]
    return {"moneda_origen": "GBP", "moneda_destino": "MXN", "cantidad": data.cantidad, "resultado": round(resultado, 2)}


# --- SECCIÓN 2: MÉTODOS DE PESOS MXN A OTRA MONEDA ---

@app.post("/convertir/mxn-eur")
def mxn_a_eur(data: RequestModel):
    resultado = data.cantidad / TASAS["EUR_TO_MXN"]
    return {"moneda_origen": "MXN", "moneda_destino": "EUR", "cantidad": data.cantidad, "resultado": round(resultado, 4)}

@app.post("/convertir/mxn-usd")
def mxn_a_usd(data: RequestModel):
    resultado = data.cantidad / TASAS["USD_TO_MXN"]
    return {"moneda_origen": "MXN", "moneda_destino": "USD", "cantidad": data.cantidad, "resultado": round(resultado, 4)}

@app.post("/convertir/mxn-cad")
def mxn_a_cad(data: RequestModel):
    resultado = data.cantidad / TASAS["CAD_TO_MXN"]
    return {"moneda_origen": "MXN", "moneda_destino": "CAD", "cantidad": data.cantidad, "resultado": round(resultado, 4)}

@app.post("/convertir/mxn-gbp")
def mxn_a_gbp(data: RequestModel):
    resultado = data.cantidad / TASAS["GBP_TO_MXN"]
    return {"moneda_origen": "MXN", "moneda_destino": "GBP", "cantidad": data.cantidad, "resultado": round(resultado, 4)}