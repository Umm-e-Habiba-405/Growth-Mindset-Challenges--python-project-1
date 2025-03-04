# import streamlit as st
# import pandas as pd 
# import os 
# from io import BytesIO



# st.set_page_config(page_title="Data Sweeper", layout='wide')
# st.title('Data Sweeper')
# st.write("Transform your file between CSV into Excel format with built_in data cleaning and visualization!")
# uploaded_files = st.file_uploader("Upload your files(CSV or Excel):",  type=["csv","xlsx"], accept_multiple_files= True)
# if uploaded_files:
#     for file in uploaded_files:
#         file_ext= os.path.splitext(file.name)[-1].lower()
#         if file_ext ==".csv":
#             df =pd.read_csv(file)
#         elif file_ext ==".xlsx":
#             df =pd.read_excel(file)
#         else: st.error("Unsupported file{file_ext}")
#         continue

#     st.write(f"**File Name:**{file.name}")
#     st.write(f"**File  Size:**{file.size/1024}")

#     st.write("Preview the Head of the Dataframe")
#     st.dataframe(df.head())


#     st.subheader("Data Cleaning option")
#     if st.checkbox(f"clean data for{file.name}"):
#           col1,col2=st.columns(2)

#     with col1:
#         if st.button(f"Remove Duplicate form {file.name}"):
#            df.drop_duplicates(inplace=True)
#            st.write("Duplicates Removed!")
#     with  col2:
#         if st.button(f"Fill Missing Values For {file.name}"):     
#             numeric_cols=df.select_dtypes(include=['numbers']).columns
#             df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
#             st.write("Missing Value have been filled!")



import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout='wide')
st.title('Data Sweeper')

st.write("Transform your CSV or Excel files with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")

        st.write("### Data Preview")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"Data Cleaning Options for {file.name}")
        
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing Values Filled!")
        st.subheader("Select Columns to convert")
        columns= st.multiselect(f"Choose column for{file.name}",df.columns,default=df.columns)
        df=df[columns]


        st.subheader("Data Visualization")
        if st.checkbox(f"show visualization for{file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])  


    st.subheader("Conversion Options")
    Conversion_type=st.radio(f"convert{file.name}to:",["CSV","Excel"],key=file.name)
    if st.button(f"convert {file.name}"):
        buffer = BytesIO() 
        if Conversion_type=="CSV":
            df.to_csv(buffer,index=False)
            file_name= file.name.replace(file_ext,".csv")
            mime_type="text/csv"
        elif Conversion_type=="Excel":
             df.to_excel(buffer,index=False)
             file_name= file.name.replace(file_ext,".xlsx")
             mime_type="application/vnd.openxmlformats-officedocuments.spreadsheetml.sheet"
             buffer.seek(0)


             st.download_button(
                 label=f"Download{file.name} as {Conversion_type}",
                 data=buffer,
                 file_name= file_name,
                 mime=mime_type

             )
st.success("All files processed!")

            
            

