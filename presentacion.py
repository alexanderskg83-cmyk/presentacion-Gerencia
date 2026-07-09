import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Control Nicalapia", page_icon="📊", layout="wide")

# ==========================================
# ESTILOS CSS (Animaciones y Diseño)
# ==========================================
st.markdown("""
<style>
    .main-header { font-size: 50px; font-weight: 900; color: #124491; text-transform: uppercase; margin-bottom: 0px;}
    .sub-header { font-size: 25px; color: #008080; font-style: italic; margin-bottom: 20px;}
    .card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.3s;}
    .card:hover { transform: scale(1.02); }
    .highlight { color: #124491; font-weight: bold; }
    div[data-testid="stSidebar"] { background-color: #f8f9fa; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# MENÚ DE NAVEGACIÓN LATERAL
# ==========================================
# Ícono de Dashboard / Analítica
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1055/1055685.png", width=90) 
st.sidebar.title("Sistema de Control Interno")
diapositiva = st.sidebar.radio("Navegación:", [
    "1. Inicio y Visión", 
    "2. El Problema vs La Solución", 
    "3. Demostración de Módulos", 
    "4. Calidad y Normativa BRCGS", 
    "5. Roadmap y Futuro"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Navega entre las secciones para explorar la arquitectura del sistema.")

# ==========================================
# SLIDE 1: INICIO Y VISIÓN
# ==========================================
if diapositiva == "1. Inicio y Visión":
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown('<div class="main-header">📊 NICALAPIA S.A.</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">Gestión de Datos y Trazabilidad en Planta</div>', unsafe_allow_html=True)
        st.write("Bienvenido al futuro del procesamiento. Nuestra Web App centraliza, agiliza y asegura todos los registros de calidad, transformando datos en papel a un panel de control interactivo (Dashboard).")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Procesos Digitalizados", "100%", "+ Eficiencia")
        c2.metric("Reducción de Errores", "99.9%", "Cálculo Exacto")
        c3.metric("Tiempo de Auditoría", "-60%", "Búsqueda Rápida")
        
        if st.button("🚀 Iniciar Presentación"):
            st.success("¡Sistema en línea! Listos para transformar el control de datos.")

    with col2:
        # Imagen sobria de un panel de control / gráficos
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80", caption="Visión de Control y Analítica de Datos", use_container_width=True)

# ==========================================
# SLIDE 2: EL PROBLEMA VS LA SOLUCIÓN
# ==========================================
elif diapositiva == "2. El Problema vs La Solución":
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

# ==========================================
# SLIDE 3: DEMOSTRACIÓN DE MÓDULOS
# ==========================================
elif diapositiva == "3. Demostración de Módulos":
    st.title("Arquitectura del Sistema ⚙️")
    st.write("Explora la lógica interna de los módulos operacionales:")
    
    tab1, tab2, tab3 = st.tabs(["📊 1. Recepción (FT-HACCP-005)", "🔍 2. Trazabilidad (FT-PROD-03)", "🖨️ 3. Reportes Oficiales"])
    
    with tab1:
        st.subheader("Clasificación y Recepción")
        st.write("Automatiza la captura de evaluación sensorial (olor, color, textura), temperatura de termos, y lotes en una matriz dinámica de pesaje.")
        with st.expander("Ver lógica del sistema (Backend)"):
            st.code('pesos = [pw[i].number_input(f"P{i+1}") for i in range(8)]', language='python')
            
    with tab2:
        st.subheader("Seguimiento de Producto en Proceso")
        st.write("Vincula el producto desde la bodega hasta el empaque, eliminando el trabajo manual del supervisor para calcular eficiencias.")
        with st.expander("Fórmula Automática de Eficiencia"):
            st.code('rendimiento_porcentaje = (peso_final / peso_inicial) * 100', language='python')

    with tab3:
        st.subheader("Generación de Documentos Oficiales")
        st.info("La aplicación genera plantillas estructuradas idénticas a los formatos vigentes de Nicalapia, inyectando los datos de forma inmutable y con auto-relleno de filas en blanco para evitar adulteraciones posteriores.")

# ==========================================
# SLIDE 4: CALIDAD Y BRCGS
# ==========================================
elif diapositiva == "4. Calidad y Normativa BRCGS":
    st.title("🏆 Cumplimiento Normativo Internacional")
    st.write("Interactúa con los botones para descubrir cómo el sistema respalda la auditoría BRCGS y HACCP:")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        if st.checkbox("🔍 Cláusula 3.9 (Trazabilidad)"):
            st.success("Permite rastrear la genealogía de un lote específico (del proveedor al producto terminado) en minutos, cumpliendo el límite de tiempo exigido por la norma.")
            
        if st.checkbox("📝 Cláusula 3.2 (Control de Registros)"):
            st.success("Garantiza registros legibles, estandarizados y sin enmendaduras. Todos los documentos impresos mantienen su código y versión oficial (Ej: FT-PROD-03).")
            
        if st.checkbox("🌡️ Sección 2 (HACCP) - Límites Críticos"):
            st.success("El sistema estandariza la captura de temperaturas (≤ 4°C) y parámetros sensoriales, previniendo el ingreso de materia prima fuera de especificación.")
            
    with col2:
        # Imagen de Dashboard enfocado en calidad/métricas
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", caption="Control de Indicadores Críticos (KPIs)", use_container_width=True)

# ==========================================
# SLIDE 5: ROADMAP Y FUTURO
# ==========================================
elif diapositiva == "5. Roadmap y Futuro":
    st.title("🚀 Evolución Tecnológica (Business Intelligence)")
    
    if st.button("Mostrar Avance de Proyecto"):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success("¡Infraestructura Fase 1 Desplegada!")

    st.markdown("""
    <div style="margin-top: 30px; background-color: #f8f9fa; padding: 20px; border-left: 5px solid #124491;">
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
