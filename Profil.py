import streamlit as st
import re
import time

title = "Welcome to My Portfolio 🚀"

placeholder = st.empty()

for i in range(len(title) + 1):
    placeholder.markdown(
        f"""
        <h1 style='font-size:40px; color:white;'>
        {title[:i]}
        </h1>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.05)


import streamlit as st
st.set_page_config(
    page_title="My Profile | Bio Data",
    page_icon=":raising_hand_man:",
)


with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/288869966?s=400&u=8ecfcc15e5d5cff767f8c2e3d4f3be10d860d42a&v=4", caption="Hariswara Reddy")
    st.title("Hey, I am Hariswara")
    st.write("👉Python Developer")
    st.write("👉streamlit Creater")
    st.write("👉Student")
    st.write("👉Basketball Player")
    st.divider()
    st.title("Lets Connect")
    st.subheader("📞Contact")
    st.write("📧 avulahariswarareddy@gmail.com")
    st.write(" +91-9000320544")
    st.markdown("[📍Google office, Hyderabed, Telengana](https://share.google/sh9haSC7h4IcINDGi)")
    st.markdown("----")
    st.write("🎓Academics")
    st.markdown("**College:** Resonance \n\n**Branch:** MPC \n\n**Year:** 2026")
    st.markdown("----")
    st.write("🌐Languages:")
    st.markdown(" - English")
    st.markdown(" - Telugu")
    st.markdown(" - Hindi")

    st.title("💗Connect With Me")
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown("[![Github](https://toppng.com/uploads/preview/github-logo-png-download-11659780035ovo4tgsfgr.png)](https://github.com/avulahariswarareddy)")
        st.write("Github")
    with col2:
        st.markdown("[![Instagram](https://img.magnific.com/premium-vector/modern-badge-logo-instagram-icon_578229-124.jpg?semt=ais_hybrid&w=740&q=80)](https://www.instagram.com/harishwar_reddy_avula/)")
        st.write("Instagram")
    with col3:
         st.markdown("[![Whatsapp](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJCXHUHLcHEK1YfnI5LoabzhIzSfWAZHDtnw&s)](https://wa.me/qr/NSKTC2IA3AIYM1)")
         st.write("Whatsapp")


tab1, tab2, tab3, tab4, tab5= st.tabs(["Home", "Education", "Projects","Skills & achievements" ,"Contact"])

with tab1:
    c1,c2=st.columns([4,2])
    with c1:
         st.subheader("About me")
         st.write("I am Harishwar, a passionate student and aspiring Python developer born on 14th September 2009. I have a strong interest in building interactive and creative web applications using Streamlit and Python. I enjoy turning ideas into real projects and continuously improving my skills through hands-on learning and experimentation. My interests include Python programming, AI, automation, UI design, and problem-solving. Alongside coding, I also enjoy basketball and fitness, which help me stay disciplined, focused, and motivated. I believe in learning by building, which is why I spend time creating projects that challenge me and help me grow as a developer. My goal is to become a skilled software developer capable of building impactful and innovative applications that solve real-world problems.")
         st.divider()
         st.subheader("🎯Career Goals")
         st.write("• Become a skilled Python developer")
         st.write("• Learn Artificial Intelligence and Machine Learning")
         st.write("• Build modern and interactive web applications")
         st.write("• Create real-world projects that solve problems")
         st.divider()
         st.subheader("🌟 Philosophy")
         st.write(">Learning by building, improving by failing, and growing every single day. 🚀")
    with c2:
        st.image("https://static.vecteezy.com/system/resources/previews/059/296/693/non_2x/push-beyond-your-limits-inspirational-quotes-poster-design-template-represents-growth-success-skill-development-and-motivation-vector.jpg")


    

with tab2:
    st.title("History")
    st.subheader("🎓 10th Grade — Bhashyam Blooms")
    st.write("• Studied 10th Grade at Bhashyam Blooms School.")
    st.write("• Explored different interests and activities to better understand my strengths and future goals.")
    st.write("• Developed essential qualities such as discipline, responsibility, and consistency.")
    st.write("• Learned the importance of focus, time management, and hard work.")
    st.write("• Gradually gained clarity about my academic and career aspirations.")
    st.write("• Built a strong foundation for personal growth, learning, and future success.")
    st.divider()
    st.subheader("🎓 11th Grade — Resonance Global Campus")
    st.write("• Pursuing 11th Grade at Resonance Global Campus.")
    st.write("• Developed a stronger focus on academics, personal growth, and long-term career goals.")
    st.write("• Set a clear objective of pursuing undergraduate studies abroad and began working consistently toward achieving it.")
    st.write("• Improved discipline, dedication, and time-management skills through a more goal-oriented approach.")
    st.write("• Discovered a strong interest in Python programming, technology, and software development.")
    st.write("• Started building projects and exploring practical applications of coding and problem-solving.")
    st.write("• Continued to expand technical knowledge while preparing for future academic and professional opportunities.")
    st.divider()
    st.subheader("🎓 12th Grade — Resonance Global Campus")
    st.write("• Currently pursuing 12th Grade at Resonance Global Campus.")
    st.write("• Maintaining a strong focus on academics while continuously developing technical and professional skills.")
    st.write("• Preparing for international undergraduate opportunities and working toward long-term academic goals.")
    st.write("• Simultaneously preparing for the JEE examination as a backup pathway for higher education.")
    st.write("• Actively enhancing programming skills through consistent learning and practice.")
    st.write("• Building interactive projects using Python and Streamlit to gain hands-on development experience.")
    st.write("• Exploring modern technologies, software development concepts, and problem-solving techniques.")
    st.write("• Committed to continuous learning and growth with the goal of becoming a skilled software developer.")
    st.divider()
    
    st.title("📊Score Records")
    with st.container(border=True):
       
        st.write(" **11th Class Marks**")

        col1, col2= st.columns([1,3])
        with col1:
            st.write("French")
        with col2:
            st.progress(0.95, text="95/100")


        col1, col2 = st.columns([1,3])
        with col1:
            st.write("English")
        with col2:
            st.progress(0.91, text="91/100")


        col1, col2 = st.columns([1,3])
        with col1:
            st.write("Physics")
        with col2:
            st.progress(1.0, text="60/60")
        col1, col2 = st.columns([1,3])

        with col1:
            st.write("Chemistry")
        with col2:
            st.progress(1.0, text="60/60")
        col1, col2 = st.columns([1,3])

        with col1:
            st.write("Mathematics 1A")
        with col2:
            st.progress(0.986, text="74/75")

        with col1:
            st.write("Mathematics 1B")
        with col2:
            st.progress(1.0, text="75/75")

with tab3:
    st.title("What I've Built")
    st.divider()
    st.subheader("1.💰 Expense Tracker & Budget Splitter")
    with st.expander("💰Tap to see"):
        
        st.title("💰 Expense Tracker & Budget Splitter")
        st.subheader("Calculate how much each person should pay.")

        bill = st.number_input(
            "Enter Total Bill Amount (₹)",
                min_value=0.0,
                step=1.0
         )

        tip = st.slider(
            "Select Tip Percentage",
            min_value=0,
            max_value=100,
            value=10
        )

        people = st.number_input(
            "Number of People",
            min_value=1,
            step=1
        )

        tip_amount = bill * (tip / 100)
        total_bill = bill + tip_amount
        share = total_bill / people

        st.divider()

        st.subheader("📊 Results")

        st.write(f"Tip Amount: ₹{tip_amount:.2f}")
        st.write(f"Total Bill: ₹{total_bill:.2f}")
    
    st.write("**Status:** ✅ Completed")
    st.write("Difficulty: ⭐⭐⭐☆☆")
    st.write("A financial utility application that helps users calculate expenses and split bills fairly among friends. The app allows users to enter the total bill amount, select a tip percentage, and specify the number of people sharing the expense. It then instantly calculates the final amount and each person's share, making group payments simple and transparent.")
    st.write("**🛠 Technologies Used:**")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("**✨ Key Features:**")
    st.write("• Bill amount input")
    st.write("• Adjustable tip percentage slider")
    st.write("• Automatic per-person cost calculation")
    st.write("• Clean and interactive user interface")
    st.divider()

    st.subheader("2.📏 Body Mass Index Calculator")

    with st.expander("📏 Tap to see"):

        st.subheader("BMI Calculator")

        weight = st.number_input(
            "Enter your weight (kg)",
        min_value=1.0,
        step=0.1
        )

        height = st.number_input(
            "Enter your height (m)",
            min_value=0.1,
            step=0.01
        )

        if st.button("Calculate BMI"):

            bmi = weight / (height ** 2)

            st.write(f"Your BMI is: **{bmi:.2f}**")

            if bmi < 18.5:
                st.warning("Underweight")
            elif bmi < 25:
                st.success("Normal Weight")
            elif bmi < 30:
                st.warning("Overweight")
            else:
                st.error("Obese")
    st.write("**Status:** ✅ Completed")
    st.write("Difficulty: ⭐⭐☆☆☆")
    st.write("A health and fitness application that calculates a user's Body Mass Index (BMI) based on their height and weight. The app instantly determines the BMI value and classifies it into categories such as Underweight, Normal Weight, Overweight, or Obese, helping users better understand their health status.")
    st.write("**🛠 Technologies Used:**")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("**✨ Key Features:**")
    st.write("• Weight input in kilograms")
    st.write("• Height input in meters")
    st.write("• Instant BMI calculation")
    st.write("• Automatic health category classification")
    st.write("• Simple and user-friendly interface")
    st.divider() 

    st.subheader("3.🏦 Interest Calculator")
    with st.expander("🏦Tap to see"):

        st.title("🏦 Interest Calculator")

        a=st.selectbox("What would you like to do?", ["--Select--","Simple Interest", "Compound Interest"])

        if a=="Simple Interest":
            principal=st.number_input("Enter the principal amount between $1 to $100000" , min_value=1.0 , max_value=100000.0, step=100.0 , value=10.0)
            time=st.number_input("Enter the Tenure in years", min_value=1.0 , max_value=100.0, step=1.0 , value=5.0)
            interest=st.number_input("Enter the rate of interest")

            Simple_interest=(principal*time*interest)/100
            Total_Amount= principal+Simple_interest

            st.divider()

            st.subheader("Result")
            st.metric(label="simple interest", value=f"${Simple_interest}")
            st.metric(label="Total_Amount", value=f"${Total_Amount}")


        elif a=="Compound Interest":
            principal=st.number_input("Enter the principal amount between $1 to $100000" , min_value=1.0 , max_value=100000.0, step=100.0 , value=10.0)
            time=st.number_input("Enter the Tenure in years", min_value=1.0 , max_value=100.0, step=1.0 , value=5.0)
            interest=st.number_input("Enter the rate of interest")

            Compound_interest=(principal*(1+interest/100)**time)
            Total_Amount= principal+Compound_interest

            st.divider()

            st.subheader("Result")
            st.metric(label="compound interest", value=f"${Compound_interest}")
            st.metric(label="Total_Amount", value=f"${Total_Amount}")

    st.write("**Status:** ✅ Completed")
    st.write("Difficulty: ⭐⭐⭐☆☆")
    st.write("A financial application that calculates both Simple Interest and Compound Interest based on the user's principal amount, interest rate, and investment period. The app instantly displays the interest earned and the final amount, helping users understand how money grows over time.")
    st.write("**🛠 Technologies Used:**")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("**✨ Key Features:**")
    st.write("• Principal amount input")
    st.write("• Interest rate input")
    st.write("• Investment period input")
    st.write("• Simple Interest calculation")
    st.write("• Compound Interest calculation")
    st.write("• Instant result display")
    st.write("• Clean and interactive user interface")

with tab4:
    co1,co2=st.columns([5,3])
    with co1:
        with st.container(border=True):
             st.subheader("💻Technical Skills")

             col1, col2= st.columns([1,3])
             with col1:
                st.write("Python")
             with col2:
                st.progress(0.80, text="80%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("Java")
             with col2:
                st.progress(0.20, text="20%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("HTML")
             with col2:
                st.progress(0.10, text="10%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("C++")
             with col2:
                st.progress(0.05, text="5%")
    with co2:
        with st.container(border=True):
             st.subheader("☀️Soft Skills")

             col1, col2= st.columns([1,3])
             with col1:
                st.write("Leadership")
             with col2:
                st.progress(0.80, text="80%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("Communication")
             with col2:
                st.progress(0.90, text="90%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("Team collab")
             with col2:
                st.progress(0.80, text="80%")
             col1, col2= st.columns([1,3])
             with col1:
                st.write("Problem-Solving")
             with col2:
                st.progress(0.85, text="85%")

    with st.container(border=True):
        st.subheader("🏆Awards & Honors")
        y1,y2,y3=st.columns([1,1,1])
        with y1:
            with st.container(border=True):
                st.write("📚 Awarded for Academic Excellence")
        with y2:
            with st.container(border=True):
                st.write("🏀 Captained Runner-Up Basketball Team")
        with y3:
            with st.container(border=True):
                st.write("💻 Winner, Python Competition 2025")


with tab5:
    st.header("🤝 Get In Touch")
    st.write("I am always open to meaningful conversations, exciting opportunities, and collaborative projects. If my work interests you or if you")
    with st.form(key="Form1"):
        col1, col2, col3= st.columns(3)
        with col1:
        
            st.subheader("Personal Information")
            Your_name= st.text_input("Your name- ")
            DOB=st.date_input("Choose your Date Of Birth")
            Email=st.text_input("Enter you Email Address", placeholder="example - abc@gmail.com")
            Phone=st.text_input("Phone number", placeholder="+91 9876543210")
            find=st.selectbox("How did you know about me?", ['--select--','Youtube', 'Facebook', 'Instagram'])
            email_validator=r"^[a-zA-Z0-9._]+@gmail.com$"

        with col2:
            st.divider()
            st.subheader("Current Situation")
            role=st.selectbox("what are you currently doing?", ['--select--', 'Student', 'Job', 'Others'])
            others=st.text_input("If choosen others-")

        with col3:
            st.divider()
            st.subheader("Requirement")
            st.text_input("what made you to fill this form?")
            Photo=st.file_uploader("Upload a file, If needed.")
            Submit=st.form_submit_button("Click to submit")

            if Submit:
                clean_email = Email.strip()
                if not clean_email:
                    st.warning("Email cannot be empty")
                elif not re.match(email_validator, clean_email):
                    st.error("check the email")
                else:
                    st.balloons()
                    st.success("Your form is been submitted!!")

st.divider()
st.write("💻 Designed & Developed by **Avula Hariswara Reddy**")
st.write("Python • Streamlit • Continuous Learning")
st.write(">Turning ideas into reality through code.")
st.write("© 2026 All Rights Reserved")
st.divider()
