# Signs of AI writing — reference list

Sources: [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), plus general observations on LLM output patterns (ChatGPT/Claude/etc). Wikipedia-specific stuff (broken wikitext, citation bugs, category errors) is left out — only what applies to general German/English prose is kept.

## 1. Em dashes (hard ban, see SKILL.md)

AI output uses em dashes far more than typical human writing, usually with spaces around them, in places a human would use a comma, colon, parenthesis, or just a period. Zero tolerance, no "used sparingly" exception.

## 2. Overused vocabulary

Flag these when they show up as filler rather than the one precise word for the job. Frequency is the tell: one of these in a whole document is fine, three in a paragraph is not.

**English:** delve, tapestry, testament, pivotal, underscore(s), landscape (metaphorical — "the ever-evolving landscape of X"), foster(ing), boast(s), vibrant, crucial, meticulous, intricate, interplay, garner(ed), bolstered, enduring, showcasing, emphasizing/highlighting (as filler, not as an actual claim), enhance, align with, robust, seamless, navigate (metaphorical), realm, plethora, groundbreaking, renowned, nestled, rich (as in "rich history/culture"), journey (metaphorical for anything non-literal), game-changer/game-changing.

**Phrases:** "unlock the potential of", "unleash the power of", "embark on", "at the forefront of", "harness the power of", "pave the way for", "bridging the gap between", "in the realm of".

**German:** maßgeblich, vielfältig, spannende Reise, im Bereich von, wegweisend, ganzheitlich (als Füllwort), auf Augenhöhe (als Buzzword ohne Substanz), Landschaft (metaphorisch — "die sich wandelnde Landschaft von"), bahnbrechend.

## 3. Copula avoidance

Replacing a plain "is/are" ("ist/sind") with a fancier verb when the plain version is clearer:

- "X serves as the foundation" → just say "X is the foundation"
- "X stands as a testament to Y" → "X shows Y" or cut it
- "Das Unternehmen fungiert als Vermittler" → "Das Unternehmen vermittelt"

Not every "represents/marks/features" is wrong — only when it's dressing up a plain "is" for no reason.

## 4. Negative parallelism / rule of three

- "It's not just X, it's Y" / "Nicht nur X, sondern auch Y" — fine occasionally when there's a real contrast, a tell when it's reflexive.
- Mechanical triplets: "innovative, transformative, and groundbreaking" — three adjectives doing the job of zero specific ones.

## 5. Formulaic transitions used as filler

Moreover, furthermore, additionally, in conclusion, "it's important to note that", "it's worth noting that" — außerdem, darüber hinaus, "es ist wichtig zu betonen, dass", "zusammenfassend lässt sich sagen". Not banned outright, but if a sentence works with the transition deleted, delete it.

## 6. Vague attribution

"Industry reports suggest", "some critics argue", "observers have noted" — "Experten zufolge", "manche Kritiker argumentieren", used without a real, checkable source behind them. Either name the actual source or cut the claim.

## 7. Promotional/brochure tone in non-marketing text

boasts, showcases, exemplifies, "commitment to", "diverse array" — fine in actual ad copy, out of place in an email, a report, or a personal message.

## 8. Structural tells

- Generic "Fazit"/conclusion paragraph that just restates the intro without adding anything new.
- False-balance "on the other hand" padding when there's no real tension to weigh.
- Bolding half the nouns in a paragraph for emphasis.
- Title-casing headings when that's not the house style.

---

## Before / after examples

**DE, business:**
- Vorher: "Unser Catering-Service bietet eine vielfältige Auswahl an Speisen und fungiert als verlässlicher Partner für Ihre Veranstaltung — von der Planung bis zur Umsetzung."
- Nachher: "Unser Catering deckt alles ab, von der Planung bis zur Umsetzung, mit einer Auswahl, die zu Ihrer Veranstaltung passt."

**DE, locker:**
- Vorher: "Das war echt eine spannende Reise — von der ersten Idee bis zum fertigen Produkt war es ein ganzheitlicher Prozess, der uns viel gelehrt hat."
- Nachher: "War ne coole Zeit. Von der ersten Idee bis zum fertigen Ding haben wir eine Menge gelernt."

**EN, business:**
- Before: "Our platform serves as a testament to innovation, boasting a robust set of features that pave the way for seamless collaboration — delivering value at every step of the journey."
- After: "Our platform has a solid feature set built for real collaboration, and it delivers value at every step."

**EN, casual:**
- Before: "Honestly, this trip was a game-changer for me — it really underscored how important it is to embark on new adventures and step outside your comfort zone."
- After: "Honestly, this trip changed a lot for me. It showed me how much I need to just try new things and get out of my comfort zone."
