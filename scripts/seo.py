"""SEO helpers for generate_book_pages.py: meta tags, JSON-LD, FAQ, related books, sitemap, homepage prerender."""
import datetime
import html
import json
import os
import re

from seo_keywords import EXTRA_KEYWORDS, GENERIC_BY_CATEGORY, KICKER_KEYWORDS

SITE_URL = "https://parvindkumar.com"
SITE_NAME = "Parvind Kumar"
TWITTER_HANDLE = "@parvind_writes"
PERSON_ID = SITE_URL + "/#person"
WEBSITE_ID = SITE_URL + "/#website"
SAME_AS = [
    "https://github.com/parvind-kumar",
    "https://www.instagram.com/parvindsharma",
    "https://x.com/parvind_writes",
    "https://www.facebook.com/people/Parvind-Kumar/61593388342955/",
]
AUTHOR_BIO = {
    "en": "Parvind Kumar is an independent Indian author whose books span fiction, relationships, marriage, mythology, personal growth, health and contemporary social themes.",
    "hi": "परविन्द कुमार एक स्वतंत्र भारतीय लेखक हैं, जिनकी पुस्तकें कथा साहित्य, रिश्तों, विवाह, पौराणिक कथाओं, व्यक्तिगत विकास और समकालीन सामाजिक विषयों पर केंद्रित हैं।",
}
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
TODAY = datetime.date.today().isoformat()


def esc(value):
    return html.escape(str(value), quote=True)


def esct(value):
    return html.escape(str(value), quote=False)


def lang_code(book):
    return "hi" if book["language"].lower() == "hindi" else "en"


def book_url(slug):
    return f"{SITE_URL}/books/{slug}/"


def is_real_play(url):
    return bool(url) and "play.google.com/store/books/details" in url


def is_real_amazon(url):
    return bool(url) and "/dp/" in url


def is_real_goodreads(url):
    return bool(url) and "/book/show/" in url


def real_isbn(isbn):
    digits = re.sub(r"\D", "", isbn or "")
    return digits if len(digits) == 13 and digits[:3] in ("978", "979") else None


def cover_src(url, width=800):
    return re.sub(r"fife=w\d+", f"fife=w{width}", url)


def cover_alt(book):
    if lang_code(book) == "hi":
        return f"{book['title']} — परविन्द कुमार की पुस्तक का कवर"
    return f"{book['title']} by Parvind Kumar — book cover"


def pub_year_month(book):
    parts = book["publication_date"].split("-")
    if len(parts) == 3:
        return f"{MONTHS_EN[int(parts[1]) - 1]} {parts[0]}"
    return book["publication_date"]


def meta_title(book):
    base = f"{book['title']} by {'परविन्द कुमार' if lang_code(book) == 'hi' else 'Parvind Kumar'}"
    for suffix in (f" | {book['kicker']} Book", f" | {book['kicker']}"):
        if len(base + suffix) <= 65:
            return base + suffix
    return base


def meta_description(book):
    text = book["description"].strip()
    if lang_code(book) == "hi":
        return text if len(text) <= 160 else text[:157].rsplit(" ", 1)[0] + "…"
    if len(text) > 160:
        return text[:157].rsplit(" ", 1)[0].rstrip(",;—- ") + "…"
    if len(text) < 120:
        first_sentence = re.split(r"(?<=[.!?])\s+", book["long_description"].strip())[0]
        if len(text) + 1 + len(first_sentence) <= 160:
            text = f"{text} {first_sentence}"
    for extra in ("Read it on Google Play Books.", "By Parvind Kumar."):
        if is_real_play(book.get("google_play")) or extra != "Read it on Google Play Books.":
            if len(text) + 1 + len(extra) <= 160:
                text = f"{text} {extra}"
    return text


def keywords(book):
    title = book["title"]
    author = "परविन्द कुमार" if lang_code(book) == "hi" else "Parvind Kumar"
    out = [title, f"{title} {author}", f"{title} ebook"]
    if is_real_play(book.get("google_play")):
        out.append(f"{title} Google Play Books")
    if is_real_amazon(book.get("amazon")):
        out.append(f"{title} paperback")
    out += EXTRA_KEYWORDS.get(book["slug"], [])
    out += KICKER_KEYWORDS.get(book["kicker"], [])
    for cat in book["category"]:
        out += GENERIC_BY_CATEGORY.get(cat, [])
    out += ["Parvind Kumar books", "Parvind Kumar author", "परविन्द कुमार" if lang_code(book) == "hi" else "Indian author ebooks"]
    seen, unique = set(), []
    for kw in out:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            unique.append(kw)
    return unique[:18]


def genres(book):
    result = []
    if "fiction" in book["category"]:
        result.append("Fiction")
    if "nonfiction" in book["category"]:
        result.append("Non-fiction")
    result.append(book["kicker"])
    return result


def faq_items(book, trans):
    """Question/answer pairs built only from facts already on the page."""
    hi = lang_code(book) == "hi"
    title = book["title"]
    first_para = book["long_description"].split("\n\n")[0].strip()
    stores = []
    if is_real_play(book.get("google_play")):
        stores.append("Google Play Books")
    if is_real_amazon(book.get("amazon")):
        stores.append("Amazon.in")
    month_year = pub_year_month(book)
    if hi:
        where = " और ".join(stores) if stores else "इस पृष्ठ पर दिए गए लिंक"
        return [
            (f"{title} किस बारे में है?", first_para),
            (f"{title} के लेखक कौन हैं?", f"{title} के लेखक परविन्द कुमार हैं। {AUTHOR_BIO['hi']}"),
            (f"{title} कहाँ पढ़ें या खरीदें?", f"{title} {where} पर उपलब्ध है।"),
            (f"{title} कितने पृष्ठों की है और किस भाषा में है?", f"यह पुस्तक {book['language']} भाषा में है, लगभग {book['pages']} पृष्ठों की है और {month_year} में प्रकाशित हुई। प्रारूप: {book['formats']}।"),
        ]
    where = " and ".join(stores) if stores else "the links on this page"
    return [
        (f"What is {title} about?", first_para),
        (f"Who is the author of {title}?", f"{title} is written by Parvind Kumar. {AUTHOR_BIO['en']}"),
        (f"Where can I read or buy {title}?", f"{title} is available on {where}."),
        (f"How many pages is {title} and what language is it in?", f"{title} is published in {book['language']}, runs to about {book['pages']} pages, and was published in {month_year}. Format: {book['formats']}."),
    ]


def related_books(book, books, count=8):
    idx = books.index(book)
    scored = []
    for j, other in enumerate(books):
        if other is book:
            continue
        score = 0
        if other["kicker"] == book["kicker"]:
            score += 4
        score += 2 * len(set(other["category"]) & set(book["category"]) - {"nonfiction", "fiction"})
        score += 1 * len(set(other["category"]) & set(book["category"]))
        if other["language"] == book["language"]:
            score += 1
        if other["title"].split()[0] == book["title"].split()[0] and book["title"].split()[0].isdigit():
            score += 5
        scored.append((-score, (j - idx) % len(books), other))
    scored.sort(key=lambda row: (row[0], row[1]))
    return [row[2] for row in scored[:count]]


def card_html(book, base, lazy=True, ctx="detail"):
    """Static book card shared by detail-page 'related' blocks and the homepage prerender."""
    title, slug = esct(book["title"]), book["slug"]
    href = f"{base}{slug}/"
    status = ' <span class="status">Currently unavailable</span>' if book.get("unavailable") else ""
    loading = "lazy" if lazy else "eager"
    return f"""
              <article class="book-card reveal visible">
                <a href="{href}" aria-label="Read details of {esc(book['title'])}">
                  <div class="book-cover {book['coverClass']} has-img">
                    <img class="cover-img" src="{esc(cover_src(book['coverImage'], 400))}" alt="{esc(cover_alt(book))}" width="240" height="353" loading="{loading}" decoding="async">
                    <span class="cover-kicker">{esct(book['kicker'].upper())}</span>
                    <span class="cover-title">{title}</span>
                    <span class="cover-author">PARVIND KUMAR</span>
                  </div>
                </a>
                <div class="book-meta">
                  <h3><a href="{href}">{title}</a></h3>
                  <p>{esct(book['description'])}{status}</p>
                  <a class="book-link" href="{href}">Read Book Details &rarr;</a>
                </div>
              </article>"""


def head_html(book, trans):
    """Everything between <meta viewport> and the favicon: title, meta, social, hreflang."""
    lc = lang_code(book)
    url = book_url(book["slug"])
    title = meta_title(book)
    desc = meta_description(book)
    kws = keywords(book)
    img = book["coverImage"]
    alt = cover_alt(book)
    locale = "hi_IN" if lc == "hi" else "en_IN"
    isbn = real_isbn(book.get("isbn"))
    tags = "\n".join(f'  <meta property="book:tag" content="{esc(k)}">' for k in kws[:8])
    isbn_tag = f'\n  <meta property="book:isbn" content="{isbn}">' if isbn else ""
    return f"""<title>{esct(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="keywords" content="{esc(', '.join(kws))}">
  <meta name="author" content="{esc(trans['author_name'])}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="theme-color" content="#131210">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="{lc}" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">
  <link rel="preconnect" href="https://play.google.com" crossorigin>
  <meta property="og:type" content="book">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:locale" content="{locale}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{esc(img)}">
  <meta property="og:image:secure_url" content="{esc(img)}">
  <meta property="og:image:alt" content="{esc(alt)}">
  <meta property="book:author" content="{SITE_URL}/">
  <meta property="book:release_date" content="{book['publication_date']}">{isbn_tag}
{tags}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="{TWITTER_HANDLE}">
  <meta name="twitter:creator" content="{TWITTER_HANDLE}">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{esc(img)}">
  <meta name="twitter:image:alt" content="{esc(alt)}">"""


def person_node():
    return {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "Parvind Kumar",
        "url": SITE_URL + "/",
        "jobTitle": "Author",
        "sameAs": SAME_AS,
    }


def json_ld(book, trans, faq, related):
    lc = lang_code(book)
    url = book_url(book["slug"])
    book_id = url + "#book"
    page_id = url + "#webpage"
    isbn = real_isbn(book.get("isbn"))
    desc = meta_description(book)

    editions = []
    if is_real_play(book.get("google_play")):
        editions.append({
            "@type": "Book",
            "bookFormat": "https://schema.org/EBook",
            "name": f"{book['title']} (eBook)",
            "inLanguage": lc,
            "url": book["google_play"],
            "potentialAction": {
                "@type": "ReadAction",
                "target": {
                    "@type": "EntryPoint",
                    "urlTemplate": book["google_play"],
                    "actionPlatform": ["http://schema.org/DesktopWebPlatform", "http://schema.org/MobileWebPlatform"],
                },
            },
        })
    if is_real_amazon(book.get("amazon")):
        editions.append({
            "@type": "Book",
            "bookFormat": "https://schema.org/Paperback",
            "name": f"{book['title']} (Paperback)",
            "inLanguage": lc,
            "url": book["amazon"],
            "potentialAction": {"@type": "ReadAction", "target": {"@type": "EntryPoint", "urlTemplate": book["amazon"]}},
        })

    same_as = [u for u in (book.get("google_play") if is_real_play(book.get("google_play")) else None,
                           book.get("amazon") if is_real_amazon(book.get("amazon")) else None,
                           book.get("goodreads") if is_real_goodreads(book.get("goodreads")) else None) if u]

    book_node = {
        "@type": "Book",
        "@id": book_id,
        "name": book["title"],
        "alternateName": book["subtitle"],
        "url": url,
        "mainEntityOfPage": {"@id": page_id},
        "author": {"@id": PERSON_ID},
        "creator": {"@id": PERSON_ID},
        "publisher": {"@type": "Organization", "name": book["publisher"]},
        "inLanguage": lc,
        "genre": genres(book),
        "keywords": ", ".join(keywords(book)),
        "numberOfPages": book["pages"],
        "datePublished": book["publication_date"],
        "image": {"@type": "ImageObject", "url": book["coverImage"], "caption": cover_alt(book)},
        "description": desc,
        "abstract": book["long_description"].split("\n\n")[0].strip(),
        "workExample": editions,
    }
    if isbn:
        book_node["isbn"] = isbn
    if same_as:
        book_node["sameAs"] = same_as
    if not editions:
        del book_node["workExample"]

    page_node = {
        "@type": "WebPage",
        "@id": page_id,
        "url": url,
        "name": meta_title(book),
        "description": desc,
        "inLanguage": lc,
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": book_id},
        "primaryImageOfPage": {"@type": "ImageObject", "url": book["coverImage"]},
        "breadcrumb": {"@id": url + "#breadcrumb"},
        "dateModified": TODAY,
    }
    breadcrumb = {
        "@type": "BreadcrumbList",
        "@id": url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": "Books", "item": SITE_URL + "/#books"},
            {"@type": "ListItem", "position": 3, "name": book["title"], "item": url},
        ],
    }
    faq_node = {
        "@type": "FAQPage",
        "@id": url + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }
    graph = [person_node(), page_node, book_node, breadcrumb, faq_node]
    payload = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    payload = payload.replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{payload}\n  </script>'


def sitemap_xml(books):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
             "  <url>", f"    <loc>{SITE_URL}/</loc>", f"    <lastmod>{TODAY}</lastmod>",
             "    <changefreq>weekly</changefreq>", "    <priority>1.0</priority>", "  </url>"]
    for book in sorted(books, key=lambda b: b["slug"]):
        lines += ["  <url>", f"    <loc>{book_url(book['slug'])}</loc>", f"    <lastmod>{TODAY}</lastmod>",
                  "    <changefreq>monthly</changefreq>", "    <priority>0.8</priority>",
                  "    <image:image>", f"      <image:loc>{html.escape(book['coverImage'])}</image:loc>",
                  f"      <image:title>{html.escape(book['title'])}</image:title>",
                  f"      <image:caption>{html.escape(cover_alt(book))}</image:caption>", "    </image:image>", "  </url>"]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def homepage_itemlist(books):
    node = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Books by Parvind Kumar",
        "numberOfItems": len(books),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": book_url(b["slug"]), "name": b["title"]}
            for i, b in enumerate(books)
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(node, ensure_ascii=False, indent=2).replace("</", "<\\/") + "\n  </script>"


def inject_between(text, start, end, content):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise SystemExit(f"Marker {start} not found in index.html")
    return pattern.sub(lambda _: f"{start}\n{content}\n        {end}", text)


def update_homepage(base_dir, books):
    path = os.path.join(base_dir, "index.html")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    cards = "".join(card_html(b, "books/", lazy=True) for b in books)
    text = inject_between(text, "<!-- BOOKS:START -->", "<!-- BOOKS:END -->", cards)
    text = inject_between(text, "<!-- BOOKLIST-LD:START -->", "<!-- BOOKLIST-LD:END -->", "  " + homepage_itemlist(books))
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
