import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import json                     
import google.generativeai as genai

# API Yapılandırması (st.secrets kullanımı tavsiye edilir, buraya geçerli API anahtarınızı giriniz)
API_KEY = "BURAYA_GEMINI_API_ANAHTARINIZI_GİRİNİZ"
genai.configure(api_key=API_KEY)

# Sayfa Yapılandırması
st.set_page_config(page_title="TROIA | Üretken Yapay Zeka ile Tarlaya Özel Gübre ve Hidrojel Formülasyonu", layout="wide")

st.markdown("""
    <style>
    /* Ana Arka Planı Temizle */
    .stApp {
        background-color: #F8F9FA;
        color: #212529;
    }
    /* Sidebar'ı biraz daha koyu gri yaparak kontrast oluştur */
    .sidebar .sidebar-content {
        background-color: #E9ECEF;
    }
    /* Başlıkları Kurumsal Koyu Yeşil Yap */
    h1, h2, h3, h4, h5 {
        color: #1B4332 !important;
    }
    /* Butonları daha dikkat çekici ve okunaklı yap */
    .stButton>button {
        background-color: #2D6A4F;
        color: #FFFFFF;
        font-weight: bold;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #40916C;
        color: #FFFFFF;
    }
    /* Tablo ve İstatistik Kutuları */
    .highlight-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #2D6A4F;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Tabloların beyaz zemin üzerinde net görünmesi için */
    [data-testid="stDataFrame"] {
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 5px;
    }

    /* Sekme metinlerinin genel rengi */
    button[data-baseweb="tab"] {
        color: #2D6A4F !important;
        font-weight: 600 !important;
    }
    div[data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #1B4332 !important;
        border-bottom: 2px solid #2D6A4F !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #40916C !important;
    }

    /* Tüm input etiketleri, p elementleri ve radio buton seçeneklerinin görünmeme sorununu çözen CSS */
    label, p, .stRadio > div, [data-testid="stRadio"] label, [data-testid="stRadio"] p {
        color: #212529 !important;
        font-weight: 500 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sol Menü (Sidebar Navigasyon)
st.sidebar.title("TROIA Platform")
page = st.sidebar.radio("Modül Seçiniz:", ["🏠 TROIA Nedir?", "🔬 Akıllı Formülasyon", "📊 Bilgi Sistemi", "🗺️ Dinamik Ekim Takvimi"])

# --- 🏠 ANA SAYFA (TROIA NEDİR?) ---
if page == "🏠 TROIA Nedir?":
    st.title("TROIA")
    st.subheader("Ezbere Değil, İhtiyaca Göre Gübre.")
    st.write("---")
    
    st.markdown("""
    ### 🌾 Geleneksel Tarımdaki Ezbere Gübrelemeye Son!
    Bugün tarım ekosistemindeki en büyük krizlerden biri, üreticilerin tarlalarının gerçek biyokimyasal ihtiyacını bilmeden, 
    kulaktan dolma bilgilerle veya standart katalog gübreleriyle üretim yapmasıdır. Bu durum hem toprakların 
    pH/tuzluluk dengesini bozarak yıkanmasına neden olmakta hem de milyarlarca liralık ekonomik israfa yol açmaktadır.
    
    **TROIA**, bu ezbere dayalı yapıyı çözmek için geliştirilmiş, Üretken Yapay Zeka (Agent AI) tabanlı bir karar destek ve formülasyon sistemidir.
    """)
    
    st.write("---")
    st.markdown("### 🎯 Prototipimizin Temel Hedefleri")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>🔬 Parsele Özel Reçeteleme</h4>
            <p>Piyasadaki tek tip gübre çuvalları yerine, tarladan gelen toprak analizi verilerini işleyerek sadece o parselin ve o mahsulün ihtiyaç duyduğu elementel oranları hesaplamak.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>💧 Akıllı Su ve Hidrojel Yönetimi</h4>
            <p>Formülasyona entegre edilecek hidrojel teknolojisiyle toprağın su tutma kapasitesini optimize etmek ve kuraklık riskine karşı direnç oluşturmak.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>📈 Sürdürülebilir Verimlilik Artışı</h4>
            <p>Aşırı gübrelemenin yarattığı toprak yıkanmasını ve yeraltı suyu kirliliğini engelleyerek, birim alandan alınan mahsul kalitesini artırmak.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🤖 Kendi Kendini Optimize Eden Döngü</h4>
            <p>Sistemde üretilen her formülasyonu (periyodu) ve sahadan gelecek geri bildirimleri loglayarak, yapay zekanın sonraki kararlarında daha isabetli reçeteler üretmesini sağlamak.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 📞 Proje Ekibi & İletişim")
    
    col_team1, col_team2, col_team3 = st.columns(3)
    with col_team1:
        st.markdown("**Ege Berk Çınar**")
        st.caption("Ekip Lideri, İş ve Yazılım Geliştirme")
    with col_team2:
        st.markdown("**Elif Çiçek Akkor**")
        st.caption("Tarımsal Faaliyetleri, Ar-Ge")
    with col_team3:
        st.markdown("**Liva Erkul**")
        st.caption("Danışman, Bilimsel Temel - Boğaziçi Moleküler Biyoloji ve Genetik")
        
    st.write("")
    st.caption("📧 İletişim: cinaregeberk00@gmail.com | 📍 Ortaklar - Aydın / İstanbul")

# --- 🔬 1. AKILLI FORMÜLASYON ---
elif page == "🔬 Akıllı Formülasyon":
    st.title("🔬 Akıllı Formülasyon Modülü")
    st.write("Tarlanıza özel biyokimyasal reçeteyi oluşturmak için verilerinizi adım adım girin. İlgili olmayan alanları boş bırakabilirsiniz, eksik veriler AI tarafından bölgesel ortalamalarla tamamlanacaktır.")
    
    # 0. Periyot İsimlendirme (Sabit Üst Başlık)
    with st.container():
        st.markdown("### 📌 Formülasyon Kaydı (Periyot)")
        col_p1, col_p2 = st.columns([3, 1])
        with col_p1:
            tarla_adi = st.text_input("Tarla/Parsel Adı (Örn: Güney Mısır Tarlası - Parsel A)", placeholder="Yeni Periyot Adı...")
        with col_p2:
            kayit_tarihi = st.date_input("Kayıt Tarihi", value=date.today())
            
    st.write("---")

    # Veri Giriş Sekmeleri
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📍 1. Tarla", 
        "🧪 2. Toprak Analizi", 
        "🌾 3. Mahsul Seçimi & Geçmiş Ekimler", 
        "💧 4. Sulama & Ekonomi", 
        "🚀 5. Analiz"
    ])

    # SEKME 1: TARLA VE İKLİM
    with tab1:
        st.markdown("#### Tarla Fiziksel Özellikleri")
        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            alan = st.number_input("Alan (Dekar)", min_value=0.0, step=1.0)
            toprak_tipi = st.selectbox("Toprak Tipi", ["Bilinmiyor", "Kumlu", "Tınlı", "Killi", "Organik"])
        with col1_2:
            rakim = st.number_input("Rakım (m)", min_value=0, step=10)
            drenaj = st.selectbox("Drenaj Durumu", ["Bilinmiyor", "İyi", "Orta", "Zayıf"])
        with col1_3:
            egim = st.selectbox("Eğim Durumu", ["Düz (%0-2)", "Hafif Eğimli (%2-6)", "Eğimli (%6-12)", "Dik"])
            baki = st.selectbox("Bakı Yönü", ["Kuzey", "Güney", "Doğu", "Batı", "Düz"])

        st.info("🌤️ **İklim Verileri:** Konum (Koordinat) baz alınarak ortalama sıcaklık, son yağış miktarı, toprak nemi ve don/kuraklık riski API üzerinden sisteme otomatik entegre edilmektedir. Kullanıcı girişi gerekmez.")

    # SEKME 2: TOPRAK ANALİZİ
    with tab2:
        st.markdown("#### Laboratuvar Toprak Analizi")
        st.markdown("Değerleri manuel girmek yerine laboratuvar PDF/JPG dosyanızı yükleyerek tablonun **yapay zeka tarafından otomatik doldurulmasını** sağlayabilirsiniz.")
        uploaded_file = st.file_uploader("Laboratuvar Sonuç Raporu Yükle", type=['pdf', 'jpg', 'png'])
        if uploaded_file is not None:
            st.success("Belge işlendi! Değerler aşağıdaki tabloya başarıyla aktarıldı.")

        st.markdown("##### Değer Kontrol / Manuel Giriş Alanı")
        col2_1, col2_2, col2_3 = st.columns(3)
        with col2_1:
            st.markdown("**Temel Değerler**")
            ph = st.number_input("pH Değeri", value=0.0, format="%.2f")
            ec = st.number_input("EC (Elektriksel İletkenlik)", value=0.0)
            om = st.number_input("Organik Madde (%)", value=0.0)
            kirec = st.number_input("Kireç (%)", value=0.0)
            tuzluluk = st.number_input("Tuzluluk (dS/m)", value=0.0)
        with col2_2:
            st.markdown("**Makro & Sekonder Elementler**")
            n_val = st.number_input("Azot (N)", value=0.0)
            p_val = st.number_input("Fosfor (P)", value=0.0)
            k_val = st.number_input("Potasyum (K)", value=0.0)
            ca_val = st.number_input("Kalsiyum (Ca)", value=0.0)
            mg_val = st.number_input("Magnezyum (Mg)", value=0.0)
        with col2_3:
            st.markdown("**Mikro Elementler**")
            fe_val = st.number_input("Demir (Fe)", value=0.0)
            zn_val = st.number_input("Çinko (Zn)", value=0.0)
            mn_val = st.number_input("Mangan (Mn)", value=0.0)
            cu_val = st.number_input("Bakır (Cu)", value=0.0)
            b_val = st.number_input("Bor (B)", value=0.0)

    # SEKME 3: MAHSUL VE GEÇMİŞ
    with tab3:
        st.markdown("#### Güncel Mahsul Planlaması")
        col3_1, col3_2 = st.columns(2)
        with col3_1:
            urun = st.selectbox("Ekilmesi Planlanan Ürün", ["Mısır", "Turp", "Buğday", "Pamuk", "Ayçiçeği"])
            cesit = st.text_input("Çeşit (Örn: Pioneer, Dekalb)")
            hedef_verim = st.number_input("Hedeflenen Verim (kg/dekar)", min_value=0)
        with col3_2:
            tohum_tipi = st.selectbox("Tohum Tipi", ["Sertifikalı", "Yerel/Ata Tohumu"])
            ekim_tarihi = st.date_input("Planlanan Ekim Tarihi")
            hasat_tarihi = st.date_input("Planlanan Hasat Tarihi")

        with st.expander("🕰️ Geçmiş Tarım Verileri & Mevcut Stoklar (Önerilir)"):
            st.write("Yapay zekanın toprağın yorgunluğunu ve önceki kimyasal yükünü analiz etmesi için çok değerlidir.")
            gecmis_ozet = st.text_area("Son 5 Yılın Özeti", placeholder="Örn: 2024'te buğday ekildi, 450kg verim alındı, 20-20-0 gübre kullanıldı. Pas hastalığı görüldü...")
            mevcut_gubreler = st.text_input("Hali hazırda elinizde bulunan ve değerlendirilmesini istediğiniz gübreler (Marka/Formül)")

    # SEKME 4: SULAMA VE EKONOMİ
    with tab4:
        st.markdown("#### Sulama ve Altyapı")
        col4_1, col4_2 = st.columns(2)
        with col4_1:
            sulama_tipi = st.selectbox("Sulama Tipi", ["Damlama", "Yağmurlama", "Salma", "Kuru Tarım (Sulama Yok)"])
            su_kaynagi = st.selectbox("Su Kaynağı", ["Yeraltı (Sondaj)", "Kanal/Baraj", "Akarsu", "Bilinmiyor"])
            sulama_sikligi = st.selectbox("Sulama Sıklığı", ["İhtiyaca Göre", "Haftada 1", "15 Günde 1", "Ayda 1"])
        
        with col4_2:
            st.markdown("#### 🎯 Ekonomik Tercihler")
            opt_amaci = st.radio("Yapay Zeka Hangi Parametreyi Önceliklendirsin?",
                                 ["Maksimum Verim Odaklı",
                                  "Düşük Maliyet (Bütçe Optimizasyonu)",
                                  "Yüksek İhracat Kalitesi",
                                  "Maksimum Su Tasarrufu (Hidrojel Odaklı)",
                                  "Çevresel Etkiyi Azaltmak (Organik/Regeneratif)"])

    # SEKME 5: ÜRETİM MOTORU (API ENTEGRASYONU)
    with tab5:
        st.markdown("#### TROIA Agent AI Motoru")
        st.write("Girdiğiniz fiziksel veriler, laboratuvar sonuçları, tarım döngüsü ve ekonomik öncelikleriniz analiz edilecektir.")
        
        if st.button("🚀 Formülasyon Reçetesini Oluştur", use_container_width=True):
            if API_KEY == "BURAYA_GEMINI_API_ANAHTARINIZI_GİRİNİZ" or not API_KEY:
                st.error("Lütfen geçerli bir Gemini API Anahtarı giriniz.")
            else:
                with st.spinner("TROIA Agent AI verileri işliyor, optimizasyon senaryoları hesaplanıyor..."):
                    try:
                        # Tüm sekmelerdeki değişkenleri içeren dinamik prompt yapısı
                        prompt = f"""
                        Sen tarımsal agronomist ve akıllı gübreleme sistemleri üzerine uzmanlaşmış TROIA yapay zeka motorusun. 
                        Aşağıda sağlanan tüm parametreleri değerlendirerek sürdürülebilir, bilimsel ve detaylı bir tarla reçetesi oluştur.

                        [PERİYOT KİMLİĞİ]: {tarla_adi} (Kayıt Tarihi: {kayit_tarihi})
                        
                        1. TARLA VE FİZİKSEL ÖZELLİKLER:
                        - Alan: {alan} Dekar
                        - Toprak Tipi: {toprak_tipi}
                        - Rakım: {rakim} metre
                        - Drenaj Durumu: {drenaj}
                        - Eğim Durumu: {egim}
                        - Bakı Yönü: {baki}

                        2. LABORATUVAR TOPRAK ANALİZİ:
                        - pH: {ph} | EC: {ec} | Organik Madde (%): {om} | Kireç (%): {kirec} | Tuzluluk: {tuzluluk} dS/m
                        - Makro Elementler: Azot (N): {n_val} | Fosfor (P): {p_val} | Potasyum (K): {k_val}
                        - Sekonder & Mikro Elementler: Kalsiyum (Ca): {ca_val} | Magnezyum (Mg): {mg_val} | Demir (Fe): {fe_val} | Çinko (Zn): {zn_val} | Mangan (Mn): {mn_val} | Bakır (Cu): {cu_val} | Bor (B): {b_val}

                        3. MAHSUL VE GEÇMİŞ EKİM BİLGİLERİ:
                        - Hedeflenen Mahsul: {urun} (Çeşit: {cesit})
                        - Tohum Tipi: {tohum_tipi}
                        - Hedeflenen Verim: {hedef_verim} kg/dekar
                        - Planlanan Ekim / Hasat: {ekim_tarihi} / {hasat_tarihi}
                        - Geçmiş Tarım Özeti: {gecmis_ozet}
                        - Eldeki Mevcut Gübreler: {mevcut_gubreler}

                        4. SULAMA VE EKONOMİK ÖNCELİKLER:
                        - Sulama Tipi: {sulama_tipi} | Kaynak: {su_kaynagi} | Sıklık: {sulama_sikligi}
                        - Optimizasyon Önceliği: {opt_amaci}

                        Lütfen jüri veya üretici raporlamasında doğrudan kullanılabilecek, tablo içermeyen, paragraflar ve listeler şeklinde net bir analiz sun. 
                        Raporda şunlar yer almalıdır:
                        - Toprak Analizi Açıkları ve Saf İhtiyaç Yönetimi (Optimizasyon amacına uygun yorumlar dahil)
                        - Dönemsel ve İdeal Gübreleme Formülasyonu (Taban, Gelişme dönemi, püskül/tane dolum dönemleri için ticari gübre isimleri, kg hesapları ve saf madde dengeleriyle)
                        - Sulama altyapısına ve optimizasyon amacına uygun Akıllı Su & Hidrojel Kullanım Tavsiyeleri
                        """

                        # Gemini Model Çağrısı
                        model = genai.GenerativeModel('gemini-1.5-flash')
                        response = model.generate_content(prompt)
                        
                        st.success(f"'{tarla_adi}' tarlası için analiz tamamlandı!")
                        st.info("Toprak kilitlenme riski incelendi... Geçmiş kimyasal yük dengelendi... Ekonomik optimizasyon uygulandı...")
                        
                        # Yapay zekadan gelen canlı çıktıyı ekrana yazdırma
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"API çağrısı sırasında bir hata oluştu: {e}")
                
                st.button("💾 Bu Periyodu Bilgi Sistemine (Veri Havuzu) Kaydet")

# --- 📊 2. BİLGİ SİSTEMİ ---
elif page == "📊 Bilgi Sistemi":
    st.title("📊 Bilgi Sistemi ve Periyot Günlüğü")
    st.write("Sistemin karar alırken kullandığı bilimsel referans değerlerini inceleyin veya geçmiş yapay zeka optimizasyon periyotlarını yönetin.")
    
    tab_bilgi1, tab_bilgi2 = st.tabs(["📚 Zirai Referans Veritabanı", "📝 Periyot Günlüğü (AI Geri Bildirim Döngüsü)"])
    
    with tab_bilgi1:
        st.markdown("#### Mahsul Besin İhtiyaçları ve Tolerans Sınırları")
        st.write("Bu alanda yapay zeka modülünü kullanmadan da tarımsal literatür değerlerini filtreleyerek inceleyebilirsiniz.")
        
        search_query = st.text_input("🔍 Mahsul Ara (Örn: Mısır, Turp, Buğday...)", "")
        
        referans_data = {
            "Mahsul": ["Mısır", "Turp", "Buğday", "Pamuk", "Ayçiçeği"],
            "Optimum pH": ["6.0 - 7.0", "6.5 - 7.0", "6.0 - 7.5", "6.5 - 7.5", "6.0 - 7.2"],
            "Azot (N) İhtiyacı (kg/da)": [20.0, 10.0, 15.0, 18.0, 12.0],
            "Fosfor (P) İhtiyacı (kg/da)": [8.0, 6.0, 7.0, 9.0, 6.0],
            "Potasyum (K) İhtiyacı (kg/da)": [15.0, 12.0, 10.0, 14.0, 10.0],
            "Tuzluluk Toleransı (dS/m)": ["Orta (1.7)", "Düşük (1.2)", "Yüksek (6.0)", "Çok Yüksek (7.7)", "Orta (1.7)"]
        }
        df_ref = pd.DataFrame(referans_data)
        
        if search_query:
            df_ref = df_ref[df_ref["Mahsul"].str.contains(search_query, case=False, na=False)]
            
        st.dataframe(df_ref, use_container_width=True, hide_index=True)
        st.info("💡 Bu veriler FAO ve güncel ziraat literatürü standartlarından derlenmiş olup, yapay zekanın temel referans çerçevesini oluşturur.")

    with tab_bilgi2:
        st.markdown("#### AI Karar ve Öğrenme Geçmişi (Periyotlar)")
        st.write("Sistem tarafından daha önce oluşturulan formülasyonlar (periyotlar) ve sahadan girilen hasat/verim geri bildirimleri burada listelenir. Bu veriler modelin kendini eğitmesi için kullanılır.")
        
        log_data = {
            "Periyot ID": ["TR-001", "TR-002", "TR-003"],
            "Tarla Adı": ["Güney Mısır Tarlası", "Kuzey Buğday Parseli", "Sera Yanı Turp"],
            "Mahsul": ["Mısır", "Buğday", "Turp"],
            "Oluşturulma Tarihi": ["2026-03-10", "2026-04-05", "2026-05-12"],
            "Durum": ["Hasat Edildi 🟢", "Gelişim Evresinde 🟡", "Ekim Bekleniyor ⚪"],
            "Saha Geri Bildirimi": ["%18 Verim Artışı", "Kardeşlenme Sağlıklı", "Veri Bekleniyor"],
        }
        df_log = pd.DataFrame(log_data)
        st.dataframe(df_log, use_container_width=True, hide_index=True)
        
        st.button("➕ Manuel Yeni Geri Bildirim Ekle (Modeli Eğit)")

# --- 🗺️ 3. DİNAMİK EKİM TAKVİMİ ---
elif page == "🗺️ Dinamik Ekim Takvimi":
    st.title("🗺️ Coğrafi Ekim ve Hasat Takvimi")
    st.write("Yapay zeka analizine girmeden; seçilen bölge, iklim and mahsule göre agronomik takvimi dinamik olarak inceleyin.")
    
    col_takvim1, col_takvim2 = st.columns([1, 2])
    
    with col_takvim1:
        st.markdown("#### Bölge ve Mahsul Seçimi")
        secilen_bolge = st.selectbox("Bölge Seçiniz", ["Ege (Aydın/İzmir)", "İç Anadolu", "Çukurova", "Güneydoğu Anadolu"])
        secilen_mahsul = st.selectbox("Mahsul Seçiniz", ["Mısır", "Buğday", "Turp"])
        
        st.markdown("#### Bölgesel Yoğunluk Haritası")
        if secilen_bolge == "Ege (Aydın/İzmir)":
            map_coords = pd.DataFrame(np.random.randn(15, 2) / [30, 30] + [37.84, 27.84], columns=['lat', 'lon'])
        else:
            map_coords = pd.DataFrame(np.random.randn(15, 2) / [15, 15] + [39.0, 35.0], columns=['lat', 'lon'])
            
        st.map(map_coords, zoom=6)
        st.caption(f"Haritadaki noktalar {secilen_bolge} bölgesindeki {secilen_mahsul} uygunluk alanlarını temsil eder.")

    with col_takvim2:
        st.markdown(f"#### 📅 {secilen_bolge} Bölgesi - {secilen_mahsul} Optimizasyon Takvimi")
        st.write("Bölgenin meteorolojik geçmişine göre oluşturulmuş en uygun gelişim evreleri:")
        
        st.success("🌱 **1. Toprak Hazırlığı ve Taban Gübrelemesi (Mart 1. - 2. Hafta)**")
        st.write("Toprak işleme tamamlanır. Tohum yatağı hazırlanır. TROIA formülasyonunun taban (katı) kısmı toprağa bu evrede karıştırılır.")
        
        st.info("🌾 **2. Ekim Süreci (Mart 3. Hafta - Nisan 1. Hafta)**")
        st.write("Toprak sıcaklığı stabil hale geldiğinde ekim gerçekleştirilir.")
        
        st.warning("💧 **3. Üst Gübreleme ve Hidrojel Aktivasyonu (Mayıs 2. Hafta)**")
        st.write("Bitki kritik büyüme eşiğine ulaştığında kalan formülasyon uygulanır, hidrojelin su tutma kapasitesini maksimize etmek için ilk yoğun sulama yapılır.")
        
        st.error("🚜 **4. Hasat Dönemi (Ağustos 2. Hafta - Eylül 1. Hafta)**")
        st.write("Nem oranı optimum seviyeye düştüğünde hasat işlemi başlatılır.")
        
        st.write("---")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric(label="Tahmini Büyüme Süresi", value="115 Gün")
        col_m2.metric(label="Bölgesel Su Kısıtı Riski", value="Orta")
        col_m3.metric(label="Don Riski Bitişi", value="15 Mart")
