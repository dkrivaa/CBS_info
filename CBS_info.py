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
            "path": ",".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df2 = pd.DataFrame(data)
    dfi2 = df2.reset_index(drop=True)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    choice2 = st.selectbox('Level 2 - Select area of interest', df2['name'])
    path2 = (df2['path'][df2['name'].tolist().index(choice2)])
    st.write(path2)


# Level3
url = 'https://apis.cbs.gov.il/series/catalog/level?id=3&subject=' + path1 + '&format=xml&download=false'
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
            "path": ",".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df3 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    len2 = len(path2)
    dfi = df3.loc[df3['path'].str[:len2] == path2]
    dfi = dfi.reset_index(drop=True)
    choice3 = st.selectbox('Level 3 - Select area of interest', dfi['name'])
    path3 = (dfi['path'][dfi['name'].tolist().index(choice3)])
    st.write(path3)

# Level4
url = 'https://apis.cbs.gov.il/series/catalog/level?id=4&subject=' + path1 + '&format=xml&download=false'
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
            "path": ", ".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df4 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    len3 = len(path3)
    dfs = df4.loc[df4['path'].str[:len3] == path3]
    dfs = dfs.reset_index(drop=True)
    choice4 = st.selectbox('Level 4 - Select area of interest', dfs['name'])
    path4 = (dfs['path'][dfs['name'].tolist().index(choice4)])
    st.write(path4)

# Level5
url = 'https://apis.cbs.gov.il/series/catalog/level?id=4&subject=' + path1 + '&format=xml&download=false'
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
            "path": ", ".join([str(int_element.text) for int_element in level.findall("path/int")]),
            "name": level.find("name").text,
        }
        data.append(item_data)
    # Create a DataFrame from the list of dictionaries
    df5 = pd.DataFrame(data)
    # Now you can work with the DataFrame
    # For example, you can display the first few rows:
    choice5 = st.selectbox('Level 5 - Select area of interest', df5['name'])
    path5 = (df5['path'][df5['name'].tolist().index(choice5)])
    st.write(path5)
