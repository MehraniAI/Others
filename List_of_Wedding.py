import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Suhail Kumar Marriage List",
    page_icon="💍",
    layout="wide"
)

# Custom CSS for better styling
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
    .dataframe {
        width: 100%;
    }
    .dataframe thead th {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .dataframe tbody tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .dataframe tbody tr:hover {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="main-header">💍 Suhail Kumar Marriage List</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">List of guests for the wedding ceremony</div>', unsafe_allow_html=True)
    
    # Create the data
    data = {
        'SR#': list(range(1, 23)),
        'Name': [
            'Mr. Moti Ram',
            'Mr. Chahnoo Mal',
            'Mr. Suresh Kumar',
            'Mr. Chetan Mal',
            'Mr. Karo Mal',
            'Mr. Jhandho Mal',
            'Mr. Bhamar Lal',
            'Mr. Prem Kumar',
            'Mr. Keship Lal',
            'Mr. Prem Manjani',
            'Mr. Roop Chand Tapedar',
            'Mr. Partab Ria HST',
            'Mr.',
            'Mr. Anand Kumar',
            'Mr. Dileep Kumar PST',
            'Mr. Rejhoo Mal JST',
            'Mr. Mendharo Mal',
            'Mr. Sawan Sindhi Advocate',
            'Mr. Sikandar ASI',
            'Mr. Khusal Kumar Adovcate',
            'Mr. Tinoo Mal',
            ''
        ],
        'Village/City': [
            'Malhanor Veena',
            'Malhanor Veena',
            'Malhanor Veena',
            'Malhanor Veena',
            'Malhanor Veena',
            'Malhanor Veena',
            'Malhanor Veena',
            '',
            '',
            '',
            'Islamkot',
            'Mithi',
            '',
            'Kalio',
            'Kalio',
            'Kalio',
            'Sobedar Sarang',
            'Karachi',
            'Badin',
            'Karachi',
            'Sobedar Sarang',
            ''
        ],
        'WhatsApp No': [''] * 22
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Display the table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=800
    )
    
    # Add some statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Guests", len(df))
    
    with col2:
        villages_with_data = df[df['Village/City'] != '']['Village/City'].nunique()
        st.metric("Cities/Villages", villages_with_data)
    
    with col3:
        complete_profiles = len(df[(df['Name'] != '') & (df['Name'] != 'Mr.')])
        st.metric("Complete Profiles", complete_profiles)
    
    # Add a section for filtering
    st.subheader("🔍 Filter Guests")
    
    col1, col2 = st.columns(2)
    
    with col1:
        village_filter = st.selectbox(
            "Filter by Village/City:",
            options=['All'] + sorted(df['Village/City'].unique().tolist())
        )
    
    with col2:
        search_name = st.text_input("Search by Name:")
    
    # Apply filters
    filtered_df = df.copy()
    
    if village_filter != 'All':
        filtered_df = filtered_df[filtered_df['Village/City'] == village_filter]
    
    if search_name:
        filtered_df = filtered_df[filtered_df['Name'].str.contains(search_name, case=False, na=False)]
    
    if village_filter != 'All' or search_name:
        st.subheader(f"Filtered Results ({len(filtered_df)} guests)")
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )
    
    # Add download button
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