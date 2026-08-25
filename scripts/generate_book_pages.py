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
        "google_play": "https://play.google.com/store/search?q=Parvind+Kumar+Crime+Suspense+Stories&c=books",
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
        "google_play": "https://play.google.com/store/search?q=The+Complete+Guide+to+Lo+Shu+Grid+Numerology+Parvind+Kumar&c=books",
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
        "google_play": "https://play.google.com/store/search?q=Before+we+said+goodbye+Parvind+Kumar&c=books",
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
        "google_play": "https://play.google.com/store/search?q=The+Vintage+Between+Us+A+Tuscan+Vineyard+Romance+Parvind+Kumar&c=books",
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
        "google_play": "https://play.google.com/store/search?q=Complete+Guide+Building+Happy+Marriage+Lasting+Love+Parvind+Kumar&c=books",
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
        "google_play": "https://play.google.com/store/search?q=Complete+Guide+to+Mindfulness+Meditation+Parvind+Kumar&c=books",
        "goodreads": "https://www.goodreads.com/search?q=Complete+Guide+to+Mindfulness+Meditation+Parvind+Kumar",
        "formats": "Paperback, eBook (Kindle)",
        "description": "A practical journey into mindfulness, meditation, attention and everyday calm.",
        "unavailable": True,
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
        "google_play": "https://play.google.com/store/search?q=What+Happens+After+Death+Parvind+Kumar&c=books",
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
        "google_play": "https://play.google.com/store/search?q=Talaq+Se+Pehle+Parvind+Kumar&c=books",
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
              "urlTemplate": "{amazon}",
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
          <a class="button button-dark buy-btn amazon-btn" href="{amazon}" target="_blank" rel="noopener">Buy on Amazon <span>↗</span></a>
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
  ".cover-fourteen": ["#743326", "#fbe8e4"]
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
