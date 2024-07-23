# AI Content Generator Project

## Overview

This project is an AI-powered content generation tool that uses advanced language models to create and edit various types of content, including social media posts and blog articles. It provides functionality for generating content in both English and Swedish, and includes an editing agent to improve the quality of blog posts based on specific criteria.

## Features

- **Social Media Post Generation**: Create engaging social media posts tailored to different platforms (Twitter, Instagram, Facebook, LinkedIn) in both English and Swedish.
- **Blog Writing and Editing**: Generate comprehensive blog articles with sections like introduction, body, conclusion, and create corresponding social media posts. Edit and enhance blog posts to improve their novelty, clarity, and prose.

## Components

1. **Agents**
   - **Social Media Agent**: Generates social media posts based on provided topics.
   - **Blog Writing and Social Media Agent**: Handles the end-to-end process of writing a blog article and creating related social media posts.
   - **Editor Agent**: Focuses on editing blog posts to enhance their quality.

2. **Streamlit Application**
   - Provides a user-friendly interface for generating and viewing content.
   - Allows users to select an agent, input content topics, and view the generated output.
   - Includes copy buttons to easily copy generated content.

## Setup Instructions

### Prerequisites

1. Python 3.12 or later
2. Required Python libraries (Streamlit, Agents package, etc.)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Waqar-Rahim/AI_Agents.git
    cd AI_Agents
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Your Environment**

    Make sure to set up any required environment variables or configuration files. This may include API keys or other settings.

### Running the Application

1. **Start the Streamlit App**

    ```bash
    streamlit run app.py
    ```

2. **Access the Application**

    Open a web browser and navigate to `http://localhost:8501` to use the content generator.
