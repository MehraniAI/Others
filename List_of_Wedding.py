import streamlit as st
import pandas as pd
import os

# 🎉 App title
st.title("💒 Sohail Kumar Wedding – Guest List Manager")

# CSV file to store guests
DATA_FILE = "guest_list.csv"

# Load guest list from file or initialize
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)

    # ✅ Auto-fix Suhail → Sohail if it exists
    df['Name'] = df['Name'].replace('Mr. Suhail Kumar', 'Mr. Sohail Kumar')
    df.to_csv(DATA_FILE, index=False)

else:
    df = pd.DataFrame({
        'SR#': list(range(1, 23)),
        'Name': [
            'Mr. Moti Ram', 'Mr. Chahnoo Mal', 'Mr. Suresh Kumar', 'Mr. Chetan Mal', 'Mr. Karo Mal',
            'Mr. Jhandho Mal', 'Mr. Bhamar Lal', 'Mr. Prem Kumar', 'Mr. Keship Lal', 'Mr. Prem Manjani',
            'Mr. Roop Chand Tapedar', 'Mr. Partab Ria HST', 'Mr.', 'Mr. Anand Kumar', 'Mr. Dileep Kumar PST',
            'Mr. Rejhoo Mal JST', 'Mr. Mendharo Mal', 'Mr. Sawan Sindhi Advocate', 'Mr. Sikandar ASI',
            'Mr. Khusal Kumar Adovcate', 'Mr. Tinoo Mal', 'Mr. Sohail Kumar'  # ✅ fixed name here
        ],
        'Village/City': [
            'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena',
            'Malhanor Veena', 'Malhanor Veena', '', '', '', 'Islamkot', 'Mithi', '', 'Kalio', 'Kalio',
            'Kalio', 'Sobedar Sarang', 'Karachi', 'Badin', 'Karachi', 'Sobedar Sarang', ''
        ],
        'Invited': [False] * 22
    })
    df.to_csv(DATA_FILE, index=False)

# --- Add new guest ---
with st.form("add_guest"):
    name = st.text_input("Enter guest name:")
    village = st.text_input("Enter Village/City:")
    invited = st.checkbox("Invited ✅")
    submitted = st.form_submit_button("Add Guest")

    if submitted:
        if name.strip():
            new_sr = df['SR#'].max() + 1 if not df.empty else 1
            new_guest = pd.DataFrame({
                'SR#': [new_sr],
                'Name': [name.strip()],
                'Village/City': [village.strip()],
                'Invited': [invited]
            })
            df = pd.concat([df, new_guest], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Added: {name}")
        else:
            st.warning("⚠️ Please enter a name before adding.")

st.divider()

# --- Display guest list ---
if not df.empty:
    st.subheader("📋 Guest List")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # --- Edit or remove guest ---
    names = df['Name'].dropna().tolist()
    if names:
        selected = st.selectbox("Select a guest to edit/remove:", names)
        guest_index = df[df['Name'] == selected].index[0]

        new_name = st.text_input("Edit Name:", df.at[guest_index, 'Name'])
        new_village = st.text_input("Edit Village/City:", df.at[guest_index, 'Village/City'])
        new_invited = st.checkbox("Invited ✅", value=bool(df.at[guest_index, 'Invited']))

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Update Changes"):
                df.at[guest_index, 'Name'] = new_name
                df.at[guest_index, 'Village/City'] = new_village
                df.at[guest_index, 'Invited'] = new_invited
                df.to_csv(DATA_FILE, index=False)
                st.success("✅ Changes saved successfully!")

        with col2:
            if st.button("🗑️ Remove Guest"):
                df = df.drop(guest_index).reset_index(drop=True)
                df.to_csv(DATA_FILE, index=False)
                st.success(f"🗑️ Removed {selected}")

else:
    st.info("No guests added yet. Add some above!")

# --- Footer / Credit line ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🖋️ Prepared by <b>Susheel Kumar</b></p>", unsafe_allow_html=True)
