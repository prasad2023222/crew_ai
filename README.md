# CrewAI Blog Generator

A CrewAI-powered project that automatically generates blog posts by researching YouTube videos and creating comprehensive content based on video topics.

## Overview

This project uses CrewAI framework to orchestrate AI agents that work together to:
1. **Research** YouTube videos on a given topic from a specific channel
2. **Write** a blog post summarizing and expanding on the video content

The system uses Google's Gemini AI model and YouTube channel search tools to create informative blog content automatically.

## Project Structure

```
crew ai/
├── agents.py          # Defines AI agents (researcher and writer)
├── crew.py            # Main crew orchestration and execution
├── tasks.py           # Defines tasks for each agent
├── tools.py           # YouTube search tool configuration
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Features

- 🤖 **Multi-Agent System**: Two specialized AI agents working in sequence
- 📺 **YouTube Integration**: Searches and analyzes videos from IBM's YouTube channel
- ✍️ **Automatic Blog Generation**: Creates markdown blog posts from video content
- 🧠 **Memory & Caching**: Agents maintain context and cache results for efficiency
- 🔄 **Sequential Processing**: Tasks execute in order for optimal workflow

## Agents

### 1. Blog Researcher (`blog_reasercher`)
- **Role**: YouTube video researcher
- **Goal**: Find relevant video content for a given topic from YouTube channel
- **Expertise**: AI, Data Science, Machine Learning
- **Capabilities**: 
  - Searches YouTube channel for relevant videos
  - Extracts and analyzes video content
  - Provides comprehensive research reports

### 2. Blog Writer (`blog_writer`)
- **Role**: Content writer
- **Goal**: Write engaging blog posts based on researched content
- **Expertise**: Simplifying complex topics into accessible narratives
- **Capabilities**:
  - Transforms research into well-structured blog content
  - Creates educational and engaging narratives
  - Outputs markdown-formatted blog posts

## Tasks

### Research Task
- Identifies relevant videos for the given topic
- Extracts detailed information from YouTube channel videos
- Generates a comprehensive 3-paragraph report

### Writing Task
- Summarizes information from YouTube videos
- Creates blog content based on the researched topic
- Outputs to `new-blog-post.md` file

## Setup

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. Clone or navigate to the project directory:
```bash
cd "crew ai"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Dependencies

- `crewai` - AI agent orchestration framework
- `crewai_tools` - Pre-built tools for CrewAI agents
- `langchain_google_genai` - Google Gemini integration
- `python-dotenv` - Environment variable management

## Usage

1. **Configure the YouTube Channel** (optional):
   Edit `tools.py` to change the YouTube channel handle:
   ```python
   yt_tool=YoutubeChannelSearchTool(youtube_channel_handel="@YourChannel")
   ```

2. **Set Your Topic**:
   Edit `crew.py` to change the topic:
   ```python
   result=crew.kickoff(inputs={'topic':'Your Topic Here'})
   ```

3. **Run the Crew**:
   ```bash
   python crew.py
   ```

4. **Check Output**:
   The generated blog post will be saved in `new-blog-post.md`

## Example

The default configuration processes the topic: **"AI VS ML VS DL vs Data Science"**

The crew will:
1. Search IBM's YouTube channel for relevant videos
2. Research and extract information from those videos
3. Generate a comprehensive blog post
4. Save it to `new-blog-post.md`

## Configuration

### Model Settings
- **Model**: `gemini-2.5-flash`
- **Provider**: Google Generative AI

### Crew Settings
- **Process**: Sequential (tasks run one after another)
- **Memory**: Enabled (agents remember context)
- **Cache**: Enabled (results are cached)
- **Max RPM**: 100 requests per minute
- **Share Crew**: Enabled

## Output

The blog writer agent generates a markdown file (`new-blog-post.md`) containing:
- Summarized information from YouTube videos
- Comprehensive content on the specified topic
- Well-structured, educational narrative

## Customization

### Change YouTube Channel
Modify `tools.py`:
```python
yt_tool=YoutubeChannelSearchTool(youtube_channel_handel="@YourChannel")
```

### Modify Agent Behavior
Edit `agents.py` to change:
- Agent roles and goals
- Backstories
- Tool assignments
- Delegation permissions

### Adjust Tasks
Edit `tasks.py` to modify:
- Task descriptions
- Expected outputs
- Tool assignments
- Output file names

## Notes

- Ensure you have a valid Google Gemini API key
- The YouTube channel handle should be in the format `@ChannelName`
- Agents use verbose mode for detailed logging
- Memory is enabled to maintain context across tasks

## License

This project is open source and available for modification and distribution.
