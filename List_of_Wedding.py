import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(
    page_title="Suhail Kumar Marriage List",
    page_icon="💍",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<div class="main-header">💍 Suhail Kumar Marriage List</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">List of guests for the wedding ceremony</div>', unsafe_allow_html=True)

    # Default guest data
    data = {
        'SR#': list(range(1, 23)),
        'Name': [
            'Mr. Moti Ram', 'Mr. Chahnoo Mal', 'Mr. Suresh Kumar', 'Mr. Chetan Mal', 'Mr. Karo Mal',
            'Mr. Jhandho Mal', 'Mr. Bhamar Lal', 'Mr. Prem Kumar', 'Mr. Keship Lal', 'Mr. Prem Manjani',
            'Mr. Roop Chand Tapedar', 'Mr. Partab Ria HST', 'Mr.', 'Mr. Anand Kumar', 'Mr. Dileep Kumar PST',
            'Mr. Rejhoo Mal JST', 'Mr. Mendharo Mal', 'Mr. Sawan Sindhi Advocate', 'Mr. Sikandar ASI',
            'Mr. Khusal Kumar Adovcate', 'Mr. Tinoo Mal', ''
        ],
        'Village/City': [
            'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena', 'Malhanor Veena',
            'Malhanor Veena', 'Malhanor Veena', '', '', '', 'Islamkot', 'Mithi', '', 'Kalio', 'Kalio',
            'Kalio', 'Sobedar Sarang', 'Karachi', 'Badin', 'Karachi', 'Sobedar Sarang', ''
        ],
        'WhatsApp No': [''] * 22,
        'Invited': ['❌'] * 22  # Default not invited
    }

    df = pd.DataFrame(data)

    # --- Edit Mode ---
    edit_mode = st.checkbox("✏️ Enable Edit Mode")

    if edit_mode:
        st.subheader("🧾 Edit Guest List (Mark ✅ for invited guests)")
        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "Invited": st.column_config.SelectboxColumn(
                    "Invited",
                    options=["✅", "❌"],
                    help="Mark guest as invited (✅) or not invited (❌)"
                )
            }
        )
        st.write("✅ Edited guest list below:")
        st.dataframe(edited_df, use_container_width=True)
        df = edited_df
    else:
        st.dataframe(df, use_container_width=True, hide_index=True, height=800)

    # --- Stats Section ---
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Guests", len(df))
    with col2:
        invited_count = (df['Invited'] == '✅').sum()
        st.metric("Invited Guests ✅", invited_count)
    with col3:
        not_invited = (df['Invited'] == '❌').sum()
        st.metric("Not Invited ❌", not_invited)
    with col4:
        villages_with_data = df[df['Village/City'] != '']['Village/City'].nunique()
        st.metric("Cities/Villages", villages_with_data)

    # --- Filter Guests ---
    st.subheader("🔍 Filter Guests")
    col1, col2, col3 = st.columns(3)
    with col1:
        village_filter = st.selectbox(
            "Filter by Village/City:",
            options=['All'] + sorted(df['Village/City'].unique().tolist())
        )
    with col2:
        search_name = st.text_input("Search by Name:")
    with col3:
        invited_filter = st.selectbox("Filter by Invitation Status:", ['All', '✅ Invited', '❌ Not Invited'])

    filtered_df = df.copy()

    if village_filter != 'All':
        filtered_df = filtered_df[filtered_df['Village/City'] == village_filter]
    if search_name:
        filtered_df = filtered_df[filtered_df['Name'].str.contains(search_name, case=False, na=False)]
    if invited_filter == '✅ Invited':
        filtered_df = filtered_df[filtered_df['Invited'] == '✅']
    elif invited_filter == '❌ Not Invited':
        filtered_df = filtered_df[filtered_df['Invited'] == '❌']

    if len(filtered_df) != len(df):
        st.subheader(f"Filtered Results ({len(filtered_df)} guests)")
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # --- Download Button ---
    st.subheader("📥 Download Data")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="suhail_kumar_marriage_list.csv",
        mime="text/csv"
    )

    # Footer
    st.markdown("---")
    st.markdown("**Wedding Guest List** • Created with Streamlit")

if __name__ == "__main__":
    main()
