import os
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = "data/interviews.csv"

def save_interview(candidate,email,role,experience,score,recommendation):

    row = {

        "Candidate":candidate,

        "Email":email,

        "Role":role,

        "Experience":experience,

        "Score":score,

        "Recommendation":recommendation,

        "Date":pd.Timestamp.now()

    }

    if os.path.exists(DATA_FILE):

        df = pd.read_csv(DATA_FILE)

    else:

        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        df = pd.DataFrame(columns=row.keys())

    df = pd.concat([df,pd.DataFrame([row])],ignore_index=True)

    df = df.drop_duplicates(
        subset=[
            "Candidate",
            "Email",
            "Role",
            "Experience",
            "Score",
            "Recommendation",
            "Date"
        ],
        keep="first"
    )

    df.to_csv(DATA_FILE,index=False)

def show_dashboard():

    st.title("📊 Recruiter Dashboard")

    if not os.path.exists(DATA_FILE):

        st.warning("No interviews found.")

        return

    df = pd.read_csv(DATA_FILE)

    search = st.text_input("Search Candidate")

    if search:

        df = df[df["Candidate"].str.contains(search,case=False)]

    role = st.selectbox(

        "Filter by Role",

        ["All"]+sorted(df["Role"].unique().tolist())

    )

    if role!="All":

        df=df[df["Role"]==role]

    df = df.reset_index(drop=True)
    df["__delete_key"] = df.index.astype(str) + " | " + df["Candidate"] + " | " + df["Date"].astype(str)

    st.dataframe(df.drop(columns=["__delete_key"]), use_container_width=True)

    st.metric("Total Interviews",len(df))

    st.metric("Average Score",round(df["Score"].mean(),2))

    st.markdown("---")
    st.subheader("Delete interview records")
    st.write("Select one or more records below to remove them permanently from the dashboard.")

    delete_options = df["__delete_key"].tolist()
    selected_to_delete = st.multiselect(
        "Select records to delete",
        options=delete_options,
        help="Choose one or more interview records to remove permanently."
    )

    if st.button("Delete selected records"):
        if selected_to_delete:
            keep_mask = ~df["__delete_key"].isin(selected_to_delete)
            df = df.loc[keep_mask].drop(columns=["__delete_key"])
            df.to_csv(DATA_FILE, index=False)
            st.success(f"Deleted {len(selected_to_delete)} record(s).")
            st.rerun()
        else:
            st.warning("Please select at least one record to delete.")

    fig=px.bar(

        df,

        x="Candidate",

        y="Score",

        color="Recommendation"

    )

    st.plotly_chart(fig,use_container_width=True)

    fig2=px.pie(

        df,

        names="Recommendation"

    )

    st.plotly_chart(fig2,use_container_width=True)