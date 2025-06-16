
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Consulta de Vida Útil", layout="centered")

st.title("🔍 Consulta de Vida Útil por SKU")

st.markdown("Sube tu archivo `.xlsx` con las columnas necesarias.")

archivo = st.file_uploader("📂 Subir archivo Excel", type=["xlsx"])

if archivo:
    try:
        df = pd.read_excel(archivo)
        df.columns = [col.strip().lower() for col in df.columns]

        st.subheader("📋 Vista previa de datos:")
        st.dataframe(df.head())

        sku_input = st.text_input("🔎 Ingresa o escanea el SKU:")

        if sku_input:
            resultado = df[df['sku'].astype(str) == sku_input.strip()]
            if not resultado.empty:
                for _, row in resultado.iterrows():
                    st.success(f"📦 Producto: **{row['producto']}**")
                    st.info(f"🕒 Vida útil: **{row['vida útil']}**")
            else:
                st.warning("❌ SKU no encontrado.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
else:
    st.info("🔁 Esperando que subas un archivo Excel válido.")
