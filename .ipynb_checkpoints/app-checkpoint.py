
# ============================================================
# NETFLIX CONTENT ANALYTICS DASHBOARD
# Built with Python, Pandas, Matplotlib, Seaborn and Streamlit
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Netflix Content Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------------------------
# 2. DASHBOARD STYLING
# ------------------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        h1 {
            color: #E50914;
        }

        [data-testid="stMetric"] {
            background-color: #f7f7f7;
            border: 1px solid #e5e5e5;
            padding: 18px;
            border-radius: 12px;
        }

        [data-testid="stMetricLabel"] {
            color: #555555;
        }

        [data-testid="stMetricValue"] {
            color: #E50914;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid #e5e5e5;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# 3. CHART THEME
# ------------------------------------------------------------

sns.set_theme(style="whitegrid", context="notebook")


# ------------------------------------------------------------
# 4. LOAD DATASET
# ------------------------------------------------------------

@st.cache_data
def load_data():
    file_path = "data/Netflix_Content_Analysis_1500_Records.xlsx"

    data = pd.read_excel(file_path)

    return data


try:
    df = load_data()

except FileNotFoundError:
    st.error(
        "Dataset not found. Make sure the Excel file is inside "
        "the project's data folder."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()


# ------------------------------------------------------------
# 5. DASHBOARD HEADER
# ------------------------------------------------------------

st.title("🎬 Netflix Content Analytics Dashboard")

st.write(
    "Explore movies, TV shows, genres, content ratings, "
    "countries, and release-year trends."
)

st.caption(
    "Interactive data analysis dashboard built using Python and Streamlit."
)

st.divider()


# ------------------------------------------------------------
# 6. SIDEBAR FILTERS
# ------------------------------------------------------------

st.sidebar.title("🔎 Dashboard Filters")

st.sidebar.caption(
    "Choose the filters below to explore the dataset."
)


# Content type filter
selected_type = st.sidebar.multiselect(
    "Content Type",
    options=sorted(df["Type"].dropna().unique()),
    default=sorted(df["Type"].dropna().unique())
)


# Country filter
selected_country = st.sidebar.multiselect(
    "Country",
    options=sorted(df["Country"].dropna().unique()),
    default=sorted(df["Country"].dropna().unique())
)


# Genre filter
selected_genre = st.sidebar.multiselect(
    "Genre",
    options=sorted(df["Genre"].dropna().unique()),
    default=sorted(df["Genre"].dropna().unique())
)


# Release year range filter
release_year_min = int(df["Release Year"].min())
release_year_max = int(df["Release Year"].max())

selected_year_range = st.sidebar.slider(
    "Release Year Range",
    min_value=release_year_min,
    max_value=release_year_max,
    value=(release_year_min, release_year_max)
)


# Reset filters button
if st.sidebar.button("🔄 Reset Filters", use_container_width=True):
    st.rerun()


# ------------------------------------------------------------
# 7. APPLY FILTERS
# ------------------------------------------------------------

filtered_df = df[
    (df["Type"].isin(selected_type))
    & (df["Country"].isin(selected_country))
    & (df["Genre"].isin(selected_genre))
    & (df["Release Year"] >= selected_year_range[0])
    & (df["Release Year"] <= selected_year_range[1])
].copy()


# Handle empty results
if filtered_df.empty:
    st.warning(
        "No titles match your selected filters. "
        "Please change your selections in the sidebar."
    )
    st.stop()


# ------------------------------------------------------------
# 8. KEY PERFORMANCE INDICATORS (KPI CARDS)
# ------------------------------------------------------------

st.subheader("📊 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Titles",
        value=f"{len(filtered_df):,}"
    )

with col2:
    movie_count = (filtered_df["Type"] == "Movie").sum()

    st.metric(
        label="Movies",
        value=f"{movie_count:,}"
    )

with col3:
    tv_count = (filtered_df["Type"] == "TV Show").sum()

    st.metric(
        label="TV Shows",
        value=f"{tv_count:,}"
    )

with col4:
    genre_count = filtered_df["Genre"].nunique()

    st.metric(
        label="Unique Genres",
        value=f"{genre_count:,}"
    )


st.divider()


# ------------------------------------------------------------
# 9. CONTENT TYPE AND COUNTRY ANALYSIS
# ------------------------------------------------------------

st.subheader("🌍 Content Type and Country Analysis")

col1, col2 = st.columns(2)


# Chart 1: Movies vs TV Shows
with col1:

    type_counts = filtered_df["Type"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=type_counts.index,
        y=type_counts.values,
        ax=ax
    )

    ax.set_title("Movies vs TV Shows")
    ax.set_xlabel("Content Type")
    ax.set_ylabel("Number of Titles")

    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f", padding=3)

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# Chart 2: Top 10 Countries
with col2:

    country_counts = (
        filtered_df["Country"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=country_counts.values,
        y=country_counts.index,
        ax=ax
    )

    ax.set_title("Top 10 Countries")
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Country")

    fig.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


st.divider()


# ------------------------------------------------------------
# 10. GENRE ANALYSIS
# ------------------------------------------------------------

st.subheader("🎭 Content Distribution by Genre")

genre_counts = (
    filtered_df["Genre"]
    .value_counts()
    .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=genre_counts.values,
    y=genre_counts.index,
    ax=ax
)

ax.set_title("Number of Titles by Genre")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# ------------------------------------------------------------
# 11. CONTENT RATING ANALYSIS
# ------------------------------------------------------------

st.subheader("🔞 Content Rating Distribution")

rating_counts = (
    filtered_df["Rating"]
    .value_counts()
    .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=rating_counts.values,
    y=rating_counts.index,
    ax=ax
)

ax.set_title("Number of Titles by Content Rating")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Content Rating")

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# ------------------------------------------------------------
# 12. RELEASE YEAR TIMELINE
# ------------------------------------------------------------

st.subheader("📅 Content Release Timeline")

release_counts = (
    filtered_df["Release Year"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(
    x=release_counts.index,
    y=release_counts.values,
    marker="o",
    ax=ax
)

ax.set_title("Number of Titles by Release Year")
ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

ax.grid(alpha=0.3)

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)


st.divider()


# ------------------------------------------------------------
# 13. EXPLORE CONTENT TABLE
# ------------------------------------------------------------

st.subheader("🎞️ Explore Netflix Content")

st.caption(
    f"{len(filtered_df):,} titles match your selected filters."
)

display_columns = [
    "Title",
    "Type",
    "Genre",
    "Country",
    "Rating",
    "Release Year",
    "Year Added"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True,
    height=450
)


# ------------------------------------------------------------
# 14. DOWNLOAD FILTERED DATA
# ------------------------------------------------------------

st.divider()

st.subheader("📥 Export Data")

st.write(
    "Download the data currently displayed after applying your filters."
)

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv_data,
    file_name="netflix_filtered_data.csv",
    mime="text/csv",
    use_container_width=False
)


# ------------------------------------------------------------
# 15. ABOUT THIS DASHBOARD
# ------------------------------------------------------------

st.divider()

with st.expander("ℹ️ About This Dashboard"):

    st.markdown(
        """
        ## Netflix Content Analytics Dashboard

        This project explores a dataset containing 1,500 records
        related to movies and TV shows.

        ### Key Features

        - Interactive content-type filters
        - Country and genre filters
        - Release-year range selection
        - Dynamic KPI cards
        - Movies versus TV shows analysis
        - Country distribution analysis
        - Genre distribution analysis
        - Content rating analysis
        - Release-year timeline
        - Filtered CSV downloads

        ### Technologies Used

        - Python
        - Pandas
        - Matplotlib
        - Seaborn
        - Streamlit
        - Excel

        ### Project Objective

        Demonstrate data analysis, exploratory data analysis (EDA),
        data visualization, and interactive dashboard development.

        ### Dataset Disclaimer

        The results describe the supplied 1,500-record dataset.
        They should not be interpreted as verified statistics for
        Netflix's complete content catalog.
        """
    )


# ------------------------------------------------------------
# 16. FOOTER
# ------------------------------------------------------------

st.divider()

st.caption(
    "Netflix Content Analytics Dashboard | "
    "Built with Python, Pandas, Matplotlib, Seaborn and Streamlit"
)

