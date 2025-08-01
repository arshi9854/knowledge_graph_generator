#Import necessary modules
import streamlit as st
import streamlit.components.v1 as components #For embedding custom HTML
from generate_knowledge_graph import generate_knowledge_graph

#Set up streamlit page configuration
st.set_page_config(
    page_icon=None,
    layout="wide", # use wide layout for better graph display
    initial_sidebar_state="auto",
    menu_items=None)

#Set teh title of the app
st.title("Knowledge Graph From Text")

#Sidebar section for user input method
st.sidebar.title("Input document")
input_method = st.sidebar.radio(
    "Choose an input method:",
    ["Upload txt", "Input text"],
    )

#Case 1 : User chooses to uplaod a .txt file
if input_method == "Uplaod txt":
    #File uplaoded widget in the sidebar
    uplaoded_file = st.sidebar.file_uplaoder(label="Upload file", type=["txt"])

    if uplaoded_file is not None:
        #Read the uplaoded file content and decode it as UTF-8 text
        text = uplaoded_file.read().decode("utf-8")

        #Button to generate the knowledge graph
        if st.sidebar.button("Generate knowledge Graph"):
            with st.spinner("Generating knowledge graph....."):
                #Call the funcion to generate the graph from the text
                net = generate_knowledge_graph(text)
                st.success("Knowledge graph generated successfully!!")

                #save the graph to an HTML file
                output_file = "knowledge_graph.html"
                net.save_graph(output_file)

                #Open the HTML file and display it whithin the streamlit app
                HtmlFile = open(output_file, 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=1000)

#case 2: User chooses to directly input text
else:
    #Text area for manual input
    text = st.sidebar.text_area("Input text", height=300)

    if text:
        #check if the text area is not empty
        if st.sidebar.button("Generate Knowledge Graph"):
            with st.spinner("Generating knowledge graph....."):
                #call the function to generate the graph from the input text
                net = generate_knowledge_graph(text)
                st.success("Knowledge graph generated successfully!!")

                #Save the graph to an HTML file
                output_file = "knowledge_graph.html"
                net.save_graph(output_file)

                #Open the HTML file and display it within the streamlit app
                HtmlFile = open(output_file, 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=1000)