import os
import json

# Define the books database
BOOKS = [
    {
        "slug": "six-lanes-of-kamathipura",
        "title": "Six Lanes of Kamathipura",
        "subtitle": "A Novel of Resilience and Survival in Mumbai's Red-Light District",
        "kicker": "A Novel",
        "category": ["fiction"],
        "coverClass": "cover-one",
        "coverBg": "#2e2a27",
        "coverFg": "#d0a57b",
        "coverImage": "https://m.media-amazon.com/images/I/51Z5ASHf3nL._SY445_SX342_FMwebp_.jpg",
        "language": "English",
        "pages": 240,
        "publication_date": "2023-04-15",
        "isbn": "978-81-965412-0-1",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Six-Lanes-Kamathipura-Parvind-Kumar/dp/9376504801",
        "google_play": "https://play.google.com/store/search?q=Six+Lanes+of+Kamathipura+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=Six+Lanes+of+Kamathipura+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "A story of lives, choices and the city behind the headlines.",
        "long_description": (
            "Six Lanes of Kamathipura is a contemporary fiction novel by Indian author Parvind Kumar. "
            "Set in the heart of Mumbai's most infamous red-light district, the book tells a raw and "
            "deeply human story of resilience, hope, and the search for identity. "
            "Through a cast of rich, complex characters, the novel explores the invisible threads that "
            "connect people living on the margins of society and the difficult choices they must make "
            "to survive. It is an honest portrayal of a world that is often reduced to sensational headlines, "
            "focusing instead on the quiet dignity, dreams, and relationships that thrive in the shadows."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Lane of Whispers", "summary": "An introduction to the bustling, sensory world of Kamathipura and the main characters who call it home."},
            {"chapter": "Chapter 2: Dust and Dreams", "summary": "Exploring the childhood memories and quiet aspirations of the protagonists as they navigate their surroundings."},
            {"chapter": "Chapter 3: Shadows of the Past", "summary": "Secrets from the past begin to emerge, threatening the fragile peace they have built."},
            {"chapter": "Chapter 4: A Quiet Resolve", "summary": "Faced with an unexpected crisis, the community must come together and make a difficult stand."},
            {"chapter": "Chapter 5: Crossing the Red Line", "summary": "High-stakes choices test the limits of loyalty, friendship, and survival."},
            {"chapter": "Chapter 6: The Unspoken Bond", "summary": "A moving conclusion highlighting the endurance of the human spirit amidst hardship."}
        ],
        "reviews": [
            {"quote": "A raw and deeply moving portrayal of resilience. Kumar's characters stay with you long after you turn the final page.", "source": "Reader Review"},
            {"quote": "An honest look into a world often ignored. Beautifully written and structurally brilliant.", "source": "Literary Corner Review"}
        ]
    },
    {
        "slug": "when-hope-came-home",
        "title": "When Hope Came Home",
        "subtitle": "A Heartwarming Story of Family, Forgiveness, and Reconciliation",
        "kicker": "Fiction",
        "category": ["fiction"],
        "coverClass": "cover-two",
        "coverBg": "#d6c5ab",
        "coverFg": "#4b352b",
        "coverImage": "https://m.media-amazon.com/images/I/717J3Te5ReL._SL1500_.jpg",
        "language": "English",
        "pages": 242,
        "publication_date": "2023-09-10",
        "isbn": "978-81-965412-1-8",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/When-Hope-Came-Parvind-Kumar/dp/9376504275/",
        "google_play": "https://play.google.com/store/search?q=When+Hope+Came+Home+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=When+Hope+Came+Home+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "A story about hope, home and the courage to begin again.",
        "long_description": (
            "When Hope Came Home is an emotionally resonant drama novel by Indian author Parvind Kumar. "
            "It follows the journey of a young protagonist who returns to their ancestral village after "
            "confronting devastating failure in the city. The story explores the complexities of returning "
            "home, reconciling with estranged family members, and healing from psychological trauma. "
            "It is a story about the warmth of small-town communities, the quiet strength of relationships, "
            "and the realization that sometimes, starting over is the bravest thing one can do."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Return", "summary": "Leaving behind the echoes of the city, the protagonist journeys back to the old house."},
            {"chapter": "Chapter 2: Whispers in the Wind", "summary": "Unfamiliar yet familiar faces and the quiet awkwardness of reconnection."},
            {"chapter": "Chapter 3: Rebuilding the Hearth", "summary": "Focuses on physical and emotional labor as the old ancestral home is slowly restored."},
            {"chapter": "Chapter 4: Unfinished Conversations", "summary": "Confronting past arguments and seeking forgiveness from loved ones."},
            {"chapter": "Chapter 5: The Dawn of Healing", "summary": "A peaceful dawn breaks as the protagonist discovers a new purpose and accepts the past."}
        ],
        "reviews": [
            {"quote": "Deeply emotional and uplifting. It reminds us that no matter how far we wander, home is where we find ourselves.", "source": "Books & Beyond"},
            {"quote": "A beautiful exploration of forgiveness and new beginnings. Highly recommended.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "live-in-relationships",
        "title": "Live-In Relationships: The Untold Truth",
        "subtitle": "Understanding Legal Rights, Emotional Boundaries, and Societal Realities in Modern India",
        "kicker": "Relationships",
        "category": ["relationships", "nonfiction"],
        "coverClass": "cover-three",
        "coverBg": "#213c37",
        "coverFg": "#d6b58d",
        "coverImage": "https://m.media-amazon.com/images/I/71PEl-ynwaL._SL1500_.jpg",
        "language": "English",
        "pages": 210,
        "publication_date": "2024-06-20",
        "isbn": "978-81-965412-2-5",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Live-Relationships-Untold-Parvind-Kumar/dp/9376504062",
        "google_play": "https://play.google.com/store/search?q=Live-In+Relationships+The+Untold+Truth+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=Live-In+Relationships+The+Untold+Truth+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Love, independence, commitment and the realities behind modern live-in relationships.",
        "long_description": (
            "Live-In Relationships: The Untold Truth is a non-fiction relationships and legal guide by Indian author Parvind Kumar. "
            "The book takes an objective, comprehensive look at the growing phenomenon of live-in relationships in modern India. "
            "It navigates the complex landscape of legal rights, financial agreements, emotional boundaries, and social perceptions. "
            "Offering practical checklists, case studies, and legal advice, this book serves as a vital guide for young couples "
            "contemplating this path, helping them understand both their rights and responsibilities."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Modern Shift", "summary": "How changing values, careers, and urban lifestyles are redefining commitment and partnership in India."},
            {"chapter": "Chapter 2: Legal Rights and Protections", "summary": "A deep dive into judicial rulings, domestic violence protections, and children's inheritance rights in live-in setups."},
            {"chapter": "Chapter 3: Managing Family Expectations", "summary": "Conversations, boundaries, and strategies for handling parents, relatives, and societal pressure."},
            {"chapter": "Chapter 4: The Emotional Dynamics", "summary": "Navigating division of chores, finances, privacy, and maintaining long-term emotional intimacy without a marriage contract."},
            {"chapter": "Chapter 5: Moving In: A Checklist", "summary": "Practical steps, legal agreements (cohabitation contracts), and advice to align expectations before sharing a key."}
        ],
        "reviews": [
            {"quote": "An essential read for every modern couple. Clear, balanced, and highly informative.", "source": "Legal & Social Journal"},
            {"quote": "Brilliant analysis of the legal aspects of cohabitation in India. Extremely practical.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "11-shades-of-love",
        "title": "11 Shades of Love: Modern Indian Stories",
        "subtitle": "Stories of Passion, Conflict, Heartbreak, and New Beginnings",
        "kicker": "11 Stories",
        "category": ["fiction", "relationships"],
        "coverClass": "cover-four",
        "coverBg": "#6e3029",
        "coverFg": "#f0d7bb",
        "coverImage": "https://m.media-amazon.com/images/I/71+156bp10L._SL1500_.jpg",
        "language": "English",
        "pages": 75,
        "publication_date": "2026-07-12",
        "isbn": "978-9376503285",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/11-Shades-Love-Modern-Stories/dp/9376503287",
        "google_play": "https://play.google.com/store/books/details/Parvind_Kumar_11_Shades_of_Love_Modern_Indian_Stor?id=zHL_EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/book/show/256574851-11-shades-of-love",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Modern Indian love stories of passion, conflict, heartbreak and new beginnings.",
        "long_description": (
            "11 Shades of Love: Modern Indian Stories is a fiction anthology by Indian author Parvind Kumar. "
            "This book gathers eleven moving short stories that capture the sheer diversity of love in contemporary India. "
            "From high-tech romance in Bangalore to quiet, shared moments in old Delhi, the stories deal with "
            "long-distance struggles, inter-caste marriages, dating apps, and the bittersweet task of moving on. "
            "Each story offers a unique window into the human heart, depicting love not as a single fairy tale, but "
            "as a rich, complicated spectrum of human emotion."
        ),
        "table_of_contents": [
            {"chapter": "Story 1: Swipe Right, Fall Wrong", "summary": "A dating app's algorithm keeps matching two exes — is it fate, or just good retention design?"},
            {"chapter": "Story 2: The Reservation", "summary": "A caste divide tests a young doctor's engagement to the man who's loved her since college."},
            {"chapter": "Story 3: Trending in 24 Hours", "summary": "A private proposal goes viral — and a couple must fight to keep their own story their own."},
            {"chapter": "Story 4: Ten Years, One Delivery", "summary": "A delivery rider and a doctor, reunited ten years after poverty pulled them apart."},
            {"chapter": "Story 5: Metro Line 3", "summary": "Two strangers, stranded together by a city-wide protest, meet on the same metro line — again and again."},
            {"chapter": "Story 6: Ganga Ki Godh Mein", "summary": "On the ghats of Varanasi, a priest's daughter falls for the boy whose family keeps the sacred fire."},
            {"chapter": "Story 7: Twenty Goats and a Good Name", "summary": "Ten goats, a half-acre plot, and a poor farmer's quiet plan to earn a landlord's respect."},
            {"chapter": "Story 8: Mileage", "summary": "A fuel protest, a mechanic, and the woman from the transport department who starts listening."},
            {"chapter": "Story 9: Election Se Pehle", "summary": "Two rival campaign managers, one election, and an attraction neither of them can afford."},
            {"chapter": "Story 10: What the Water Left Behind", "summary": "A flood, a rescue, and a week that neither of them can stop looking for again."},
            {"chapter": "Story 11: The Chatbot Confession", "summary": "A four-month romance built on messages — until one confession changes what 'real' even means."}
        ],
        "reviews": [
            {"quote": "Every story is distinct and leaves you thinking about it for days.", "source": "Aditi Rao"},
            {"quote": "Short, sweet, and emotionally resonant. Kumar's writing style is effortlessly engaging.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "crime-suspense-stories",
        "title": "Crime Suspense Stories",
        "subtitle": "Anthology of Mystery, Secrets, and Dark Human Choices",
        "kicker": "Suspense",
        "category": ["fiction"],
        "coverClass": "cover-five",
        "coverBg": "#24282c",
        "coverFg": "#c9a76c",
        "coverImage": "https://m.media-amazon.com/images/I/71PYcSfIf3L._SL1500_.jpg",
        "language": "English",
        "pages": 220,
        "publication_date": "2023-08-18",
        "isbn": "978-81-965412-4-9",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Crime-suspense-stories-Parvind-Kumar/dp/9376502892/",
        "google_play": "https://play.google.com/store/books/details?id=WpH8EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Parvind+Kumar+Crime+Suspense+Stories",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Stories built around mystery, crime, secrets and the consequences of hidden choices.",
        "long_description": (
            "Crime Suspense Stories is a gripping fiction collection by Indian author Parvind Kumar. "
            "Perfect for fans of mysteries and psychological dramas, the book compiles several thrilling stories "
            "where ordinary people find themselves in extraordinary, dangerous situations. "
            "The narratives explore themes of betrayal, greed, the flawless alibi, and the ultimate psychological toll of crime. "
            "With sharp pacing, sharp dialogues, and unexpected plot twists, this anthology keeps readers "
            "on the edge of their seats until the final revelation."
        ),
        "table_of_contents": [
            {"chapter": "Story 1: The Locked Study", "summary": "A late-night mystery in a locked study room leads to a shocking family discovery."},
            {"chapter": "Story 2: Footprints in the Dust", "summary": "Unusual tracks at a crime scene become the key clue for a determined investigator."},
            {"chapter": "Story 3: A False Alibi", "summary": "A suspect creates an elaborate alibi, only to be betrayed by a small digital footprint."},
            {"chapter": "Story 4: The Witness's Silence", "summary": "A witness refuses to speak out, hiding a dark secret that could alter the entire case."},
            {"chapter": "Story 5: Red Herring", "summary": "A series of misleading clues leads the police away from the real mastermind."},
            {"chapter": "Story 6: Final Judgment", "summary": "A high-stakes resolution where justice is served in the most unexpected way."}
        ],
        "reviews": [
            {"quote": "Quick, snappy, and very suspenseful stories.", "source": "Vikram Seth"},
            {"quote": "Well-crafted mysteries with psychological depth and relatable characters.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "lo-shu-grid-numerology",
        "title": "The Complete Guide to Lo Shu Grid Numerology",
        "subtitle": "Discover the Ancient Chinese Magic Square and Remedies for Balance and Prosperity",
        "kicker": "Numerology",
        "category": ["nonfiction"],
        "coverClass": "cover-six",
        "coverBg": "#3d3a5d",
        "coverFg": "#d9c58c",
        "coverImage": "https://m.media-amazon.com/images/I/81V5OZmGHoL._SL1500_.jpg",
        "language": "English",
        "pages": 180,
        "publication_date": "2024-02-01",
        "isbn": "978-81-965412-5-6",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Complete-Guide-Shu-Grid-Numerology/dp/9376502825",
        "google_play": "https://play.google.com/store/books/details?id=SR_3EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+Complete+Guide+to+Lo+Shu+Grid+Numerology",
        "formats": "Paperback, eBook (Kindle)",
        "description": "An accessible guide to understanding the Lo Shu Grid and its traditional numerological framework.",
        "long_description": (
            "The Complete Guide to Lo Shu Grid Numerology is a practical non-fiction book by Indian author Parvind Kumar. "
            "It introduces readers to the ancient Chinese system of numerology based on the Lo Shu Grid—a magic square of order 3. "
            "The book provides clear, step-by-step instructions on how to construct a grid using birth dates, "
            "analyze the strength of different numbers, understand the impact of missing numbers, and determine "
            "auspicious directions. Written in an accessible and easy-to-understand format, it offers practical remedies "
            "such as colors, elements, and gemstones to bring balance, health, and prosperity into your life."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Origin of Lo Shu Grid", "summary": "The history and mythology behind the ancient magic square discovered on a tortoise shell."},
            {"chapter": "Chapter 2: The Nine Numbers and Meanings", "summary": "Detailed characteristics, elemental associations, and significance of numbers 1 through 9."},
            {"chapter": "Chapter 3: Constructing Your Grid", "summary": "A practical guide to placing birth dates into the grid and calculating basic driving numbers."},
            {"chapter": "Chapter 4: Analyzing Strengths and Weaknesses", "summary": "Understanding vertical, horizontal, and diagonal planes (willpower, action, intellect, etc.)."},
            {"chapter": "Chapter 5: Missing Numbers and Remedies", "summary": "How to balance the energy of missing grid coordinates using elements, crystals, and simple home remedies."}
        ],
        "reviews": [
            {"quote": "An excellent book for beginners. The explanations are clear and the remedies are practical and easy to apply.", "source": "Astrology Today"},
            {"quote": "A systematic, logical approach to numerology that avoids superstitious fear-mongering.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "before-we-said-goodbye",
        "title": "Before we said goodbye.",
        "subtitle": "Moving Stories of Love, Closure, and the Courage to Let Go",
        "kicker": "Love Stories",
        "category": ["fiction", "relationships"],
        "coverClass": "cover-seven",
        "coverBg": "#c9b5a1",
        "coverFg": "#573f39",
        "coverImage": "https://m.media-amazon.com/images/I/71Uo5ZlPL6L._SL1500_.jpg",
        "language": "English",
        "pages": 204,
        "publication_date": "2024-05-20",
        "isbn": "978-81-965412-6-3",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Before-said-goodbye-Parvind-Kumar/dp/937650321X",
        "google_play": "https://play.google.com/store/books/details?id=6_f-EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Before+we+said+goodbye+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Stories about love, loss, memories and the words left unsaid.",
        "long_description": (
            "Before we said goodbye. is a fiction collection of emotionally charged stories by Indian author Parvind Kumar. "
            "This book explores the sensitive threshold that couples cross right before deciding to walk separate paths. "
            "Rather than focusing on the bitter end, it highlights the quiet moments—the final cups of coffee, "
            "the unsent drafts in email folders, the shared laughter over old jokes, and the unspoken realization that "
            "their paths have diverged. It is a thoughtful exploration of closure, mutual respect, and the quiet dignity "
            "of letting go of someone you once loved."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Final Cafe", "summary": "Two former partners meet at their favorite college spot to return belongings and say their last words."},
            {"chapter": "Chapter 2: Photographs of Yesterday", "summary": "Sorting through old digital albums brings back forgotten memories, highlighting why things changed."},
            {"chapter": "Chapter 3: A Train Ticket to Elsewhere", "summary": "A couple spends a long, introspective train ride before moving to separate cities for their careers."},
            {"chapter": "Chapter 4: Unsent Emails", "summary": "A story written through draft folders containing thoughts that were too honest to ever be sent."},
            {"chapter": "Chapter 5: The Quiet Departure", "summary": "A peaceful and understanding goodbye that values the love that was, without clinging to a broken future."}
        ],
        "reviews": [
            {"quote": "Poignant and beautifully written. It perfectly captures the quiet ache of letting go of what you love.", "source": "Literary Review Weekly"},
            {"quote": "Every story in this book hits close to the heart. A masterpiece of relational storytelling.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "vintage-between-us",
        "title": "The Vintage Between Us: A Tuscan Vineyard Romance",
        "subtitle": "A Slow-Burn Romance Caught Between Family Heritage and the Desires of the Heart",
        "kicker": "Romance",
        "category": ["fiction", "relationships"],
        "coverClass": "cover-eight",
        "coverBg": "#31554b",
        "coverFg": "#dfc99e",
        "coverImage": "https://m.media-amazon.com/images/I/61eVBttz0DL._SY522_.jpg",
        "language": "English",
        "pages": 290,
        "publication_date": "2024-04-05",
        "isbn": "978-81-965412-7-0",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Vintage-Between-Us-Vineyard-Romance/dp/B0H95CSR8H/",
        "google_play": "https://play.google.com/store/books/details?id=hNn2EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+Vintage+Between+Us+A+Tuscan+Vineyard+Romance",
        "formats": "Paperback, eBook (Kindle)",
        "description": "A Tuscan vineyard, two people and a romance caught between past and present.",
        "long_description": (
            "The Vintage Between Us: A Tuscan Vineyard Romance is a romantic drama by Indian author Parvind Kumar. "
            "Set in the rolling hills and sun-drenched vineyards of Tuscany, the novel tells the story of an "
            "Indian architect, Kabir, who travels to Italy to restore an old family estate, and Alessia, "
            "a local winemaker determined to save her family's heritage. As they collaborate to rebuild the ancient property, "
            "they uncover a decades-old secret connecting their families, forcing them to choose between "
            "honoring their family duties and following their hearts. It is a slow-burn romance rich in atmosphere, wine culture, "
            "and emotional depth."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Autumn in Tuscany", "summary": "Kabir arrives in Italy, met with the breathtaking beauty of the vineyard and the cold skepticism of Alessia."},
            {"chapter": "Chapter 2: The Legacy of the Vine", "summary": "Learning the art of winemaking and uncovering the historical significance of the estate."},
            {"chapter": "Chapter 3: Shared Sunsets", "summary": "Conversations over local dinners build a bridge of understanding between Kabir and Alessia."},
            {"chapter": "Chapter 4: Fermenting Secrets", "summary": "Letters found in an old cellar chest reveal a forbidden romance from the 1960s."},
            {"chapter": "Chapter 5: Harvest and Heartbreak", "summary": "The peak of the harvest season brings emotional conflicts and family ultimatums to a boil."},
            {"chapter": "Chapter 6: The Vintage Uncorked", "summary": "Resolving past family guilt and building a shared future among the vines."}
        ],
        "reviews": [
            {"quote": "An atmospheric and beautifully paced romance. I could almost smell the grapes and feel the Tuscan sun.", "source": "Romance Readers Digest"},
            {"quote": "A lovely escape. A perfect blend of romance, history, and family secrets.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "after-the-promise-broke",
        "title": "After the Promise Broke",
        "subtitle": "A Romantic Thriller of Betrayal, Passion, and the Search for Redemption",
        "kicker": "Romance · Thriller",
        "category": ["fiction", "relationships"],
        "coverClass": "cover-nine",
        "coverBg": "#4a2730",
        "coverFg": "#d6a28e",
        "coverImage": "https://m.media-amazon.com/images/I/71rSw1nyW7L._SL1500_.jpg",
        "language": "English",
        "pages": 258,
        "publication_date": "2024-03-22",
        "isbn": "978-81-965412-8-7",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/After-Promise-Broke-Parvind-Kumar/dp/9376503481/",
        "google_play": "https://play.google.com/store/search?q=After+the+Promise+Broke+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=After+the+Promise+Broke+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Stories of betrayal, romance, psychological tension and the search for redemption.",
        "long_description": (
            "After the Promise Broke is a romantic thriller novel by Indian author Parvind Kumar. "
            "This book examines the dark, intense side of love and relationships. When trust is shattered "
            "by betrayal or secrets, the human mind enters a complex zone of grief, denial, and sometimes, "
            "the urge for retribution. Combining elements of psychological suspense with deep emotional drama, "
            "these stories follow individuals navigating the wreckage of broken marriages, corporate conspiracies, "
            "and long-held family secrets, exploring their path towards either destruction or healing."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Broken Vow", "summary": "A wedding anniversary reveals a dark secret that turns a happy marriage into a psychological chess game."},
            {"chapter": "Chapter 2: Shadows in the Hallway", "summary": "A woman discovers her husband's business partner has been hiding key evidence about a fatal accident."},
            {"chapter": "Chapter 3: The Price of Silence", "summary": "Faced with blackmails, a young politician must decide between saving his career or his family's trust."},
            {"chapter": "Chapter 4: Unravelling the Lie", "summary": "A therapist realizes one of her patients is connected to her husband's mysterious past."},
            {"chapter": "Chapter 5: The Final Confrontation", "summary": "A high-stakes resolution where truth is finally brought to light and consequences must be paid."}
        ],
        "reviews": [
            {"quote": "A thrilling read that balances relationship drama with genuine, spine-chilling suspense.", "source": "Thriller Hub Reviews"},
            {"quote": "Gripping, dark, and fast-paced, with a surprising emotional depth.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "building-happy-marriage",
        "title": "The Complete Guide to Building a Happy Marriage & Lasting Love",
        "subtitle": "Practical Ideas for Communication, Trust, Intimacy, and Building a Lasting Partnership",
        "kicker": "Marriage",
        "category": ["relationships", "nonfiction"],
        "coverClass": "cover-ten",
        "coverBg": "#8b5d39",
        "coverFg": "#f1dec4",
        "coverImage": "https://m.media-amazon.com/images/I/71evLi+WBrL._SL1500_.jpg",
        "language": "English",
        "pages": 310,
        "publication_date": "2023-10-14",
        "isbn": "978-81-965412-9-4",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Complete-Guide-Building-Marriage-Lasting/dp/9376502906/",
        "google_play": "https://play.google.com/store/books/details?id=Ps74EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Complete+Guide+Building+Happy+Marriage+Lasting+Love",
        "formats": "Paperback, eBook (Kindle)",
        "description": "Practical ideas for communication, trust, intimacy and building a lasting partnership.",
        "long_description": (
            "The Complete Guide to Building a Happy Marriage & Lasting Love is a relationships handbook by Indian author Parvind Kumar. "
            "Drawing on marriage counseling insights, psychological research, and real-life case studies, the book provides "
            "practical, actionable advice for couples at any stage of their relationship. From building a foundation of deep trust "
            "and learning active listening, to navigating differences in finances, in-laws, and values, this guide offers "
            "a roadmap to handle inevitable conflicts constructively and keep emotional and physical intimacy alive."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Foundation of Trust", "summary": "Why trust is a daily habit and how consistency builds safety in a marriage."},
            {"chapter": "Chapter 2: The Art of Active Listening", "summary": "Moving beyond hearing to understanding: validation techniques that prevent miscommunication."},
            {"chapter": "Chapter 3: Navigating Conflict", "summary": "Rules for fighting fair, managing disagreements, and learning to compromise without losing yourself."},
            {"chapter": "Chapter 4: Keeping the Spark Alive", "summary": "Practical methods for maintaining physical affection, emotional connection, and intimacy over the years."},
            {"chapter": "Chapter 5: Shared Goals and Individual Growth", "summary": "How to grow together as a couple while supporting each other's individual dreams and space."}
        ],
        "reviews": [
            {"quote": "A sensible, grounded, and modern guide to marriage. Free of cliches, full of real wisdom.", "source": "Family Well-being Journal"},
            {"quote": "Helped us communicate better from the very first week. A must-read for engaged couples.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "mindfulness-meditation",
        "title": "The Complete Guide to Mindfulness & Meditation",
        "subtitle": "A Practical Companion for Daily Presence, Focus, and Everyday Calm",
        "kicker": "Mindfulness",
        "category": ["mind", "nonfiction"],
        "coverClass": "cover-eleven",
        "coverBg": "#31445a",
        "coverFg": "#c7d6d8",
        "coverImage": "https://m.media-amazon.com/images/I/71KHnfkhauL._SL1500_.jpg",
        "language": "English",
        "pages": 200,
        "publication_date": "2024-01-05",
        "isbn": "978-81-965413-0-0",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Complete-Guide-Mindfulness-Meditation/dp/9360381705/",
        "google_play": "https://play.google.com/store/books/details?id=_Nz2EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Complete+Guide+to+Mindfulness+Meditation+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "A practical journey into mindfulness, meditation, attention and everyday calm.",
        "long_description": (
            "The Complete Guide to Mindfulness & Meditation is a self-help and wellness book by Indian author Parvind Kumar. "
            "In our fast-paced, screen-dominated world, finding quiet is harder than ever. This book demystifies meditation, "
            "making it accessible to beginners and regular practitioners alike. It outlines simple breathing exercises, "
            "body scans, and mental models to manage stress, reduce anxiety, and reclaim your focus. Beyond formal meditation, "
            "the book teaches how to bring mindfulness into everyday actions, from eating and walking to working and communicating."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Understanding Mindfulness", "summary": "Demystifying what mindfulness is and isn't. Exploring the scientific benefits on brain structure and stress response."},
            {"chapter": "Chapter 2: The Breath as an Anchor", "summary": "Basic breathing techniques (box breathing, diaphragmatic breathing) to calm the nervous system instantly."},
            {"chapter": "Chapter 3: Silent Sitting: Steps to Meditate", "summary": "A step-by-step physical and mental layout for setting up a daily 10-minute meditation habit."},
            {"chapter": "Chapter 4: Overcoming the Restless Mind", "summary": "How to handle thoughts, distractions, and physical discomfort during meditation without judgment."},
            {"chapter": "Chapter 5: Mindfulness in Daily Actions", "summary": "Methods to cultivate awareness during routine chores, eating, walking, and digital interactions."}
        ],
        "reviews": [
            {"quote": "A wonderful, jargon-free introduction to meditation. Highly recommended for modern, stressful lives.", "source": "Mindful Living Magazine"},
            {"quote": "Practical, grounding, and scientifically backed. A great companion for daily mindfulness practice.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "escape-endless-scroll",
        "title": "Escape the Endless Scroll",
        "subtitle": "Reclaim Your Time, Attention, and Mental Peace in the Digital Age",
        "kicker": "Digital Wellbeing",
        "category": ["mind", "nonfiction"],
        "coverClass": "cover-twelve",
        "coverBg": "#282b2f",
        "coverFg": "#91b1a5",
        "coverImage": "https://m.media-amazon.com/images/I/71znBiXKnVL._SL1500_.jpg",
        "language": "English",
        "pages": 215,
        "publication_date": "2024-07-01",
        "isbn": "978-81-965413-1-7",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Escape-Endless-Scroll-Parvind-Kumar/dp/9376503260/",
        "google_play": "https://play.google.com/store/search?q=Escape+the+Endless+Scroll+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=Escape+the+Endless+Scroll+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "How to reduce screen time, break the scrolling cycle and reclaim real life.",
        "long_description": (
            "Escape the Endless Scroll is a digital health and self-improvement guide by Indian author Parvind Kumar. "
            "Technology companies design social feeds to trap our attention, leading to constant scrolling, anxiety, "
            "and a loss of real-world connection. This book details the psychology of screen addiction and provides "
            "an actionable blueprint to take back control. With practical advice on digital detoxes, notifications audits, "
            "and reshaping your relationship with smartphones, Kumar helps you build sustainable habits to prioritize "
            "your mental peace, relationships, and deep focus."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Attention Economy", "summary": "How social platforms use dopamine loops, variable rewards, and infinite scroll to monetize our attention."},
            {"chapter": "Chapter 2: Why We Can't Stop Scrolling", "summary": "The psychological traps of FOMO (Fear Of Missing Out), social comparisons, and mindless habit loops."},
            {"chapter": "Chapter 3: The Screen Time Audit", "summary": "A practical method to track and analyze where your digital hours are going, uncovering hidden habits."},
            {"chapter": "Chapter 4: Designing a Distraction-Free Phone", "summary": "Step-by-step optimization of phone settings, greyscale modes, notification limits, and app layouts."},
            {"chapter": "Chapter 5: Reclaiming Boredom and Focus", "summary": "How to fill screen-free blocks with meaningful real-world habits, hobbies, and deep, quiet thinking."}
        ],
        "reviews": [
            {"quote": "Crucial reading for the smartphone age. Kumar offers practical, realistic strategies that actually work.", "source": "Tech & Wellness Magazine"},
            {"quote": "A highly actionable guide that helped me cut my phone usage by half and sleep much better.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "what-happens-after-death",
        "title": "What Happens After Death?",
        "subtitle": "The Soul, Near-Death Experiences, Reincarnation, and the Scientific Search for Life After Death",
        "kicker": "Personal Development",
        "category": ["nonfiction", "Personal Development"],
        "coverClass": "cover-twelve",
        "coverBg": "#282b2f",
        "coverFg": "#91b1a5",
        "coverImage": "https://m.media-amazon.com/images/I/819+67sYZhL._SL1500_.jpg",
        "language": "English",
        "pages": 230,
        "publication_date": "2026-08-25",
        "isbn": "978-937650546-8",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/dp/9376505468",
        "google_play": "https://play.google.com/store/books/details?id=EtEDEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/book/show/213600647-what-happens-after-death",
        "formats": "Paperback, eBook (Kindle)",
        "description": "The Soul, Near-Death Experiences, Reincarnation, and the Scientific Search for Life After Death.",
        "long_description": (
            "What Happens After Death? is a philosophical and scientific exploration by Indian author Parvind Kumar. "
            "The book delves into the oldest mystery of humanity: the ultimate fate of consciousness. "
            "Integrating case studies of near-death experiences (NDEs), clinical research on cardiac arrest patients, "
            "hypnotherapy records, and documentation of past-life memories with ancient Eastern and Western philosophical "
            "traditions, this book investigates if consciousness survives the body's biological death. "
            "It is a comforting, fascinating, and thoroughly researched look at the soul's potential journey."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Enigma of Death", "summary": "Historical attitudes toward death and how different cultures have conceptualized the afterlife."},
            {"chapter": "Chapter 2: Science and Near-Death Experiences", "summary": "Analyzing reports of out-of-body experiences, tunnel visions, and medical explanations of NDEs."},
            {"chapter": "Chapter 3: Reincarnation: Myth or Reality?", "summary": "Looking at Ian Stevenson's scientific research and documented case studies of children who recall past lives."},
            {"chapter": "Chapter 4: The Journey of the Soul in Ancient Traditions", "summary": "Eastern philosophies (Karma and Samsara) and Western spiritualism regarding the soul's progression."},
            {"chapter": "Chapter 5: Consciousness Beyond the Brain", "summary": "Quantum theories of consciousness and the possibility of non-local awareness after brain death."}
        ],
        "reviews": [
            {"quote": "A fascinating, well-researched book that bridges science and spirituality on the ultimate question.", "source": "Consciousness Review"},
            {"quote": "Thought-provoking, balanced, and deeply comforting. Recommended for anyone seeking answers.", "source": "Reader Review"}
        ]
    },
    {
        "slug": "ganga-expressway",
        "title": "The Ganga Expressway",
        "subtitle": "Colossal Infrastructure, Socio-Economic Change, and the Future of Uttar Pradesh",
        "kicker": "Business",
        "category": ["business", "nonfiction"],
        "coverClass": "cover-thirteen",
        "coverBg": "#3b4c5b",
        "coverFg": "#c8a46b",
        "coverImage": "https://m.media-amazon.com/images/I/81hqsU3lBkL._SL1500_.jpg",
        "language": "English",
        "pages": 275,
        "publication_date": "2024-06-10",
        "isbn": "978-81-965413-2-4",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/Ganga-Expressway-Parvind-Kumar/dp/9376503511/",
        "google_play": "https://play.google.com/store/search?q=The+Ganga+Expressway+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=The+Ganga+Expressway+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "India's longest expressway just opened — and it's changing Uttar Pradesh forever.",
        "long_description": (
            "The Ganga Expressway is a comprehensive business and infrastructure analysis by Indian author Parvind Kumar. "
            "Focusing on the 594-kilometer, six-lane greenfield expressway connecting Meerut with Prayagraj, the book explores "
            "the colossal engineering, planning, acquisition, and financial models behind one of India's biggest highway projects. "
            "It looks at the socio-economic transformations, regional connectivity, industrial corridors, and the overall "
            "impact on real estate, local agriculture, and business logistics in Uttar Pradesh. This book is a detailed study "
            "for policy makers, infrastructure enthusiasts, and business analysts."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Vision and Greenfield Planning", "summary": "The origin of the project, route alignment, and the strategy for fast land acquisition."},
            {"chapter": "Chapter 2: Engineering a 594-Kilometer Corridor", "summary": "Bridges, interchanges, runways, and the technical specifications of the six-lane layout."},
            {"chapter": "Chapter 3: Financial Structure and PPP Model", "summary": "A deep dive into the public-private partnership structure, concessions, and funding allocation."},
            {"chapter": "Chapter 4: Economic Corridors and Industrial Impact", "summary": "How the expressway connects agricultural hubs with manufacturing centers to boost industrialization."},
            {"chapter": "Chapter 5: Re-shaping Uttar Pradesh", "summary": "The long-term socio-economic growth, job creation, and logistical changes for northern India."}
        ],
        "reviews": [
            {"quote": "An exhaustive, detail-oriented study of one of India's largest infrastructure achievements. Highly useful.", "source": "Economic Digest"},
            {"quote": "A detailed and fascinating look at the engineering and financial scale of modern Indian highways.", "source": "Infra Review"}
        ]
    },
    {
        "slug": "talaq-se-pehle",
        "title": "Talaq Se Pehle",
        "subtitle": "वैवाहिक जीवन को बचाने और आपसी समझ बढ़ाने की एक व्यावहारिक निर्देशिका",
        "kicker": "Marriage & Divorce Guide",
        "category": ["relationships", "nonfiction"],
        "coverClass": "cover-fourteen",
        "coverBg": "#743326",
        "coverFg": "#fbe8e4",
        "coverImage": "https://m.media-amazon.com/images/I/71evLi+WBrL._SL1500_.jpg",
        "language": "Hindi",
        "pages": 230,
        "publication_date": "2024-11-12",
        "isbn": "978-81-965413-3-1",
        "publisher": "Independent",
        "amazon": "https://www.amazon.in/s?k=Talaq+Se+Pehle+Parvind+Kumar",
        "google_play": "https://play.google.com/store/books/details?id=EPf2EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Talaq+Se+Pehle+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "तलाक से पहले (Talaq Se Pehle) लेखक परविन्द कुमार द्वारा वैवाहिक और सामाजिक विषयों पर लिखी गई एक महत्वपूर्ण रचना है।",
        "long_description": (
            "Talaq Se Pehle (तलाक से पहले) is a Hindi relationship and marriage guide book by Indian author Parvind Kumar. "
            "It is a compassionate, practical, and legal guide designed for couples going through marital discord. "
            "Written in accessible Hindi, the book addresses the common causes of cracks in relationships, "
            "practical communication exercises to rebuild trust, and guidelines on when to seek professional counseling. "
            "Importantly, it also provides legal awareness regarding divorce, maintenance, and child custody laws in India, "
            "allowing couples to make informed, mature, and thoughtful choices rather than impulsive actions."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: विवाह की नीव (Foundations of Marriage)", "summary": "Understanding modern relational stress, ego clashes, and breakdown of everyday communication."},
            {"chapter": "Chapter 2: आपसी मतभेद और संचार (Conflicts & Communication)", "summary": "Active steps couples can take to re-establish dialogue, forgive past wounds, and work on intimacy."},
            {"chapter": "Chapter 3: रिश्ते में कड़वाहट के मुख्य कारण (Root Causes of Discord)", "summary": "A self-reflection guide on emotional readiness, child impact, and evaluating if the marriage is truly unsalvageable."},
            {"chapter": "Chapter 4: तलाक का निर्णय: एक पुनर्विचार (The Decision of Divorce: A Rethink)", "summary": "An easy-to-understand breakdown of Hindu and Muslim personal laws, mutual consent divorce, alimony, and custody."},
            {"chapter": "Chapter 5: बच्चों पर प्रभाव (Impact on Children)", "summary": "Analyzing how separation affects children's mental wellbeing and how to mitigate negative impacts."},
            {"chapter": "Chapter 6: एक नई शुरुआत (A New Beginning)", "summary": "Moving forward with peace and clarity, whether that means rebuilding the marriage or parting ways with dignity."}
        ],
        "reviews": [
            {"quote": "विवाह और संबंधों को समझने की एक बहुत ही व्यावहारिक मार्गदर्शिका। लेखक ने बहुत ही संवेदनशीलता से इस विषय को छुआ है।", "source": "Dr. Alok Verma"},
            {"quote": "A must-read book before taking any extreme step. The advice is highly practical and compassionate.", "source": "Priyanka Singh"}
        ]
    },
    {
        "slug": "why-india-cancer-capital",
        "title": "Why Is India Becoming the Cancer Capital?",
        "subtitle": "The Hidden Causes, Lifestyle Changes, Pollution, Tobacco, Food, Stress and the Fight for Survival",
        "kicker": "Public Health",
        "category": ["nonfiction"],
        "coverClass": "cover-fifteen",
        "coverBg": "#5c2a2a",
        "coverFg": "#e8c9a0",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/5XwDEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 180,
        "publication_date": "2026-08-10",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=5XwDEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Why+Is+India+Becoming+the+Cancer+Capital+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "Why more Indians are facing cancer, what pollution, tobacco, diet and delayed diagnosis really have to do with it, and what an ordinary family can do about it.",
        "long_description": (
            "Why Is India Becoming the Cancer Capital? is a public-health investigation by Indian author Parvind Kumar into one of the country's most urgent and least understood crises. Rather than pointing to a single cause, the book traces how population growth and ageing, tobacco use, air pollution, changing diets, obesity, alcohol, and gaps in screening and diagnosis combine into a complex national burden.\n\n"
            "The book moves chapter by chapter through the numbers behind the headlines, the outsized role of tobacco in its many Indian forms, the evidence on air pollution and PM2.5, and the cancers — breast, lung, oral, cervical, colorectal, and prostate — that the country cannot afford to ignore. It also examines how late diagnosis and the financial cost of treatment fall unevenly across regions, income groups, and rural and urban India.\n\n"
            "Written to separate scientific evidence from popular myth, the book closes with a practical look at prevention — what individuals, families, clinicians, and policymakers can realistically do. It is, at its core, a book about awareness without panic and action without fatalism."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Cancer Numbers", "summary": "What India's incidence, mortality, and age-standardized rates actually mean, and why raw numbers alone mislead."},
            {"chapter": "Chapter 2: Tobacco and Cancer", "summary": "Cigarettes, bidis, gutka, khaini, and paan, and why tobacco remains the single most preventable risk."},
            {"chapter": "Chapter 3: Air Pollution and the Body", "summary": "What the evidence on PM2.5 and indoor smoke says about cancer risk."},
            {"chapter": "Chapter 4: Food, Obesity and Modern Life", "summary": "How processed diets, alcohol, and sedentary living are reshaping India's risk profile."},
            {"chapter": "Chapter 5: Late Diagnosis and Inequality", "summary": "Why cancer caught late changes outcomes, and how urban-rural and income gaps widen the divide."},
            {"chapter": "Chapter 6: Prevention and Action", "summary": "Realistic steps for individuals, families, and policymakers."}
        ],
        "reviews": [
            {"quote": "A clear-eyed, necessary book. It replaces fear with facts, and that is exactly what this subject needs.", "source": "Reader Review"},
            {"quote": "Rigorous without being alarmist. A useful starting point for any Indian family trying to understand real cancer risk.", "source": "Public Health Digest"}
        ]
    },
    {
        "slug": "the-virus-between-us",
        "title": "The Virus Between Us",
        "subtitle": "One Diagnosis. One Dead Doctor. A Secret That Could Destroy Everything.",
        "kicker": "Romance · Thriller",
        "category": ["fiction"],
        "coverClass": "cover-sixteen",
        "coverBg": "#1f2937",
        "coverFg": "#a9c4d9",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/ul4EEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 260,
        "publication_date": "2026-08-21",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=ul4EEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+Virus+Between+Us+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "An HIV diagnosis, a doctor's suspicious death, and a woman who won't stop asking questions — a suspenseful story about stigma, secrets, and redemption.",
        "long_description": (
            "The Virus Between Us is a romantic thriller by Indian author Parvind Kumar. Maya Sharma's life is upended by a single test result — and further upended when the doctor who delivered it is found dead, in what is officially ruled a suicide. Maya doesn't believe it, and when her own medical records vanish, she realizes someone doesn't want her asking questions.\n\n"
            "Her investigation pulls in a former lover, a fiancé with his own secrets, a powerful hospital owner, and a string of patients whose stories were quietly buried. Every answer she finds only opens another question, and every person she trusts turns out to be hiding something.\n\n"
            "Beneath its mystery, the novel is also a story about stigma — about what an HIV diagnosis does and doesn't mean, and about a woman deciding to understand her own truth before she can help anyone else understand theirs."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Diagnosis", "summary": "Maya receives the result that changes everything, hours before her doctor is found dead."},
            {"chapter": "Chapter 2: Missing Records", "summary": "A quiet disappearance from the hospital's files convinces Maya the death was no suicide."},
            {"chapter": "Chapter 3: Old Ties, New Doubts", "summary": "A former lover and a hospital owner both know more than they're saying."},
            {"chapter": "Chapter 4: What the Patients Knew", "summary": "Buried case files connect the doctor to a pattern no one was meant to notice."},
            {"chapter": "Chapter 5: The Truth About the Virus", "summary": "Maya confronts what her diagnosis means — and doesn't mean — for her future."},
            {"chapter": "Chapter 6: Reckoning", "summary": "The people hiding the truth are finally forced to answer for it."}
        ],
        "reviews": [
            {"quote": "A gripping mystery that never loses its heart. Kumar handles a difficult subject with real sensitivity.", "source": "Reader Review"},
            {"quote": "Tense, humane, and genuinely surprising. A thriller with something honest to say about stigma.", "source": "Fiction Weekly"}
        ]
    },
    {
        "slug": "the-bageshwar-phenomenon",
        "title": "The Bageshwar Phenomenon",
        "subtitle": "The Life, Faith, Controversies and Extraordinary Rise of Dhirendra Krishna Shastri",
        "kicker": "Biography",
        "category": ["nonfiction"],
        "coverClass": "cover-seventeen",
        "coverBg": "#4a3728",
        "coverFg": "#d8c3a5",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/-VUCEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 160,
        "publication_date": "2026-08-16",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=-VUCEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+Bageshwar+Phenomenon+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "The life, rise and controversies of Dhirendra Krishna Shastri — from a village in Madhya Pradesh to one of India's most talked-about spiritual figures.",
        "long_description": (
            "The Bageshwar Phenomenon is a biography by Indian author Parvind Kumar tracing the extraordinary rise of Dhirendra Krishna Shastri — from his childhood and family background in Gadha village to his emergence as one of India's most discussed contemporary spiritual figures.\n\n"
            "The book follows his religious storytelling, his association with Bageshwar Dham, the growth of the Divya Darbar, and the social-media presence that carried his following far beyond the temple town. It also examines the social initiatives associated with his name and the controversies that have followed his rise.\n\n"
            "Rather than simply praising or criticizing its subject, the book aims to separate documented fact from belief, presenting the story so far and leaving readers to form their own judgment about a figure whose story is still unfolding."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: A Village Called Gadha", "summary": "Family background and the early life that shaped a future spiritual leader."},
            {"chapter": "Chapter 2: The Kathavachak's Path", "summary": "Religious storytelling and the early years of public devotion."},
            {"chapter": "Chapter 3: Bageshwar Dham and the Divya Darbar", "summary": "How a local place of devotion became a national phenomenon."},
            {"chapter": "Chapter 4: Faith in the Feed", "summary": "Social media, virality, and the modern shape of religious celebrity."},
            {"chapter": "Chapter 5: Claims and Controversies", "summary": "The criticisms, debates, and questions that have followed his rise."}
        ],
        "reviews": [
            {"quote": "A balanced, well-researched account of a genuinely complicated public figure.", "source": "Reader Review"},
            {"quote": "Fair to both devotees and skeptics. Kumar resists the temptation to simplify.", "source": "Culture & Faith Review"}
        ]
    },
    {
        "slug": "pati-patni-aur-woh",
        "title": "पति, पत्नी और वो",
        "subtitle": "एक रहस्यमयी प्रेम कहानी",
        "kicker": "रहस्य रोमांस",
        "category": ["fiction"],
        "coverClass": "cover-eighteen",
        "coverBg": "#6b1f2a",
        "coverFg": "#f2d9c4",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/69_2EQAAQBAJ?fife=w800",
        "language": "Hindi",
        "pages": 190,
        "publication_date": "2026-07-21",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=69_2EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Pati+Patni+Aur+Woh+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "आर्यन, मीरा और रोहन की कहानी — प्यार, शक और राज़ जब एक ही छत के नीचे टकराते हैं, तो सच्चाई किसी ने सोची भी नहीं थी।",
        "long_description": (
            "पति, पत्नी और वो लेखक परविन्द कुमार की एक रहस्यमयी प्रेम कहानी है। आर्यन और मीरा की शादी को बारह साल हो चुके हैं, जब मीरा की अधूरी कहानी का किरदार रोहन वापस लौटता है। एक रात आर्यन की लाश ऑफिस में मिलती है, और शक की सुई रोहन की तरफ जाती है।\n\n"
            "इंस्पेक्टर देवेंद्र सिंह जैसे-जैसे सच के करीब पहुँचता है, करोड़ों की हेराफेरी, एक खतरनाक बिज़नेसमैन, एक छुपी हुई डायरी और एक सीलबंद लिफाफा — हर राज़ एक नई परत खोलता है।\n\n"
            "यह कहानी है रिश्तों की दरारों की, उस प्यार की जो जुनून बन जाता है, और उस औरत की जो हर झूठ के बाद भी खुद को टूटने नहीं देती।"
        ),
        "table_of_contents": [
            {"chapter": "अध्याय 1: बारह साल बाद", "summary": "आर्यन और मीरा की शादी में लौटती खामोशी, और रोहन की वापसी।"},
            {"chapter": "अध्याय 2: लाश और शक", "summary": "आर्यन का ऑफिस में मिलना, और पुलिस का पहला शक।"},
            {"chapter": "अध्याय 3: छुपी हुई डायरी", "summary": "मीरा के अतीत से जुड़े राज़ सामने आने लगते हैं।"},
            {"chapter": "अध्याय 4: करोड़ों की हेराफेरी", "summary": "एक बिज़नेसमैन और एक सीलबंद लिफाफे की कहानी।"},
            {"chapter": "अध्याय 5: असली गुनहगार", "summary": "इंस्पेक्टर देवेंद्र सिंह के सामने आता है वह सच, जो किसी ने सोचा भी नहीं था।"}
        ],
        "reviews": [
            {"quote": "एक कसी हुई रहस्य कहानी, जो आखिरी पन्ने तक बांधे रखती है।", "source": "Reader Review"},
            {"quote": "A tightly plotted Hindi thriller with real emotional depth beneath the mystery.", "source": "Fiction Weekly"}
        ]
    },
    {
        "slug": "the-american-distance",
        "title": "The American Distance",
        "subtitle": "Two People. One Country Divided. A Love That Refuses to Choose Sides.",
        "kicker": "Contemporary Romance",
        "category": ["fiction", "relationships"],
        "coverClass": "cover-nineteen",
        "coverBg": "#2d4a4a",
        "coverFg": "#d9b98d",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/HfACEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 230,
        "publication_date": "2026-08-11",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=HfACEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+American+Distance+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "An immigration lawyer and a tech executive fall for each other just as she uncovers that the algorithm hurting her client was built by his own company.",
        "long_description": (
            "The American Distance is a contemporary romance novel by Indian author Parvind Kumar. Maya Rao, an immigration lawyer fighting to keep her client Sofia from being deported over an unexplained fraud flag, collides — almost literally, over a spilled coffee — with Ethan Carter, a rising executive at the AI company behind the very software making that decision.\n\n"
            "What begins as an accidental meeting becomes something neither of them planned for, even as Maya digs deeper into the system quietly mapping and selling the American public, and discovers the man she can't stop thinking about helped build it.\n\n"
            "The novel follows Ethan's reckoning with what his company is really building, and Maya's own lesson that being right isn't always the same as being careful — a love story that refuses to look away from the country, and the systems, it's set inside."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: A Spilled Coffee", "summary": "Maya and Ethan meet outside a federal building, on opposite sides of a fight neither has named yet."},
            {"chapter": "Chapter 2: Four Minutes to Be Somewhere", "summary": "Taco-cart dates and a dinner where Ethan lies about a company name without quite meaning to."},
            {"chapter": "Chapter 3: What the Algorithm Decided", "summary": "Maya discovers the system flagging her client as fraud — and who built it."},
            {"chapter": "Chapter 4: The Distance Between Them", "summary": "Ethan is pulled deeper into what Halcyon AI is really building."},
            {"chapter": "Chapter 5: Putting a Name on It", "summary": "Ethan decides what it means to finally stand behind something hard."}
        ],
        "reviews": [
            {"quote": "A smart, timely romance that doesn't shy away from the systems shaping real lives.", "source": "Reader Review"},
            {"quote": "Genuinely moving, with a conscience. Kumar writes both the romance and the politics with a light hand.", "source": "Contemporary Fiction Review"}
        ]
    },
    {
        "slug": "lose-weight-without-dieting",
        "title": "Lose Weight Without Dieting",
        "subtitle": "Simple Lifestyle Habits That Work",
        "kicker": "Health & Wellness",
        "category": ["nonfiction", "mind"],
        "coverClass": "cover-twenty",
        "coverBg": "#3a5a40",
        "coverFg": "#dad7cd",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/hjXvEQAAQBAJ?fife=w800",
        "language": "English",
        "pages": 35,
        "publication_date": "2026-06-27",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=hjXvEQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Lose+Weight+Without+Dieting+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "A short, science-backed guide to losing weight through mindful eating, sleep, stress and movement — without restriction or calorie counting.",
        "long_description": (
            "Lose Weight Without Dieting is a concise health guide by Indian author Parvind Kumar for readers tired of diets that leave them hungry and back where they started. Rather than restriction or calorie counting, the book focuses on the daily habits — mindful eating, hydration, sleep, stress, and movement — that bring the body to its natural weight and keep it there.\n\n"
            "It explains why crash diets slow metabolism and make weight loss harder, how to eat less without feeling deprived, and the sleep and stress habits that directly affect fat storage. A step-by-step 30-Day Action Plan turns the ideas into a routine readers can actually keep."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Why Diets Fail", "summary": "How crash dieting slows metabolism and sets up the next relapse."},
            {"chapter": "Chapter 2: Eating Without Restriction", "summary": "Mindful eating habits that reduce intake without deprivation."},
            {"chapter": "Chapter 3: Sleep, Stress and Fat Storage", "summary": "The habits that quietly control weight from the inside."},
            {"chapter": "Chapter 4: Hydration and Metabolism", "summary": "Simple daily habits that add up."},
            {"chapter": "Chapter 5: The 30-Day Action Plan", "summary": "A step-by-step path to building habits that last."}
        ],
        "reviews": [
            {"quote": "Short, practical, and refreshingly free of diet-culture guilt.", "source": "Reader Review"},
            {"quote": "No gimmicks, just habits that actually stick. A quick, useful read.", "source": "Wellness Notes"}
        ]
    },
    {
        "slug": "101-stories-of-lord-shiva",
        "title": "101 Stories of Lord Shiva",
        "subtitle": "Timeless Tales of Divine Power, Wisdom, Devotion, and the Lessons We Still Need Today",
        "kicker": "Mythology",
        "category": ["nonfiction"],
        "coverClass": "cover-twenty-one",
        "coverBg": "#35281a",
        "coverFg": "#e3b23c",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/XtMEEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 280,
        "publication_date": "2026-08-23",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=XtMEEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=101+Stories+of+Lord+Shiva+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "101 stories of Mahadev — from the endless pillar of light to Shiva's many forms and sacred places — and the lessons they still offer today.",
        "long_description": (
            "101 Stories of Lord Shiva is a mythology collection by Indian author Parvind Kumar bringing together stories from across the many names and forms of Shiva — Mahadev, Shankara, Neelkanth, Rudra, Nataraja, Pashupatinath, and more. It moves from the mysterious Endless Pillar of Light through the stories of Sati and Parvati, the birth of Ganesha and Kartikeya, and the devotion of figures like Ravana, Markandeya, and Kannappa.\n\n"
            "The collection also explores Shiva's many forms and the sacred places associated with him — Kailash, Kashi, Kedarnath, Somnath, Rameshwaram, and the Jyotirlingas — while asking what each story still has to teach: about stillness, transformation, humility, and the quiet strength that doesn't need to announce itself."
        ),
        "table_of_contents": [
            {"chapter": "Section 1: The Endless Pillar of Light", "summary": "The mystery at the heart of Shiva's origin stories."},
            {"chapter": "Section 2: Sati and Parvati", "summary": "Love, loss and devotion across two lifetimes."},
            {"chapter": "Section 3: Devotees and Demons", "summary": "Ravana, Markandeya, Kannappa and the many faces of devotion."},
            {"chapter": "Section 4: The Many Forms of Mahadev", "summary": "Nataraja, Ardhanarishvara, Bhairava and what each form represents."},
            {"chapter": "Section 5: Sacred Places", "summary": "Kailash, Kashi, Kedarnath and the geography of devotion."},
            {"chapter": "Section 6: What Shiva Still Teaches", "summary": "Reflections on stillness, transformation and inner strength for today."}
        ],
        "reviews": [
            {"quote": "Beautifully retold and easy to read aloud to the whole family.", "source": "Reader Review"},
            {"quote": "A warm, accessible entry point into Shiva's many stories and forms.", "source": "Dharma Digest"}
        ]
    },
    {
        "slug": "101-stories-of-buddha",
        "title": "101 Stories of Buddha",
        "subtitle": "Timeless Tales of Wisdom, Compassion, Mindfulness, and the Lessons We Still Need Today",
        "kicker": "Mythology & Philosophy",
        "category": ["nonfiction", "mind"],
        "coverClass": "cover-twenty-two",
        "coverBg": "#22303a",
        "coverFg": "#c9a66b",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/OQwFEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 260,
        "publication_date": "2026-08-24",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=OQwFEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=101+Stories+of+Buddha+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "The journey of Siddhartha Gautama and 101 stories exploring anger, attachment, mindfulness, and how ancient Buddhist wisdom applies to modern, distracted life.",
        "long_description": (
            "101 Stories of Buddha is a collection by Indian author Parvind Kumar tracing Siddhartha Gautama's journey from a life of privilege to his awakening beneath the Bodhi tree, and the teachings that followed. Across ten thematic sections, it explores the Four Noble Truths and the Eightfold Path, compassion and loving-kindness, anger and forgiveness, attachment, mindfulness, ego, karma, and impermanence.\n\n"
            "The stories include kings, scholars, monks and ordinary people — a grieving mother searching for a mustard seed, an insult refused, a sick monk needing compassion — and a final section that carries these teachings into distinctly modern territory: traffic, social media, comparison, and information overload.\n\n"
            "It is less a book to admire than one meant to be practiced — an invitation to notice what a reader is holding on to, and where compassion might replace anger."
        ),
        "table_of_contents": [
            {"chapter": "Section 1: The Journey of Siddhartha Gautama", "summary": "From the royal palace to the discovery of the Middle Way."},
            {"chapter": "Section 2: The Four Noble Truths and the Eightfold Path", "summary": "The foundation of the Buddha's teaching."},
            {"chapter": "Section 3: Compassion, Anger and Forgiveness", "summary": "Stories of loving-kindness and letting go of resentment."},
            {"chapter": "Section 4: Attachment and Letting Go", "summary": "What the Buddha's parables teach about clinging and release."},
            {"chapter": "Section 5: Mindfulness and the Present Moment", "summary": "Living with attention in an inattentive world."},
            {"chapter": "Section 6: Ancient Wisdom, Modern Life", "summary": "Traffic, social media and distraction seen through Buddhist parables."}
        ],
        "reviews": [
            {"quote": "Gentle, clear, and genuinely useful for daily life — not just ancient history.", "source": "Reader Review"},
            {"quote": "The modern parables in the final section make this collection stand out.", "source": "Mindful Living Magazine"}
        ]
    },
    {
        "slug": "focused-101",
        "title": "Focused 101",
        "subtitle": "How to Reclaim Your Attention, Beat Distraction, and Get More Done in a Distracted World",
        "kicker": "Productivity",
        "category": ["nonfiction", "mind"],
        "coverClass": "cover-twenty-three",
        "coverBg": "#263238",
        "coverFg": "#80cbc4",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/l1ACEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 150,
        "publication_date": "2026-08-13",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=l1ACEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Focused+101+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "A practical system for reclaiming attention and beating distraction — from Notification Zero to a structured 90-Day Focus Challenge.",
        "long_description": (
            "Focused 101 is a productivity guide by Indian author Parvind Kumar built around a simple idea: in a world of notifications and constant information, the real challenge is no longer managing time but managing attention. The book identifies four enemies of focus — Distractions, Switching, Friction, and Mental Clutter — and offers concrete countermeasures for each.\n\n"
            "Techniques like the 5-Minute Beginning, Phone-Free Hour, Notification Zero, Single-Tasking, and Focus Sessions are applied across studying, professional work, entrepreneurship, and relationships. The book also introduces Digital Minimalism, the One-Goal Principle, and the idea of an Attention Budget for making more deliberate daily choices.\n\n"
            "It closes with a structured 90-Day Focus Challenge and a Focus Toolkit of worksheets and trackers, designed to turn the ideas into a lasting habit rather than a one-time read."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Four Enemies of Focus", "summary": "Distractions, Switching, Friction and Mental Clutter."},
            {"chapter": "Chapter 2: Small Starts", "summary": "The 5-Minute Beginning and building momentum without willpower."},
            {"chapter": "Chapter 3: Notification Zero", "summary": "Redesigning a phone and a day around fewer interruptions."},
            {"chapter": "Chapter 4: Single-Tasking and Focus Sessions", "summary": "Structured blocks of real, undivided attention."},
            {"chapter": "Chapter 5: The Attention Budget", "summary": "Digital minimalism and the One-Goal Principle."},
            {"chapter": "Chapter 6: The 90-Day Focus Challenge", "summary": "A structured path from distracted to deeply focused."}
        ],
        "reviews": [
            {"quote": "Practical without being preachy. I actually finished the 90-day challenge.", "source": "Reader Review"},
            {"quote": "A clear, well-organized system for a problem most productivity books only complain about.", "source": "Productivity Weekly"}
        ]
    },
    {
        "slug": "the-new-indian-marriage",
        "title": "The New Indian Marriage",
        "subtitle": "Love, Dating Apps, Live-In Relationships, Divorce, Infidelity and the Changing Indian Family",
        "kicker": "Society & Relationships",
        "category": ["nonfiction", "relationships"],
        "coverClass": "cover-twenty-four",
        "coverBg": "#4b2e39",
        "coverFg": "#e0b0a0",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/6DoCEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 220,
        "publication_date": "2026-08-09",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=6DoCEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+New+Indian+Marriage+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "What Indian marriage actually looks like today — arranged marriage in the smartphone era, live-in relationships, dowry, dating apps, and a generation delaying marriage entirely.",
        "long_description": (
            "The New Indian Marriage is a nonfiction study by Indian author Parvind Kumar examining what marriage actually looks like across India today, not what it's supposed to look like. Each chapter opens with a real story and is grounded in a Supreme Court ruling, a national survey, or a government dataset, with fifteen charts and a full source list backing the claims.\n\n"
            "The book covers arranged marriage in the smartphone era, dowry and why the law hasn't stopped it, inter-caste and interfaith love still fought over in court, live-in couples with nowhere to legally rent, dating apps quietly becoming marriage bureaus, financial independence and the resentment it can trigger, and divorce, infidelity, surrogacy and LGBTQ+ rights.\n\n"
            "It doesn't argue that arranged marriage is outdated or love marriage is better. It shows, honestly, what marriage in India looks like now — messy, uneven, and still somehow holding a country together."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Arranged Marriage in the Smartphone Era", "summary": "WhatsApp introductions and the persistence of family-arranged matches."},
            {"chapter": "Chapter 2: Dowry, Sixty Years Later", "summary": "Why a decades-old law hasn't ended the practice."},
            {"chapter": "Chapter 3: Love Across the Lines", "summary": "Inter-caste and interfaith marriage, still fought over in court."},
            {"chapter": "Chapter 4: Live-In and Legally Invisible", "summary": "Couples navigating a country with no clear rental or legal status for cohabitation."},
            {"chapter": "Chapter 5: Dating Apps as Marriage Bureaus", "summary": "How swiping quietly became a modern matchmaking system."},
            {"chapter": "Chapter 6: Divorce, Infidelity and What Comes Next", "summary": "Surrogacy, LGBTQ+ rights, and a generation delaying marriage."}
        ],
        "reviews": [
            {"quote": "Data-driven and genuinely even-handed — rare for a book on this subject.", "source": "Reader Review"},
            {"quote": "Fifteen charts and real court rulings back up every claim. This isn't opinion writing.", "source": "Family & Society Journal"}
        ]
    },
    {
        "slug": "freedom-and-partition",
        "title": "Freedom and Partition",
        "subtitle": "The Struggle for Independence, the Decisions Behind Partition, and the Human Cost of 1947",
        "kicker": "History",
        "category": ["nonfiction"],
        "coverClass": "cover-twenty-five",
        "coverBg": "#33312e",
        "coverFg": "#c1a875",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/QCcCEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 210,
        "publication_date": "2026-08-15",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=QCcCEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Freedom+and+Partition+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "How India's freedom movement led to Partition — from Gandhi's mass movements to the Radcliffe Line and the refugee crisis that followed August 1947.",
        "long_description": (
            "Freedom and Partition is a history by Indian author Parvind Kumar tracing India's path from British colonial rule to independence — and why that journey ended in the division of the subcontinent. It follows the rise of Indian nationalism and Gandhi's mass movements, the emergence of Muhammad Ali Jinnah and the Muslim League, and the negotiations of the 1940s through the Cabinet Mission, the Mountbatten Plan, and the Radcliffe Line.\n\n"
            "Rather than a simple story of heroes and villains, the book examines the competing ambitions, fears, and failures that brought the subcontinent to its final crossroads — and the enormous refugee crisis that followed the celebrations of August 1947.\n\n"
            "At its center is one enduring question: how the dream of freedom became intertwined with the division of a country, and what that meant for the millions of ordinary lives transformed by 1947."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Rise of Indian Nationalism", "summary": "Gandhi's mass movements and the growing demand for self-rule."},
            {"chapter": "Chapter 2: Jinnah and the Muslim League", "summary": "The emergence of a rival political vision."},
            {"chapter": "Chapter 3: The Cabinet Mission and Mountbatten Plan", "summary": "The negotiations that shaped the final settlement."},
            {"chapter": "Chapter 4: The Radcliffe Line", "summary": "How a border was drawn, and what it failed to account for."},
            {"chapter": "Chapter 5: August 1947", "summary": "Independence, celebration, and the immediate aftermath."},
            {"chapter": "Chapter 6: The Human Cost", "summary": "The refugee crisis and the families divided by a new map."}
        ],
        "reviews": [
            {"quote": "A measured, well-sourced account that resists easy heroes and villains.", "source": "Reader Review"},
            {"quote": "Clear-eyed history writing that never loses sight of the human cost.", "source": "History Quarterly"}
        ]
    },
    {
        "slug": "101-stories-of-lord-krishna",
        "title": "101 Stories of Lord Krishna",
        "subtitle": "Timeless Tales of Divine Love, Wisdom, Courage, Dharma, and the Lessons Krishna Still Teaches Us Today",
        "kicker": "Mythology",
        "category": ["nonfiction"],
        "coverClass": "cover-twenty-six",
        "coverBg": "#1a2a4a",
        "coverFg": "#e8c468",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/fqgDEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 280,
        "publication_date": "2026-08-20",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=fqgDEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=101+Stories+of+Lord+Krishna+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "From Krishna's birth in Mathura to the battlefield of Kurukshetra — 101 stories of divine love, friendship, courage and dharma.",
        "long_description": (
            "101 Stories of Lord Krishna is a mythology collection by Indian author Parvind Kumar that follows Krishna's journey from his birth in Mathura and childhood in Vrindavan to the battlefield of Kurukshetra and the wisdom of the Bhagavad Gita. It travels through his playful childhood, his bond with Radha and the gopis, the lifting of Govardhan Hill, his friendship with Sudama, and his role as Arjuna's charioteer.\n\n"
            "The collection presents Krishna as a genuinely multifaceted figure — mischievous child, devoted friend, strategic leader, and spiritual teacher — and asks what each story still offers today: courage in fear, humility in success, and faith when the path ahead is uncertain."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Birth and Childhood in Vrindavan", "summary": "Krishna's early life among the gopis and Yashoda."},
            {"chapter": "Chapter 2: Govardhan Hill and the Protection of Vrindavan", "summary": "Krishna's defiance of Indra and his devotion to his people."},
            {"chapter": "Chapter 3: Friendship and Loyalty", "summary": "Sudama, Draupadi and Krishna's bonds beyond the divine."},
            {"chapter": "Chapter 4: The Charioteer of Kurukshetra", "summary": "Krishna's role in the Pandavas' story and the Bhagavad Gita."},
            {"chapter": "Chapter 5: The Wisdom of the Gita", "summary": "Teachings on action, fear, attachment and dharma."},
            {"chapter": "Chapter 6: What Krishna Still Teaches", "summary": "Reflections on courage, friendship and faith for modern readers."}
        ],
        "reviews": [
            {"quote": "A joyful, accessible retelling that both children and adults will love.", "source": "Reader Review"},
            {"quote": "Faithful to tradition while making every story feel immediate and alive.", "source": "Dharma Digest"}
        ]
    },
    {
        "slug": "the-price-of-an-ordinary-life",
        "title": "The Price of an Ordinary Life",
        "subtitle": "A Modern Indian Novel About Money, Marriage, Work, Debt, Family, and the Fight for Dignity",
        "kicker": "Fiction",
        "category": ["fiction"],
        "coverClass": "cover-twenty-seven",
        "coverBg": "#3d3d3d",
        "coverFg": "#e0c097",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/vqYCEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 240,
        "publication_date": "2026-08-12",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=vqYCEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=The+Price+of+an+Ordinary+Life+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "A middle-class man in Delhi NCR loses his job — and a year strips away every assumption his family made about security.",
        "long_description": (
            "The Price of an Ordinary Life is a family drama by Indian author Parvind Kumar following Raghav Sharma — not poor, not rich, an ordinary middle-class man with a home loan, two children, ageing parents, and a job he loses in the opening pages. What follows is a year of hospital bills, a credit card whose minimum due turns out to be a trap, a farmer father drowning in his own kind of debt, and a wife rediscovering the career she once set aside.\n\n"
            "The novel follows three generations of one family — a grandfather who needed only enough to survive, a father taught to need enough to succeed, and children only beginning to ask what it means to be free — set between a North Indian village and a rapidly changing NCR.\n\n"
            "It is a story about EMIs and dignity, about a sister who refuses a marriage proposal that reduced her to a checklist, and about how much an ordinary life actually costs when the bill finally comes due."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Job Raghav Loses", "summary": "A comfortable middle-class life begins to unravel."},
            {"chapter": "Chapter 2: The Minimum Due", "summary": "Debt, a hospital bill, and the trap hidden in fine print."},
            {"chapter": "Chapter 3: Two Kinds of Debt", "summary": "Raghav's father, a farmer in Uttar Pradesh, faces his own version of the same fight."},
            {"chapter": "Chapter 4: What the Children Found", "summary": "A ledger discovered by accident changes what the family understands about itself."},
            {"chapter": "Chapter 5: The Job Offer", "summary": "Raghav is offered the one job that could fix everything, if he becomes what once broke him."},
            {"chapter": "Chapter 6: The Price", "summary": "What the family finally decides an ordinary life is worth."}
        ],
        "reviews": [
            {"quote": "Painfully real. This is the story of half of urban India's middle class.", "source": "Reader Review"},
            {"quote": "A quiet, devastating portrait of dignity under financial pressure.", "source": "Literary Review Weekly"}
        ]
    },
    {
        "slug": "101-stories-of-lord-ganesha",
        "title": "101 Stories of Lord Ganesha",
        "subtitle": "Timeless Tales of Divine Wisdom, Courage, Devotion, and the Lessons We Still Need Today",
        "kicker": "Mythology",
        "category": ["nonfiction"],
        "coverClass": "cover-twenty-eight",
        "coverBg": "#b0413e",
        "coverFg": "#fdf0d5",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/IZ4EEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 240,
        "publication_date": "2026-08-22",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=IZ4EEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=101+Stories+of+Lord+Ganesha+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "From the boy guarding his mother's door to the remover of obstacles celebrated at every festival — 101 stories of Ganesha's life, legend and teachings.",
        "long_description": (
            "101 Stories of Lord Ganesha is a mythology collection by Indian author Parvind Kumar tracing Ganesha's full story — his dramatic birth on Kailash, his mischievous childhood, the legendary race around the world with his brother Kartikeya, and his service as sage Vyasa's scribe for the Mahabharata.\n\n"
            "Alongside the traditional accounts sit original teaching parables — of proud scholars humbled and farmers who nearly gave up — each illustrating the patience and devotion Ganesha represents. The book is upfront about its sources throughout, labeling clearly what is traditional Puranic story, festival custom, and original parable, so readers always know which is which."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: The Birth on Kailash", "summary": "The confrontation that shaped Ganesha's role as guardian."},
            {"chapter": "Chapter 2: The Race Around the World", "summary": "Ganesha's wit against Kartikeya's speed."},
            {"chapter": "Chapter 3: Scribe of the Mahabharata", "summary": "Ganesha's service to sage Vyasa."},
            {"chapter": "Chapter 4: Festival Origins", "summary": "The stories behind the customs still celebrated today."},
            {"chapter": "Chapter 5: Original Parables", "summary": "New stories of patience, humility and devotion in Ganesha's spirit."}
        ],
        "reviews": [
            {"quote": "A lovely collection to read aloud with children before Ganesh Chaturthi.", "source": "Reader Review"},
            {"quote": "Refreshingly honest about which stories are tradition and which are retellings.", "source": "Dharma Digest"}
        ]
    },
    {
        "slug": "marriage-turned-murder",
        "title": "Marriage Turned Murder",
        "subtitle": "India's Most Shocking Husband and Wife Crimes, 20 True Stories",
        "kicker": "True Crime",
        "category": ["nonfiction"],
        "coverClass": "cover-twenty-nine",
        "coverBg": "#261c1c",
        "coverFg": "#c94c4c",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/FeP_EQAAQBAJ?fife=w800",
        "language": "English",
        "pages": 200,
        "publication_date": "2026-08-01",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=FeP_EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Marriage+Turned+Murder+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "Twenty real Indian marriages that ended in murder — built from police statements, court filings, and verified news reports.",
        "long_description": (
            "Marriage Turned Murder is a true crime collection by Indian author Parvind Kumar documenting twenty real cases where an Indian marriage ended in murder — among them the Blue Drum Murder, the Cobra Plot, the Tandoor Murder, and the Faridkot NRI case, drawn from Delhi, Bihar, Kerala, Punjab, Karnataka, Maharashtra and beyond.\n\n"
            "Built from police statements, court filings, and verified news reports, each chapter follows the same structure — the victim, the marriage, the crime, the investigation, and where the case stands today — asking how well anyone truly knows the person sleeping beside them."
        ),
        "table_of_contents": [
            {"chapter": "Case 1: The Blue Drum Murder", "summary": "A case that shocked Delhi and exposed a marriage's hidden violence."},
            {"chapter": "Case 2: The Cobra Plot", "summary": "A meticulously planned crime that nearly went undetected."},
            {"chapter": "Case 3: The Tandoor Murder", "summary": "One of India's most infamous marital crimes, revisited."},
            {"chapter": "Case 4: The Faridkot NRI Case", "summary": "A cross-border marriage that ended in tragedy."},
            {"chapter": "Cases 5–20: Sixteen More Cases", "summary": "Sixteen further verified cases from across India, and what they reveal."}
        ],
        "reviews": [
            {"quote": "Meticulously researched and told without sensationalism.", "source": "Reader Review"},
            {"quote": "Sober, well-sourced true crime — exactly what this genre needs more of.", "source": "True Crime Digest"}
        ]
    },
    {
        "slug": "digital-product-sales-marketing-strategy",
        "title": "Digital Product Sales & Marketing Strategy",
        "subtitle": "A 27-Chapter Playbook for Building, Launching, and Scaling a Digital Product Business",
        "kicker": "Business",
        "category": ["business", "nonfiction"],
        "coverClass": "cover-thirty",
        "coverBg": "#1b3a4b",
        "coverFg": "#8ecae6",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/VIn3EQAAQBAJ?fife=w800",
        "language": "English",
        "pages": 164,
        "publication_date": "2026-07-23",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=VIn3EQAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=Digital+Product+Sales+Marketing+Strategy+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "A 164-page, 27-chapter practitioner guide to building, launching and scaling a digital product business, with templates for every step.",
        "long_description": (
            "Digital Product Sales & Marketing Strategy is a business playbook by Indian author Parvind Kumar covering the complete lifecycle of a digital product business — from validating a product idea to building a sales funnel, running email and paid campaigns, launching to a list, and scaling internationally.\n\n"
            "The book is organized into six parts: Foundation, Infrastructure, Marketing, Growth, Optimisation & Scale, and a closing section on AI and future trends. It backs its claims with over 40 primary source citations and 18 real creator case studies, and includes nearly 30 copy-paste templates — email sequences, ad account structures, and a pricing calculator among them — plus a 90-Day Action Plan tying every task to a specific chapter."
        ),
        "table_of_contents": [
            {"chapter": "Part I: Foundation", "summary": "Choosing the right product, buyer persona, and brand positioning."},
            {"chapter": "Part II: Infrastructure", "summary": "Payment platforms, sales funnels, pricing, and legal compliance."},
            {"chapter": "Part III: Marketing", "summary": "SEO, email marketing, social ads, video, and community building."},
            {"chapter": "Part IV: Growth", "summary": "Affiliate marketing, launch frameworks, upselling, and buyer psychology."},
            {"chapter": "Part V: Optimisation & Scale", "summary": "Analytics, retention, international pricing, and creator mindset."},
            {"chapter": "Part VI: Future", "summary": "An AI toolkit for creators and the trends shaping digital commerce ahead."}
        ],
        "reviews": [
            {"quote": "The most actionable digital products book I've read — templates, not just theory.", "source": "Reader Review"},
            {"quote": "Dense with real numbers and real case studies. A genuine reference, not another marketing pep talk.", "source": "Business Playbook Review"}
        ]
    },
    {
        "slug": "101-public-speaking-tips",
        "title": "101 Public Speaking Tips",
        "subtitle": "Master the Stage, Own the Room, Change Minds",
        "kicker": "Self-Help",
        "category": ["nonfiction", "mind"],
        "coverClass": "cover-thirty-one",
        "coverBg": "#4a4e69",
        "coverFg": "#f2e9e4",
        "coverImage": "https://play.google.com/books/publisher/content/images/frontcover/eCoDEgAAQBAJ?fife=w800",
        "language": "English",
        "pages": 220,
        "publication_date": "2026-06-28",
        "isbn": "Digital Edition — Google Play",
        "publisher": "Independent",
        "amazon": "",
        "google_play": "https://play.google.com/store/books/details?id=eCoDEgAAQBAJ",
        "goodreads": "https://www.goodreads.com/search?q=101+Public+Speaking+Tips+Parvind+Kumar",
        "formats": "eBook (Google Play)",
        "description": "101 actionable techniques for public speaking — from conquering fear to structuring speeches, vocal delivery, and a 30-day action plan.",
        "long_description": (
            "101 Public Speaking Tips is a practical guide by Indian author Parvind Kumar covering the complete public-speaking journey in 101 actionable techniques — conquering fear without waiting to feel ready, researching an audience, structuring stronger openings and conclusions, and mastering vocal delivery, pace, and pauses.\n\n"
            "The book also covers body language and stage presence, storytelling, audience interaction, presentation design, and handling difficult Q&A. It closes with a 30-Day Public Speaking Action Plan that pushes readers to practice progressively, record themselves, and ultimately deliver a speech to a live audience."
        ),
        "table_of_contents": [
            {"chapter": "Chapter 1: Conquering Fear", "summary": "Building confidence without waiting to feel ready."},
            {"chapter": "Chapter 2: Structure and Preparation", "summary": "Stronger openings, transitions, and conclusions."},
            {"chapter": "Chapter 3: Vocal Delivery and Body Language", "summary": "Pace, pitch, pauses, and stage presence."},
            {"chapter": "Chapter 4: Storytelling and Engagement", "summary": "Making ideas memorable and keeping an audience involved."},
            {"chapter": "Chapter 5: Slides, Q&A and Difficult Moments", "summary": "Presenting with clarity and handling pressure with composure."},
            {"chapter": "Chapter 6: The 30-Day Action Plan", "summary": "A structured path from nervous speaker to confident one."}
        ],
        "reviews": [
            {"quote": "Practical, specific, and genuinely confidence-building.", "source": "Reader Review"},
            {"quote": "The 30-day plan alone is worth the read. I used it before a real conference talk.", "source": "Communication Quarterly"}
        ]
    }
]

TRANSLATIONS = {
    "en": {
        "lang": "en",
        "author_by": "by",
        "author_name": "Parvind Kumar",
        "book_info": "Book Details",
        "published": "Published",
        "pages": "Pages",
        "language": "Language",
        "genre": "Genre",
        "publisher": "Publisher",
        "rating_label": "(Goodreads Ratings)",
        "toc_title": "Table of Contents",
        "reviews_title": "Reviews & Testimonials",
        "back_to_library": "← Back to Library",
        "other_books": "Other books by <em>Parvind Kumar</em>",
        "explore_more": "EXPLORE MORE",
        "discover_other": "Discover other works in relationships, fiction, and mindfulness.",
        "isbn": "ISBN",
        "formats": "Format"
    },
    "hi": {
        "lang": "hi",
        "author_by": "लेखक:",
        "author_name": "परविन्द कुमार",
        "book_info": "पुस्तक विवरण",
        "published": "प्रकाशन तिथि",
        "pages": "पृष्ठ संख्या",
        "language": "भाषा",
        "genre": "श्रेणी",
        "publisher": "प्रकाशक",
        "rating_label": "(समीक्षाएँ)",
        "toc_title": "विषय-सूची",
        "reviews_title": "समीक्षाएँ",
        "back_to_library": "← पुस्तकालय पर वापस जाएँ",
        "other_books": "लेखक <em>परविन्द कुमार</em> की अन्य पुस्तकें",
        "explore_more": "और खोजें",
        "discover_other": "रिश्तों, कथा साहित्य और माइंडफुलनेस पर अन्य पुस्तकें देखें।",
        "isbn": "ISBN",
        "formats": "प्रारूप"
    }
}

# Path configurations
BASE_DIR = "/Users/parvindkumar/Documents/p/parvind-kumar.github.io"
BOOKS_DIR = os.path.join(BASE_DIR, "books")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} by Parvind Kumar | {kicker}</title>
  <meta name="description" content="{description}">
  <meta name="author" content="Parvind Kumar">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="book">
  <meta property="og:title" content="{title} by Parvind Kumar | {kicker}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://parvind-kumar.github.io/books/{slug}/">
  <meta property="og:image" content="{cover_image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://parvind-kumar.github.io/books/{slug}/">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%23131210'/%3E%3Ctext x='50' y='66' font-size='55' text-anchor='middle' fill='%23f4efe7' font-family='serif'%3EP%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "{title}",
    "author": {{
      "@type": "Person",
      "name": "Parvind Kumar",
      "url": "https://parvind-kumar.github.io/"
    }},
    "isbn": "{isbn}",
    "datePublished": "{publication_date}",
    "inLanguage": "{language}",
    "numberOfPages": {pages},
    "publisher": {{
      "@type": "Organization",
      "name": "{publisher}"
    }},
    "image": "{cover_image}",
    "description": "{description}",
    "workExample": [
      {{
        "@type": "Book",
        "isbn": "{isbn}",
        "potentialAction": {{
          "@type": "ReadAction",
          "target": [
            {{
              "@type": "EntryPoint",
              "urlTemplate": "{primary_buy_link}",
              "actionPlatform": [
                "http://schema.org/DesktopWebPlatform",
                "http://schema.org/MobileWebPlatform"
              ]
            }}
          ]
        }}
      }}
    ]
  }}
  </script>
</head>
<body class="book-detail-page">
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="container nav-wrap">
      <a class="brand" href="../../" aria-label="Parvind Kumar home">
        <span class="brand-mark">P</span>
        <span>
          <strong>Parvind Kumar</strong>
          <small>Author · Novelist · Writer</small>
        </span>
      </a>

      <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation">
        <span></span><span></span><span></span>
      </button>

      <nav id="site-nav" class="site-nav" aria-label="Main navigation">
        <a href="../../#books">Books</a>
        <a href="../../#about">About</a>
        <a href="../../#ideas">Ideas</a>
        <a href="../../#author">Author Journey</a>
        <a href="../../#contact">Contact</a>
        <a class="nav-cta" href="../../#books">Explore Books</a>
      </nav>
    </div>
  </header>

  <main id="main" class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb">
      <a href="../../">Home</a>
      <span class="separator">/</span>
      <a href="../../#books">Books</a>
      <span class="separator">/</span>
      <span class="current" aria-current="page">{title}</span>
    </nav>

    <div class="book-detail-grid">
      <!-- Left Column: Visuals & Buying Actions -->
      <div class="book-detail-visual">
        <div class="book-cover {cover_class}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.7) 100%), url('{cover_image}');">
          <span class="cover-kicker">{kicker_upper}</span>
          <span class="cover-title">{title}</span>
          <span class="cover-author">PARVIND KUMAR</span>
        </div>
        {unavailable_badge}

        <div class="buy-buttons">
          {amazon_btn}
          {google_play_btn}
          <a class="button buy-btn goodreads-btn" href="{goodreads}" target="_blank" rel="noopener">View on Goodreads <span>↗</span></a>
        </div>

        <div class="meta-box">
          <h4>{t_book_info}</h4>
          <div class="meta-row">
            <span>{t_isbn}</span>
            <strong>{isbn}</strong>
          </div>
          <div class="meta-row">
            <span>{t_published}</span>
            <strong>{publication_date_str}</strong>
          </div>
          <div class="meta-row">
            <span>{t_pages}</span>
            <strong>{pages}</strong>
          </div>
          <div class="meta-row">
            <span>{t_language}</span>
            <strong>{language}</strong>
          </div>
          <div class="meta-row">
            <span>{t_formats}</span>
            <strong>{formats}</strong>
          </div>
          <div class="meta-row">
            <span>{t_genre}</span>
            <strong>{genre}</strong>
          </div>
        </div>
      </div>

      <!-- Right Column: Description & Contents -->
      <div class="book-detail-copy">
        <p class="eyebrow">{kicker_upper}</p>
        <h1>{title}</h1>
        <p class="book-subtitle">{subtitle}</p>
        <p class="author-attribution">{t_author_by} {t_author_name}</p>
        
        <div class="book-rating" aria-label="Rating: 5 out of 5 stars">
          <span class="stars">★★★★★</span>
          <span class="rating-value">{rating_value} / 5</span>
          <span class="rating-count">{t_rating_label}</span>
        </div>

        <div class="full-description">
          <p class="lead-description"><strong>{description}</strong></p>
          {long_description_html}
        </div>

        <div class="detail-section toc-section">
          <h3>{t_toc_title}</h3>
          <ul class="toc-list">
            {toc_html}
          </ul>
        </div>

        <div class="detail-section reviews-section">
          <h3>{t_reviews_title}</h3>
          <div class="reviews-grid">
            {reviews_html}
          </div>
        </div>

        <div class="back-to-library">
          <a class="text-link" href="../../#books">{t_back_to_library}</a>
        </div>
      </div>
    </div>
  </main>

  <!-- Related Books -->
  <section class="section related-books-section">
    <div class="container">
      <div class="section-heading reveal visible">
        <div>
          <p class="eyebrow">{t_explore_more}</p>
          <h2>{t_other_books}</h2>
        </div>
        <p>{t_discover_other}</p>
      </div>
      <div class="book-grid">
        {related_books_html}
      </div>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container footer-top">
      <div>
        <a class="brand footer-brand" href="../../">
          <span class="brand-mark">P</span>
          <span><strong>Parvind Kumar</strong><small>Author · Novelist · Writer</small></span>
        </a>
        <p>Stories, ideas and books about modern life.</p>
      </div>
      <div class="footer-links">
        <a href="../../#books">Books</a>
        <a href="../../#about">About</a>
        <a href="../../#ideas">Ideas</a>
        <a href="../../#contact">Contact</a>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>&copy; <span id="year"></span> Parvind Kumar. All rights reserved.</span>
      <span>Hosted with GitHub Pages.</span>
    </div>
  </footer>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
    // Mobile navigation toggle
    const menuToggle = document.querySelector(".menu-toggle");
    const siteNav = document.getElementById("site-nav");
    menuToggle.addEventListener("click", () => {{
      const open = siteNav.classList.toggle("open");
      menuToggle.setAttribute("aria-expanded", open ? "true" : "false");
    }});
  </script>
</body>
</html>
"""

def generate_pages():
    # Make sure output books directory exists
    if not os.path.exists(BOOKS_DIR):
        os.makedirs(BOOKS_DIR)
        print(f"Created directory {BOOKS_DIR}")

    # Generate each book detail page
    for i, book in enumerate(BOOKS):
        slug = book["slug"]
        title = book["title"]
        subtitle = book["subtitle"]
        kicker = book["kicker"]
        lang = book["language"]
        
        book_dir = os.path.join(BOOKS_DIR, slug)
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            print(f"Created book folder {book_dir}")

        # Choose translation dictionary
        t_key = "hi" if lang.lower() == "hindi" else "en"
        trans = TRANSLATIONS[t_key]

        # Formulate variables
        kicker_upper = kicker.upper()
        
        # Decide dynamic publication date display
        pub_parts = book["publication_date"].split("-")
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if len(pub_parts) == 3:
            year = pub_parts[0]
            month_idx = int(pub_parts[1]) - 1
            month_name = months[month_idx]
            publication_date_str = f"{month_name} {year}"
        else:
            publication_date_str = book["publication_date"]

        genre_name = ", ".join([c.capitalize() for c in book["category"]])
        if "fiction" in book["category"]:
            genre_name = "Fiction"
        elif "nonfiction" in book["category"]:
            genre_name = "Non-Fiction"
        
        if "relationships" in book["category"]:
            genre_name += " / Relationships"
        elif "mind" in book["category"]:
            genre_name += " / Mindfulness & Wellbeing"
        elif "business" in book["category"]:
            genre_name += " / Business & Infrastructure"

        # Split long description into paragraphs
        long_desc_paras = book["long_description"].split("\n\n")
        long_description_html = "\n".join([f"<p>{p}</p>" for p in long_desc_paras])

        # Table of contents HTML
        toc_html = ""
        for item in book["table_of_contents"]:
            toc_html += f'<li><span>{item["chapter"]}: {item["summary"]}</span></li>'

        # Reviews HTML
        reviews_html = ""
        for rev in book["reviews"]:
            # Random rating or default 5 stars
            stars_str = "★★★★★"
            reviews_html += f'''
            <div class="review-card">
              <div class="review-stars">{stars_str}</div>
              <p class="review-text">&ldquo;{rev["quote"]}&rdquo;</p>
              <span class="reviewer">&mdash; {rev["source"]}</span>
            </div>
            '''

        # Status badge if unavailable
        unavailable_badge = ""
        if book.get("unavailable"):
            unavailable_badge = '<div style="background:var(--accent); color:white; font-size:12px; font-weight:700; text-transform:uppercase; padding:8px; text-align:center; border-radius:4px; margin-top:-10px; margin-bottom:15px;">Currently Unavailable</div>'

        # Related books HTML (pick 4 books excluding this one)
        related_books = []
        for other in BOOKS:
            if other["slug"] != slug:
                related_books.append(other)
            if len(related_books) == 4:
                break
        
        related_books_html = ""
        for other in related_books:
            related_books_html += f'''
              <article class="book-card reveal visible">
                <a href="../{other["slug"]}/" aria-label="Find {other["title"]} details">
                  <div class="book-cover {other["coverClass"]}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.7) 100%), url('{other["coverImage"]}');">
                    <span class="cover-kicker">{other["kicker"].upper()}</span>
                    <span class="cover-title">{other["title"]}</span>
                    <span class="cover-author">PARVIND KUMAR</span>
                  </div>
                </a>
                <div class="book-meta">
                  <h3>{other["title"]}</h3>
                  <p>{other["description"]}</p>
                  <a class="book-link" href="../{other["slug"]}/">Read Details &rarr;</a>
                </div>
              </article>
            '''

        # Render Google Play Button if link exists
        google_play_btn = ""
        if book.get("google_play"):
            google_play_btn = f'<a class="button buy-btn play-btn" href="{book["google_play"]}" target="_blank" rel="noopener">Google Play Books <span>↗</span></a>'

        # Render Amazon Button if link exists
        amazon_btn = ""
        if book.get("amazon"):
            amazon_btn = f'<a class="button button-dark buy-btn amazon-btn" href="{book["amazon"]}" target="_blank" rel="noopener">Buy on Amazon <span>↗</span></a>'

        primary_buy_link = book.get("amazon") or book.get("google_play") or book.get("goodreads")

        rating_val = "5" if "11 Shades" in title or "Talaq" in title or "Kamathipura" in title else "4.8"

        # Format and write template
        rendered_html = HTML_TEMPLATE.format(
            lang_code=trans["lang"],
            title=title,
            subtitle=subtitle,
            slug=slug,
            kicker=kicker,
            kicker_upper=kicker_upper,
            description=book["description"],
            cover_image=book["coverImage"],
            cover_class=book["coverClass"],
            isbn=book["isbn"],
            publication_date=book["publication_date"],
            publication_date_str=publication_date_str,
            language=book["language"],
            pages=book["pages"],
            genre=genre_name,
            publisher=book["publisher"],
            amazon=book["amazon"],
            amazon_btn=amazon_btn,
            primary_buy_link=primary_buy_link,
            google_play_btn=google_play_btn,
            goodreads=book["goodreads"],
            long_description_html=long_description_html,
            toc_html=toc_html,
            reviews_html=reviews_html,
            unavailable_badge=unavailable_badge,
            related_books_html=related_books_html,
            rating_value=rating_val,
            
            # Translated fields
            t_author_by=trans["author_by"],
            t_author_name=trans["author_name"],
            t_book_info=trans["book_info"],
            t_isbn=trans["isbn"],
            t_published=trans["published"],
            t_pages=trans["pages"],
            t_language=trans["language"],
            t_formats=trans["formats"],
            t_genre=trans["genre"],
            t_rating_label=trans["rating_label"],
            t_toc_title=trans["toc_title"],
            t_reviews_title=trans["reviews_title"],
            t_back_to_library=trans["back_to_library"],
            t_other_books=trans["other_books"],
            t_explore_more=trans["explore_more"],
            t_discover_other=trans["discover_other"],
            formats=book["formats"]
        )

        out_path = os.path.join(book_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"Generated {out_path}")

    # Now, let's write out the new js/script.js automatically to sync databases
    # Create the JS array content
    js_books = []
    for book in BOOKS:
        js_books.append({
            "slug": book["slug"],
            "title": book["title"],
            "category": book["category"],
            "kicker": book["kicker"].upper(),
            "description": book["description"],
            "amazon": book["amazon"],
            "coverClass": book["coverClass"],
            "coverImage": book["coverImage"],
            "unavailable": book.get("unavailable", False)
        })

    # Prepare JS content
    js_content = f"""const books = {json.dumps(js_books, indent=2)};

const bookGrid = document.getElementById("bookGrid");

function renderBooks(filter = "all") {{
  const visible = books.filter(book => filter === "all" || book.category.includes(filter));

  bookGrid.innerHTML = visible.map(book => `
    <article class="book-card reveal">
      <a href="books/${{book.slug}}/" aria-label="Read details of ${{escapeHtml(book.title)}}">
        <div class="book-cover ${{book.coverClass}}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.7) 100%), url('${{book.coverImage}}');">
          <span class="cover-kicker">${{escapeHtml(book.kicker)}}</span>
          <span class="cover-title">${{escapeHtml(book.title)}}</span>
          <span class="cover-author">PARVIND KUMAR</span>
        </div>
      </a>
      <div class="book-meta">
        <h3>${{escapeHtml(book.title)}}</h3>
        <p>${{escapeHtml(book.description)}}${{book.unavailable ? ' <span class="status">Currently unavailable</span>' : ''}}</p>
        <a class="book-link" href="books/${{book.slug}}/">Read Book Details &rarr;</a>
      </div>
    </article>
  `).join("");

  observeReveals();
}}

document.querySelectorAll(".filter").forEach(button => {{
  button.addEventListener("click", () => {{
    document.querySelectorAll(".filter").forEach(b => b.classList.remove("active"));
    button.classList.add("active");
    renderBooks(button.dataset.filter);
  }});
}});

function escapeHtml(value) {{
  return value.replace(/[&<>"']/g, char => ({{
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
  }}[char]));
}}

const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.getElementById("site-nav");

menuToggle.addEventListener("click", () => {{
  const open = siteNav.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", open ? "true" : "false");
}});

siteNav.querySelectorAll("a").forEach(link => {{
  link.addEventListener("click", () => {{
    siteNav.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
  }});
}});

function observeReveals() {{
  const items = document.querySelectorAll(".reveal:not(.observed)");
  if (!("IntersectionObserver" in window)) {{
    items.forEach(el => el.classList.add("visible"));
    return;
  }}
  const observer = new IntersectionObserver(entries => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add("visible");
        entry.target.classList.add("observed");
        observer.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.08 }});
  items.forEach(item => observer.observe(item));
}}

document.getElementById("year").textContent = new Date().getFullYear();

const coverClasses = {{
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
}};

const style = document.createElement("style");
let css = "";
Object.entries(coverClasses).forEach(([selector, [bg, fg]]) => {{
  css += `${{selector}}{{background-color:${{bg}};color:#fffdf7;}}`;
}});
style.textContent = css;
document.head.appendChild(style);

renderBooks();
observeReveals();
"""

    js_path = os.path.join(BASE_DIR, "js", "script.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Updated {js_path}")

if __name__ == "__main__":
    generate_pages()
