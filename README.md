# MCQ Generator

An AI-powered multiple-choice question generator built with Streamlit, LangChain, and OpenAI. The app accepts PDF or text input, generates MCQs for a selected subject and difficulty level, and displays the result in a table for quick review.

## Features

- Upload PDF or text files
- Generate a custom number of MCQs
- Set the subject and question complexity
- Uses LangChain to structure the generation workflow
- Tracks OpenAI token usage and estimated API cost
- Displays generated questions in a Streamlit table
- Includes a review field for generated quiz quality

## Tech Stack

- Python 3.10
- Streamlit
- LangChain and LangChain Community
- OpenAI / LangChain OpenAI
- PyPDF2
- Pandas
- python-dotenv

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shrikantpandit94/mcqgen.git
cd mcqgen
```

### 2. Create and activate a virtual environment

```bash
conda create -p venv python=3.10 -y
conda activate ./venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the Streamlit app

```bash
streamlit run StreamlitAPP.py
```

## How It Works

1. Upload a PDF or text file.
2. Enter the number of MCQs to generate.
3. Provide the subject and complexity level.
4. The app extracts text from the uploaded file.
5. LangChain sends the structured prompt to the LLM.
6. The generated quiz is parsed into table format.
7. The app displays the MCQs and a quality review.

## AWS EC2 Deployment Notes

Install system tools and Python dependencies on your EC2 instance:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install git curl unzip tar sudo vim wget python3-pip -y
git clone https://github.com/shrikantpandit94/mcqgen.git
cd mcqgen
pip3 install -r requirements.txt
```

Create the `.env` file with your OpenAI API key, then run:

```bash
python3 -m streamlit run StreamlitAPP.py
```

For remote access, open inbound TCP port `8501` in the EC2 security group.

## Use Cases

- Creating quizzes from study material
- Generating practice questions for students
- Building assessment drafts for teachers
- Demonstrating LLM-powered educational tools

## Future Improvements

- Add export to CSV, Excel, or PDF
- Add answer explanations
- Add support for multiple difficulty levels in one quiz
- Add validation for malformed LLM responses
- Replace hard-coded local paths with portable project-relative paths
- Add screenshots or a deployed demo link
