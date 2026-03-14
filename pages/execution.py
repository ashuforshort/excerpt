import random
import requests
import streamlit as st

if 'reveal' not in st.session_state:
    st.session_state.reveal = False

if 'randomRow' not in st.session_state:
    st.session_state.randomRow = None

def setReveal(bool):
    st.session_state.reveal = bool

@st.cache_data(ttl=300)
def getDBList(internalIntegrationSecret):
    dbResponse = requests.post("https://api.notion.com/v1/search", headers={"Authorization": f"Bearer {internalIntegrationSecret}", "Content-Type": "application/json", "Notion-Version": "2025-09-03"}, json={"filter":{"value":"data_source","property":"object"},"sort": {"direction": "ascending","timestamp": "last_edited_time"}}, verify=True)
    if dbResponse.json():
        dbList = {}
        for db in dbResponse.json()['results']:
            dbList[db['title'][0]['plain_text']] = db['id']
        return dbList
    else:
        return []

@st.cache_data(ttl=300)
def getDataSourceResponse(dataSourceID: str):
    dataSourceResponse = requests.post("https://api.notion.com/v1/data_sources/"+dataSourceID+"/query", headers={"Authorization": f"Bearer {internalIntegrationSecret}", "Content-Type": "application/json", "Notion-Version": "2025-09-03"}, verify=True)
    st.session_state.row = dataSourceResponse.json()['results'][random.randint(0,len(dataSourceResponse.json()['results']) - 1)]
    return dataSourceResponse

st.set_page_config(page_title="EXCERPT", page_icon=":material/genetics:", layout="wide", initial_sidebar_state=None,
	menu_items={
	'About': 'GitHub: https://github.com/ashuforshort/excerpt',
		'Get help': 'mailto:admin@ashuforshort.xyz',
		'Report a bug': 'mailto:admin@ashuforshort.xyz'
	}
)

headerColumns = st.columns([3,1])

with headerColumns[0]:
    st.title(body=":material/genetics: EXCERPT: Your Notion, Gamified.", anchor=False, help=None, width="stretch", text_alignment="left")
with headerColumns[1]:
    with st.container(border=True, width="stretch", height="stretch", horizontal_alignment="center", vertical_alignment="center", gap="small"):
        st.page_link(page="excerpt.py",label="Go Back", icon=":material/first_page:", help=None, disabled=False, width="content", query_params=None)

st.subheader(body="", anchor=None, help=None, divider="violet", width="stretch", text_alignment="left")

secretColumn, dbColumn = st.columns(spec=2, gap="small", vertical_alignment="center", border=True, width="stretch")

with secretColumn:
    internalIntegrationSecret = st.text_input(label="Enter Notion Internal Integration Secret:", value="", max_chars=50, key="internalIntegrationSecret", type="password", help="Navigate to https://www.notion.so/profile/integrations", autocomplete=None, placeholder="Bearer Token", disabled=False, label_visibility="visible", icon=":material/key:", width="stretch")
with dbColumn:
    dbListPlaceholder = st.empty()
    dbListPlaceholder.selectbox(label="Databases accessible through this integration:", options=[], index=None, key="dbListPlaceholder", help=None, placeholder="Select your Notion Database", disabled=True, label_visibility="visible", accept_new_options=False, width="stretch")

if internalIntegrationSecret != "":
    dbList = getDBList(internalIntegrationSecret)
    selectedDB = dbListPlaceholder.selectbox(label="Databases accessible through this integration:", options=dbList.keys(), index=None, key="dbList", help="DB List in the Cache is refreshed every 5 minutes.", placeholder="Select your Notion Database", disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")
    if selectedDB:
        dataSourceResponse = getDataSourceResponse(dataSourceID=dbList[selectedDB])
        totalRows = len(dataSourceResponse.json()['results'])
        columnsList = list(dataSourceResponse.json()['results'][0]['properties'].keys())
        columnsList.sort()
        with st.container(border=True, width="stretch", height="stretch", horizontal_alignment="center", vertical_alignment="center", gap="small"):
            pillsSelection = st.pills(label="Select column(s) to mask (all columns are unmasked by default):", options=columnsList, selection_mode="multi", default=None, help=None, disabled=False, label_visibility="visible", width="stretch")
        leftButton, rightButton = st.columns(2)
        with leftButton:
            if st.button(label="Pick a Random Row", key="generateButton", help=None, type="primary", icon=":material/shuffle:", icon_position="left", disabled=False, width="stretch", shortcut="Tab"):
                st.session_state.randomRow = dataSourceResponse.json()['results'][random.randint(0,totalRows - 1)]
                st.session_state.reveal = False
        with rightButton:
            if st.button(label="Reveal / Hide", key="revealButton", help=None, type="primary", icon=":material/eye_tracking:", icon_position="left", disabled=False, width="stretch", shortcut="Space"):
                if st.session_state.randomRow == None:
                    st.toast(body="Generate data first!", icon=":material/error:", duration="short")
                else:
                    st.session_state.reveal = not st.session_state.reveal
        st.subheader(body="", anchor=None, help=None, divider="violet", width="stretch", text_alignment="center")
        if st.session_state.randomRow != None:
            attribute, tuple = st.columns(spec=[0.2,0.8], gap="small", vertical_alignment="center", border=False, width="stretch")
            for column in columnsList:
                if column in pillsSelection:
                    if st.session_state.reveal == False:
                        with attribute:
                            with st.container(border=True, key=column+"Atrribute", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                                st.subheader(body="**"+column+"**", anchor=None, help=None, divider=None, width="stretch", text_alignment="center")
                        with tuple:
                            with st.container(border=True, key=column+"Tuple", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                                st.subheader(body="XXXXXXXXXX", anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                    else:
                        with attribute:
                            with st.container(border=True, key=column+"Atrribute", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                                st.subheader(body="**"+column+"**", anchor=None, help=None, divider=None, width="stretch", text_alignment="center")
                        with tuple:
                            with st.container(border=True, key=column+"Tuple", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                                try:
                                    columnType = st.session_state.randomRow['properties'][column]['type']
                                    st.subheader(body=st.session_state.randomRow['properties'][column][columnType][0]['plain_text'], anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                                except KeyError:
                                    st.subheader(body="[Error]", anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                                    st.toast(body="This usually happens when the DB is switched. Please pick a random row for \""+column+"\".", icon=":material/error:", duration="short")
                                except IndexError:
                                    st.subheader(body="[Error]", anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                                    st.toast(body="Column \""+column+"\" seems to be empty. Can you please check in your Notion DB once?", icon=":material/error:", duration="short")
                else:
                    with attribute:
                        with st.container(border=True, key=column+"Atrribute", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                            st.subheader(body="**"+column+"**", anchor=None, help=None, divider=None, width="stretch", text_alignment="center")
                    with tuple:
                        with st.container(border=True, key=column+"Tuple", width="stretch", height="stretch", horizontal=True, horizontal_alignment="center", vertical_alignment="center", gap="small"):
                            try:
                                columnType = st.session_state.randomRow['properties'][column]['type']
                                st.subheader(body=st.session_state.randomRow['properties'][column][columnType][0]['plain_text'], anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                            except KeyError:
                                st.subheader(body="[Error]", anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                                st.toast(body="This usually happens when the DB is switched. Please pick a random row for \""+column+"\".", icon=":material/error:", duration="short")
                            except IndexError:
                                st.subheader(body="[Error]", anchor=None, help=None, divider=None, width="stretch", text_alignment="left")
                                st.toast(body="Column \""+column+"\" seems to be empty. Can you please check in your Notion DB once?", icon=":material/error:", duration="short")