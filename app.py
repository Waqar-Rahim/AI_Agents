import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model='gpt-4o-mini')

search_tool = SerperDevTool()
def write_social_media_post(user_input):
    social_media_writer = Agent(
        role='Social Media Post Writer',
        goal='Create engaging social media posts.',
        backstory="You specialize in crafting concise and compelling social media content.",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
        llm=llm
    )

    social_media_task = Task(
        description=f"Write posts for Twitter, Instagram, Facebook, and LinkedIn on the topic '{user_input}'. Tailor the posts to each platform's tone. Generate the posts in both Swedish and English.",
        expected_output="Well-written posts for Twitter, Instagram, Facebook, and LinkedIn in both Swedish and English.",
        agent=social_media_writer,
    )
    
    crew = Crew(
        tasks=[social_media_task],
        agents=[social_media_writer],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result


def write_blog_post(user_input):
    blog_post_writer = Agent(
        role='Blog Writer',
        goal='Generate informative and engaging blogs.',
        backstory="You excel at writing detailed and engaging blog articles.",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
        llm=llm
    )

    blog_post_reviewer = Agent(
        role='Blog Reviewer',
        goal="Review the blog post for quality, coherence, and accuracy.",
        backstory="You have a keen eye for detail and ensure content is of high quality.",
        verbose=True,
        allow_delegation=True,
        llm = llm
    )

    blog_writer_task = Task(
        description=f"Write a blog article on the topic of '{user_input}' that includes sections such as introduction, body (with subheadings), conclusion, and sources cited at the end. Generate the blog in both Swedish and English.",
        expected_output="A well-written blog article in both Swedish and English with proper headings and sources cited at the end.",
        agent=blog_post_writer,
    )

    blog_post_reviewer_task = Task(
        description="Review the blog post for quality, and coherence.",
        expected_output="A reviewed blog post with necessary corrections.",
        agent=blog_post_reviewer,
    )

    crew = Crew(
        tasks=[blog_writer_task, blog_post_reviewer_task],
        agents=[blog_post_writer, blog_post_reviewer],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result


def write_blog_post_from_info(user_input):
    blog_writer_from_info = Agent(
        role='Blog Writer',
        goal=f"Create an engaging, informative, and well-structured blog post using the provided information: {user_input}. Ensure the content is captivating and easy to read.",
        backstory="You are a skilled writer known for producing comprehensive and captivating blog posts that keep readers engaged and informed.",
        verbose=True,
        allow_delegation=True,
        llm = llm
    )

    blog_reviewer = Agent(
        role='Blog Reviewer',
        goal="Thoroughly review the blog post for quality, coherence, and accuracy, ensuring it adheres to the highest standards of content excellence.",
        backstory="You possess an exceptional eye for detail and are dedicated to ensuring that all content is polished, coherent, and of the highest quality.",
        verbose=True,
        allow_delegation=True,
        llm = llm
    )

    post_writer_from_info_task = Task(
        description=f"Write a blog post in both Swedish and English based on provided user information: '{user_input}'. The blog must include sections such as introduction, body (with subheadings), conclusion.",
        expected_output="A well-written blog post in both Swedish and English with proper headings.",
        agent=blog_writer_from_info,
    )

    post_reviewer_task = Task(
        description="Review the blog post for quality, and coherence.",
        expected_output="A reviewed blog post with necessary corrections.",
        agent=blog_reviewer,
    )

    crew = Crew(
        tasks=[post_writer_from_info_task, post_reviewer_task],
        agents=[blog_writer_from_info, blog_reviewer],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result

st.title("Content Generator")

option = st.selectbox("Choose the content type you want to generate:", 
                      ("Select an option", "Social Media Agent", "Blog Article Agent", "Compose Agent"))

user_input = st.text_area("Enter the topic or information for your content:")

if st.button("Generate Content"):
    if option == "Social Media Agent":
        result = write_social_media_post(user_input)
        st.write(result)
    elif option == "Blog Article Agent":
        result = write_blog_post(user_input)
        st.write(result)
    elif option == "Compose Agent":
        result = write_blog_post_from_info(user_input)
        st.write(result)
    else:
        st.write("Please select a valid option.")
