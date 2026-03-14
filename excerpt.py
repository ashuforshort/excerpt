import pandas as pd
import streamlit as st

st.set_page_config(page_title="EXCERPT", page_icon=":material/genetics:", layout="wide", initial_sidebar_state=None,
	menu_items={
	'About': 'GitHub: https://github.com/ashuforshort/excerpt',
		'Get help': 'mailto:admin@ashuforshort.xyz',
		'Report a bug': 'mailto:admin@ashuforshort.xyz'
	}
)

st.title(body=":material/genetics: EXCERPT: Your Notion, Gamified.", anchor=False, help=None, width="stretch", text_alignment="left")
st.subheader(body="", anchor=None, help=None, divider="violet", width="stretch", text_alignment="left")

st.write("Most people use [Notion](https://notion.so) to store information. But storing information isn't the same as learning it. **EXCERPT** is a lightweight Streamlit app designed to bridge that gap.", unsafe_allow_html=False)
st.write("Whether you are a **_\"Notion-head\"_** with a hundred databases or a student looking for a better way to study, **EXCERPT** turns your static notes into a dynamic, interactive quiz — **for free**.", unsafe_allow_html=False)

with st.expander(label="Who is **EXCERPT** for?", expanded=False, icon=":material/cognition_2:", width="stretch"):
	st.write("""
		You don't need to be a tech wizard to use **EXCERPT**. If you can type in a table, you can create a curriculum.
		* **Language Learners (The Duolingo Duo):** Using Duolingo? When you come across a new word, phrase, or tricky conjugation, drop it into your Notion DB. Use **EXCERPT** to randomly test your recall of those specific phrases later that day.
		* **IELTS & TOEFL Aspirants:** Put the "Word" in one column and the "Definition/Synonym" in another. Master vocabulary while waiting for your cab.
		* **Corporate Professionals:** Finally memorize those endless company acronyms. Hide the "Meaning" column and test yourself between meetings.
		* **Students:** Perfect for Geography (Country vs. Capital), Science (Element vs. Atomic Weight), or History (Event vs. Date).
		* **Trivia Buffs:** Build your own database of fun facts while listening to podcasts or traveling.
		""", unsafe_allow_html=False)

with st.expander(label="Why use **EXCERPT**?", expanded=False, icon=":material/question_mark:", width="stretch"):
	st.write("""
		* **Active Recall:** Stop mindlessly scrolling your notes. Forcing your brain to "guess" is the fastest way to commit info to long-term memory.
		* **Seamless Integration:** Update your database on the Notion mobile app while you're walking or traveling; **EXCERPT** will reflect those changes instantly.
		* **Privacy & Cost:** It's your data and your API key. No monthly subscriptions, no "pro" tiers — just you and your brain.
		* **Pro Tip:** Keep your Notion app open on your phone to add new rows as you learn them, then use **EXCERPT** on your laptop to drill those same rows later that evening!
		""", unsafe_allow_html=False)

with st.expander(label="The **Make-Your-Own-Quiz (MYOQ)** Method", expanded=False, icon=":material/flaky:", width="stretch"):
	st.write("""
		**EXCERPT** connects to your **Notion Workspace** via an API key and lets you generate **flashcards** from your **Notion Databases**.
		1. **Connect:** Input your Notion API Key.
		2. **Select:** Pick any database from your workspace.
		3. **Customise:** Choose which columns to **Show** (your clues) and which to **Hide** (your answers).
		4. **Play:** The app pulls a random row. Look at the clues, make your guess, and reveal the answer!
		""", unsafe_allow_html=False)

with st.expander(label="**Getting Started:** your 3-minute setup", expanded=False, icon=":material/joystick:", width="stretch"):
	gettingStartedColumn, gifColumn = st.columns([0.6,0.4], gap="small", vertical_alignment="center", border=False, width="stretch")
	with gettingStartedColumn:
		st.write("""
			To use **EXCERPT**, you just need to give the app a "secret handshake" with your Notion account. Here's how to set it up for the first time:
			1. Create your "Secret Key" (Notion Integration)
				* Go to the [Notion Developers](https://www.notion.so/profile/integrations) page and click the **"+ Create a new integration"** button.
				* Give it a name (like "Excerpt App"), keep the **Type** as **Internal**, and hit **Create**.
				* Under **Associated workspace**, select the **Notion Workspace** you want to connect (that has your databases).
				* Once the integration is created, click on **Configure integration settings** when the pop-up appears.
				* Restrict the integration's capabilities to **Read content** only. This ensures the app can only "see" your data, not modify it.	
				* Under **"Internal integration secret",** click **Show** and then **Copy**. This is your Notion API Key — keep it safe!
			2. Edit Access
				* To further restrict the access only to selective pages, switch to **Access** tab, and click on **Edit access**.
				* Check / Uncheck the top-level pages under **Workspace** and/or **Private**.
			""", unsafe_allow_html=False)
	with gifColumn:
		st.image("./resources/GIFs/Notion-Integration.gif", caption="Notion Integration Setup", width="content", clamp=False, channels="RGB", output_format="auto")
	
with st.expander(label="A Note on **Privacy**", expanded=False, icon=":material/security:", width="stretch"):
	st.write("Your API Key is only used to fetch your database content. **EXCERPT** does not store your key or your data on any external servers — everything stays between you and your **Notion Workspace**.", unsafe_allow_html=False)

with st.expander(label="**Best Practices**", expanded=False, icon=":material/done_outline:", width="stretch"):
	exampleSetups = pd.DataFrame(
		{
			"Clue Column (SHOW)": ["Shortened Words — \"FBI\", \"ISRO\", \"URL\", etc.", "Buzzwords — \"circling back\", \"low hanging fruit\", \"the elephant in the room\", etc.", "Algorithm Types — \"Binary Tree\", \"Linked List\", \"Stacks\", etc.", "Country Names — \"Argentina\", \"Maldives\", \"Papua New Guinea\", etc.", "Sentences — \"¿Cómo te llamas?\", \"Terve! Minä olen Ash.\", \"je t\'aime\", etc."],
			"Answer Column (HIDE)": ["Full Form", "Meaning", "Description", "Capital City", "Translation"]
		},
		index=["Acronyms", "Corporate Jargons", "Data Structures", "Geography", "Language Learning"]
	)
	bestPracticesColumn, gifColumn = st.columns([0.6,0.4], gap="small", vertical_alignment="center", border=False, width="stretch")
	with bestPracticesColumn:
		st.write("""
			To make the app truly effective, you need to build your **Notion Databases** for "optimal guessing". If a database is messy, the quiz won't feel right.
			\n Not every **Notion Database** is a good quiz. To get the most out of **EXCERPT**, follow these simple structural tips:
			\n 1. **The "One-to-One" Rule:** For the best experience, ensure each row has a clear "Clue" column and a clear "Answer" column.
			\n\t * _Bad:_ Putting 5 different definitions in one cell.
			\n\t * _Good:_ Creating 5 separate rows for 5 different words.
			\n 2. **Use Descriptive Headers:** Name your columns clearly (e.g., "Term," "Definition," "Example Sentence," "Context"). This makes it easier to toggle them.
			\n 3. **Keep it Mobile-Friendly:** Since you'll be adding entries while walking or commuting, use **Simple Text** or **Select** properties. Avoid burying your "Answers" inside page icons; **EXCERPT** works best with data visible in the table view.
		   \n Example setups to try:
			""", unsafe_allow_html=False)
		st.table(exampleSetups)
	with gifColumn:
		st.image("./resources/GIFs/Notion-DB-Best-Practices.gif", caption="Notion Database Best Practices", width="content", clamp=False, channels="RGB", output_format="auto")

with st.expander(label="**Troubleshooting:** Having Trouble?", expanded=False, icon=":material/handyman:", width="stretch"):
	st.write("""
		If things aren't loading quite right, don't worry! Usually, it's just a quick setting in **Notion** that needs a tweak. Most issues with the **Notion API** usually boil down to permissions or "sharing" settings.
		\n 1. **"My database isn't appearing in the list!"** — This is the most common issue. Even if you've created an API Key, you must explicitly grant access to each database you want to use.
		\n\t * **The Fix:** Go to the [Notion Developers](https://www.notion.so/profile/integrations) page and open the **Notion Integration** you created. Switch to **Access** tab → click on **Edit access** → check / uncheck the top-level pages under **Workspace** and / or **Private** (that has your databases).
		\n 2. **"The app says 'No Data Found'"** — **EXCERPT** needs a table to read. If your database is empty or only contains "Empty Pages", there's nothing for the app to pick!
		\n\t * **The Fix:** Make sure you have at least 1-2 rows with text in the columns you want to hide / show.
		\n 3. **"I'm getting a 'Connection Error'"** — Check your internet connection and ensure your **API Key (Internal Integration Secret)** was copied correctly.
		\n\t * **The Fix:** Make sure there are no accidental spaces at the beginning or end of the key when you paste it into the app.
		\n 4. **"Some columns are missing"** — **EXCERPT** works best with **Text** property.
		\n\t * Some complex properties (like 'Select,' 'Multi-select,' 'Number,' and 'Date') can be tricky for the API to read instantly. Stick to simple text columns for the best **"Make-Your-Own-Quiz (MYOQ)"** experience.
		\n **Still stuck?** If you've checked the connections and it's still acting up, try refreshing the Streamlit page. This will reset the connection and fetch a fresh list of your databases.
		""", unsafe_allow_html=False)
	
with st.expander(label="**Mission Statement**", expanded=False, icon=":material/self_improvement:", width="stretch"):
	st.write("""
		Why I built **EXCERPT**?
		\n I'm a firm believer that knowledge shouldn't be locked behind a paywall. We spend so much of our lives "collecting" information — saving bookmarks, clipping articles, and typing notes into **Notion**.
		\n But most of that data just sits there, gathering digital dust. I wanted a way to turn those idle moments — like waiting for a bus or sipping a coffee — into active learning sessions.
		\n I built **EXCERPT** because I needed a tool that was:
		\n * **Minimalist:** No clutter, just the quiz.
		\n * **Flexible:** It adapts to your notes, not a pre-set curriculum.
		\n * **Free:** You shouldn't have to pay a subscription to quiz yourself on your own data.
		\n **EXCERPT** is my contribution to the **_\"Notion-head\"_** community and lifelong learners everywhere. It's designed to help you stop just storing information and start owning it.
		""", unsafe_allow_html=False)
	
with st.expander(label="**Join the Journey**", expanded=False, icon=":material/handshake:", width="stretch"):
	st.write("""
		Created with :purple_heart: using [Streamlit](https://streamlit.io/) and the [Notion API](https://developers.notion.com/reference/intro).
		\n This app is a labor of love and is constantly evolving. If you have a feature request, found a bug, or just want to share how you're using **EXCERPT** to ace your exams or level up your career, I'd love to hear from you!
		""", unsafe_allow_html=False)
	github, linkedin, twitter, portfolio = st.columns(spec=4, gap="small", vertical_alignment="center", border=False, width="stretch")
	with github:
		st.link_button(label="GitHub", url="https://github.com/ashuforshort", help=None, type="primary", icon=None, icon_position="left", disabled=False, width="stretch", shortcut="G")
	with linkedin:
		st.link_button(label="LinkedIn", url="https://linkedin.com/in/ashuforshort", help=None, type="primary", icon=None, icon_position="left", disabled=False, width="stretch", shortcut="L")
	with twitter:
		st.link_button(label="Twitter / X", url="https://x.com/ashuforshort", help=None, type="primary", icon=None, icon_position="left", disabled=False, width="stretch", shortcut="X")
	with portfolio:
		st.link_button(label="Portfolio", url="https://ashuforshort.xyz", help=None, type="primary", icon=None, icon_position="left", disabled=False, width="stretch", shortcut="P")

with st.container(border=True, width="content", height="stretch", horizontal_alignment="center", gap="small"):
	st.page_link(page="pages/execution.py", label="Let's Jump In!", icon=":material/directions_run:", help=None, disabled=False, width="content", query_params=None)