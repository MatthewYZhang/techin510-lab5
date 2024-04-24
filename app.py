import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert at help others modify their resume to fit the job they want to apply for.

First, analyze the user's resume fitness to the job on a scale of 1 to 10, 1 is not fit, and 10 is a complete fit.

Then, give out possible improvements of the resume. For example, if the resume says "I worked with my manager to enhance the robustness of the scripts", you can suggest the following improvement in this format:
Original: I worked with my manager to enhance the robustness of the scripts
Improved: I reduced the downtime of this specific script by 85% time collaborating with my manager
Why: include metrics to enhance contribution

For every point, seperate them using different indentation. 

The user's resume is:
{resume}

The job description is:
{description}
"""

def generate_content(resume, job_description):
    response = model.generate_content(prompt_template.format(resume=resume, description=job_description))
    return response.text

def stream_output():
    for word in reply.split(" "):
        yield word + " "
        time.sleep(0.02)

st.title("Resume Builder")

c1, c2 = st.columns(2)

with c1:
    resume = st.text_area("Enter your current resume", height=300)
with c2:
    job_description = st.text_area("Enter the job description of the job you want to apply to", height=300)

reply = None

if st.button("Make my resume better!", use_container_width=True):
    reply = generate_content(resume, job_description)
    # print(reply, type(reply))
    # st.write(reply)
    st.write_stream(stream_output)