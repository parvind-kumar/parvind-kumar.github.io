const books = [
  {
    "slug": "six-lanes-of-kamathipura",
    "title": "Six Lanes of Kamathipura",
    "category": [
      "fiction"
    ],
    "kicker": "A NOVEL",
    "description": "A story of lives, choices and the city behind the headlines.",
    "amazon": "https://www.amazon.in/Six-Lanes-Kamathipura-Parvind-Kumar/dp/9376504801",
    "coverClass": "cover-one",
    "coverImage": "https://m.media-amazon.com/images/I/51Z5ASHf3nL._SY445_SX342_FMwebp_.jpg",
    "unavailable": false
  },
  {
    "slug": "when-hope-came-home",
    "title": "When Hope Came Home",
    "category": [
      "fiction"
    ],
    "kicker": "FICTION",
    "description": "A story about hope, home and the courage to begin again.",
    "amazon": "https://www.amazon.in/When-Hope-Came-Parvind-Kumar/dp/9376504275/",
    "coverClass": "cover-two",
    "coverImage": "https://m.media-amazon.com/images/I/717J3Te5ReL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "live-in-relationships",
    "title": "Live-In Relationships: The Untold Truth",
    "category": [
      "relationships",
      "nonfiction"
    ],
    "kicker": "RELATIONSHIPS",
    "description": "Love, independence, commitment and the realities behind modern live-in relationships.",
    "amazon": "https://www.amazon.in/Live-Relationships-Untold-Parvind-Kumar/dp/9376504062",
    "coverClass": "cover-three",
    "coverImage": "https://m.media-amazon.com/images/I/71PEl-ynwaL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "11-shades-of-love",
    "title": "11 Shades of Love: Modern Indian Stories",
    "category": [
      "fiction",
      "relationships"
    ],
    "kicker": "11 STORIES",
    "description": "Modern Indian love stories of passion, conflict, heartbreak and new beginnings.",
    "amazon": "https://www.amazon.in/11-Shades-Love-Modern-Stories/dp/9376503287",
    "coverClass": "cover-four",
    "coverImage": "https://m.media-amazon.com/images/I/71+156bp10L._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "crime-suspense-stories",
    "title": "Crime Suspense Stories",
    "category": [
      "fiction"
    ],
    "kicker": "SUSPENSE",
    "description": "Stories built around mystery, crime, secrets and the consequences of hidden choices.",
    "amazon": "https://www.amazon.in/Crime-suspense-stories-Parvind-Kumar/dp/9376502892/",
    "coverClass": "cover-five",
    "coverImage": "https://m.media-amazon.com/images/I/71PYcSfIf3L._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "lo-shu-grid-numerology",
    "title": "The Complete Guide to Lo Shu Grid Numerology",
    "category": [
      "nonfiction"
    ],
    "kicker": "NUMEROLOGY",
    "description": "An accessible guide to understanding the Lo Shu Grid and its traditional numerological framework.",
    "amazon": "https://www.amazon.in/Complete-Guide-Shu-Grid-Numerology/dp/9376502825",
    "coverClass": "cover-six",
    "coverImage": "https://m.media-amazon.com/images/I/81V5OZmGHoL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "before-we-said-goodbye",
    "title": "Before we said goodbye.",
    "category": [
      "fiction",
      "relationships"
    ],
    "kicker": "LOVE STORIES",
    "description": "Stories about love, loss, memories and the words left unsaid.",
    "amazon": "https://www.amazon.in/Before-said-goodbye-Parvind-Kumar/dp/937650321X",
    "coverClass": "cover-seven",
    "coverImage": "https://m.media-amazon.com/images/I/71Uo5ZlPL6L._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "vintage-between-us",
    "title": "The Vintage Between Us: A Tuscan Vineyard Romance",
    "category": [
      "fiction",
      "relationships"
    ],
    "kicker": "ROMANCE",
    "description": "A Tuscan vineyard, two people and a romance caught between past and present.",
    "amazon": "https://www.amazon.in/Vintage-Between-Us-Vineyard-Romance/dp/B0H95CSR8H/",
    "coverClass": "cover-eight",
    "coverImage": "https://m.media-amazon.com/images/I/61eVBttz0DL._SY522_.jpg",
    "unavailable": false
  },
  {
    "slug": "after-the-promise-broke",
    "title": "After the Promise Broke",
    "category": [
      "fiction",
      "relationships"
    ],
    "kicker": "ROMANCE \u00b7 THRILLER",
    "description": "Stories of betrayal, romance, psychological tension and the search for redemption.",
    "amazon": "https://www.amazon.in/After-Promise-Broke-Parvind-Kumar/dp/9376503481/",
    "coverClass": "cover-nine",
    "coverImage": "https://m.media-amazon.com/images/I/71rSw1nyW7L._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "building-happy-marriage",
    "title": "The Complete Guide to Building a Happy Marriage & Lasting Love",
    "category": [
      "relationships",
      "nonfiction"
    ],
    "kicker": "MARRIAGE",
    "description": "Practical ideas for communication, trust, intimacy and building a lasting partnership.",
    "amazon": "https://www.amazon.in/Complete-Guide-Building-Marriage-Lasting/dp/9376502906/",
    "coverClass": "cover-ten",
    "coverImage": "https://m.media-amazon.com/images/I/71evLi+WBrL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "mindfulness-meditation",
    "title": "The Complete Guide to Mindfulness & Meditation",
    "category": [
      "mind",
      "nonfiction"
    ],
    "kicker": "MINDFULNESS",
    "description": "A practical journey into mindfulness, meditation, attention and everyday calm.",
    "amazon": "https://www.amazon.in/Complete-Guide-Mindfulness-Meditation/dp/9360381705/",
    "coverClass": "cover-eleven",
    "coverImage": "https://m.media-amazon.com/images/I/71KHnfkhauL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "escape-endless-scroll",
    "title": "Escape the Endless Scroll",
    "category": [
      "mind",
      "nonfiction"
    ],
    "kicker": "DIGITAL WELLBEING",
    "description": "How to reduce screen time, break the scrolling cycle and reclaim real life.",
    "amazon": "https://www.amazon.in/Escape-Endless-Scroll-Parvind-Kumar/dp/9376503260/",
    "coverClass": "cover-twelve",
    "coverImage": "https://m.media-amazon.com/images/I/71znBiXKnVL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "what-happens-after-death",
    "title": "What Happens After Death?",
    "category": [
      "nonfiction",
      "Personal Development"
    ],
    "kicker": "PERSONAL DEVELOPMENT",
    "description": "The Soul, Near-Death Experiences, Reincarnation, and the Scientific Search for Life After Death.",
    "amazon": "https://www.amazon.in/dp/9376505468",
    "coverClass": "cover-twelve",
    "coverImage": "https://m.media-amazon.com/images/I/819+67sYZhL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "ganga-expressway",
    "title": "The Ganga Expressway",
    "category": [
      "business",
      "nonfiction"
    ],
    "kicker": "BUSINESS",
    "description": "India's longest expressway just opened \u2014 and it's changing Uttar Pradesh forever.",
    "amazon": "https://www.amazon.in/Ganga-Expressway-Parvind-Kumar/dp/9376503511/",
    "coverClass": "cover-thirteen",
    "coverImage": "https://m.media-amazon.com/images/I/81hqsU3lBkL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "talaq-se-pehle",
    "title": "Talaq Se Pehle",
    "category": [
      "relationships",
      "nonfiction"
    ],
    "kicker": "MARRIAGE & DIVORCE GUIDE",
    "description": "\u0924\u0932\u093e\u0915 \u0938\u0947 \u092a\u0939\u0932\u0947 (Talaq Se Pehle) \u0932\u0947\u0916\u0915 \u092a\u0930\u0935\u093f\u0928\u094d\u0926 \u0915\u0941\u092e\u093e\u0930 \u0926\u094d\u0935\u093e\u0930\u093e \u0935\u0948\u0935\u093e\u0939\u093f\u0915 \u0914\u0930 \u0938\u093e\u092e\u093e\u091c\u093f\u0915 \u0935\u093f\u0937\u092f\u094b\u0902 \u092a\u0930 \u0932\u093f\u0916\u0940 \u0917\u0908 \u090f\u0915 \u092e\u0939\u0924\u094d\u0935\u092a\u0942\u0930\u094d\u0923 \u0930\u091a\u0928\u093e \u0939\u0948\u0964",
    "amazon": "https://www.amazon.in/s?k=Talaq+Se+Pehle+Parvind+Kumar",
    "coverClass": "cover-fourteen",
    "coverImage": "https://m.media-amazon.com/images/I/71evLi+WBrL._SL1500_.jpg",
    "unavailable": false
  },
  {
    "slug": "why-india-cancer-capital",
    "title": "Why Is India Becoming the Cancer Capital?",
    "category": [
      "nonfiction"
    ],
    "kicker": "PUBLIC HEALTH",
    "description": "Why more Indians are facing cancer, what pollution, tobacco, diet and delayed diagnosis really have to do with it, and what an ordinary family can do about it.",
    "amazon": "",
    "coverClass": "cover-fifteen",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/5XwDEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "the-virus-between-us",
    "title": "The Virus Between Us",
    "category": [
      "fiction"
    ],
    "kicker": "ROMANCE \u00b7 THRILLER",
    "description": "An HIV diagnosis, a doctor's suspicious death, and a woman who won't stop asking questions \u2014 a suspenseful story about stigma, secrets, and redemption.",
    "amazon": "",
    "coverClass": "cover-sixteen",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/ul4EEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "the-bageshwar-phenomenon",
    "title": "The Bageshwar Phenomenon",
    "category": [
      "nonfiction"
    ],
    "kicker": "BIOGRAPHY",
    "description": "The life, rise and controversies of Dhirendra Krishna Shastri \u2014 from a village in Madhya Pradesh to one of India's most talked-about spiritual figures.",
    "amazon": "",
    "coverClass": "cover-seventeen",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/-VUCEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "pati-patni-aur-woh",
    "title": "\u092a\u0924\u093f, \u092a\u0924\u094d\u0928\u0940 \u0914\u0930 \u0935\u094b",
    "category": [
      "fiction"
    ],
    "kicker": "\u0930\u0939\u0938\u094d\u092f \u0930\u094b\u092e\u093e\u0902\u0938",
    "description": "\u0906\u0930\u094d\u092f\u0928, \u092e\u0940\u0930\u093e \u0914\u0930 \u0930\u094b\u0939\u0928 \u0915\u0940 \u0915\u0939\u093e\u0928\u0940 \u2014 \u092a\u094d\u092f\u093e\u0930, \u0936\u0915 \u0914\u0930 \u0930\u093e\u091c\u093c \u091c\u092c \u090f\u0915 \u0939\u0940 \u091b\u0924 \u0915\u0947 \u0928\u0940\u091a\u0947 \u091f\u0915\u0930\u093e\u0924\u0947 \u0939\u0948\u0902, \u0924\u094b \u0938\u091a\u094d\u091a\u093e\u0908 \u0915\u093f\u0938\u0940 \u0928\u0947 \u0938\u094b\u091a\u0940 \u092d\u0940 \u0928\u0939\u0940\u0902 \u0925\u0940\u0964",
    "amazon": "",
    "coverClass": "cover-eighteen",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/69_2EQAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "the-american-distance",
    "title": "The American Distance",
    "category": [
      "fiction",
      "relationships"
    ],
    "kicker": "CONTEMPORARY ROMANCE",
    "description": "An immigration lawyer and a tech executive fall for each other just as she uncovers that the algorithm hurting her client was built by his own company.",
    "amazon": "",
    "coverClass": "cover-nineteen",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/HfACEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "lose-weight-without-dieting",
    "title": "Lose Weight Without Dieting",
    "category": [
      "nonfiction",
      "mind"
    ],
    "kicker": "HEALTH & WELLNESS",
    "description": "A short, science-backed guide to losing weight through mindful eating, sleep, stress and movement \u2014 without restriction or calorie counting.",
    "amazon": "",
    "coverClass": "cover-twenty",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/hjXvEQAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "101-stories-of-lord-shiva",
    "title": "101 Stories of Lord Shiva",
    "category": [
      "nonfiction"
    ],
    "kicker": "MYTHOLOGY",
    "description": "101 stories of Mahadev \u2014 from the endless pillar of light to Shiva's many forms and sacred places \u2014 and the lessons they still offer today.",
    "amazon": "",
    "coverClass": "cover-twenty-one",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/XtMEEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "101-stories-of-buddha",
    "title": "101 Stories of Buddha",
    "category": [
      "nonfiction",
      "mind"
    ],
    "kicker": "MYTHOLOGY & PHILOSOPHY",
    "description": "The journey of Siddhartha Gautama and 101 stories exploring anger, attachment, mindfulness, and how ancient Buddhist wisdom applies to modern, distracted life.",
    "amazon": "",
    "coverClass": "cover-twenty-two",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/OQwFEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "focused-101",
    "title": "Focused 101",
    "category": [
      "nonfiction",
      "mind"
    ],
    "kicker": "PRODUCTIVITY",
    "description": "A practical system for reclaiming attention and beating distraction \u2014 from Notification Zero to a structured 90-Day Focus Challenge.",
    "amazon": "",
    "coverClass": "cover-twenty-three",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/l1ACEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "the-new-indian-marriage",
    "title": "The New Indian Marriage",
    "category": [
      "nonfiction",
      "relationships"
    ],
    "kicker": "SOCIETY & RELATIONSHIPS",
    "description": "What Indian marriage actually looks like today \u2014 arranged marriage in the smartphone era, live-in relationships, dowry, dating apps, and a generation delaying marriage entirely.",
    "amazon": "",
    "coverClass": "cover-twenty-four",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/6DoCEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "freedom-and-partition",
    "title": "Freedom and Partition",
    "category": [
      "nonfiction"
    ],
    "kicker": "HISTORY",
    "description": "How India's freedom movement led to Partition \u2014 from Gandhi's mass movements to the Radcliffe Line and the refugee crisis that followed August 1947.",
    "amazon": "",
    "coverClass": "cover-twenty-five",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/QCcCEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "101-stories-of-lord-krishna",
    "title": "101 Stories of Lord Krishna",
    "category": [
      "nonfiction"
    ],
    "kicker": "MYTHOLOGY",
    "description": "From Krishna's birth in Mathura to the battlefield of Kurukshetra \u2014 101 stories of divine love, friendship, courage and dharma.",
    "amazon": "",
    "coverClass": "cover-twenty-six",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/fqgDEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "the-price-of-an-ordinary-life",
    "title": "The Price of an Ordinary Life",
    "category": [
      "fiction"
    ],
    "kicker": "FICTION",
    "description": "A middle-class man in Delhi NCR loses his job \u2014 and a year strips away every assumption his family made about security.",
    "amazon": "",
    "coverClass": "cover-twenty-seven",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/vqYCEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "101-stories-of-lord-ganesha",
    "title": "101 Stories of Lord Ganesha",
    "category": [
      "nonfiction"
    ],
    "kicker": "MYTHOLOGY",
    "description": "From the boy guarding his mother's door to the remover of obstacles celebrated at every festival \u2014 101 stories of Ganesha's life, legend and teachings.",
    "amazon": "",
    "coverClass": "cover-twenty-eight",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/IZ4EEgAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "marriage-turned-murder",
    "title": "Marriage Turned Murder",
    "category": [
      "nonfiction"
    ],
    "kicker": "TRUE CRIME",
    "description": "Twenty real Indian marriages that ended in murder \u2014 built from police statements, court filings, and verified news reports.",
    "amazon": "",
    "coverClass": "cover-twenty-nine",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/FeP_EQAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "digital-product-sales-marketing-strategy",
    "title": "Digital Product Sales & Marketing Strategy",
    "category": [
      "business",
      "nonfiction"
    ],
    "kicker": "BUSINESS",
    "description": "A 164-page, 27-chapter practitioner guide to building, launching and scaling a digital product business, with templates for every step.",
    "amazon": "",
    "coverClass": "cover-thirty",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/VIn3EQAAQBAJ?fife=w800",
    "unavailable": false
  },
  {
    "slug": "101-public-speaking-tips",
    "title": "101 Public Speaking Tips",
    "category": [
      "nonfiction",
      "mind"
    ],
    "kicker": "SELF-HELP",
    "description": "101 actionable techniques for public speaking \u2014 from conquering fear to structuring speeches, vocal delivery, and a 30-day action plan.",
    "amazon": "",
    "coverClass": "cover-thirty-one",
    "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/eCoDEgAAQBAJ?fife=w800",
    "unavailable": false
  }
];

const bookGrid = document.getElementById("bookGrid");

function renderBooks(filter = "all") {
  const visible = books.filter(book => filter === "all" || book.category.includes(filter));

  bookGrid.innerHTML = visible.map(book => `
    <article class="book-card reveal">
      <a href="books/${book.slug}/" aria-label="Read details of ${escapeHtml(book.title)}">
        <div class="book-cover ${book.coverClass}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.7) 100%), url('${book.coverImage}');">
          <span class="cover-kicker">${escapeHtml(book.kicker)}</span>
          <span class="cover-title">${escapeHtml(book.title)}</span>
          <span class="cover-author">PARVIND KUMAR</span>
        </div>
      </a>
      <div class="book-meta">
        <h3>${escapeHtml(book.title)}</h3>
        <p>${escapeHtml(book.description)}${book.unavailable ? ' <span class="status">Currently unavailable</span>' : ''}</p>
        <a class="book-link" href="books/${book.slug}/">Read Book Details &rarr;</a>
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
  ".cover-thirteen": ["#3b4c5b", "#c8a46b"],
  ".cover-fourteen": ["#743326", "#fbe8e4"],
  ".cover-fifteen": ["#5c2a2a", "#e8c9a0"],
  ".cover-sixteen": ["#1f2937", "#a9c4d9"],
  ".cover-seventeen": ["#4a3728", "#d8c3a5"],
  ".cover-eighteen": ["#6b1f2a", "#f2d9c4"],
  ".cover-nineteen": ["#2d4a4a", "#d9b98d"],
  ".cover-twenty": ["#3a5a40", "#dad7cd"],
  ".cover-twenty-one": ["#35281a", "#e3b23c"],
  ".cover-twenty-two": ["#22303a", "#c9a66b"],
  ".cover-twenty-three": ["#263238", "#80cbc4"],
  ".cover-twenty-four": ["#4b2e39", "#e0b0a0"],
  ".cover-twenty-five": ["#33312e", "#c1a875"],
  ".cover-twenty-six": ["#1a2a4a", "#e8c468"],
  ".cover-twenty-seven": ["#3d3d3d", "#e0c097"],
  ".cover-twenty-eight": ["#b0413e", "#fdf0d5"],
  ".cover-twenty-nine": ["#261c1c", "#c94c4c"],
  ".cover-thirty": ["#1b3a4b", "#8ecae6"],
  ".cover-thirty-one": ["#4a4e69", "#f2e9e4"]
};

const style = document.createElement("style");
let css = "";
Object.entries(coverClasses).forEach(([selector, [bg, fg]]) => {
  css += `${selector}{background-color:${bg};color:#fffdf7;}`;
});
style.textContent = css;
document.head.appendChild(style);

renderBooks();
observeReveals();
