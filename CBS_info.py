import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd
import requests

# Level1
url = 'https://apis.cbs.gov.il/series/catalog/level?id=1&format=xml&download=false'
# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    # Extract the data you need from the XML and store it in a list of dictionaries
    data = []
    for level in root.findall(".//Level"):
        # Extract relevant data from each item and store it in a dictionary
        item_data = {
            "path": " ".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df1 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    choice1 = st.selectbox('Level 1 - Select area of interest', df1['name'])
    path1 = (df1['path'][df1['name'].tolist().index(choice1)])
    st.write(path1)
else:
    st.write("Failed to retrieve data. Error:", response.status_code)

# Level2
url = 'https://apis.cbs.gov.il/series/catalog/level?id=2&subject=' + path1 + '&format=xml&download=false'
# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    # Extract the data you need from the XML and store it in a list of dictionaries
    data = []
    for level in root.findall(".//Level"):
        # Extract relevant data from each item and store it in a dictionary
        item_data = {
            "path": " ".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df2 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    choice2 = st.selectbox('Level 2 - Select area of interest', df2['name'])
    path2 = (df2['path'][df2['name'].tolist().index(choice2)])
    st.write(path2[2])

# Level3
url = 'https://apis.cbs.gov.il/series/catalog/path?id=' + path2 + '&format=xml&download=false'
# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    # Extract the data you need from the XML and store it in a list of dictionaries
    data = []
    for level in root.findall(".//Level"):
        # Extract relevant data from each item and store it in a dictionary
        item_data = {
            "path": " ".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df3 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    choice3 = st.selectbox('Level 3 - Select area of interest', df3['name'])
    path3 = (df3['path'][df3['name'].tolist().index(choice3)])
    st.write(path3[2])
