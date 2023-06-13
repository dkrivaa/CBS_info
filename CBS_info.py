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
    df = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:

    choice1 = st.selectbox('select area of interest', df['name'])
    path1 = (df['path'][df['name'].tolist().index(choice1)])
    st.write(path1)
else:
    print("Failed to retrieve data. Error:", response.status_code)

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
    df = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    df['path'] = df['path']
    st.write(df.head())
