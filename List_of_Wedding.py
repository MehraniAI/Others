import streamlit as st
import pandas as pd
import os

st.title("💒 Sohail Kumar Wedding – Guest List Manager")

DATA_FILE = "guest_list.csv"

# ✅ All existing guest names
names = [
    "Adv, Vasand Thari", "Adv. Devat Rai", "Adv. Dayal Das", "Adv. Mohan Lal Manthrani", "Ugo Mal DDA",
    "Adv. Kanji Mal ASC MPK", "Ad, Altaf junejo Sindh Bar council", "Adv. Sarang Ram", "Adv. Qamat Rai",
    "Adv. Permanand", "Adv. Ramesh Kumar", "Adv. Shanker Lal Meghwar", "Adv. Hotchand Togani", "Adv. Vishandas",
    "Adv. Dasrat kumar Sukhani", "Gulab rai MRI", "Adv, Raichand Harijan MPK", "Adv. Ramchand Archna",
    "Adv. Kuldeep sharma", "Adv. Sheroz Chang", "Adv. Asad ali Murree", "Dasrat Kumar", "Adv. Chaman Lal",
    "Adv Pithumal Parwano", "Adv. Love Kumar", "Adv. Ranghan", "Adv. Shoukat Sindhi", "Adv. Shanker Lal Rathore",
    "Adv. Dayal Das Meghwar", "Adv. Zaheer Nohri", "Adv. Zaheeruddin Junejo", "Adv. Suneel Shatrogan",
    "Adv. Bhoro Kolhi", "Adv. Chander Kumar Kolhi", "Adv. Anad Gonh", "Adv. Bhrulal Heemarani", "Adv. Rajesh Kumar",
    "Adv. Suneel Kumar goswami", "Adv. Teerath kumar Jhangi", "Adv. Vikram meshwari", "Adv. Vishal",
    "Adv. Pirkash singh", "Adv. Bharat heemrani", "Adv. Tano mal", "Mukesh revenue mithi", "Adv. Qurban ali samejo",
    "Adv. Heemraj bheel", "Adv. Kewal gomani", "Adv. Ghamoon mal", "Adv. Lajpat rai panjwani", "Adv. Om parkash",
    "Adv. Leelaram", "Adv. Rai singh sodho", "Adv. Kanwar amar", "Adv. Zakaullah bajeer", "Adv. Bhawan kumar MPK",
    "Adv. Hamir ji bheel", "Adv. Mustafa hingorjo", "Adv. Roopchan ragastani", "Suresh jodhani DDA",
    "Adv. Faqeer munwar sagar", "Lekhraj Mithi", "Vishan das nahto", "Amar lal nahto", "Rajnesh kumar",
    "Ramesh kumar halerio", "Ashok kumar diplo", "Amolakh das Uk", "Adv. Preet pal singh", "Adv. Roopl mala singh",
    "Adv. Dileep kummar Karachi", "Adv. Subhan Samejo", "Adv. Faresh Kumar", "Adv. Subash Sharma",
    "Adv. Adam rajar", "Adv. Anchalaram", "Adv. Ashaque ali bajeer", "Adv. Bhagchand bheel", "Adv .Bhgwandas bheel",
    "Adv. Bhopat kolhi", "Adv. Faqeer mohd laghari", "Adv. Ghulamullah abro", "Adv. Hamlesh suthar",
    "Adv. Islamuddin rahmoon", "Adv. Javaid Akhtar", "Adv. Kundhan malhi", "Adv. Malook khaskhali",
    "Adv. Maeen bajeer", "Adv. Mir Moh samejo", "Adv. Mohan lal rathore MPK", "Adv. Moula bux bajeer",
    "Adv. Muhammad bajeer", "Adv. Muhammad hingorjo", "Adv. Nabi bux Inspector", "Adv. Naeem Talpur APG",
    "Adv. Neel Parkash MPK", "Adv. Partab rai", "Adv. Rafique Hingorjo", "Adv. Kabeer Rajar",
    "Adv. Mohan lal bheel", "Adv. Santosh kolhi", "Adv. Shanker Suthar", "Adv. Hemandas Sanghani",
    "Adv. Parkash Kumar", "Adv. Chaman Lal", "Adv. Dhanraj Palani", "Adv. Aneel Kumar Rathore a",
    "Adv. Noor Ahmed Soomro", "Adv. Abdul Qayoom Malkani", "Adv. Mukesh Kumar Rathore", "Adv. Chander Tharani",
    "Adv. Imam Bux Dars", "Adv. Muhammad Amir Qureshi", "Adv. Jethanand", "Adv. Jai Ki Rai", "Adv. Naveed Jarwar s",
    "Adv. Ghulam Hussain Palari", "Adv. Muhammad Ramzan Chandio", "Adv. Sanaullah Jhetiyal", "Adv. Saffar Khokhar",
    "Adv. Aftab Ghori", "Adv. Ravi Kumar", "Adv. Mir Sajid Khoso", "Adv, Naeem Gaddai", "Adv. Vikram Kumar",
    "Adv. Sooba Bhatti", "Adv. Yasir Khoso", "Adv. Rizwan Memon", "Abdul Sattar Shaikh Ac", "Adv. Murtaza Keerio",
    "Adv. Shahbaz Khaskhali", "Adv. Taimor Ali Shah", "Adv. Majid Aziz", "Adv. Shabeer Arbab Hala",
    "Adv. Abdul Jabbar Abbassi", "Adv. Riaz Ali Panhwar", "Adv. Rajesh Kumar Uk", "Adv. Wahid Khan Adpp",
    "Adv. Ameer Hamzo", "Adv. Atta Chandio", "Adv. Abid Chang", "Adv. Imran Memon Adpp", "Adv. Wazeer Chandio",
    "Adv. Waqar Dda", "Adv. Zahid Shah", "Adv. Abdul Sattar Bajeer", "Adv. Mohammad Khan Bajeer", "Adv. Mangal Meghwar",
    "Adv. Ashok Kumar hyd", "Adv. Ramesh kumar Depal", "Adv. Santosh Kumar", "Adv. Goving Mehraj", "Adv. Shewak Rathore",
    "Adv. Govind Meghwar diplo", "Adv. Samiullah Abbassi", "Adv. Khaleel Laghari", "Adv. Abdullah Laghari",
    "Adv Velji Rathore", "Adv. Kewal Bheel", "Adv. Jai Dev Suthar", "Gulji Inspector", "Hajan Abro", "Moula Bux Mirjat",
    "Vijay Kumar", "Sajjid Nizamani", "Abdul Qayoom Mehar", "Akhlaque Hussain Larik", "Abdul Rasheed Khoso",
    "Adv. Ramesh Kumar Oad", "Adv. Sooraj Kumar Qambar", "Abdullah Shoro", "Hafeez", "Adv. Gulab Meghwar",
    "Adv. Kelash Kolhi", "Imtiaz Khoso", "Manoj Kumar", "Abdullah Channa", "Saleem Chandio", "Ishaque Channa",
    "Dodo Khan Jatio", "Hakeem Magrio", "Shahjahan", "Inam Kandhro", "Raheel Abbassi", "Ravi Malkani",
    "Dr. Lal Malkani", "Hafeez Sindhi", "Govinda Rwf", "Ali Hyder Ac", "Adv. Wahab Channa", "Adv. Arif Kellar",
    "Adv. Asad Memon", "Adv. Haroon Keerio", "Adv. Inderjeet Lohano", "Adv. Jairam Das", "Jairam Das Kasbo",
    "Adv. Jameel Khanzado", "Adv. Kaleemullah", "Adv. Nadeem Tagar", "Asghar Jalalani", "Adv. Hassan Jalalani",
    "Santosh Oad", "Adv. Mahesh Bheel", "Adv. Lajpat Rai Soorani", "Adv. Hameed laghari", "Adv. Abdul Razzak Dars",
    "Adv. Hashim laghari", "Adv. Mumtaz jarwar", "Adv. Suneel parhiyar", "Adv. Muneer Gilal", "Abdul shakoor",
    "Amjad tunio", "Kamran magsi", "Naveed Qureshi", "Adv. Qamar nohri", "Shahzaib jatt", "Hasrat parkash",
    "Ashok khatwani", "Kirshan pphi", "Ghansham chaglani", "Haresh kumar nkt", "Mohsin Ali HYd",
    "Muhammad Shahid Shaikh", "Wazeer Oad", "Amar lal Oad", "Ravi Oad", "Prem Oad", "Akash Oad", "Vinod Oad",
    "Gul Bahar Oad", "Javed ali", "Muhammad Ali Solangi", "Ahmed Ali Solangi", "Rashid Soomro", "Majid ali Soomro",
    "Zulfiquar Solangi", "Nisar Solangi", "Haji Ameer Jatt", "Kami (Shahid Jatt)", "Abdullah Meo", "Haji Meo",
    "Khursheed Meo", "Saddar Meo", "Malik Mulazam Hussain", "Malik Sarfraz", "Malik Qasir", "Malik Sohail",
    "Malik Shahzad", "Malik Sajjid", "Danish Shaikh", "Imran Shaikh", "Seth Valam", "Thakro Mal", "Khushal Diplo",
    "Akash Santorai", "Attam kumar", "Eng. Damoon Mal", "Rajesh Chahoo", "Chander Kanji mal", "Toto Mal SSGC",
    "Hoat LUMHS", "Mukesh Kumar Khatwani", "Bhuralal Chaglani", "Dewan Teekchand", "Sukhram Das", "Reejhu Mal",
    "Vishan Das NBP", "Seth Nihal Chand", "Bhemraj", "Ravi shanker", "Chando Mal", "Qadar Bux Sahito",
    "Aftab Abbassi", "Hassan Ali Durani", "Amrat Lal Punhnani", "Ramesh kumar HESCO", "Ubaidullah Nahinoon",
    "Chatro AM", "Bhagchand House building", "Chahno mal house building", "Ramesh kumar Jaronbari", "Ishtiaque tower mrkt",
    "Babar Book Depo", "Salman Book Depo", "Adeeb Book Depo", "Junaid Iqbal Qureshi Thatta", "Irfan Qureshi Thatta",
    "Shahzad Qureshi Thatta", "Jabbar Shaikh", "Revachand", "Devan Service hospital", "Kirshan", "Audu Mal",
    "Devan Inspector lecio", "Doongar Doothi", "Veenjho Paru JI dhani", "Amolakh Jhapio", "Sambhu Arnario",
    "Gordhan NBP Mithi", "Mevaram Galhoro MPK", "Rahul Khetlarai", "Long Lekhmiyar", "Sarwan Tagusar",
    "Altaf Dimro State life", "Nihal chand SPSC", "Jeevat Rai SPSC", "Dr. Khanji Mal", "Dr. Raja", "Prof. Sujo Mal",
    "Waseem Panhwar", "Nagaram Judge", "Akash Kumar Judge", "Bhopat Rai Judge", "Jai Sooraj Judge", "Reejhu Mal Judge",
    "Parkash Kumar Judge", "Noor Ahmed Chandio Judge", "Nadeem Buririo Judge"
]

# ✅ VIP names to add
vip_names = [
    ("Mr. & Mrs. Sharjeel Inam Memon", "Karachi"),
    ("Mr. & Mrs. Rawal Memon", "Karachi"),
    ("Mr. Izhar Hussain Buriro", "Karachi"),
    ("Mr. Syed Abid Shah", "Karachi"),
    ("Mr. Kamran Memon", "Karachi"),
    ("Mr. Salman Memon", "Karachi"),
    ("Mr. Zeeshan Memon", "Karachi"),
    ("Mr. Salman Mansoor", "Karachi"),
    ("Mr. Khalid (Information Department)", "Karachi"),
    ("Mr. Sarang Chandio (Information Department)", "Karachi"),
    ("Mr. Hussain Mansoor", "Karachi"),
    ("Mr. Zameer Abbasi", "Karachi"),
    ("Mr. Atif Bhatti", "Karachi"),
    ("Mr. Raheel Memon", "Karachi"),
    ("Mr. Abdul Rasheed Solangi", "Karachi"),
    ("Mr. Kazi Abid Asid", "Karachi"),
    ("Mr. Long (Badar Commercial)", "Karachi"),
    ("Mr. Imtiaz Bhutto", "Karachi"),
    ("Mr. Kashif Samoon", "Karachi"),
    ("Mr. Ravi Shankar", "Karachi")
]

# --- Load or create DataFrame ---
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
    existing = df["Name"].tolist()
    # Add all names
    for n in names:
        if n not in existing:
            new_sr = df["SR#"].max() + 1
            df.loc[len(df)] = [new_sr, n, "", False]
    for n, city in vip_names:
        if n not in existing:
            new_sr = df["SR#"].max() + 1
            df.loc[len(df)] = [new_sr, n, city, False]
    df.to_csv(DATA_FILE, index=False)
else:
    combined_names = names + [n for n, _ in vip_names]
    combined_cities = [""]*len(names) + [city for _, city in vip_names]
    df = pd.DataFrame({
        "SR#": list(range(1, len(combined_names)+1)),
        "Name": combined_names,
        "Village/City": combined_cities,
        "Invited": [False]*len(combined_names)
    })
    df.to_csv(DATA_FILE, index=False)

st.divider()

# Filter by city
city_filter = st.text_input("🔍 Search by City/Village")
filtered_df = df.copy()
if city_filter.strip():
    filtered_df = filtered_df[filtered_df["Village/City"].str.contains(city_filter, case=False, na=False)]

# Detect duplicates
duplicate_names = df["Name"].value_counts()
duplicates = duplicate_names[duplicate_names > 1].index.tolist()

def highlight_duplicates(row):
    color = 'color: red; font-weight: bold;' if row["Name"] in duplicates else ''
    return [color]*len(row)

styled_df = filtered_df.style.apply(highlight_duplicates, axis=1)

st.subheader("📋 Guest List (Filtered + Duplicates Highlighted)")
st.dataframe(styled_df, use_container_width=True)

st.divider()

# --- Add guest ---
with st.form("add_guest"):
    st.subheader("➕ Add Guest")
    new_name = st.text_input("Enter Name:")
    new_village = st.text_input("Village/City:")
    new_invited = st.checkbox("Invited ✅")
    submit_add = st.form_submit_button("Add Guest")
    if submit_add:
        if new_name.strip() == "":
            st.warning("⚠ Name cannot be empty!")
        else:
            new_sr = df["SR#"].max() + 1
            df.loc[len(df)] = [new_sr, new_name, new_village, new_invited]
            df.to_csv(DATA_FILE, index=False)
            st.success(f"✅ Guest '{new_name}' added!")

st.divider()
# --- Remove guest ---
st.subheader("🗑 Remove Guest")
guest_options_remove = df["Name"].tolist()
selected_remove = st.selectbox("Select Guest to Remove", guest_options_remove, key="remove_guest")

if selected_remove:
    if st.button("Remove Guest"):
        df = df[df["Name"] != selected_remove]
        # Reassign SR# to keep it sequential
        df["SR#"] = range(1, len(df)+1)
        df.to_csv(DATA_FILE, index=False)
        st.success(f"❌ Guest '{selected_remove}' has been removed!")

# --- Edit guest ---
st.subheader("✏️ Edit Guest")
guest_options = df["Name"].tolist()
selected_guest = st.selectbox("Select Guest to Edit", guest_options)

if selected_guest:
    guest_index = df[df["Name"] == selected_guest].index[0]
    edited_name = st.text_input("Edit Name", df.at[guest_index, "Name"])
    edited_village = st.text_input("Edit Village/City", df.at[guest_index, "Village/City"])
    edited_invited = st.checkbox("Invited ✅", df.at[guest_index, "Invited"])

    if st.button("Save Updates"):
        df.at[guest_index, "Name"] = edited_name
        df.at[guest_index, "Village/City"] = edited_village
        df.at[guest_index, "Invited"] = edited_invited
        df.to_csv(DATA_FILE, index=False)
        st.success(f"✅ Guest '{edited_name}' updated successfully!")

st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>🖋 Prepared by <b>Susheel Kumar</b></p>", unsafe_allow_html=True)
