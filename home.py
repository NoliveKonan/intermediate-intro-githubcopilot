import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Tutoring Signup",
    page_icon="📚",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FFE4E6 0%, #FFF0F5 50%, #FFE4E6 100%);
    }
    .main-header {
        text-align: center;
        font-size: 3rem;
        color: #D63384;
        margin-bottom: 0.5rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        text-shadow: 2px 2px 4px rgba(214, 51, 132, 0.2);
        letter-spacing: -1px;
    }
    .tagline {
        text-align: center;
        font-size: 1.5rem;
        color: #B83280;
        margin-bottom: 2rem;
        font-style: normal;
        font-weight: 400;
        font-family: 'Poppins', sans-serif;
        letter-spacing: 0.5px;
    }
    .form-container {
        background: linear-gradient(135deg, #FFF5F8 0%, #FFE4E9 100%);
        padding: 2rem;
        border-radius: 25px;
        border: 2px solid #F8BBD9;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(248, 187, 217, 0.3);
    }
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 50%, #FFC0CB 100%);
        color: #FFFFFF;
        border-radius: 30px;
        border: none;
        padding: 1.2rem 2.5rem;
        font-size: 1.2rem;
        font-weight: 500;
        font-family: 'Poppins', sans-serif;
        width: 100%;
        margin-top: 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.4);
        display: block !important;
        visibility: visible !important;
        text-shadow: none;
        letter-spacing: 0.5px;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #FFB6C1 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.6);
    }
    .stButton {
        display: block !important;
        width: 100%;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        border: 2px solid #F8BBD9;
        border-radius: 15px;
        background-color: #FFF8FB;
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 16px;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: #FF69B4;
        box-shadow: 0 0 10px rgba(255, 105, 180, 0.3);
    }
    .stTextInput label, .stTextArea label {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 17px;
        color: #B83280;
    }
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        font-family: 'Poppins', sans-serif;
    }
    .stMarkdown h3 {
        font-weight: 600;
        color: #D63384;
    }
    .stMarkdown h4 {
        font-weight: 500;
        color: #B83280;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🌸 Sign up today for tutoring! 🌸</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">✨ Efficiency, fun, and education! ✨</p>', unsafe_allow_html=True)

# Form container
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    # Create the form
    with st.form("tutoring_signup_form"):
        # First Name
        first_name = st.text_input("💖 First Name", placeholder="Enter your first name")
        
        # Last Name
        last_name = st.text_input("💝 Last Name", placeholder="Enter your last name")
        
        # Background
        background = st.text_area("🌺 Background", 
                                placeholder="Tell us about your academic background, experience, or what you'd like help with",
                                height=100)
        
        # List of courses
        courses = st.selectbox("📚 List of courses", 
                              options=[
                                  "Select a course...",
                                  "Mathematics (Calculus I, II, III)",
                                  "Statistics & Probability", 
                                  "Physics (General, Mechanics, E&M)",
                                  "Chemistry (General, Organic, Physical)",
                                  "Biology (General, Molecular, Genetics)",
                                  "Computer Science (Programming, Data Structures)",
                                  "English Literature & Composition",
                                  "Writing & Communication",
                                  "Psychology (Intro, Cognitive, Social)",
                                  "Economics (Micro, Macro)",
                                  "Accounting & Finance",
                                  "Business Administration",
                                  "Political Science",
                                  "History (World, American, European)",
                                  "Philosophy & Ethics",
                                  "Foreign Languages (Spanish, French, German)",
                                  "Art & Art History",
                                  "Music Theory & Performance",
                                  "Engineering (Mechanical, Electrical, Civil)",
                                  "Pre-Med/Pre-Health Sciences",
                                  "Test Prep (SAT, ACT, GRE, MCAT)",
                                  "Other (Please specify in background)"
                              ],
                              index=0)
        
        # Email Address
        email = st.text_input("💌 Email Address", 
                             placeholder="Enter your email address")
        
        # Add some spacing before the button
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Submit button
        submitted = st.form_submit_button("🌟 Join Our Tutoring Family! 🌟")
        
        # Handle form submission
        if submitted:
            # Validation
            if not first_name or not last_name or not email:
                st.error("Please fill in all required fields (First Name, Last Name, and Email Address)")
            elif "@" not in email:
                st.error("Please enter a valid email address")
            elif courses == "Select a course...":
                st.error("Please select a course from the dropdown menu")
            else:
                # Save to CSV file
                csv_file = "tutoring_signups.csv"
                
                # Create new row of data
                new_data = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Background": background if background else "Not provided",
                    "Courses": courses if courses != "Select a course..." else "Not specified"
                }
                
                # Check if file exists
                if os.path.exists(csv_file):
                    # Read existing data and append new row
                    df = pd.read_csv(csv_file)
                    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                else:
                    # Create new dataframe
                    df = pd.DataFrame([new_data])
                
                # Save to CSV
                df.to_csv(csv_file, index=False)
                
                # Success message
                st.success("🎉💕 Thank you for signing up for tutoring! 💕🎉")
                st.balloons()
                
                # Display submitted information
                st.markdown("### 🌈 Your Information:")
                st.write(f"**👤 Name:** {first_name} {last_name}")
                st.write(f"**📧 Email:** {email}")
                if background:
                    st.write(f"**🌺 Background:** {background}")
                if courses and courses != "Select a course...":
                    st.write(f"**📚 Course:** {courses}")
                
                st.info("💌 We'll contact you soon to schedule your first tutoring session! 💌")
                st.success("✅ Your information has been saved successfully!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("### 🌸 Why Choose Our Tutoring? 🌸")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🎯💖 Efficiency")
    st.write("Focused learning sessions tailored to your needs")

with col2:
    st.markdown("#### 🎉🌟 Fun")
    st.write("Engaging and interactive learning experience")

with col3:
    st.markdown("#### 📚🌺 Education")
    st.write("Quality education from experienced tutors")

# Admin section to view responses
st.markdown("---")
st.markdown("### 👀 View All Signups (Admin)")

# Add a checkbox to show/hide the responses
show_responses = st.checkbox("Show all tutoring signups")

if show_responses:
    csv_file = "tutoring_signups.csv"
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        if not df.empty:
            st.markdown("#### 📋 All Tutoring Signups:")
            st.dataframe(df, use_container_width=True)
            
            # Download button
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Signups as CSV",
                data=csv_data,
                file_name=f"tutoring_signups_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("No signups yet!")
    else:
        st.info("No signups file found. Responses will appear here after the first submission!")