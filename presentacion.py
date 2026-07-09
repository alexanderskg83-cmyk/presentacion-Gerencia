import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Control Nicalapia (Versión PDF)", page_icon="📊", layout="wide")

# ==========================================
# ESTILOS CSS (Optimizados para impresión)
# ==========================================
st.markdown("""
<style>
    /* Ocultar el menú lateral para que el PDF ocupe toda la hoja */
    div[data-testid="stSidebar"] { display: none; }
    
    .main-header { font-size: 50px; font-weight: 900; color: #124491; text-transform: uppercase; margin-bottom: 0px;}
    .sub-header { font-size: 25px; color: #008080; font-style: italic; margin-bottom: 20px;}
    .card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px;}
    .highlight { color: #124491; font-weight: bold; }
    .slide-divider { margin: 60px 0; border: none; border-top: 4px solid #124491; border-radius: 2px;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SLIDE 1: INICIO Y VISIÓN
# ==========================================
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="main-header">📊 NICALAPIA S.A.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Gestión de Datos y Trazabilidad en Planta</div>', unsafe_allow_html=True)
    st.write("Bienvenido al futuro del procesamiento. Nuestra Web App centraliza, agiliza y asegura todos los registros de calidad, transformando datos en papel a un panel de control interactivo (Dashboard).")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Procesos Digitalizados", "100%", "+ Eficiencia")
    c2.metric("Reducción de Errores", "99.9%", "Cálculo Exacto")
    c3.metric("Tiempo de Auditoría", "-60%", "Búsqueda Rápida")
    
    st.success("¡Sistema en línea! Listos para transformar el control de datos.")

with col2:
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80", caption="Visión de Control y Analítica de Datos", use_container_width=True)

st.markdown('<hr class="slide-divider">', unsafe_allow_html=True)

# ==========================================
# SLIDE 2: EL PROBLEMA VS LA SOLUCIÓN
# ==========================================
st.title("Optimización de Registros 🏭")
st.write("La transición de formatos físicos a una arquitectura de datos digital:")

col_prob, col_sol = st.columns(2)

with col_prob:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.error("❌ El Desafío del Formato Físico")
    st.write("- **Riesgo de pérdida:** Documentos expuestos a humedad en planta.")
    st.write("- **Errores Humanos:** Fallos en calculadoras al sumar múltiples pesajes.")
    st.write("- **Tiempos muertos:** Búsqueda manual de lotes históricos en bodegas.")
    st.write("- **Falta de métricas:** Difícil calcular tendencias sin digitar todo a Excel.")
    st.markdown('</div>', unsafe_allow_html=True)
    
with col_sol:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.success("✅ Sistema Integral (Web App)")
    st.write("- **Captura segura:** Ingreso de datos in situ mediante pantallas en planta.")
    st.write("- **Cálculos Automáticos:** Rendimientos y mermas al instante sin errores.")
    st.write("- **Trazabilidad a un clic:** Base de datos estructurada e inmediata.")
    st.write("- **Listos para auditar:** Generación de PDFs oficiales bloqueados.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="slide-divider">', unsafe_allow_html=True)

# ==========================================
# SLIDE 3: DEMOSTRACIÓN DE MÓDULOS (Desplegados para PDF)
# ==========================================
st.title("Arquitectura del Sistema ⚙️")
st.write("Explora la lógica interna de los módulos operacionales:")

# Módulo 1
st.markdown("### 📊 1. Recepción (FT-HACCP-005)")
st.write("Automatiza la captura de evaluación sensorial (olor, color, textura), temperatura de termos, y lotes en una matriz dinámica de pesaje.")
with st.expander("Ver lógica del sistema (Backend)", expanded=True):
    st.code('pesos = [pw[i].number_input(f"P{i+1}") for i in range(8)]', language='python')

st.write("---")

# Módulo 2
st.markdown("### 🔍 2. Seguimiento de Producto en Proceso (FT-PROD-03)")
st.write("Vincula el producto desde la bodega hasta el empaque, eliminando el trabajo manual del supervisor para calcular eficiencias.")
with st.expander("Fórmula Automática de Eficiencia", expanded=True):
    st.code('rendimiento_porcentaje = (peso_final / peso_inicial) * 100', language='python')

st.write("---")

# Módulo 3
st.markdown("### 🖨️ 3. Generación de Documentos Oficiales")
st.info("La aplicación genera plantillas estructuradas idénticas a los formatos vigentes de Nicalapia, inyectando los datos de forma inmutable y con auto-relleno de filas en blanco para evitar adulteraciones posteriores.")

st.markdown('<hr class="slide-divider">', unsafe_allow_html=True)

# ==========================================
# SLIDE 4: CALIDAD Y BRCGS
# ==========================================
st.title("🏆 Cumplimiento Normativo Internacional")
st.write("Cómo el sistema respalda la auditoría BRCGS y HACCP de forma automática:")

col_norma1, col_norma2 = st.columns([1.5, 1])

with col_norma1:
    st.success("**🔍 Cláusula 3.9 (Trazabilidad):**\nPermite rastrear la genealogía de un lote específico (del proveedor al producto terminado) en minutos, cumpliendo el límite de tiempo exigido por la norma.")
        
    st.success("**📝 Cláusula 3.2 (Control de Registros):**\nGarantiza registros legibles, estandarizados y sin enmendaduras. Todos los documentos impresos mantienen su código y versión oficial (Ej: FT-PROD-03).")
        
    st.success("**🌡️ Sección 2 (HACCP) - Límites Críticos:**\nEl sistema estandariza la captura de temperaturas (≤ 4°C) y parámetros sensoriales, previniendo el ingreso de materia prima fuera de especificación.")
        
with col_norma2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", caption="Control de Indicadores Críticos (KPIs)", use_container_width=True)

st.markdown('<hr class="slide-divider">', unsafe_allow_html=True)

# ==========================================
# SLIDE 5: ROADMAP Y FUTURO
# ==========================================
st.title("🚀 Evolución Tecnológica (Business Intelligence)")

st.progress(100)
st.success("¡Infraestructura Fase 1 Desplegada y Operativa!")

st.markdown("""
<div style="margin-top: 30px; background-color: #f8f9fa; padding: 20px; border-left: 5px solid #124491; border-radius: 5px;">
    <h3 class="highlight">🟢 Fase 1: Digitalización (Actual)</h3>
    <p>Implementación de la Web App en planta para Recepción de Materia Prima y Trazabilidad en Proceso.</p>
    <hr style="border-top: 1px dashed #ccc;">
    <h3 class="highlight">🟡 Fase 2: Escalabilidad de Datos (Siguiente paso)</h3>
    <p>Integración con bases de datos en la nube (SQL). Adición de módulos de Control de Despacho y Monitoreo Diario de Agua.</p>
    <hr style="border-top: 1px dashed #ccc;">
    <h3 class="highlight">🔴 Fase 3: Dashboards Gerenciales (Visión)</h3>
    <p>Paneles de Control (BI) en tiempo real para toma de decisiones: gráficas de productividad, histórico de rendimientos por proveedor y análisis de mermas.</p>
</div>
""", unsafe_allow_html=True)
