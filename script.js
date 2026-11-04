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
