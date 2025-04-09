import streamlit as st
from datetime import datetime
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Initialize session state for student data if it doesn't exist
if 'students' not in st.session_state:
    st.session_state.students = pd.DataFrame(columns=[
        'first_name', 'last_name', 'dob', 'gender',
        'email', 'whatsapp', 'alt_contact',
        'qualification', 'skills', 'institution', 'completion_year'
    ])

def main():
    st.title("Student Proforma Form")
    
    # Create navigation sublinks
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Go to", 
                             ["Personal Information", 
                              "Contact Details", 
                              "Education Details",
                              "View Records",
                              "Update Records",
                              "Search Records"])
    
    if section == "Personal Information":
        display_personal_info()
    elif section == "Contact Details":
        display_contact_details()
    elif section == "Education Details":
        display_education_info()
    elif section == "View Records":
        view_records()
    elif section == "Update Records":
        update_records()
    elif section == "Search Records":
        search_records()

def display_personal_info():
    st.header("Personal Information")
    
    # Name input
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name*", key="first_name")
    with col2:
        last_name = st.text_input("Last Name*", key="last_name")
    
    # Date of Birth
    dob = st.date_input("Date of Birth*", min_value=datetime(1900, 1, 1), key="dob")
    
    # Gender selection (using inclusive options)
    gender = st.selectbox("Gender", 
                         ["Male", "Female", "Non-binary", "Prefer not to say", "Other"], 
                         key="gender")
    
    if st.button("Save Personal Info"):
        if not first_name or not last_name:
            st.error("Please fill all required fields (*)")
        else:
            # Save to session state
            st.session_state.temp_personal = {
                'first_name': first_name,
                'last_name': last_name,
                'dob': dob,
                'gender': gender
            }
            st.success("Personal information saved temporarily!")

def display_contact_details():
    st.header("Contact Details")
    
    # Email validation
    email = st.text_input("Email Address*", key="email")
    
    # WhatsApp number with validation
    whatsapp = st.text_input("WhatsApp Number*", 
                           help="Please include country code (e.g., +1 1234567890)",
                           key="whatsapp")
    
    # Alternative contact
    alt_contact = st.text_input("Alternative Contact Number", key="alt_contact")
    
    if st.button("Save Contact Details"):
        if not email or not whatsapp:
            st.error("Please fill all required fields (*)")
        elif "@" not in email or "." not in email:
            st.error("Please enter a valid email address")
        else:
            # Save to session state
            st.session_state.temp_contact = {
                'email': email,
                'whatsapp': whatsapp,
                'alt_contact': alt_contact
            }
            st.success("Contact details saved temporarily!")

def display_education_info():
    st.header("Education Details")
    
    # Highest qualification
    qualification = st.selectbox("Highest Qualification*", 
                               ["High School", 
                                "Diploma", 
                                "Bachelor's Degree", 
                                "Master's Degree", 
                                "PhD", 
                                "Other"],
                               key="qualification")
    
    # Skills input
    skills = st.text_area("Skills (comma separated)", 
                         help="List your skills separated by commas, e.g., Python, Data Analysis, Communication",
                         key="skills")
    
    # Institution
    institution = st.text_input("Institution Name*", key="institution")
    
    # Year of completion
    current_year = datetime.now().year
    completion_year = st.slider("Year of Completion", 
                               min_value=1950, 
                               max_value=current_year, 
                               value=current_year,
                               key="completion_year")
    
    if st.button("Save Education Info"):
        if not institution:
            st.error("Please fill all required fields (*)")
        else:
            # Save to session state
            st.session_state.temp_education = {
                'qualification': qualification,
                'skills': skills,
                'institution': institution,
                'completion_year': completion_year
            }
            st.success("Education information saved temporarily!")
    
    if st.button("Submit All Information", key="submit_all"):
        if ('temp_personal' in st.session_state and 
            'temp_contact' in st.session_state and 
            'temp_education' in st.session_state):
            
            # Combine all data
            student_data = {
                **st.session_state.temp_personal,
                **st.session_state.temp_contact,
                **st.session_state.temp_education
            }
            
            # Add to DataFrame
            st.session_state.students = pd.concat([
                st.session_state.students,
                pd.DataFrame([student_data])
            ], ignore_index=True)
            
            # Clear temporary data
            del st.session_state.temp_personal
            del st.session_state.temp_contact
            del st.session_state.temp_education
            
            st.success("All student information saved successfully!")
        else:
            st.error("Please complete all sections before submitting")

def generate_excel():
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    st.session_state.students.to_excel(writer, index=False, sheet_name='Students')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

def generate_pdf():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Create styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']
    
    # Create elements
    elements = []
    
    # Add title
    title = Paragraph("Student Records", title_style)
    elements.append(title)
    
    # Add date
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = Paragraph(f"Generated on: {date_str}", normal_style)
    elements.append(date)
    
    # Add space
    elements.append(Paragraph("<br/><br/>", normal_style))
    
    # Convert dataframe to list of lists for the table
    data = [list(st.session_state.students.columns)]
    data.extend(st.session_state.students.values.tolist())
    
    # Create table
    table = Table(data)
    
    # Add style to table
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ])
    table.setStyle(style)
    
    elements.append(table)
    
    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()

def view_records():
    st.header("View All Student Records")
    
    if st.session_state.students.empty:
        st.warning("No student records found.")
    else:
        st.dataframe(st.session_state.students)
        
        # Add download buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download as Excel"):
                excel_data = generate_excel()
                st.download_button(
                    label="Click to download Excel",
                    data=excel_data,
                    file_name="student_records.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        with col2:
            if st.button("Download as PDF"):
                pdf_data = generate_pdf()
                st.download_button(
                    label="Click to download PDF",
                    data=pdf_data,
                    file_name="student_records.pdf",
                    mime="application/pdf"
                )

def update_records():
    st.header("Update Student Records")
    
    if st.session_state.students.empty:
        st.warning("No student records found to update.")
        return
    
    # Select student to update
    student_list = st.session_state.students.apply(
        lambda x: f"{x['first_name']} {x['last_name']} ({x['email']})", axis=1
    ).tolist()
    
    selected_student = st.selectbox("Select student to update", student_list)
    
    if selected_student:
        student_index = student_list.index(selected_student)
        student_data = st.session_state.students.iloc[student_index].to_dict()
        
        # Display editable form with current data
        with st.form("update_form"):
            st.subheader("Edit Student Information")
            
            col1, col2 = st.columns(2)
            with col1:
                new_first = st.text_input("First Name*", value=student_data['first_name'])
            with col2:
                new_last = st.text_input("Last Name*", value=student_data['last_name'])
            
            new_dob = st.date_input("Date of Birth*", 
                                  value=datetime.strptime(str(student_data['dob']), '%Y-%m-%d').date(),
                                  min_value=datetime(1900, 1, 1))
            new_gender = st.selectbox("Gender", 
                                     ["Male", "Female", "Non-binary", "Prefer not to say", "Other"],
                                     index=["Male", "Female", "Non-binary", "Prefer not to say", "Other"].index(student_data['gender']))
            
            new_email = st.text_input("Email Address*", value=student_data['email'])
            new_whatsapp = st.text_input("WhatsApp Number*", value=student_data['whatsapp'])
            new_alt = st.text_input("Alternative Contact", value=student_data['alt_contact'])
            
            new_qual = st.selectbox("Highest Qualification", 
                                   ["High School", "Diploma", "Bachelor's Degree", 
                                    "Master's Degree", "PhD", "Other"],
                                   index=["High School", "Diploma", "Bachelor's Degree", 
                                          "Master's Degree", "PhD", "Other"].index(student_data['qualification']))
            new_skills = st.text_area("Skills", value=student_data.get('skills', ''))
            new_inst = st.text_input("Institution Name*", value=student_data['institution'])
            new_year = st.slider("Year of Completion", 
                                min_value=1950, 
                                max_value=datetime.now().year, 
                                value=student_data['completion_year'])
            
            if st.form_submit_button("Update Record"):
                # Validate required fields
                if not (new_first and new_last and new_email and new_whatsapp and new_inst):
                    st.error("Please fill all required fields (*)")
                else:
                    # Update the record
                    updated_data = {
                        'first_name': new_first,
                        'last_name': new_last,
                        'dob': new_dob,
                        'gender': new_gender,
                        'email': new_email,
                        'whatsapp': new_whatsapp,
                        'alt_contact': new_alt,
                        'qualification': new_qual,
                        'skills': new_skills,
                        'institution': new_inst,
                        'completion_year': new_year
                    }
                    
                    st.session_state.students.iloc[student_index] = updated_data
                    st.success("Student record updated successfully!")

def search_records():
    st.header("Search Student Records")
    
    if st.session_state.students.empty:
        st.warning("No student records found to search.")
        return
    
    search_option = st.radio("Search by", ["Name", "Email", "Institution", "Skills"])
    search_query = st.text_input("Enter search term")
    
    if st.button("Search"):
        if not search_query:
            st.error("Please enter a search term")
        else:
            if search_option == "Name":
                results = st.session_state.students[
                    (st.session_state.students['first_name'].str.contains(search_query, case=False)) |
                    (st.session_state.students['last_name'].str.contains(search_query, case=False))
                ]
            elif search_option == "Email":
                results = st.session_state.students[
                    st.session_state.students['email'].str.contains(search_query, case=False)
                ]
            elif search_option == "Institution":
                results = st.session_state.students[
                    st.session_state.students['institution'].str.contains(search_query, case=False)
                ]
            else:  # Skills
                results = st.session_state.students[
                    st.session_state.students['skills'].str.contains(search_query, case=False)
                ]
            
            if results.empty:
                st.warning("No matching records found")
            else:
                st.dataframe(results)
                
                # Add download buttons for search results
                st.markdown("---")
                st.subheader("Download Search Results")
                col1, col2 = st.columns(2)
                with col1:
                    excel_data = BytesIO()
                    results.to_excel(excel_data, index=False)
                    st.download_button(
                        label="Download as Excel",
                        data=excel_data.getvalue(),
                        file_name="search_results.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                with col2:
                    # Simplified PDF download for search results
                    pdf_data = BytesIO()
                    doc = SimpleDocTemplate(pdf_data, pagesize=letter)
                    elements = []
                    elements.append(Paragraph("Search Results", getSampleStyleSheet()['Title']))
                    elements.append(Paragraph(f"Search Criteria: {search_option} = {search_query}", 
                                           getSampleStyleSheet()['Normal']))
                    
                    # Convert results to table
                    pdf_table = [list(results.columns)] + results.values.tolist()
                    table = Table(pdf_table)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,0), colors.grey),
                        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                        ('GRID', (0,0), (-1,-1), 1, colors.black)
                    ]))
                    elements.append(table)
                    doc.build(elements)
                    st.download_button(
                        label="Download as PDF",
                        data=pdf_data.getvalue(),
                        file_name="search_results.pdf",
                        mime="application/pdf"
                    )

if __name__ == "__main__":
    main()