import streamlit as st

st.set_page_config(page_title="Presentación Nicalapia", page_icon="🐟", layout="wide")

st.markdown("""
<style>
    /* Estilos generales */
    .slide-container { background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 40px; }
    .main-title { color: #124491; font-size: 48px; font-weight: 900; text-align: center; margin-bottom: 5px; text-transform: uppercase;}
    .sub-title { color: #008080; font-size: 24px; text-align: center; font-style: italic; margin-bottom: 30px;}
    .section-title { color: #124491; font-size: 32px; font-weight: bold; border-bottom: 3px solid #008080; padding-bottom: 10px; margin-bottom: 20px;}
    .highlight-text { font-size: 18px; line-height: 1.6; color: #333;}
    .feature-box { background-color: #f8f9fa; padding: 20px; border-left: 5px solid #124491; border-radius: 5px; margin-bottom: 15px;}
    hr { margin: 40px 0; border: none; border-top: 2px dashed #ccc; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DIAPOSITIVA 1: PORTADA
# ==========================================
st.markdown('<div class="slide-container">', unsafe_allow_html=True)
st.markdown('<div class="main-title">🐟 NICALAPIA S.A.</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Transformación Digital en la Industria Pesquera</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Procesos Digitalizados", "100%", "+ Eficiencia")
col2.metric("Reducción de Errores", "99.9%", "Cálculo Automático")
col3.metric("Tiempo de Auditoría", "-60%", "Trazabilidad Inmediata")

st.markdown("<br><p style='text-align: center; font-size: 18px;'>Presentación de la Web App Integral para Control de Calidad y Trazabilidad (FT-HACCP-005 y FT-PROD-03)</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# DIAPOSITIVA 2: EL PROBLEMA VS LA SOLUCIÓN
# ==========================================
st.markdown('<div class="slide-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">El Cambio Necesario en Planta</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.error("❌ El Desafío del Papel")
    st.markdown("""
    <div class="highlight-text">
    <ul>
        <li><b>Manchas y Daños:</b> Áreas húmedas destruyen registros físicos.</li>
        <li><b>Errores Humanos:</b> Fallos al sumar libras en 8 pesajes continuos.</li>
        <li><b>Lentitud:</b> Horas buscando lotes anteriores para auditorías.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.success("✅ La Solución: Nicalapia App")
    st.markdown("""
    <div class="highlight-text">
    <ul>
        <li><b>Tablets en Planta:</b> Captura de datos en tiempo real.</li>
        <li><b>Cálculos Matemáticos Cero Fricción:</b> Rendimientos y totales automáticos.</li>
        <li><b>Información unificada:</b> Proveedores, granjas y calidad en un solo clic.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# DIAPOSITIVA 3: CARACTERÍSTICAS DE LA APP
# ==========================================
st.markdown('<div class="slide-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">¿Qué hace nuestra App?</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown('<div class="feature-box"><b>⚖️ Módulo de Recepción (FT-HACCP-005)</b><br>Captura de evaluación sensorial (olor, color, textura), temperatura de termos, y lotes en una matriz dinámica de pesaje. Genera PDF oficial estandarizado.</div>', unsafe_allow_html=True)
    with st.expander("Ver fragmento de código de Recepción"):
        st.code("""
        # Matriz dinámica para ingreso rápido de libras
        pw = st.columns(8)
        pesos = [pw[i].number_input(f"P{i+1}") for i in range(8)]
        """, language="python")

with col_b:
    st.markdown('<div class="feature-box"><b>🔍 Módulo de Trazabilidad (FT-PROD-03)</b><br>Vincula el producto desde la bodega hasta el proceso de fileteo/empaque. Calcula el % de rendimiento real automáticamente por lote procesado.</div>', unsafe_allow_html=True)
    with st.expander("Ver fragmento de código de Trazabilidad"):
        st.code("""
        # El sistema calcula el rendimiento sin intervención humana
        rend_real = (p_final / p_inicial * 100) if p_inicial > 0 else 0.0
        """, language="python")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# DIAPOSITIVA 4: CERTIFICACIÓN BRCGS Y VENTAJAS
# ==========================================
st.markdown('<div class="slide-container">', unsafe_allow_html=True)
st.markdown('<div class="section-title">El Camino hacia la Certificación (BRCGS)</div>', unsafe_allow_html=True)

st.info("Implementar esta herramienta no es solo modernizar; es cumplir con estándares globales de inocuidad alimentaria.")

c3, c4, c5 = st.columns(3)
with c3:
    st.markdown("### 🏷️ Trazabilidad Total")
    st.markdown("**(Cláusula 3.9 BRCGS)**<br>Permite rastrear el camino de un lote específico desde la granja hasta el cliente final en minutos.", unsafe_allow_html=True)

with c4:
    st.markdown("### 📝 Control de Registros")
    st.markdown("**(Cláusula 3.2 BRCGS)**<br>Elimina tachaduras y enmendaduras. Formularios inmutables con control de versiones (Versión Mayo 2026).", unsafe_allow_html=True)

with c5:
    st.markdown("### 🌡️ Límites Críticos")
    st.markdown("**(Sección 2 HACCP)**<br>Supervisa obligatoriamente la regla de Temperatura ≤ 4°C y rechaza productos que no cumplen análisis sensorial.", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# DIAPOSITIVA 5: EL FUTURO
# ==========================================
st.markdown('<div class="slide-container" style="background-color: #124491; color: white;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: white; text-align: center;">🚀 Evolución y Siguientes Pasos</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="font-size: 20px; line-height: 1.8; text-align: center; margin-top: 20px;">
    <b>Fase 1 (Completada):</b> Digitalización de Formatos en Planta.<br>
    <b>Fase 2 (Próximamente):</b> Conexión SQL a la nube para almacenamiento de datos históricos.<br>
    <b>Fase 3 (Business Intelligence):</b> Dashboards en tiempo real de mermas y calidad para la Gerencia General.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
