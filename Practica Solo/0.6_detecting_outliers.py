import yfinance as yf
import pandas as pd

ACTIVOS = ['TSLA', 'KO', 'BTC-USD']
FECHA = '2025-10-01' # Filtramos solo los últimos meses para no saturar la terminal

print("--- BUSCANDO DÍAS DE ALTA CONVICCIÓN (>80% Eficiencia) ---")

for ticker in ACTIVOS:
    df = yf.download(ticker, start=FECHA, progress=False)
    datos = df.xs(ticker, axis=1, level='Ticker').copy()
    
   # --- 1. FILTROS DE ROBUSTEZ (Movidos arriba para limpiar antes de calcular) ---
    datos = datos[datos['Volume'] > 0].copy()
    datos = datos[datos['High'] / datos['Low'] < 1.5]

    # --- 2. CÁLCULO PROFESIONAL (Sustituye a los cálculos simples) --- [NEW]
    datos['Prev_Close'] = datos['Close'].shift(1)
    datos['TR'] = pd.concat([
        (datos['High'] - datos['Low']),
        (datos['High'] - datos['Prev_Close']).abs(),
        (datos['Low'] - datos['Prev_Close']).abs()
    ], axis=1).max(axis=1)
    
    datos['Cuerpo'] = (datos['Close'] - datos['Open']).abs()
    # Ahora usamos TR en lugar de Rango para la eficiencia
    datos['Eficiencia'] = (datos['Cuerpo'] / datos['TR']) * 100 
    
    datos.dropna(inplace=True) # Limpia el primer día que no tiene 'Prev_Close'
    
    # 2. FILTRADO: Solo queremos los días donde la eficiencia > 80%
    dias_top = datos[datos['Eficiencia'] > 80]
    
    print(f"\n" + "="*40)
    print(f"RESULTADOS PARA {ticker}:")
    print(f"Total de días analizados: {len(datos)}")
    print(f"Días de alta convicción:  {len(dias_top)}")
    
    if not dias_top.empty:
        # Mostramos los 3 días más eficientes
        print("\nTop 3 días más limpios:")
        print(dias_top['Eficiencia'].nlargest(3))
        
    # Separamos los días de alta convicción en alcistas y bajistas
    verdes = dias_top[dias_top['Close'] > dias_top['Open']]
    rojos = dias_top[dias_top['Close'] < dias_top['Open']]

    print(f"    🟢 Días Explosivos Verdes: {len(verdes)}")
    print(f"    🔴 Días Explosivos Rojos:  {len(rojos)}")
    
    # --- DENTRO DEL BUCLE FOR ---
    
    # 3. Lógica de Veredicto
    porc_verde = (len(verdes) / len(dias_top) * 100) if len(dias_top) > 0 else 0
    
    print(f"    📊 Ratio de Victoria (Explosiva): {porc_verde:.2f}%")
    
    if porc_verde > 60:
        print(f"    ✅ VEREDICTO: {ticker} es SALUDABLE para compras.")
    elif porc_verde < 40 and len(dias_top) > 0:
        print(f"    🚨 ALERTA: {ticker} tiene un sesgo bajista peligroso.")
    else:
        print(f"    🟡 VEREDICTO: {ticker} está en equilibrio (Neutral).")

    # 4. Cálculo del Desangre (Últimos 3 días)
    ultimos_3 = datos.tail(3)
    rango_reciente = ultimos_3['TR'].mean()
    eficiencia_reciente = ultimos_3['Eficiencia'].mean()

    # Si la eficiencia cae mucho después de días rojos, el desangre para
    if eficiencia_reciente < 30:
        print(f"    🩹 DESANGRE: El precio se está frenando. Posible suelo.")
        
    # CÁLCULOS DE ALTA PRECISIÓN
    rango_dolares = datos['TR']
    
    # Usamos la mediana para evitar que días "locos" nos mientan
    mediana_rango = rango_dolares.median()
    
    # Volatilidad porcentual (¿Qué tanto pesa ese rango en el precio?)
    vol_porcentual = (rango_dolares / datos['Close']).mean() * 100

    print(f"    🎯 Rango Típico (Mediana): {mediana_rango:.2f} USD")
    print(f"    📊 Volatilidad Real:       {vol_porcentual:.2f}% del precio")
    
    # --- FILTRO DE ROBUSTEZ PROFESIONAL ---
    # Ignoramos días con volumen 0 (datos corruptos o mercado cerrado)
    datos = datos[datos['Volume'] > 0].copy()

    # Si el activo se mueve más de un 50% en un día, sospechamos error de datos
    datos = datos[datos['High'] / datos['Low'] < 1.5]