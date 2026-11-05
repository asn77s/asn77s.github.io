const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
const phoneScreen = window.matchMedia('(max-width: 760px)');

function updateMenu() {
  menuButton.hidden = !phoneScreen.matches;
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.hidden = phoneScreen.matches;
}
updateMenu();
phoneScreen.addEventListener('change', updateMenu);
menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  navigation.hidden = isOpen;
});
navigation.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && phoneScreen.matches) {
    updateMenu();
    menuButton.focus();
  }
});

const themeButton = document.querySelector('#theme-toggle');
themeButton.hidden = false;
themeButton.addEventListener('click', () => {
  const lightMode = document.body.classList.toggle('light');
  themeButton.setAttribute('aria-pressed', String(lightMode));
});

const gradeForm = document.querySelector('#grade-demo');
if (gradeForm) {
  gradeForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const nameInput = document.querySelector('#student-name');
    const name = nameInput.value.trim();
    const score = document.querySelector('#student-grade').valueAsNumber;
    if (!name || !Number.isFinite(score) || score < 0 || score > 100) {
      document.querySelector('#grade-result').textContent = 'Enter a name and a grade from 0 to 100.';
      return;
    }
    const letter = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : score >= 60 ? 'D' : 'F';
    document.querySelector('#grade-result').textContent = `Hello ${name}, your grade is ${letter}.`;
  });
}

const jokeButton = document.querySelector('#fetch-joke');
if (jokeButton) {
  const result = document.querySelector('#joke-result');
  const saveButton = document.querySelector('#save-joke');
  let jokeText = '';
  jokeButton.addEventListener('click', async () => {
    jokeButton.disabled = true;
    saveButton.disabled = true;
    jokeText = '';
    result.textContent = 'Fetching a joke…';
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 10000);
    try {
      const response = await fetch('https://official-joke-api.appspot.com/random_joke', { signal: controller.signal });
      if (!response.ok) throw new Error('Request failed');
      const joke = await response.json();
      if (typeof joke.setup !== 'string' || typeof joke.punchline !== 'string') throw new Error('Invalid joke');
      jokeText = `${joke.setup}\n${joke.punchline}\n`;
      result.textContent = jokeText;
      saveButton.disabled = false;
    } catch {
      result.textContent = 'Could not fetch a joke. Check your connection and try again—the joke service may be unavailable.';
    } finally {
      clearTimeout(timeout);
      jokeButton.disabled = false;
    }
  });
  saveButton.addEventListener('click', () => {
    if (!jokeText) return;
    const url = URL.createObjectURL(new Blob([jokeText], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'jokes.txt';
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
}

const calculatorForm = document.querySelector('#calculator-demo');
if (calculatorForm) {
  calculatorForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const first = document.querySelector('#calc-first').valueAsNumber;
    const second = document.querySelector('#calc-second').valueAsNumber;
    const operation = document.querySelector('#calc-operation').value;
    let result;
    if (!Number.isFinite(first) || !Number.isFinite(second)) result = 'Enter two valid numbers.';
    else if (operation === '/' && second === 0) result = 'Cannot divide by zero.';
    else {
      switch (operation) {
        case '+': result = first + second; break;
        case '-': result = first - second; break;
        case '*': result = first * second; break;
        case '/': result = first / second; break;
        default: result = 'Choose a valid operation.';
      }
      if (typeof result === 'number' && !Number.isFinite(result)) result = 'Result is too large. Try smaller numbers.';
    }
    document.querySelector('#calc-result').textContent = String(result);
  });
}

const cartForm = document.querySelector('#cart-demo');
if (cartForm) {
  const products = [
    { name: 'Frosted Flakes', price: 299, quantity: 0 },
    { name: 'Eggs', price: 599, quantity: 0 },
    { name: 'sourdough loaf', price: 399, quantity: 0 }
  ];
  const message = document.querySelector('#cart-message');
  function renderCart() {
    const lines = products.map(item => `${item.name}: ${item.quantity} in cart · ${2 - item.quantity} on shelf`);
    const total = products.reduce((sum, item) => sum + item.price * item.quantity, 0);
    document.querySelector('#cart-summary').textContent = `${lines.join('\n')}\n\nTotal: $${(total / 100).toFixed(2)}`;
  }
  function changeCart(amount) {
    const item = products[Number(document.querySelector('#cart-product').value)];
    if (!item) return;
    if (amount === 1 && item.quantity === 2) message.textContent = `${item.name} is out of stock.`;
    else if (amount === -1 && item.quantity === 0) message.textContent = `${item.name} is not in your cart.`;
    else {
      item.quantity += amount;
      message.textContent = `${amount === 1 ? 'Added' : 'Removed'} one ${item.name}.`;
      renderCart();
    }
  }
  cartForm.addEventListener('submit', event => { event.preventDefault(); changeCart(1); });
  document.querySelector('#cart-remove').addEventListener('click', () => changeCart(-1));
  document.querySelector('#cart-reset').addEventListener('click', () => {
    products.forEach(item => { item.quantity = 0; });
    message.textContent = 'Cart reset. All products are back on the shelf.';
    renderCart();
  });
  renderCart();
}
