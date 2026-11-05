# Adrian Nogueira — Student Portfolio

A personal portfolio for Adrian Nogueira, a first-year NJIT student interested in software engineering. Built with plain HTML, CSS, and JavaScript and hosted on GitHub Pages.

**Live website:** https://asn77s.github.io/

## Pages

- **Home:** introduction, featured projects, education, interests, and email.
- **About Me:** background, NJIT and Kearny High School education, DECA membership, family roots, and sports interests.
- **Projects:** four Python projects with descriptions, example images, interactive JavaScript demos, and downloadable source.
- **Skills:** beginner Python and GitHub experience.
- **Contact:** a public email link. There is no backend or contact form.

## Features and design

The default design uses a black background, light text, and red accents. Impact/Arial Narrow display headings and Trebuchet MS/Segoe UI body text are shared across the pages. CSS media queries adapt the layout to phones and laptops.

JavaScript provides a mobile navigation menu, optional light mode, and four project demos. The menu supports Escape to close and restores focus to its button. Pages include skip links, visible keyboard focus, labeled inputs, descriptive image text, and status messages for demo results.

## Projects

| Project | What it does | Download requirements |
| --- | --- | --- |
| Python Gradebook | Accepts student names and scores, assigns letter grades, and prints a summary | Python 3 |
| Simple Calculator | Accepts two numbers and an operation; handles invalid numbers and division by zero | Python 3 |
| Shopping Cart | Tracks 12 products, stock, quantities, and totals; random prices stay fixed until reset | Python 3 |
| Random Joke Fetcher | Retrieves a joke from the Official Joke API, prints it, and saves `jokes.txt` | Python 3, `requests`, internet access |

On phone-sized screens, tapping a Python download offers **Try in browser** or **Download Python source**. The first option focuses the matching demo; the second downloads code that requires Python and may open in a phone’s file viewer.

The website demos run in JavaScript in the browser. The downloaded programs run in Python in a terminal; GitHub Pages does not execute Python. The cart is a practice project and does not accept payments. Browser demos do not save grades or carts between visits.

### Run the downloaded projects

Install Python 3, download a `.py` file from the Projects page, and open a terminal in the folder containing that file. On macOS/Linux:

```sh
python3 gradebook.py
python3 calculator.py
python3 shopping_cart.py
```

For the joke fetcher:

```sh
python3 -m pip install requests
python3 joke_fetcher.py
```

On Windows, use `py` instead of `python3`. If your browser adds a number to a filename, use that exact filename in quotes or rename the downloaded file.

- Gradebook: enter a name and a grade from 0 to 100; enter `q` as a name to view the summary and finish.
- Calculator: enter two numbers and `+`, `-`, `*`, or `/`; enter `q` at any prompt to quit.
- Cart: use the numbered menu. Item names must match the displayed spelling. Option 4 quits; option 5 clears the cart, restores stock, and generates new prices from $1.00 to $9.99.
- Joke fetcher: each successful run replaces `jokes.txt` in the terminal’s current folder.

## Local preview

No build tools or frameworks are required. Open `index.html` in a browser or use a local static server from the repository folder:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000/`. Stop the server with Ctrl+C. Final assignment checks must also be run on the live GitHub Pages site.

## Files

- `index.html`, `about.html`, `projects.html`, `skills.html`, `contact.html`: the five pages.
- `styles.css` and `script.js`: shared styling and interactions.
- `assets/`: photos, team logos, and project output/workflow illustrations.
- `projects/`: downloadable Python programs.
- `AGENTS.md`: site design and maintenance rules.
- `TESTING.md`: test steps, results, limitations, and retest history.
- `tests/evidence/`: live-site screenshots, audit reports, and verification records.
- `RUBRIC_CHECKLIST.md`: evidence mapped to the assignment criteria.
- `reports/Adrian_Nogueira_Website_Report.docx`: two-page assisted report draft with features, challenges, a corrected Codex mistake, and browser-emulated phone/laptop screenshots. Adrian should review it before submission; replace screenshots if physical-device captures are required.
- `reports/REPORT.md`: editable report text and screenshot provenance, available alongside the source code in the project folder.

## Testing and deployment

Changes are committed and pushed to `main`; GitHub Pages publishes the website. The live site is the final verification target. See [TESTING.md](TESTING.md) for the recorded checks and any remaining manual checks.

Lighthouse 13.6.0 accessibility audits run on November 4, 2026 returned **100 for all five pages on both mobile and desktop**. Full JSON reports are in [tests/evidence/lighthouse](tests/evidence/lighthouse). Automated scores complement, rather than replace, keyboard and visual testing.

## Image sources and development

Personal photos were supplied by Adrian. Project illustrations show sample output or workflows. Team image sources are listed in [assets/sports-credits.md](assets/sports-credits.md); team marks belong to their respective owners.

The portfolio was developed with Codex assistance. Adrian should review the code and explain its behavior in his own words during the in-person presentation. No phone number or home address is published.
