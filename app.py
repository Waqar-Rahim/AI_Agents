import streamlit as st
from agents import write_social_media_post, write_blog_post, edit_blog_post_for_wow

# Set up the Streamlit page configuration
st.set_page_config(page_title="Content Generator", page_icon="📝")

# Title of the application
st.title("📝 Content Generator")

# Sidebar for agent selection
st.sidebar.title("Select an Agent")
option = st.sidebar.selectbox(
    "Choose the content type you want to generate:", 
    ("Select an option", "Social Media Agent", "Blog Writing and Social Media Agent", "Editor")
)

# Display agent description based on selection
if option == "Social Media Agent":
    st.sidebar.subheader("Social Media Agent")
    st.sidebar.write("This agent will create a social media post based on any article you provide. "
                     "For example, if you have an article and you only need a social media post, this agent "
                     "will handle that for you.")
    
elif option == "Blog Writing and Social Media Agent":
    st.sidebar.subheader("Blog Writing and Social Media Agent")
    st.sidebar.write("This agent will handle the entire process: research, writing, editing, and creating "
                     "a social media post in both Swedish and English. Ideal if you want the agent to "
                     "manage research, writing, editing, and social media posting.")
    
elif option == "Editor":
    st.sidebar.subheader("Editor")
    st.sidebar.write("This agent focuses on improving and editing your provided article.")
# Text area for user input
user_input = st.text_area("Enter the topic or information for your content:")

# Button to generate content
if st.button("Generate Content"):
    if option == "Social Media Agent":
        result = write_social_media_post(user_input)
        st.markdown("## Social Media Posts")
        st.markdown(result)
        
    elif option == "Blog Writing and Social Media Agent":
        result = write_blog_post(user_input)
        st.markdown("## Blog Article")
        st.markdown(result)
        # Optionally add a section for social media post if required
        social_media_result = write_social_media_post(user_input)
        st.markdown("## Social Media Posts")
        st.markdown(social_media_result)
        
    elif option == "Editor":
        result = edit_blog_post_for_wow(user_input)
        st.markdown("## Edited Blog Article")
        st.markdown(result)
        
    else:
        st.write("Please select a valid option.")