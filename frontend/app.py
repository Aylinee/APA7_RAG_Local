import streamlit as st
import requests

# AYARLAR
BACKEND_URL = "http://127.0.0.1:8001/generate-bibliography/"

st.set_page_config(page_title="APA 7 - Next Gen AI", page_icon="🧬", layout="wide")

st.title("🧬 Yeni Nesil Kaynakça Asistanı")
st.markdown(
    """
    Bu sistem **Gemini 2.5 ve 3.0** serisi gelişmiş modelleri kullanır.
    PDF dosyalarınızı yükleyin, modelinizi seçin ve arkanıza yaslanın.
    """
)

# --- SIDEBAR: MODEL SEÇİMİ (GÖRSELDEKİ LİSTE) ---
with st.sidebar:
    st.header("🧠 Model Motoru")
    
    # Ekran görüntüsündeki modellere uygun ID listesi
    selected_model = st.selectbox(
        "Kullanılacak Modeli Seçin:",
        options=[
            "gemini-3.0-flash-preview",   # Gemini 3 Flash Preview
            "gemini-2.5-pro",             # Gemini 2.5 Pro
            "gemini-2.5-flash",           # Gemini 2.5 Flash
            "gemini-2.5-flash-lite",      # Gemini 2.5 Flash-Lite
            "gemini-2.0-flash",           # Gemini 2.0 Flash
            "gemini-2.0-flash-lite",      # Gemini 2.0 Flash-Lite (Fallback)
        ],
        index=0, # Varsayılan olarak en güçlü/yeni olanı seçelim
        help="Eğer seçtiğiniz model (örn: Preview) hata verirse, sistem otomatik olarak '2.0-flash-lite' modeline geçecektir."
    )
    
    st.divider()
    st.success(f"Seçili Motor: **{selected_model}**")
    st.info("ℹ️ Not: 1.5 serisi modeller bu listeden kaldırılmıştır.")

# --- ANA EKRAN ---
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_files = st.file_uploader(
        "📂 PDF Dosyalarını Buraya Yükle", 
        type=["pdf"], 
        accept_multiple_files=True
    )

with col2:
    st.write("### ⚙️ İşlem Paneli")
    if uploaded_files:
        st.success(f"{len(uploaded_files)} dosya hazır.")
        process_btn = st.button("Analizi Başlat ⚡", type="primary", use_container_width=True)
    else:
        st.info("Dosya bekleniyor...")
        process_btn = False

if process_btn and uploaded_files:
    with st.spinner(f"🚀 {selected_model} modeli çalışıyor... (Yedek: 2.0-Lite)"):
        try:
            # 1. Dosyaları Hazırla
            files_payload = [
                ("files", (file.name, file.getvalue(), "application/pdf")) 
                for file in uploaded_files
            ]
            
            # 2. Seçilen Modeli Backend'e Gönder
            data_payload = {"model_id": selected_model}

            # 3. İsteği At
            response = requests.post(
                BACKEND_URL, 
                files=files_payload, 
                data=data_payload,
                timeout=180 # Büyük modeller için süreyi uzattık
            )

            # 4. Sonucu İşle
            if response.status_code == 200:
                st.balloons()
                st.success("✅ İşlem Tamamlandı!")
                
                st.download_button(
                    label="📥 APA 7 Word Dosyasını İndir",
                    data=response.content,
                    file_name=f"kaynakca_{selected_model}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
            else:
                st.error(f"⚠️ Hata Oluştu: {response.status_code}")
                try:
                    st.json(response.json())
                except:
                    st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("🚨 Sunucuya ulaşılamadı! Terminalde 'main.py' açık mı?")
        except Exception as e:
            st.error(f"Beklenmeyen Hata: {e}")