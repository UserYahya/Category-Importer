# Bangla Wikipedia Category Importer

A simple web tool that helps import relevant categories from an English Wikipedia article (via Wikidata) to its Bangla Wikipedia counterpart. Built with Flask and Pywikibot, it assists editors in improving categorization on Bangla Wikipedia.

## Features

- Input any Bangla Wikipedia page name.
- Automatically fetches its linked English Wikipedia article via Wikidata.
- Extracts all visible (non-hidden) categories.
- Maps those to Bangla Wikipedia (if category items exist in Wikidata).
- Outputs ready-to-copy category markup like:  
  `[[বিষয়শ্রেণী:বাংলা বিষয়শ্রেণী নাম]]`
- Mobile-friendly, modern UI with one-click copy button.

## Demo

Coming soon...

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wiki-cat-importer.git
   cd wiki-cat-importer

2. Install dependencies:

pip install flask pywikibot



3. Run the Flask app:

python app.py


4. Open in browser:

http://localhost:5000



Deployment (PythonAnywhere)

You can easily host this on PythonAnywhere for free.

See the PythonAnywhere Hosting Guide (coming soon)


Project Structure

.
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend HTML template
├── README.md
└── requirements.txt       # Optional: for pip install

Contributing

Pull requests and suggestions are welcome! If you find a bug or want a new feature, feel free to open an issue.

License

MIT License. See LICENSE file for details.

Author

Made by Your Name

---

### Optional Files

**`requirements.txt`**
```txt
flask
pywikibot

Let me know if you'd like this converted into a live GitHub repo structure or want a Bengali version of the README too.

