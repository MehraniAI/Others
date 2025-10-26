import streamlit as st
import pandas as pd

st.set_page_config(page_title="💍 Suhail Kumar Wedding List", page_icon="💍", layout="wide")

st.title("💍 Suhail Kumar Wedding Guest List Manager")

# Default data
default_data = {
    "SR#": list(range(1, 23)),
    "Name": [
        "Mr. Moti Ram", "Mr. Chahnoo Mal", "Mr. Suresh Kumar", "Mr. Chetan Mal", "Mr. Karo Mal",
        "Mr. Jhandho Mal", "Mr. Bhamar Lal", "Mr. Prem Kumar", "Mr. Keship Lal", "Mr. Prem Manjani",
        "Mr. Roop Chand Tapedar", "Mr. Partab Ria HST", "Mr.", "Mr. Anand Kumar", "Mr. Dileep Kumar PST",
        "Mr. Rejhoo Mal JST", "Mr. Mendharo Mal", "Mr. Sawan Sindhi Advocate", "Mr. Sikandar ASI",
        "Mr. Khusal Kumar Adovcate", "Mr. Tinoo Mal", ""
    ],
    "Village/City": [
        "Malhanor Veena", "Malhanor Veena", "Malhanor Veena", "Malhanor Veena", "Malhanor Veena",
        "Malhanor Veena", "Malhanor Veena", "", "", "", "Islamkot", "Mithi", "", "Kalio", "Kalio",
        "Kalio", "Sobedar Sarang", "Karachi", "Badin", "Karachi", "Sobedar Sarang", ""
    ]
}

# Add "Invited" status
default_df = pd.DataFrame(default_data)
default_df["Invited"] = [False] * len(default_df)

# Load session data
if "guests" not in st.session_state:
    st.session_state.guests = default_df.copy()

# Form to add new guest
st.subheader("➕ Add New Guest")
with st.form("add_guest"):
    name = st.text_input("Enter Guest Name:")
    village = st.text_input("Enter Village/City:")
    invited = st.checkbox("Invited ✅")
    submitted = st.form_submit_button("Add Guest")

    if submitted:
        if name.strip():
            new_row = {
                "SR#": len(st.session_state.guests) + 1,
                "Name": name.strip(),
                "Village/City": village.strip(),
                "Invited": invited
            }
            st.session_state.guests = pd.concat(
                [st.session_state.guests, pd.DataFrame([new_row])],
                ignore_index=True
            )
            st.success(f"Added guest: {name}")
        else:
            st.warning("⚠️ Please enter a name before adding.")

st.divider()

# Show guest list
st.subheader("📋 Guest List")

# Show Invited status as ✅ or ❌
df = st.session_state.guests.copy()
df["Status"] = df["Invited"].apply(lambda x: "✅ Invited" if x else "❌ Not Invited")

st.dataframe(df[["SR#", "Name", "Village/City", "Status"]], use_container_width=True)

st.divider()

# Edit or remove guest
if not df.empty:
    st.subheader("✏️ Edit / Remove Guest")

    names = df["Name"].tolist()
    selected = st.selectbox("Select a guest:", names)

    if selected:
        guest_index = df[df["Name"] == selected].index[0]
        guest = df.loc[guest_index]

        new_name = st.text_input("Edit Name:", guest["Name"], key="edit_name")
        new_village = st.text_input("Edit Village/City:", guest["Village/City"], key="edit_village")
        new_invited = st.checkbox("Invited ✅", value=guest["Invited"], key="edit_invited")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save Changes"):
                st.session_state.guests.at[guest_index, "Name"] = new_name
                st.session_state.guests.at[guest_index, "Village/City"] = new_village
                st.session_state.guests.at[guest_index, "Invited"] = new_invited
                st.success(f"✅ Updated {new_name}")
        with col2:
            if st.button("🗑️ Remove Guest"):
                st.session_state.guests = st.session_state.guests.drop(guest_index).reset_index(drop=True)
                st.success(f"❌ Removed {selected}")

st.divider()

# Statistics
total_guests = len(st.session_state.guests)
invited_count = sum(st.session_state.guests["Invited"])
not_invited = total_guests - invited_count
villages_count = st.session_state.guests["Village/City"].replace("", None).nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Guests", total_guests)
col2.metric("Invited ✅", invited_count)
col3.metric("Villages/Places", villages_count)
