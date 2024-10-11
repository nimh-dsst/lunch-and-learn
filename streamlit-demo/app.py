import streamlit as st
from dandi.dandiapi import DandiAPIClient
from pydantic_core import ValidationError
import pandas as pd

st.title("Dandi Dataset API Explorer")
st.write(
    "This app uses the DANDI API to get information on dandisets :brain: :tophat:"
)
st.header("Dandi")


@st.cache_data
def parse_dandi() -> dict:
    dandiset_counter: int = 0
    validation_errors: int = 0
    all_keywords: list[str] = []
    with DandiAPIClient.for_dandi_instance("dandi") as client:
        dandisets = client.get_dandisets()
        for dandiset in dandisets:
            dandiset_counter += 1
            try:
                metadata = dandiset.get_metadata()
            except ValidationError:
                validation_errors += 1
                continue
            dandiset_keywords: list[str] | None = metadata.keywords
            if dandiset_keywords:
                all_keywords.extend(metadata.keywords)
            else:
                pass
    lower_keywords: list[str] = []
    for raw_keyword in all_keywords:
        if ", " in raw_keyword:
            split_keywords: list[str] = raw_keyword.split(", ")
            lower_keywords.extend([x.lower() for x in split_keywords])
        else:
            lower_keywords.append(raw_keyword.lower())

    df = pd.DataFrame({"keywords": lower_keywords})
    keyword_counts = df["keywords"].value_counts().reset_index()
    dandi_data: dict = {
        "dandiset_counter": dandiset_counter,
        "validation_errors": validation_errors,
        "all_keywords": all_keywords,
        "keyword_df": df,
        "keyword_counts": keyword_counts,
    }
    return dandi_data


dd: dict = parse_dandi()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Number of Dandisets via API", dd["dandiset_counter"])
with col2:
    st.metric("Validation Errors", dd["validation_errors"])
with col3:
    st.metric("Number of Dandiset Keywords", len(dd["all_keywords"]))


st.dataframe(dd["keyword_counts"])
