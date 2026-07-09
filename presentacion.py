import streamlit as st

st.set_page_config(page_title="Presentación Nicalapia", page_icon="🐟", layout="centered")

st.markdown("""
<style>
    .slide-title { color: #124491; font-size: 36px; font-weight: bold; margin-bottom: 10px;}
    .slide-subtitle { color: #555; font-size: 20px; margin-bottom: 20px;}
    .slide-content { font-size: 18px; line-height: 1.6;}
    hr { margin-top: 50px; margin-bottom: 50px; border: 1px solid #ddd; }
</style>
""", unsafe_allow_html=True)

# Slide 1
st.markdown('<div class="slide-title">🐟 Nicalapia S.A. - Transformación Digital en Planta</div>', unsafe_allow_html=True)
st.markdown('<div class="slide-subtitle">Sistema Integral de Control de Calidad y Trazabilidad</div>', unsafe_allow_html=True)
st.info("Innovación, Inocuidad y Eficiencia Operativa.")
st.markdown("<hr>", unsafe_allow_html=True)

# Slide 2
st.markdown('<div class="slide-title">1. El Desafío Actual en Planta</div>', unsafe_allow_html=True)
st.markdown("""
<div class="slide-content">
<ul>
    <li>Registro manual propenso a errores de transcripción y cálculo matemático.</li>
    <li>Pérdida de tiempo valioso en la búsqueda de registros físicos para auditorías.</li>
    <li>Dificultad para calcular rendimientos de proceso en tiempo real.</li>
    <li>El papel en áreas húmedas es un riesgo constante de contaminación y pérdida de datos.</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Slide 3
st.markdown('<div class="slide-title">2. La Solución: Nicalapia Web App</div>', unsafe_allow_html=True)
st.markdown("""
<div class="slide-content">
<ul>
    <li><b>100% Digital y Web:</b> Accesible desde tablets o terminales en planta.</li>
    <li><b>Interfaz Intuitiva:</b> Listas predeterminadas y flujos pensados para el operario.</li>
    <li><b>Cero Instalaciones:</b> Implementación ágil y segura.</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.code("""
modulo = st.radio("SELECCIONE EL MÓDULO:", 
         ["📊 Recepción de Materia Prima", 
          "🔍 Seguimiento de Trazabilidad"])
""", language="python")
st.markdown("<hr>", unsafe_allow_html=True)

# Slide 4
st.markdown('<div class="slide-title">3. 🏆 El Aliado Ideal para la Certificación BRCGS</div>', unsafe_allow_html=True)
st.markdown("""
<div class="slide-content">
<ul>
    <li>✅ <b>Cláusula 3.9 (Trazabilidad):</b> Ejercicios de trazabilidad hacia adelante y atrás en minutos.</li>
    <li>✅ <b>Cláusula 3.2 (Control de Registros):</b> Registros legibles, sin tachaduras y estandarizados.</li>
    <li>✅ <b>Sección 2 (HACCP):</b> Documentación rigurosa de Límites Críticos y evaluación sensorial in situ.</li>
</ul>
<br>
<i>"La app convierte la presión de una auditoría internacional en una simple consulta digital."</i>
</div>
""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Slide 5
st.markdown('<div class="slide-title">4. Siguientes Pasos (Roadmap)</div>', unsafe_allow_html=True)
st.success("""
**Fase 1:** Recepción y Trazabilidad en Proceso (Actual)  
**Fase 2:** Conexión a Base de Datos SQL y módulos de Despacho  
**Fase 3:** Dashboards de Business Intelligence para Gerencia
""")