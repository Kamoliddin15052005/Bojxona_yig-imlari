import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Bojxona Yig'imlari Kalkulyatori",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stillar
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stAlert {
        background-color: #e3f2fd;
    }
    h1 {
        color: #1976d2;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    h2 {
        color: #424242;
        border-bottom: 3px solid #1976d2;
        padding-bottom: 10px;
    }
    h3 {
        color: #555;
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .info-box {
        background: #e3f2fd;
        padding: 15px;
        border-left: 4px solid #1976d2;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sarlavha
st.markdown("<h1>📦 Bojxona Yig'imlari Kalkulyatori 2025</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Flag_of_Uzbekistan.svg", width=250)
    st.markdown("### 🏛️ O'zbekiston Respublikasi")
    st.markdown("**Vazirlar Mahkamasi qarori**")
    st.markdown("**№ 55, 31.01.2025**")
    st.divider()
    st.markdown("### 📋 Bo'limlar")
    menu = st.radio(
        "",
        ["🏠 Asosiy ma'lumot", "💰 Yig'im kalkulyatori", "📊 Stavkalar jadvali", "📈 Grafik tahlil", "ℹ️ Qo'shimcha ma'lumot"],
        label_visibility="collapsed"
    )

# BHM (Bazaviy Hisoblash Miqdori)
BHM = 340000  # 2025 yil uchun BHM

# Ma'lumotlar bazasi
tariff_data = {
    "Bojxona qiymati (AQSh dollari)": [
        "10,000 gacha",
        "10,000 - 20,000",
        "20,000 - 40,000",
        "40,000 - 60,000",
        "60,000 - 100,000",
        "100,000 - 200,000",
        "200,000 - 500,000",
        "500,000 - 1,000,000",
        "1,000,000 va undan ortiq"
    ],
    "Stavka (BHM)": [1, 1.5, 2.5, 4, 7, 10, 15, 20, 25],
    "Yig'im (so'm)": [
        340000, 510000, 850000, 1360000, 2380000, 3400000, 5100000, 6800000, 8500000
    ]
}

other_fees = {
    "Xizmat turi": [
        "Tranzit, qayta ishlash rejimi",
        "Naqd valyuta deklaratsiyasi",
        "Bojxona kirim orderi",
        "Xalqaro kuryer (1 kg)",
        "BYD o'zgartirish/qo'shimcha",
        "Ish vaqtidan tashqari (har bir BYD)",
        "Bojxona omborida saqlash (1 tonna, dastlabki 10 kun)",
        "Bojxona omborida saqlash (1 tonna, keyingi kunlar)",
        "Avtotransport hamrohligi (200 km gacha)",
        "Avtotransport hamrohligi (200 km dan ortiq)",
        "Intellektual mulk reyestriga kiritish"
    ],
    "Stavka": [
        "BHM 25%",
        "BHM 2.5 baravari",
        "BHM 25%",
        "BHM 2%",
        "BHM 25%",
        "BHM 25%",
        "BHM 3%",
        "BHM 4%",
        "BHM 2 baravari",
        "BHM 5 baravari",
        "BHM 1 baravari"
    ],
    "Yig'im (so'm)": [
        85000, 850000, 85000, 6800, 85000, 85000, 10200, 13600, 680000, 1700000, 340000
    ]
}

# ASOSIY MA'LUMOT BO'LIMI
if menu == "🏠 Asosiy ma'lumot":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #1976d2; margin: 0;'>📅 Amal qilish sanasi</h3>
            <p style='font-size: 24px; font-weight: bold; color: #424242; margin: 10px 0;'>2025-yil 1-may</p>
            <p style='color: #666; margin: 0;'>Rasmiy e'lon qilinganidan 3 oy o'tgach</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #1976d2; margin: 0;'>💵 BHM (2025)</h3>
            <p style='font-size: 24px; font-weight: bold; color: #424242; margin: 10px 0;'>{BHM:,} so'm</p>
            <p style='color: #666; margin: 0;'>Bazaviy hisoblash miqdori</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #1976d2; margin: 0;'>📋 Qaror raqami</h3>
            <p style='font-size: 24px; font-weight: bold; color: #424242; margin: 10px 0;'>№ 55</p>
            <p style='color: #666; margin: 0;'>31.01.2025</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("## 📝 Qonun haqida qisqacha")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-box'>
            <h4>🎯 Asosiy maqsad</h4>
            <ul>
                <li>Bojxona yig'imlari stavkalarini Jahon Savdo Tashkiloti (JST) talablariga moslashtirish</li>
                <li>Import va eksport yig'imlarini o'zaro muvofiqlashtirish</li>
                <li>Bojxona xarajatlarini hisoblash tizimini yaxshilash</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-box'>
            <h4>✨ Asosiy o'zgarishlar</h4>
            <ul>
                <li>Yangi stavkalar tizimi (bojxona qiymatiga bog'liq)</li>
                <li>Tranzit va qayta ishlash rejimi uchun bir xil stavka</li>
                <li>Dastlabki deklaratsiyalashda 20% chegirma</li>
                <li>Ish vaqtidan tashqari xizmatlar uchun qo'shimcha to'lov</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🔔 Muhim eslatmalar")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🎁 **Dastlabki deklaratsiyalashda 20% chegirma!**")
    
    with col2:
        st.warning("⚠️ Ish vaqtidan tashqari xizmat BHM 25% qo'shimcha to'lov talab qiladi")
    
    with col3:
        st.success("✅ Elektron deklaratsiya orqali rasmiylashtirish tezroq va arzonroq")

# KALKULYATOR BO'LIMI
elif menu == "💰 Yig'im kalkulyatori":
    st.markdown("## 💰 Bojxona Yig'imi Kalkulyatori")
    
    st.markdown("""
    <div class='info-box'>
        <p><strong>Qanday foydalanish kerak?</strong> Tovaringiz qiymatini kiriting va yig'im avtomatik hisoblanadi!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        customs_value = st.number_input(
            "Bojxona qiymati (AQSh dollari):",
            min_value=0,
            max_value=10000000,
            value=50000,
            step=1000,
            help="Tovaringizning bojxona qiymatini kiriting"
        )
        
        initial_declaration = st.checkbox("Dastlabki deklaratsiya (20% chegirma)", value=False)
        
        after_hours = st.checkbox("Ish vaqtidan tashqari rasmiylashtirish (+25%)", value=False)
    
    with col2:
        st.markdown("### 📊 Dollar kursi")
        usd_rate = st.number_input(
            "1 USD (so'm):",
            min_value=10000,
            max_value=20000,
            value=12700,
            step=100
        )
    
    # Hisoblash
    def calculate_fee(value):
        if value <= 10000:
            return 1 * BHM
        elif value <= 20000:
            return 1.5 * BHM
        elif value <= 40000:
            return 2.5 * BHM
        elif value <= 60000:
            return 4 * BHM
        elif value <= 100000:
            return 7 * BHM
        elif value <= 200000:
            return 10 * BHM
        elif value <= 500000:
            return 15 * BHM
        elif value <= 1000000:
            return 20 * BHM
        else:
            return 25 * BHM
    
    base_fee = calculate_fee(customs_value)
    
    # Chegirmalar va qo'shimchalar
    if initial_declaration:
        base_fee = base_fee * 0.8
    
    additional_fee = 0
    if after_hours:
        additional_fee = BHM * 0.25
    
    total_fee = base_fee + additional_fee
    
    st.divider()
    
    # Natijalar
    st.markdown("### 📋 Hisoblash natijalari")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Tovar qiymati",
            f"${customs_value:,}",
            f"{customs_value * usd_rate:,} so'm"
        )
    
    with col2:
        st.metric(
            "Asosiy yig'im",
            f"{base_fee:,.0f} so'm",
            f"${base_fee/usd_rate:,.2f}"
        )
    
    with col3:
        if additional_fee > 0:
            st.metric(
                "Qo'shimcha to'lov",
                f"{additional_fee:,.0f} so'm",
                "Ish vaqtidan tashqari"
            )
        else:
            st.metric("Qo'shimcha to'lov", "0 so'm")
    
    with col4:
        st.metric(
            "JAMI TO'LOV",
            f"{total_fee:,.0f} so'm",
            f"${total_fee/usd_rate:,.2f}",
            delta_color="inverse"
        )
    
    # Batafsil ma'lumot
    with st.expander("📊 Batafsil hisoblash"):
        st.markdown(f"""
        **Hisoblash jarayoni:**
        1. Bojxona qiymati: **${customs_value:,}** ({customs_value * usd_rate:,} so'm)
        2. Asosiy stavka: **{base_fee/BHM:.1f} BHM** = {base_fee:,.0f} so'm
        3. Chegirma: **{'-20%' if initial_declaration else 'Yo\'q'}**
        4. Qo'shimcha to'lov: **{'+25%' if after_hours else 'Yo\'q'}**
        5. **Jami: {total_fee:,.0f} so'm**
        """)

# JADVAL BO'LIMI
elif menu == "📊 Stavkalar jadvali":
    st.markdown("## 📊 Bojxona Yig'imlari Stavkalari Jadvali")
    
    tab1, tab2 = st.tabs(["📦 Asosiy stavkalar", "🔧 Qo'shimcha xizmatlar"])
    
    with tab1:
        st.markdown("### Bojxona qiymatiga asoslangan stavkalar")
        
        df = pd.DataFrame(tariff_data)
        
        # Ranglar qo'shish
        def highlight_rows(row):
            return ['background-color: #e3f2fd' if i % 2 == 0 else 'background-color: white' 
                    for i in range(len(row))]
        
        styled_df = df.style.apply(highlight_rows, axis=1)
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        
        st.info("💡 **Eslatma:** Dastlabki deklaratsiyalashda bu stavkalardan 20% chegirma beriladi!")
    
    with tab2:
        st.markdown("### Qo'shimcha xizmatlar uchun yig'imlar")
        
        df2 = pd.DataFrame(other_fees)
        styled_df2 = df2.style.apply(highlight_rows, axis=1)
        st.dataframe(styled_df2, use_container_width=True, hide_index=True)

# GRAFIK TAHLIL BO'LIMI
elif menu == "📈 Grafik tahlil":
    st.markdown("## 📈 Bojxona Yig'imlari Grafik Tahlili")
    
    # Ma'lumotlar tayyorlash
    values = [5000, 15000, 30000, 50000, 80000, 150000, 350000, 750000, 1500000]
    fees = [calculate_fee(v) for v in values]
    
    def calculate_fee(value):
        if value <= 10000:
            return 1 * BHM
        elif value <= 20000:
            return 1.5 * BHM
        elif value <= 40000:
            return 2.5 * BHM
        elif value <= 60000:
            return 4 * BHM
        elif value <= 100000:
            return 7 * BHM
        elif value <= 200000:
            return 10 * BHM
        elif value <= 500000:
            return 15 * BHM
        elif value <= 1000000:
            return 20 * BHM
        else:
            return 25 * BHM
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chiziqli grafik
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=values,
            y=[calculate_fee(v) for v in values],
            mode='lines+markers',
            name='Bojxona yig\'imi',
            line=dict(color='#1976d2', width=3),
            marker=dict(size=10, color='#1976d2')
        ))
        
        fig1.update_layout(
            title="Bojxona Yig'imi vs Tovar Qiymati",
            xaxis_title="Tovar qiymati (USD)",
            yaxis_title="Yig'im (so'm)",
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Bar chart
        ranges = tariff_data["Bojxona qiymati (AQSh dollari)"]
        fees_by_range = tariff_data["Yig'im (so'm)"]
        
        fig2 = go.Figure(data=[
            go.Bar(
                x=ranges,
                y=fees_by_range,
                marker_color='#667eea',
                text=[f"{f:,}" for f in fees_by_range],
                textposition='outside'
            )
        ])
        
        fig2.update_layout(
            title="Stavkalar bo'yicha yig'imlar",
            xaxis_title="Qiymat oralig'i",
            yaxis_title="Yig'im (so'm)",
            xaxis_tickangle=-45,
            template='plotly_white'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Foiz grafigi
    st.markdown("### 📊 Yig'imning tovar qiymatiga nisbati")
    
    percentages = [(calculate_fee(v) / (v * 12700)) * 100 for v in values]
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=values,
        y=percentages,
        fill='tozeroy',
        name='Foiz',
        line=dict(color='#764ba2', width=2)
    ))
    
    fig3.update_layout(
        title="Yig'imning tovar qiymatiga foiz nisbati",
        xaxis_title="Tovar qiymati (USD)",
        yaxis_title="Foiz (%)",
        template='plotly_white'
    )
    
    st.plotly_chart(fig3, use_container_width=True)

# QO'SHIMCHA MA'LUMOT
else:
    st.markdown("## ℹ️ Qo'shimcha Ma'lumot")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("❓ Tez-tez so'raladigan savollar"):
            st.markdown("""
            **1. BHM nima?**
            - BHM (Bazaviy Hisoblash Miqdori) - bu bojxona yig'imlarini hisoblash uchun asosiy miqdor
            - 2025 yilda BHM = 340,000 so'm
            
            **2. Dastlabki deklaratsiya nima?**
            - Bu tovarni birinchi marta rasmiylashtirish
            - 20% chegirma olish uchun imkoniyat
            
            **3. Ish vaqtidan tashqari xizmat nimani anglatadi?**
            - Oddiy ish vaqtidan tashqarida rasmiylashtirish
            - Dam olish va bayram kunlari
            - BHM ning 25% qo'shimcha to'lov
            """)
        
        with st.expander("📅 Muhim sanalar"):
            st.markdown("""
            - **31.01.2025** - Qaror qabul qilingan sana
            - **01.05.2025** - Qaror kuchga kiradi
            - **01.01.2026** - Ayrim pozitsiyalar kuchga kiradi
            """)
    
    with col2:
        with st.expander("📜 Huquqiy asos"):
            st.markdown("""
            **Qaror asosiy hujjatlari:**
            - O'zbekiston Respublikasi Vazirlar Mahkamasi qarori
            - № 55, 31.01.2025
            - Jahon Savdo Tashkiloti talablari asosida
            
            **Bekor qilinadigan hujjatlar:**
            - 2020-yil 9-noyabrdagi 700-son qaror
            - Va boshqa bir qator oldingi qarorlar
            """)
        
        with st.expander("🔗 Foydali havolalar"):
            st.markdown("""
            - [Bojxona qo'mitasi rasmiy sayti](https://customs.uz)
            - [Qonunchilik bazasi](https://lex.uz)
            - [Vazirlar Mahkamasi](https://gov.uz)
            """)
    
    st.divider()
    
    st.markdown("### 📞 Aloqa ma'lumotlari")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **Bojxona qo'mitasi**
        
        📞 1155 (call-markaz)
        
        📧 info@customs.uz
        """)
    
    with col2:
        st.success("""
        **Onlayn xizmatlar**
        
        🌐 my.customs.uz
        
        📱 Mobile app: "Bojxona"
        """)
    
    with col3:
        st.warning("""
        **Qo'llab-quvvatlash**
        
        🕐 Dush-Juma: 9:00-18:00
        
        📍 Toshkent sh.
        """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>© 2025 O'zbekiston Respublikasi Bojxona Qo'mitasi</p>
    <p>Ushbu dastur faqat ma'lumot berish maqsadida yaratilgan. Rasmiy hujjatlar bilan taqqoslang.</p>
    <p style='font-size: 12px; margin-top: 10px;'>
        Yaratilgan: Streamlit | Python | Plotly
    </p>
</div>
""", unsafe_allow_html=True)
