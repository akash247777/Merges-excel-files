# Merges-excel-files
Streamlit Excel Merger App
This project is a Streamlit web application that allows users to upload multiple Excel files and merge them into a single Excel file. The application automatically detects common columns across files and merges them accordingly, or concatenates the files if no common columns are found. Once merged, users can preview the data and download the final Excel file.

Key Features:
Multiple File Upload: Users can upload multiple Excel files simultaneously.
Automatic Merging: The app intelligently merges files based on common columns. If no common columns are found, files are concatenated.
File Preview: Displays the merged data directly in the app for quick review.
Download Option: Provides a download button to export the merged file as an Excel sheet.
Simple and Interactive Interface: Built using Streamlit for ease of use with minimal setup.
How to Use:
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/excel-merger-app.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:
bash
Copy code
streamlit run merge_excel.py
Upload Excel files, view the merged result, and download the final file.
Technologies Used:
Streamlit: For building the interactive web application.
Pandas: For handling data manipulation and merging of Excel files.
OpenPyXL: For reading and writing Excel files.
Future Improvements:
Add support for CSV files and other file formats.
Allow users to manually select columns to merge on.
Add more advanced merging options like inner/outer joins on multiple columns.
