# 🤖 Code Review Assistant

A web application that uses the Google Gemini API to provide automated, AI-powered reviews for source code files. Users can upload a code file through a simple dashboard and receive a detailed report on readability, performance, best practices, and potential bugs.

---

## ✨ Features

* **Simple Web Dashboard**: Easy-to-use interface for uploading code files.
* **AI-Powered Analysis**: Leverages the Google Gemini API to generate in-depth code reviews.
* **Structured Reports**: Get feedback organized into key areas like Readability, Performance, and Best Practices.
* **Fast Setup**: Runs locally with minimal configuration.
* **Real-time Feedback**: The dashboard provides status updates while the AI is at work.

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, JavaScript
* **AI Model**: Google Gemini Pro
* **Dependencies**: `google-generativeai`, `python-dotenv`

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.7+
* A Google Gemini API Key

### Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/YourUsername/code-review-assistant.git](https://github.com/YourUsername/code-review-assistant.git)
    cd code-review-assistant
    ```

2.  **Create and activate a Python virtual environment**:
    * **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * **macOS / Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables**:
    * Create a new file named `.env` in the root of the project directory.
    * Add your Google Gemini API key to this file:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

### How to Run

1.  **Start the Flask server**:
    ```bash
    flask run
    ```

2.  **Open the application**:
    * Navigate to **`http://127.0.0.1:5000`** in your web browser.

---

## 使い方 How to Use

1.  Open the web application in your browser.
2.  Click the **"Select Code File"** button.
3.  Choose a source code file (e.g., `.py`, `.js`, `.java`) from your computer.
4.  The application will automatically upload the file and display status updates.
5.  Once the analysis is complete, a detailed review report will appear on the dashboard.

