import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="💍 Wedding Guest Manager", layout="wide")
DATA_FILE = "guest_list.csv"

# ✅ Full list of names (add all remaining names in this list)
all_names = [
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
    "Adv. Aftab Ghori", "Adv. Ravi Kumar", "Adv. Mir Sajid Khoso", "Adv, Naeem Gddai", "Adv. Vikram Kumar",
    "Adv. Sooba Bhatti", "Adv. Yasir Khoso", "Adv. Rizwan Memon", "Abdul Sattar Shaikh AC", "Adv. Murtaza Keerio",
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
    "Dr. Lal Malkani", "Hafeez Sindhi", "Govinda Rwf", "Ali Hyder AC", "Adv. Wahab Channa", "Adv. Arif Kellar",
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
    "Malik Shahzad", "Malik سajjid", "Danish Shaikh", "Imran Shaikh", "Seth Valam", "Thakro Mal", "Khushal Diplo",
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
    "Waseem Panhwar", "Nagaram Judge", "Akash Kumar Judge", "Bhopat Rai Judge", "Jai Sooraj Judge",
    "Reejhu Mal Judge", "Parkash Kumar Judge", "Noor Ahmed Chandio Judge", "Nadeem Buririo Judge"
]

# --- Load or create CSV ---
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame({
        "SR#": list(range(1, len(all_names)+1)),
        "Name": all_names,
        "City": ["" for _ in all_names],
        "Invited": [False for _ in all_names]
    })
    df.to_csv(DATA_FILE, index=False)

# --- Normalize columns ---
df.rename(columns={"Village/City": "City"}, inplace=True)
for col in ["SR#", "Name", "City", "Invited"]:
    if col not in df.columns:
        if col == "SR#":
            df[col] = range(1, len(df)+1)
        elif col == "Invited":
            df[col] = False
        else:
            df[col] = ""
df["SR#"] = range(1, len(df)+1)
df.to_csv(DATA_FILE, index=False)

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Select an option",
    ["Add New Guest", "View Guest List", "Search Guest", "Update Guest", "Remove Guest"]
)

# --- Helper function to save and refresh ---
def save_and_refresh(df):
    df["SR#"] = range(1, len(df)+1)
    df.to_csv(DATA_FILE, index=False)
    st.rerun()

# --- Add New Guest ---
if option == "Add New Guest":
    st.subheader("➕ Add a New Guest")
    name = st.text_input("Guest Name")
    city = st.text_input("City")
    invited = st.checkbox("Invited ✅")
    if st.button("Add Guest"):
        if name.strip() == "":
            st.warning("⚠ Name cannot be empty!")
        else:
            df.loc[len(df)] = [len(df)+1, name.strip(), city.strip(), invited]
            save_and_refresh(df)

# --- View Guest List ---
elif option == "View Guest List":
    st.subheader("📋 Guest List")
    st.dataframe(df, use_container_width=True)

# --- Search Guest ---
elif option == "Search Guest":
    st.subheader("🔎 Search Guest")
    keyword = st.text_input("Enter name to search")
    if keyword:
        result = df[df["Name"].str.contains(keyword, case=False, na=False)]
        if result.empty:
            st.warning("No guest found")
        else:
            st.dataframe(result, use_container_width=True)
    else:
        st.info("Enter a name to search")

# --- Update Guest ---
elif option == "Update Guest":
    st.subheader("✏️ Update Guest")
    if df.empty:
        st.info("No guests to update")
    else:
        selected = st.selectbox("Select guest to update", df["Name"].tolist())
        if selected:
            guest_index = df[df["Name"] == selected].index[0]
            new_name = st.text_input("New Name", df.at[guest_index, "Name"])
            new_city = st.text_input("New City", df.at[guest_index, "City"])
            new_invited = st.checkbox("Invited ✅", df.at[guest_index, "Invited"])
            if st.button("Save Update"):
                df.at[guest_index, "Name"] = new_name.strip()
                df.at[guest_index, "City"] = new_city.strip()
                df.at[guest_index, "Invited"] = new_invited
                save_and_refresh(df)

# --- Remove Guest ---
elif option == "Remove Guest":
    st.subheader("🗑 Remove Guest")
    if df.empty:
        st.info("No guests to remove")
    else:
        selected = st.selectbox("Select guest to remove", df["Name"].tolist())
        if st.button("Delete"):
            df = df[df["Name"] != selected].reset_index(drop=True)
            save_and_refresh(df)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>🖋 Prepared by <b>Susheel Kumar</b></p>", unsafe_allow_html=True)
