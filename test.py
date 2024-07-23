

    return crew.run()

# Example call
# content_info = "Details about AI's impact on healthcare, including examples and statistics."
# write_blog_post_from_info(content_info)
def edit_blog_post_for_wow(user_input):
    blog_writer_from_info = Agent(
        role='Blog Writer',
        goal=f"Create an engaging, informative, and well-structured blog post using the provided information: {user_input}. Ensure the content is captivating and easy to read.",
        backstory="You are a skilled writer known for producing comprehensive and captivating blog posts that keep readers engaged and informed.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    blog_reviewer = Agent(
        role='Blog Reviewer',
        goal="Thoroughly review and enhance the blog post for quality, coherence, and accuracy, ensuring it adheres to the highest standards of content excellence. Add the 'wow' factor to make it a 10 out of 10 in all sections.",
        backstory="You are an expert writer and editor who excels at evaluating and enhancing the quality of content, providing various ratings and recommendations to improve novelty, clarity, and overall messaging. Your expertise includes applying the 'Wow' prompt to significantly enhance the content.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    post_writer_from_info_task = Task(
        description=f"Write a blog post based on the user information: '{user_input}'. The blog must include sections such as introduction, body (with subheadings), and conclusion. Generate the blog in both Swedish and English.",
        expected_output="A well-written blog post in both Swedish and English with proper headings.",
        agent=blog_writer_from_info,
    )

    post_reviewer_task = Task(
        description=("Review and rewrite the blog post to ensure it achieves a 'wow' factor of 10 out of 10 in all sections. "
                     "Use the 'Wow' prompt to evaluate and enhance the content, ensuring high levels of surprise, novelty, insight, value, and wisdom. "
                     "The review process should involve a thorough assessment and enhancement of the content to make it exceptional."),
        expected_output="A reviewed and enhanced blog post with a 'wow' factor of 10 out of 10 in all sections, ensuring high levels of surprise, novelty, insight, value, and wisdom.",
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
