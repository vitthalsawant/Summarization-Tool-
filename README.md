# Summarization-Tool-
Summarization Tool Using LangChain and LLM 


# Summarization Tool Using LangChain and LLM

This project provides a Streamlit application for summarizing long articles or documents into concise summaries using LangChain and a pre-trained Large Language Model (LLM).



## Prerequisites

* Python 3.7+
* An OpenAI API key (or API key from another LLM provider).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd summarization-tool
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**

    * Create a file named `.env` in the project root directory.
    * Add your OpenAI API key (or the API key from the LLM provider you choose):

        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```

    * **Important:** Add `.env` to your `.gitignore` file to prevent accidental exposure of your API keys.

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run summarization_tool.py
    ```

2.  **Open the application in your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`).

3.  **Enter text:** Paste or type the text you want to summarize into the text area.

4.  **Click "Summarize":** The application will use LangChain and the LLM to generate a summary.

5.  **View the summary:** The summary will be displayed below the input text area.

## Customization

* **Change the LLM:**
    * In `summarizer.py`, modify the `LLM` initialization to use a different provider (e.g., Hugging Face models).
    * Ensure you install the necessary library for your chosen provider.
* **Adjust summarization parameters:**
    * Experiment with different `chain_type` options in `summarizer.py` (`"stuff"`, `"map_reduce"`, `"refine"`).
    * Modify the `chunk_size` and `chunk_overlap` parameters in `RecursiveCharacterTextSplitter`.
    * Adjust LLM parameters (e.g., temperature, max tokens) in the `OpenAI` initialization.
* **Enhance the UI:**
    * Modify `summarization_tool.py` to add features like file upload, summary length control, and more user-friendly UI elements.

## Future Improvements

* Implement error handling for API key issues and network errors.
* Add progress indicators and loading spinners.
* Allow users to upload files (e.g., `.txt`, `.pdf`) for summarization.
* Implement caching to improve performance.
* Add more options for LLM parameter tuning.
* Support different LLM providers through a configuration file.
* Improve security by implementing best practices for API key management.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.


