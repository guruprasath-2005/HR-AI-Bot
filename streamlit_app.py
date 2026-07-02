import streamlit as st
import pandas as pd
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="HR AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 HR AI Assistant")

# -----------------------------
# Load CSV
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "employee.csv")

employees = pd.read_csv(CSV_PATH)

# -----------------------------
# Employee Search
# -----------------------------
emp_id = st.text_input("Enter Employee ID")

if emp_id:

    result = employees[
        employees["Employee ID"].str.upper() == emp_id.upper()
    ]

    if result.empty:
        st.error("❌ Employee not found")

    else:

        employee = result.iloc[0]

        st.success("✅ Employee Found")

        col1, col2 = st.columns([1, 2])

        # -----------------------------
        # Employee Photo
        # -----------------------------
        with col1:

            photo_path = os.path.join(
                BASE_DIR,
                "Employee_Dataset_Synthetic_100",
                employee["Photo"]
            )

            if os.path.exists(photo_path):
                st.image(photo_path, width=220)
            else:
                st.warning("Photo not found.")

        # -----------------------------
        # Employee Details
        # -----------------------------
        with col2:

            st.subheader("Employee Details")

            st.write("**Employee ID:**", employee["Employee ID"])
            st.write("**Name:**", employee["Name"])
            st.write("**Department:**", employee["Department"])
            st.write("**Designation:**", employee["Designation"])
            st.write("**Email:**", employee["Email"])
            st.write("**Phone:**", employee["Phone"])
            st.write("**Date of Birth:**", employee["Date of Birth"])
            st.write("**Joining Date:**", employee["Joining Date"])

        st.divider()

        # -----------------------------
        # Employee Documents
        # -----------------------------
        st.subheader("📂 Employee Documents")

        documents = {
            "Aadhaar": employee["Aadhaar"],
            "PAN": employee["PAN"],
            "10th": employee["10th"],
            "12th": employee["12th"],
            "TC": employee["TC"],
            "Degree": employee["Degree"],
            "Experience": employee["Experience"],
        }

        cols = st.columns(4)

        i = 0

        for name, relative_path in documents.items():

            full_path = os.path.join(
                BASE_DIR,
                "Employee_Dataset_Synthetic_100",
                relative_path
            )

            with cols[i % 4]:

                if os.path.exists(full_path):

                    with open(full_path, "rb") as file:

                        st.download_button(
                            label=f"📄 {name}",
                            data=file,
                            file_name=os.path.basename(full_path),
                            mime="application/pdf",
                            use_container_width=True
                        )

                else:
                    st.error(f"{name}\nNot Found")

            i += 1