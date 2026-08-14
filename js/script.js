const books = [
  {
    title: "Six Lanes of Kamathipura",
    category: ["fiction"],
    kicker: "A NOVEL",
    description: "A story of lives, choices and the city behind the headlines.",
    amazon: "https://www.amazon.in/s?k=Six+Lanes+of+Kamathipura",
    coverClass: "cover-one"
  },
  {
    title: "When Hope Came Home",
    category: ["fiction"],
    kicker: "FICTION",
    description: "A story about hope, home and the courage to begin again.",
    amazon: "https://www.amazon.in/s?k=When+Hope+Came+Home",
    coverClass: "cover-two"
  },
  {
    title: "Live-In Relationships: The Untold Truth",
    category: ["relationships", "nonfiction"],
    kicker: "RELATIONSHIPS",
    description: "Love, independence, commitment and the realities behind modern live-in relationships.",
    amazon: "https://www.amazon.in/s?k=Live-In+Relationships+The+Untold+Truth",
    coverClass: "cover-three"
  },
  {
    title: "11 Shades of Love: Modern Indian Stories",
    category: ["fiction", "relationships"],
    kicker: "11 STORIES",
    description: "Modern Indian love stories of passion, conflict, heartbreak and new beginnings.",
    amazon: "https://www.amazon.in/s?k=11+Shades+of+Love+Modern+Indian+Stories",
    coverClass: "cover-four"
  },
  {
    title: "Crime Suspense Stories",
    category: ["fiction"],
    kicker: "SUSPENSE",
    description: "Stories built around mystery, crime, secrets and the consequences of hidden choices.",
    amazon: "https://www.amazon.in/s?k=Parvind+Kumar+Crime+Suspense+Stories",
    coverClass: "cover-five"
  },
  {
    title: "The Complete Guide to Lo Shu Grid Numerology",
    category: ["nonfiction"],
    kicker: "NUMEROLOGY",
    description: "An accessible guide to understanding the Lo Shu Grid and its traditional numerological framework.",
    amazon: "https://www.amazon.in/s?k=The+Complete+Guide+to+Lo+Shu+Grid+Numerology",
    coverClass: "cover-six"
  },
  {
    title: "Before we said goodbye.",
    category: ["fiction", "relationships"],
    kicker: "LOVE STORIES",
    description: "Stories about love, loss, memories and the words left unsaid.",
    amazon: "https://www.amazon.in/s?k=Before+we+said+goodbye+Parvind+Kumar",
    coverClass: "cover-seven"
  },
  {
    title: "The Vintage Between Us: A Tuscan Vineyard Romance",
    category: ["fiction", "relationships"],
    kicker: "ROMANCE",
    description: "A Tuscan vineyard, two people and a romance caught between past and present.",
    amazon: "https://www.amazon.in/s?k=The+Vintage+Between+Us+A+Tuscan+Vineyard+Romance",
    coverClass: "cover-eight"
  },
  {
    title: "After the Promise Broke",
    category: ["fiction", "relationships"],
    kicker: "ROMANCE · THRILLER",
    description: "Stories of betrayal, romance, psychological tension and the search for redemption.",
    amazon: "https://www.amazon.in/s?k=After+the+Promise+Broke+Parvind+Kumar",
    coverClass: "cover-nine"
  },
  {
    title: "The Complete Guide to Building a Happy Marriage & Lasting Love",
    category: ["relationships", "nonfiction"],
    kicker: "MARRIAGE",
    description: "Practical ideas for communication, trust, intimacy and building a lasting partnership.",
    amazon: "https://www.amazon.in/s?k=Complete+Guide+Building+Happy+Marriage+Lasting+Love",
    coverClass: "cover-ten"
  },
  {
    title: "The Complete Guide to Mindfulness & Meditation",
    category: ["mind", "nonfiction"],
    kicker: "MINDFULNESS",
    description: "A practical journey into mindfulness, meditation, attention and everyday calm.",
    amazon: "https://www.amazon.in/s?k=Complete+Guide+to+Mindfulness+Meditation+Parvind+Kumar",
    coverClass: "cover-eleven",
    unavailable: true
  },
  {
    title: "Escape the Endless Scroll",
    category: ["mind", "nonfiction"],
    kicker: "DIGITAL WELLBEING",
    description: "How to reduce screen time, break the scrolling cycle and reclaim real life.",
    amazon: "https://www.amazon.in/s?k=Escape+the+Endless+Scroll+Parvind+Kumar",
    coverClass: "cover-twelve"
  },
  {
    title: "The Ganga Expressway",
    category: ["fiction"],
    kicker: "FICTION",
    description: "A journey, a road and the human stories that unfold along the way.",
    amazon: "https://www.amazon.in/s?k=The+Ganga+Expressway+Parvind+Kumar",
    coverClass: "cover-thirteen"
  }
];

const bookGrid = document.getElementById("bookGrid");

function renderBooks(filter = "all") {
  const visible = books.filter(book => filter === "all" || book.category.includes(filter));

  bookGrid.innerHTML = visible.map(book => `
    <article class="book-card reveal">
      <a href="${book.amazon}" target="_blank" rel="noopener" aria-label="Find ${escapeHtml(book.title)} on Amazon">
        <div class="book-cover ${book.coverClass}">
          <span class="cover-kicker">${escapeHtml(book.kicker)}</span>
          <span class="cover-title">${escapeHtml(book.title)}</span>
          <span class="cover-author">PARVIND KUMAR</span>
        </div>
      </a>
      <div class="book-meta">
        <h3>${escapeHtml(book.title)}</h3>
        <p>${escapeHtml(book.description)}${book.unavailable ? ' <span class="status">Currently unavailable</span>' : ''}</p>
        <a class="book-link" href="${book.amazon}" target="_blank" rel="noopener">Find on Amazon ↗</a>
      </div>
    </article>
  `).join("");

  observeReveals();
}

document.querySelectorAll(".filter").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".filter").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
    renderBooks(button.dataset.filter);
  });
});

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, char => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
  }[char]));
}

const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.getElementById("site-nav");

menuToggle.addEventListener("click", () => {
  const open = siteNav.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", open ? "true" : "false");
});

siteNav.querySelectorAll("a").forEach(link => {
  link.addEventListener("click", () => {
    siteNav.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
  });
});

function observeReveals() {
  const items = document.querySelectorAll(".reveal:not(.observed)");
  if (!("IntersectionObserver" in window)) {
    items.forEach(el => el.classList.add("visible"));
    return;
  }
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        entry.target.classList.add("observed");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  items.forEach(item => observer.observe(item));
}

document.getElementById("newsletterForm").addEventListener("submit", event => {
  event.preventDefault();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("formMessage");

  if (!email) return;
  message.textContent = "Thanks! Connect a newsletter service such as Mailchimp, Buttondown or ConvertKit to collect subscribers.";
  event.target.reset();
});

document.getElementById("year").textContent = new Date().getFullYear();

const coverClasses = {
  ".cover-one": ["#2e2a27", "#d0a57b"],
  ".cover-two": ["#d6c5ab", "#4b352b"],
  ".cover-three": ["#213c37", "#d6b58d"],
  ".cover-four": ["#6e3029", "#f0d7bb"],
  ".cover-five": ["#24282c", "#c9a76c"],
  ".cover-six": ["#3d3a5d", "#d9c58c"],
  ".cover-seven": ["#c9b5a1", "#573f39"],
  ".cover-eight": ["#31554b", "#dfc99e"],
  ".cover-nine": ["#4a2730", "#d6a28e"],
  ".cover-ten": ["#8b5d39", "#f1dec4"],
  ".cover-eleven": ["#31445a", "#c7d6d8"],
  ".cover-twelve": ["#282b2f", "#91b1a5"],
  ".cover-thirteen": ["#3b4c5b", "#c8a46b"]
};

const style = document.createElement("style");
let css = "";
Object.entries(coverClasses).forEach(([selector, [bg, fg]]) => {
  css += `${selector}{background:linear-gradient(145deg,${bg},${fg});color:#fffdf7;}`;
});
style.textContent = css;
document.head.appendChild(style);

renderBooks();
observeReveals();
