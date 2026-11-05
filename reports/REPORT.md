# Personal Portfolio Website Report

Adrian Nogueira | November 5, 2026

## Website features

My personal portfolio introduces me as a first-year NJIT student interested in software engineering. It has five pages: Home, About Me, Projects, Skills, and Contact. Home introduces my work, About Me covers my background and interests, Skills describes my beginner Python and GitHub experience, and Contact provides my public email address. The site is published at https://asn77s.github.io/.

The Projects page includes Python Gradebook, Random Joke Fetcher, Simple Calculator, and Shopping Cart. Each project has a description, an output or workflow image, a Python source download, and an interactive JavaScript browser demo. Visitors can convert a score to a letter grade, calculate with two numbers, manage a shopping cart, or fetch and save a joke.

I developed the website with Codex assistance using plain HTML, CSS, and JavaScript. All five pages share one stylesheet and one script. The design uses a black background, light text, and red accents, with an optional light mode. A responsive menu, labeled inputs, descriptive image text, visible keyboard focus, and a skip link help visitors navigate the site.

## Challenges and solutions

One challenge was making the large headings and navigation work at different screen sizes. CSS media queries adjust the layout, and JavaScript controls the phone menu. The menu also closes with Escape and resets when the screen size changes. Recorded checks at phone and laptop widths found no horizontal overflow.

Another challenge was making Python downloads useful on phones. A phone may display a Python file as text instead of running it. The download dialog now offers a matching browser demo or the Python source, with an explanation that running the source requires a Python app. The joke demo also handles connection failures by showing an error and letting the visitor try again.

## A Codex mistake and its correction

An earlier Codex-assisted version of the calculator and gradebook downloads ran fixed examples instead of accepting the visitor’s own values. This made the downloads less useful even though the browser demos were interactive. With Codex assistance, the programs were corrected to prompt for input, validate values, and provide a way to quit. The run instructions were also updated.

The corrected downloads were tested with custom input: the calculator returned 4 for 12 divided by 3, and the gradebook accepted Alex with a score of 90 and produced a summary. This example shows why generated code needs to be checked by running it and comparing its behavior with the intended task. The project test log records 57 passed checks, including navigation, layouts, keyboard access, demos, and downloads.

## Website screenshots

The Word report embeds cropped Home page screenshots from November 4, 2026: laptop layout at 1366 px wide and browser-emulated phone layout at 390 × 844 px. Source images: `tests/evidence/index-laptop-dark.png` and `tests/evidence/index-phone-dark.png`.
