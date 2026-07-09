import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Nicalapia Pitch", page_icon="🐟", layout="wide")

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
    div[data-testid="stSidebar"] { background-color: #f0f4f8; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# MENÚ DE NAVEGACIÓN LATERAL
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3063/3063822.png", width=100) # Logo genérico pescado
st.sidebar.title("Presentación Nicalapia")
diapositiva = st.sidebar.radio("Navegación:", [
    "1. Inicio y Visión", 
    "2. El Problema vs La Solución", 
    "3. Demostración de Módulos", 
    "4. Calidad y Normativa BRCGS", 
    "5. Roadmap y Futuro"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip de presentación:** Cambia de sección usando este menú para mantener la atención del público.")

# ==========================================
# SLIDE 1: INICIO Y VISIÓN
# ==========================================
if diapositiva == "1. Inicio y Visión":
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown('<div class="main-header">🐟 NICALAPIA S.A.</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">Transformación Digital en la Industria Pesquera</div>', unsafe_allow_html=True)
        st.write("Bienvenido al futuro del procesamiento de mariscos y tilapia. Nuestra nueva Web App centraliza, agiliza y asegura todos los registros de calidad en planta, eliminando el papel y potenciando la eficiencia.")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Procesos Digitalizados", "100%", "+ Eficiencia")
        c2.metric("Reducción de Errores", "99.9%", "Matemática Exacta")
        c3.metric("Tiempo de Auditoría", "-60%", "Búsqueda Rápida")
        
        if st.button("🚀 Iniciar Presentación"):
            st.balloons()
            st.success("¡Listos para transformar Nicalapia!")

    with col2:
        # Imagen de industria pesquera/tecnología
        st.image("https://images.unsplash.com/photo-1524704796725-9fc3044a58b2?auto=format&fit=crop&w=800&q=80", caption="Innovación en cada proceso", use_container_width=True)

# ==========================================
# SLIDE 2: EL PROBLEMA VS LA SOLUCIÓN
# ==========================================
elif diapositiva == "2. El Problema vs La Solución":
    st.title("El Cambio Necesario en Planta 🏭")
    st.write("¿Por qué necesitamos migrar del papel a lo digital? Veamos la comparativa:")
    
    col_prob, col_sol = st.columns(2)
    
    with col_prob:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.error("❌ El Desafío del Formato Físico")
        st.image("https://images.unsplash.com/photo-1607499699313-2df8d1c9ac6e?auto=format&fit=crop&w=600&q=80", caption="Registros en papel en áreas húmedas = Riesgo", use_container_width=True)
        st.write("- **Manchas y Daños:** Áreas húmedas destruyen registros físicos.")
        st.write("- **Errores Humanos:** Fallos en calculadoras al sumar libras.")
        st.write("- **Lentitud:** Búsqueda en bodegas para auditorías de trazabilidad.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_sol:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.success("✅ La Solución Digital (Web App)")
        st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=600&q=80", caption="Control digital en tiempo real", use_container_width=True)
        st.write("- **Tablets en Planta:** Captura de datos in situ y segura.")
        st.write("- **Cálculos Automáticos:** Rendimientos y mermas al instante.")
        st.write("- **Información Centralizada:** Base de datos accesible a un clic.")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SLIDE 3: DEMOSTRACIÓN DE MÓDULOS
# ==========================================
elif diapositiva == "3. Demostración de Módulos":
    st.title("Arquitectura de la Aplicación ⚙️")
    st.write("Explora cómo operan los módulos principales a través de estas pestañas:")
    
    tab1, tab2, tab3 = st.tabs(["📊 1. Recepción (FT-HACCP-005)", "🔍 2. Trazabilidad (FT-PROD-03)", "🖨️ 3. Reportes Oficiales"])
    
    with tab1:
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("Clasificación y Recepción")
            st.write("Captura de evaluación sensorial (olor, color, textura), temperatura de termos, y lotes en una matriz dinámica de pesaje.")
            with st.expander("Ver fragmento de código (Backend)"):
                st.code('pesos = [pw[i].number_input(f"P{i+1}") for i in range(8)]', language='python')
        with c2:
            st.image("https://images.unsplash.com/photo-1519623286359-e9f3cbef015b?auto=format&fit=crop&w=400&q=80", caption="Recepción de MP")
            
    with tab2:
        c1, c2 = st.columns([2, 1])
        with c1:
            st.subheader("Seguimiento de Producto")
            st.write("Vincula el producto desde la bodega hasta el empaque. Calcula el % de rendimiento real de fileteo automáticamente.")
            with st.expander("Fórmula Automática"):
                st.code('rend_real = (peso_final / peso_inicial) * 100', language='python')
        with c2:
            st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80", caption="Control de Procesos")

    with tab3:
        st.subheader("Listos para Imprimir")
        st.info("La aplicación genera plantillas HTML/PDF idénticas a los formatos oficiales de Nicalapia, con bloqueos anti-falsificación (filas en blanco auto-rellenadas).")
        st.image("https://images.unsplash.com/photo-1612222869049-d8ec83637a3c?auto=format&fit=crop&w=800&q=80", caption="Documentación digital inmutable", use_container_width=True)

# ==========================================
# SLIDE 4: CALIDAD Y BRCGS
# ==========================================
elif diapositiva == "4. Calidad y Normativa BRCGS":
    st.title("🏆 El Aliado Ideal para la Certificación")
    st.write("Interactúa con los botones para descubrir cómo la app resuelve los puntos críticos de auditoría (BRCGS/HACCP):")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?auto=format&fit=crop&w=600&q=80", caption="Laboratorio / Aseguramiento de Calidad", use_container_width=True)
    
    with col2:
        if st.checkbox("🔍 Cláusula 3.9 (Trazabilidad)"):
            st.success("Permite rastrear el camino de un lote específico (del proveedor a la caja final) en minutos, cumpliendo el límite de tiempo exigido por la norma.")
            
        if st.checkbox("📝 Cláusula 3.2 (Control de Registros)"):
            st.success("Elimina tachaduras, uso de correctores y garantiza registros legibles. Los formatos se imprimen con su código oficial (Ej: FT-PROD-03).")
            
        if st.checkbox("🌡️ Sección 2 (HACCP) - Límites Críticos"):
            st.success("Obliga al registro de temperatura y análisis sensorial. La estandarización evita que ingresen productos fuera de la norma (Ej: < 4°C).")

# ==========================================
# SLIDE 5: ROADMAP Y FUTURO
# ==========================================
elif diapositiva == "5. Roadmap y Futuro":
    st.title("🚀 Evolución: El Camino a Seguir")
    
    if st.button("Mostrar Avance de Proyecto"):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.success("¡Fase 1 Completada con Éxito!")

    st.markdown("""
    <div style="margin-top: 30px;">
        <h3 class="highlight">🟢 Fase 1 (Actual)</h3>
        <p>Digitalización de captura en planta: Formatos de Recepción (MP) y Trazabilidad (Proceso).</p>
        <hr>
        <h3 class="highlight">🟡 Fase 2 (Siguiente paso)</h3>
        <p>Almacenamiento en la Nube (Base de datos SQL) y nuevos módulos (Despacho y Control de Agua).</p>
        <hr>
        <h3 class="highlight">🔴 Fase 3 (Visión a largo plazo)</h3>
        <p><i>Business Intelligence:</i> Dashboards gerenciales con gráficas en vivo sobre productividad por operario, mermas semanales y calidad de proveedores.</p>
    </div>
    """, unsafe_allow_html=True)
