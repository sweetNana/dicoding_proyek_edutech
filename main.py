import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Prediksi Status Mahasiswa dari CSV",
    page_icon="🎓",
    layout="wide"
)

# --- Fungsi untuk Memuat Model (dengan caching) ---
@st.cache_resource
def load_assets():
    """Memuat model, scaler, dan label encoder yang telah dilatih."""
    try:
        model = joblib.load('model/model_rf.pkl')
        scaler = joblib.load('model/scaler.pkl')
        label_encoders = joblib.load('model/label_encoders.pkl')
        training_cols = scaler.get_feature_names_out()
        return model, scaler, label_encoders, training_cols
    except FileNotFoundError:
        st.error("File model atau preprocessing tidak ditemukan. Pastikan path file benar: 'model/model_rf.pkl', 'model/scaler.pkl', 'model/label_encoders.pkl'")
        return None, None, None, None
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat aset model: {e}")
        return None, None, None, None

# Memuat aset
model, scaler, label_encoders, training_cols = load_assets()

# --- Fungsi untuk Prediksi Batch dari DataFrame ---
def predict_batch(df_input):
    """Fungsi untuk melakukan prediksi pada seluruh DataFrame."""
    if model is None or scaler is None or label_encoders is None:
        return None, "Aset model tidak berhasil dimuat."

    df = df_input.copy()

    # Terapkan Label Encoding ke kolom kategorikal
    for col, le in label_encoders.items():
        if col in df.columns:
            try:
                # Mengatasi nilai yang mungkin tidak ada dalam encoder dengan menggantinya menjadi nilai yang paling sering muncul
                # atau cara lain yang lebih baik adalah dengan memastikan data bersih
                known_values = le.classes_
                df[col] = df[col].apply(lambda x: x if x in known_values else np.nan)
                # Jika ada NaN setelah filter, bisa diisi dengan modus atau dibiarkan untuk error
                if df[col].isnull().any():
                    st.warning(f"Kolom '{col}' memiliki nilai yang tidak dikenali dan akan diabaikan. Ini dapat mempengaruhi akurasi.")
                    # Opsi: isi dengan modus
                    # mode_val = le.transform([df[col].mode()[0]])[0]
                    # df[col] = df[col].fillna(mode_val)
                    df.dropna(subset=[col], inplace=True) # Hapus baris dengan nilai tak dikenal
                
                if not df.empty:
                    df[col] = le.transform(df[col])

            except Exception as e:
                return None, f"Error saat encoding kolom '{col}': {e}"
    
    if df.empty:
        return None, "Tidak ada data valid untuk diprediksi setelah membersihkan nilai yang tidak dikenal."

    # Pastikan urutan kolom dan ketersediaan kolom sesuai dengan saat training
    try:
        df = df[training_cols]
    except KeyError as e:
        return None, f"Kolom input pada file CSV tidak sesuai dengan model. Kolom yang hilang: {e}"
    except Exception as e:
        return None, f"Gagal menyusun ulang kolom sesuai model: {e}"

    # Scaling fitur
    data_scaled = scaler.transform(df)

    # Lakukan prediksi
    predictions = model.predict(data_scaled)
    
    # Mapping hasil prediksi ke label asli
    label_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
    predicted_labels = [label_map.get(p, 'Tidak Diketahui') for p in predictions]

    return predicted_labels, None # Mengembalikan list label, error di set ke None


# --- Antarmuka (UI) Streamlit ---

# Judul Utama
st.title("🎓 Aplikasi Prediksi Status Kelulusan Mahasiswa")
st.markdown("Unggah file CSV dengan data mahasiswa untuk mendapatkan prediksi status kelulusan (Lulus, Terdaftar, atau Dropout).")
st.markdown("---")

# --- Komponen Upload File ---
uploaded_file = st.file_uploader(
    "Pilih file CSV",
    type="csv",
    help="Pastikan file CSV Anda memiliki kolom yang sama dengan data training."
)

# Hanya jalankan jika model berhasil dimuat dan file diunggah
if model and scaler and label_encoders and training_cols is not None:
    if uploaded_file is not None:
        try:
            # Membaca data dari file CSV yang diunggah
            input_df = pd.read_csv(uploaded_file)
            st.subheader("Data Asli dari File CSV")
            st.dataframe(input_df.head(), use_container_width=True)

            # Tombol untuk memulai prediksi
            if st.button('**Mulai Prediksi**', use_container_width=True, type="primary"):
                with st.spinner('Menganalisis data dan melakukan prediksi...'):
                    
                    original_data_to_show = input_df.copy()

                    predicted_labels, error_message = predict_batch(input_df)

                    if error_message:
                        st.error(error_message)
                    else:
                        # Menambahkan kolom hasil prediksi ke DataFrame asli
                        original_data_to_show['Prediksi Status'] = predicted_labels
                        
                        st.subheader("Hasil Prediksi")
                        st.dataframe(original_data_to_show, use_container_width=True)
                        
                        # Opsi untuk mengunduh hasil
                        @st.cache_data
                        def convert_df_to_csv(df):
                           return df.to_csv(index=False).encode('utf-8')

                        csv_output = convert_df_to_csv(original_data_to_show)

                        st.download_button(
                           label="📥 Unduh Hasil Prediksi (CSV)",
                           data=csv_output,
                           file_name='hasil_prediksi_mahasiswa.csv',
                           mime='text/csv',
                           use_container_width=True
                        )

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses file: {e}")
else:
    st.warning("Aplikasi tidak dapat berjalan karena gagal memuat file model. Mohon periksa kembali file Anda di folder `model/`.")
