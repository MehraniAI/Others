import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from datetime import date
from io import BytesIO
from PIL import Image

# Database setup
def init_db():
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_name TEXT,
                    attendance_date TEXT,
                    status TEXT)''')
    conn.commit()
    conn.close()

# Add attendance record
def add_attendance(student_name, attendance_date, status):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("INSERT INTO attendance (student_name, attendance_date, status) VALUES (?, ?, ?)",
              (student_name, attendance_date, status))
    conn.commit()
    conn.close()

# Fetch attendance records
def get_attendance(student_name=None, attendance_date=None):
    conn = sqlite3.connect("attendance.db")
    query = "SELECT * FROM attendance WHERE 1=1"
    params = []
    if student_name:
        query += " AND student_name LIKE ?"
        params.append(f"%{student_name}%")
    if attendance_date:
        query += " AND attendance_date = ?"
        params.append(attendance_date.strftime('%Y-%m-%d'))
    
    df = pd.read_sql(query, conn, params=tuple(params))  
    conn.close()
    return df

# Delete attendance record
def delete_attendance(record_id):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("DELETE FROM attendance WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

# Generate QR Code - FIXED VERSION
def generate_qr_code(student_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(student_name)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

# Streamlit UI
st.title("📋 Student Attendance Management System (QR Code Enabled)")

# Initialize DB
init_db()

# Attendance Form
with st.form("attendance_form"):
    student_name = st.text_input("Student Name")
    attendance_date = st.date_input("Date", value=date.today())
    status = st.selectbox("Status", ["Present", "Absent"])
    submit_button = st.form_submit_button("Mark Attendance")
    
    if submit_button and student_name:
        add_attendance(student_name, attendance_date.strftime('%Y-%m-%d'), status)
        st.success(f"✅ Attendance marked for {student_name} on {attendance_date}")

# Generate QR Code for a student - FIXED SECTION
st.subheader("📌 Generate QR Code for Students")
qr_student_name = st.text_input("Enter Student Name for QR Code")
if st.button("Generate QR Code") and qr_student_name:
    qr_code = generate_qr_code(qr_student_name)
    st.image(qr_code, caption=f"QR Code for {qr_student_name}")
    st.download_button(
        label="📥 Download QR Code",
        data=qr_code,
        file_name=f"{qr_student_name}_qr.png",
        mime="image/png"
    )

# Filter Attendance Records
st.subheader("🔍 Filter Attendance")
filter_student = st.text_input("Search by Student Name")
filter_date = st.date_input("Filter by Date")  # Removed value=None
filter_date = filter_date if filter_date else None  # Handle None case

attendance_df = get_attendance(filter_student, filter_date)

if not attendance_df.empty:
    st.dataframe(attendance_df)

    # Delete Attendance Record
    delete_id = st.number_input("Enter ID to Delete", min_value=1, step=1)
    if st.button("Delete Record"):
        delete_attendance(delete_id)
        st.success("🗑️ Record deleted successfully!")
        st.rerun()  # ✅ Fix Streamlit rerun issue

    # Download Attendance Data
    csv = attendance_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "attendance.csv", "text/csv")

    # Monthly Summary
    st.subheader("📊 Monthly Attendance Summary")
    attendance_df["attendance_date"] = pd.to_datetime(attendance_df["attendance_date"])
    monthly_summary = attendance_df.groupby(attendance_df["attendance_date"].dt.strftime('%B'))["status"].value_counts().unstack().fillna(0)
    st.write(monthly_summary)
else:
    st.warning("⚠️ No attendance records found.")