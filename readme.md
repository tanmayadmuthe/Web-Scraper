# AI Web Scraper

An intelligent web scraping tool that combines Streamlit, Selenium, and LangChain with Google's Gemini 2.0 Flash API to extract specific information from websites using AI.

## 🚀 Features

- **Intuitive UI**: Clean Streamlit interface for easy interaction
- **Powerful Scraping**: Selenium-based web scraping with automatic handling of dynamic content
- **AI-Powered Extraction**: Leverages Gemini 2.0 Flash API through LangChain to intelligently parse and extract specific information
- **Customizable Queries**: Ask for exactly what you need from the scraped content
- **Content Processing**: Handles large websites by automatically chunking content for optimal processing

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework for the user interface
- **Selenium**: Browser automation for web scraping
- **LangChain**: Framework for working with language models
- **LangChain-Google-GenAI**: Integration with Google's Generative AI models
- **BeautifulSoup4**: HTML parsing and navigation
- **LXML/HTML5lib**: Additional HTML parsing engines
- **Python-dotenv**: Environment variable management

## 📋 Prerequisites

- Python 3.8 or higher
- Chrome browser installed (for Selenium)
- Google API key for Gemini 2.0 Flash

## 💻 Installation

1. Clone the repository:
'''bash
https://github.com/tanmayadmuthe/Web-Scraper.git
cd Web-Scraper

2. Install the required dependencies:
'''bash
pip install streamlit langchain langchain-google-genai selenium beautifulsoup4 lxml html5lib python-dotenv
'''

3. Create a `.env` file in the project root and add your Google API key:
GOOGLE_API_KEY=your_api_key_here


## 🚀 Usage

1. Start the Streamlit application:
'''bash
streamlit run main.py
'''

2. Open your web browser and navigate to the provided localhost URL (typically http://localhost:8501)

3. Enter a website URL in the input field

4. Click "Scrape Website" to fetch the content

5. Once the content is scraped, you can:
   - View the raw HTML content in the expandable text box
   - Enter a description of what information you want to extract
   - Click "Parse Content" to get the specific information using Gemini 2.0 Flash API

## 🏗️ Project Structure

ai-web-scraper/
├── main.py # Streamlit UI and main application logic
├── scraper.py # Web scraping functionality using Selenium
├── parser.py # AI parsing functionality with LangChain and Gemini
├── utils.py # Utility functions
├── requirements.txt # Project dependencies
└── .env # Environment variables (not in version control)


## 📚 Component Description

### main.py
- Implements the Streamlit user interface
- Coordinates the scraping and parsing workflow
- Manages session state and user interactions

### scrape.py
- Handles web scraping using Selenium
- Processes and cleans HTML content using BeautifulSoup
- Splits content into manageable chunks for AI processing

### parse.py
- Integrates with Google's Gemini 2.0 Flash API via LangChain
- Processes content chunks
- Extracts specific information based on user queries

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

If you have any questions or suggestions, please open an issue or contact the repository owner.

---

**Last Updated**: April 2025
