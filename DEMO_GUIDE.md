# Portfolio demo practice

This is a preparation guide, not the written report or evidence that the classroom demo has already happened.

## A short walkthrough

1. Open https://asn77s.github.io/ on a laptop. Introduce the portfolio and visit all five pages.
2. Show the About page, your education, DECA membership, and interests.
3. Open the site on a phone (or use Chrome’s phone preview). Open and close the menu and follow a link. Show that content fits without sideways scrolling.
4. Use Tab to show visible focus. Activate Skip to content with Enter. Use Shift+Tab to move backward, Enter for links, and Enter or Space for buttons. Open the mobile menu and close it with Escape.
5. Toggle light mode. Explain that CSS controls the colors and JavaScript changes the active theme class.
6. Demonstrate the gradebook with 90, then an invalid grade such as 101.
7. Calculate 10 + 10 and then try dividing by zero.
8. Add cart products, check the total, remove one, and reset. Explain why prices stay fixed until reset.
9. Fetch a joke and download `jokes.txt`. The API needs an internet connection; show the error message if the service is unavailable.
10. Show `TESTING.md`, the Lighthouse results, and the Git commit history. Download a Python project and run it in a terminal.

## Explain the shared JavaScript

Open `script.js` while practicing. Locate each named function or section and explain it without reading a memorized claim.

### Mobile menu

`querySelector` finds the button and navigation. `matchMedia('(max-width: 760px)')` checks whether the window is phone-sized. `updateMenu()` hides the desktop navigation on a phone and resets `aria-expanded` to false. A click listener changes whether the navigation is hidden. A screen-size change calls `updateMenu()` again. Escape closes the menu and puts keyboard focus back on the menu button.

`aria-expanded` tells assistive technology whether the menu is open. The `hidden` property controls whether it is displayed.

### Light mode

The theme button toggles the `light` class on the body. `styles.css` defines light-theme color variables for that class. `aria-pressed` reports the toggle’s state. Theme choice currently resets when another page loads; it is not stored.

### Gradebook

The submit listener uses `preventDefault()` so the page does not reload. It trims the name and reads the score with `valueAsNumber`. HTML `required`, `min`, and `max` attributes handle common validation; JavaScript also rejects whitespace-only names and invalid scores. Conditions choose A, B, C, D, or F. `textContent` displays the result as text rather than treating a typed name as HTML.

### Calculator

The form reads two numbers and the operation. It checks for finite numbers and rejects division by zero. A `switch` chooses the calculation. A second finite-number check catches results that exceed JavaScript’s number range.

### Shopping cart

`productNames` lists the 12 products. `newProducts()` assigns each product a random integer price in cents and a quantity of zero. `Math.floor(Math.random() * 900) + 100` creates a price from 100 through 999 cents. Two units of each product are available.

`renderOptions()` creates the dropdown options. `changeCart()` prevents buying more than the stock or removing an item that is not in the cart. `renderCart()` uses `reduce()` to add price × quantity for every product and formats the dollar amount to two decimals. Reset creates a fresh product list, so the cart clears and prices change. Prices never change during a shopping session.

### Joke fetcher

`fetch()` requests data from the public joke API. `await` waits for the response without freezing the page. The program checks the HTTP result and the response fields, then displays the setup and punchline. An `AbortController` ends a request after ten seconds. `try/catch/finally` shows an error when needed and restores the button state. Buttons are disabled while loading.

A `Blob` holds the joke text. A temporary object URL lets an anchor download that text as `jokes.txt`. The URL is revoked afterward to release the resource.

### Phone download choice

On phone-sized screens, a Python download link opens a native HTML dialog. It explains the difference between using the browser demo and downloading source code. Try in browser closes the dialog and focuses the first control in the matching demo. The source option keeps the Python file available. Native dialog behavior supports Escape, keeps focus inside while open, and restores focus when dismissed. Desktop downloads remain direct.

### Why one script works on every page

Shared menu and theme controls exist on all five pages. Each project demo is wrapped in an `if` that checks whether its form or button exists. That prevents the script from trying to attach project listeners on pages without those controls.

## Questions to practice

- What is the difference between HTML structure, CSS styling, and JavaScript behavior?
- Why does `preventDefault()` matter for a form demo?
- Why keep cart prices in cents and generate them only at the start/reset?
- What happens if the joke API is unavailable?
- Why are descriptive image text and visible keyboard focus useful?
- Why do the downloaded Python programs run in a terminal while the website demos use JavaScript?

You still need to perform the demo yourself and explain the code in your own words. The written report remains Adrian’s responsibility.
