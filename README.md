# 📄 PDFMaker

**PDFMaker** is a simple Streamlit-based web application that allows users to generate custom printable notebooks in PDF format. Users can input topics and assign a number of pages to each, then generate a structured PDF where each topic begins its own section.

This project was built as part of a self-guided learning journey, combining skills learned across multiple lessons. It demonstrates how front-end input (Streamlit) and back-end document generation (FPDF) can work together in a functional Python app.

---

## Features

- Add custom topics and assign a number of pages for each.
- Interactive checklist to manage and delete entries.
- Generate a clean, printable PDF file with section headers and blank pages.
- Simple, intuitive UI powered by [Streamlit](https://streamlit.io/).

---

## Built With

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [FPDF](https://py-pdf.github.io/fpdf2/)


---

## Installation

To run this app locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ianajharvey/PDFMaker.git
   cd PDFMaker
   ```

2. **Install dependencies:**
   (You can use pip and a virtual environment if preferred)
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

---

## Example Usage

- Enter a topic (e.g., `"Linear Algebra"`) and assign a number of pages (e.g., `5`)
- Click **Submit** to add it to the list
- Repeat for as many topics as you'd like
- Click the **Generate PDF** button to download a structured, printable notebook

---

## Future Ideas

- Option to include lined, dotted, or blank pages
- Ability to reorder topics
- Save/load preset topic lists
- UI improvements (e.g., topic preview)

---

## Learning Notes

This app was not part of a specific tutorial or course module, but a custom project created by combining:
- Streamlit UI handling
- State management
- PDF file generation
- Python form handling and iteration logic

---

## License

This project is open-source and free to use.