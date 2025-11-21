import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore", message="missing ScriptRunContext")


st.title("Aircraft Fault Log Uploader & Viewer")

uploaded_file = st.sidebar.file_uploader("Upload fault log", type=["csv", "xlsx", "txt"])

if uploaded_file:
    try:
        # Handle CSV files
        if uploaded_file.name.endswith('.csv'):
            log_df = pd.read_csv(uploaded_file)
            st.success(f"Loaded {uploaded_file.name} as CSV!")

        # Handle Excel files
        elif uploaded_file.name.endswith('.xlsx'):
            log_df = pd.read_excel(uploaded_file)
            st.success(f"Loaded {uploaded_file.name} as Excel!")

        # Handle TXT files (default: tab or comma separated, can be refined)
        elif uploaded_file.name.endswith('.txt'):
            # Try tab first, fallback to comma
            try:
                log_df = pd.read_csv(uploaded_file, delimiter='\t')
            except Exception:
                log_df = pd.read_csv(uploaded_file, delimiter=',')
            st.success(f"Loaded {uploaded_file.name} as TXT!")

        # Display dataframe
        st.subheader("Preview of Uploaded Fault Log:")
        st.dataframe(log_df)

        st.write(f"Rows: {log_df.shape[0]}, Columns: {log_df.shape[1]}")

    except Exception as e:
        st.error(f"Could not load file: {e}")

else:
    st.info("Please upload a fault log (.csv, .xlsx, or .txt file) to view it here.")

