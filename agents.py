from crewai import Agent, Task, Crew, Process
from config import llm, search_tool


def write_social_media_post(user_input):
    social_media_writer = Agent(
        role='Social Media Post Writer',
        goal='Create engaging social media posts.',
        backstory="You specialize in crafting concise and compelling social media content.",
        verbose=True,
        allow_delegation=True,
        #tools=[search_tool],
        llm=llm
    )

    social_media_task = Task(
        description=f"Write detailed posts of 250-300 words summarizing the article for Twitter, Instagram, Facebook, and LinkedIn based on the topic '{user_input}'. Tailor the posts to each platform's tone and generate them in both Swedish and English. Ensure no external links are included.",
        expected_output="Detailed summary posts of 250-300 words for Twitter, Instagram, Facebook, and LinkedIn in both Swedish and English, without any external links.",
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
        goal='Generate informative and engaging blogs and social media posts in both English and Swedish.',
        backstory="You excel at writing detailed and engaging blog articles in a proper format and also create corresponding social media posts. The blog and posts should be first in English and then in Swedish.",
        verbose=True,
        allow_delegation=True,
        tools=[search_tool],
        llm=llm
    )

    blog_writer_task = Task(
        description=f"Write a comprehensive blog article on the topic '{user_input}' including sections such as introduction, body (with subheadings), conclusion, and sources cited at the end. Additionally, create a social media post of 250-300 words summarizing the blog for each platform (Twitter, Instagram, Facebook, LinkedIn) with relavent hashtags and tailored to each platform's tone. Both the blog and social media posts should be generated first in English and then translated into Swedish.",
        expected_output=("A well-written blog article in both English and Swedish with proper headings and sources cited at the end, along with detailed social media posts for Twitter, Instagram, Facebook, and LinkedIn in both English and Swedish, without any external links. "
                         "Sources should be cited as clickable Markdown links, for example:\n"
                         "1. [Analytics Vidhya. (2023). Top 10 AI & Data Science Trends to Watch in 2023](https://www.analyticsvidhya.com/).\n"
                         "2. [Stanford University. (2023). Artificial Intelligence Index Report 2023](https://aiindex.stanford.edu/).\n"
                         "3. [SQream. (2023). The Evolution of Machine Learning in 2023 and Beyond](https://sqream.com/).\n"
                         "4. [WWT. (2023). Top 6 Data Science Trends in 2023](https://www.wwt.com/)."),
        agent=blog_post_writer,
    )


    crew = Crew(
        tasks=[blog_writer_task],
        agents=[blog_post_writer],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result

def edit_blog_post_for_wow(user_input):
    # blog_writer_from_info = Agent(
    #     role='Blog Writer',
    #     goal=(
    #         f"Create an engaging, informative, and well-structured blog post using the provided information: {user_input}. writ first in English and then in Swedish. "
    #         f"Ensure the content is captivating and easy to read."
    #     ),
    #     backstory="You are a skilled writer known for producing comprehensive and captivating blog posts that keep readers engaged and informed.",
    #     verbose=True,
    #     allow_delegation=True,
    #     llm=llm
    # )

    wow_evaluator = Agent(
        role='Wow Evaluator',
        goal="Evaluate the wow-factor of the blog post content using the provided information: '{user_input}'.",
        backstory="You are an expert at determining the wow-factor of content.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    blog_reviewer = Agent(
        role='Blog Reviewer',
        goal=(
            f"Thoroughly review the blog post for quality, coherence, and accuracy, ensuring it adheres to the highest standards of content excellence.'{user_input}' "
            "Take a step back and think step-by-step about how to achieve the best outcomes."
        ),
        backstory="You an editor who excels at evaluating the quality of writing and other content, to improve novelty, clarity, and overall messaging.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )
    # post_writer_from_info_task = Task(
    #     description=(
    #         f"Write a blog post based on the user information: '{user_input}'. The blog must include sections such as "
    #         f"introduction, body (with subheadings), conclusion. Generate the blog in both Swedish and English."
    #     ),
    #     expected_output="A well-written blog post in both Swedish and English with proper headings.",
    #     agent=blog_writer_from_info,
    # )

    wow_evaluation_task = Task(
        description=f"Evaluate the wow-factor of this blog post content: {user_input}. The evaluation will be based on criteria such as surprise, novelty, insight, value, and wisdom. The agent will deeply consume the content, extract key ideas, and assess these elements to provide a detailed wow-factor analysis.",
        expected_output="The output will include an evaluation of the wow-factor, detailing the levels of surprise, novelty, insight, value, and wisdom present in the content. The output will follow a specific JSON format, providing numeric scores and explanations for each criterion.",
        agent=wow_evaluator,
    )

    rewrite_task = Task(
        description="Rewrite the post to achieve a 10 out of 10 rating in all wow-factor sections based on the feedback provided by the Wow Evaluator.",
        expected_output="A revised blog post with maximum wow-factor in all sections: surprise, novelty, insight, value, and wisdom.",
        agent=blog_reviewer,
    )

    crew = Crew(
        tasks=[wow_evaluation_task, rewrite_task],
        agents=[wow_evaluator, blog_reviewer],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result
