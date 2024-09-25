import streamlit as st
import pandas as pd

# Streamlit app title
st.title("Merge Multiple Excel Files")

# File uploader to upload multiple Excel files
uploaded_files = st.file_uploader("Upload Excel files", type=["xlsx"], accept_multiple_files=True)

if uploaded_files:
    # Initialize an empty list to hold DataFrames
    dfs = []

    # Loop through uploaded files and read them into DataFrames
    for file in uploaded_files:
        df = pd.read_excel(file)
        dfs.append(df)

    # Find common columns among the uploaded files
    common_columns = set(dfs[0].columns)
    for df in dfs[1:]:
        common_columns.intersection_update(df.columns)

    # If common columns exist, merge on them, otherwise merge without a key
    if common_columns:
        common_column = list(common_columns)[0]  # Choose one common column for merging
        st.write(f"Merging on common column: {common_column}")
        merged_df = pd.merge(dfs[0], dfs[1], on=common_column, how='outer')

        for i in range(2, len(dfs)):
            merged_df = pd.merge(merged_df, dfs[i], on=common_column, how='outer')
    else:
        st.write("No common columns found, concatenating the files.")
        merged_df = pd.concat(dfs, axis=1)

    # Display merged DataFrame in Streamlit
    st.write("Merged Data")
    st.dataframe(merged_df)

    # Option to download the merged Excel file
    def convert_df_to_excel(df):
        # Convert the DataFrame to Excel format in memory
        from io import BytesIO
        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        return output.getvalue()

    merged_excel = convert_df_to_excel(merged_df)

    # Provide a download button to download the merged Excel file
    st.download_button(
        label="Download Merged Excel",
        data=merged_excel,
        file_name="merged_file.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
