
import html

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


# ==========================================================
# 1. PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Netflix Content Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# 2. NETFLIX-INSPIRED THEME
# ==========================================================

st.markdown(
    """
    <style>
        .stApp {
            background-color: #080808;
            color: #ffffff;
        }

        .block-container {
            max-width: 1500px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, h4 {
            color: #ffffff !important;
        }

        .netflix-logo {
            color: #E50914;
            font-size: 38px;
            font-weight: 900;
            letter-spacing: 3px;
        }

        .hero-banner {
            background:
                radial-gradient(
                    ellipse at 85% 30%,
                    rgba(229, 9, 20, 0.30),
                    transparent 50%
                ),
                linear-gradient(
                    110deg,
                    #202020,
                    #111111,
                    #260509
                );
            border: 1px solid #333333;
            border-radius: 16px;
            padding: 35px;
            margin: 20px 0 30px 0;
        }

        .hero-tag {
            color: #ff454b;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 3px;
        }

        .hero-heading {
            color: #ffffff;
            font-size: 36px;
            font-weight: 900;
            line-height: 1.25;
            margin-top: 15px;
        }

        .hero-description {
            color: #cccccc;
            font-size: 15px;
            line-height: 1.8;
            max-width: 750px;
        }

        [data-testid="stMetric"] {
            background: linear-gradient(145deg, #202020, #111111);
            border: 1px solid #353535;
            border-radius: 12px;
            padding: 18px;
        }

        [data-testid="stMetricLabel"] {
            color: #cccccc !important;
        }

        [data-testid="stMetricValue"] {
            color: #E50914 !important;
            font-weight: 800;
        }

        section[data-testid="stSidebar"] {
            background-color: #111111;
            border-right: 1px solid #292929;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] label {
            color: #dddddd !important;
        }

        .stButton > button,
        .stDownloadButton > button {
            background-color: #E50914;
            color: #ffffff;
            border: none;
            border-radius: 7px;
            font-weight: 700;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background-color: #b20710;
            color: #ffffff;
            border: none;
        }

        hr {
            border-color: #333333;
        }

        .footer-text {
            color: #888888;
            text-align: center;
            font-size: 12px;
            padding: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# 3. CHART THEME
# ==========================================================

sns.set_theme(style="darkgrid", context="notebook")


# ==========================================================
# 4. LOAD DATASET
# ==========================================================

@st.cache_data
def load_data():
    file_path = "data/Netflix_Content_Analysis_1500_Records.xlsx"
    return pd.read_excel(file_path)


try:
    df = load_data()

except Exception as error:
    st.error(
        "Unable to load the dataset. Check that the Excel file "
        "exists inside the data folder."
    )
    st.code(str(error))
    st.stop()


# Convert year columns to numeric values

df["Release Year"] = pd.to_numeric(
    df["Release Year"],
    errors="coerce"
)

df["Year Added"] = pd.to_numeric(
    df["Year Added"],
    errors="coerce"
)


# ==========================================================
# 5. HEADER
# ==========================================================

st.markdown(
    '<div class="netflix-logo">NETFLIX</div>',
    unsafe_allow_html=True
)

st.caption("CONTENT INTELLIGENCE  |  ANALYTICS STUDIO")

st.divider()


# ==========================================================
# 6. HERO BANNER
# ==========================================================

st.markdown(
    """
    
    <div class="hero-heading">
        Every Story.<br>
        One Dashboard.
    </div>

    <div class="hero-description">
        Dive into the world of entertainment. Uncover content
        trends, explore global markets, analyze audience ratings,
        and discover the stories hidden within the data.
    </div>

    """,
    unsafe_allow_html=True
)


# ==========================================================
# 7. SIDEBAR FILTERS
# ==========================================================

st.sidebar.markdown(
    """
    <div style="
        color: #E50914;
        font-size: 27px;
        font-weight: 900;
        letter-spacing: 2px;
    ">
        NETFLIX
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.subheader("🎛️ Explore & Filter")

st.sidebar.caption(
    "Customize your content analysis."
)


type_options = sorted(
    df["Type"].dropna().unique().tolist()
)

country_options = sorted(
    df["Country"].dropna().unique().tolist()
)

genre_options = sorted(
    df["Genre"].dropna().unique().tolist()
)


selected_type = st.sidebar.multiselect(
    "Content Type",
    options=type_options,
    default=type_options
)

selected_country = st.sidebar.multiselect(
    "Country",
    options=country_options,
    default=country_options
)

selected_genre = st.sidebar.multiselect(
    "Genre",
    options=genre_options,
    default=genre_options
)


valid_years = df["Release Year"].dropna()

year_min = int(valid_years.min())
year_max = int(valid_years.max())


selected_year_range = st.sidebar.slider(
    "Release Year Range",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max)
)


st.sidebar.divider()

st.sidebar.caption(
    "Built with Python, Pandas, Matplotlib, "
    "Seaborn and Streamlit."
)


# ==========================================================
# 8. APPLY FILTERS
# ==========================================================

filtered_df = df[
    df["Type"].isin(selected_type)
    & df["Country"].isin(selected_country)
    & df["Genre"].isin(selected_genre)
    & df["Release Year"].between(
        selected_year_range[0],
        selected_year_range[1]
    )
].copy()


if filtered_df.empty:
    st.warning(
        "No titles match your selected filters. "
        "Please change your selections in the sidebar."
    )
    st.stop()


# ==========================================================
# 9. KPI CARDS
# ==========================================================

st.subheader("📊 Your Content at a Glance")

st.caption(
    "Key statistics for the titles matching your filters."
)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "TOTAL TITLES",
        f"{len(filtered_df):,}"
    )


with col2:
    movie_count = (
        filtered_df["Type"] == "Movie"
    ).sum()

    st.metric(
        "MOVIES",
        f"{movie_count:,}"
    )


with col3:
    tv_count = (
        filtered_df["Type"] == "TV Show"
    ).sum()

    st.metric(
        "TV SHOWS",
        f"{tv_count:,}"
    )


with col4:
    st.metric(
        "UNIQUE GENRES",
        f"{filtered_df['Genre'].nunique():,}"
    )


# ==========================================================
# 10. CHART FORMATTING FUNCTION
# ==========================================================

def style_chart(fig, ax):

    fig.patch.set_facecolor("#111111")
    ax.set_facecolor("#111111")

    ax.tick_params(
        colors="#dddddd",
        labelsize=9
    )

    ax.xaxis.label.set_color("#cccccc")
    ax.yaxis.label.set_color("#cccccc")
    ax.title.set_color("#ffffff")

    for spine in ax.spines.values():
        spine.set_color("#333333")

    ax.grid(
        True,
        color="#333333",
        alpha=0.6,
        linestyle="--"
    )


# ==========================================================
# 11. CONTENT TYPE AND COUNTRY ANALYSIS
# ==========================================================

st.divider()

st.subheader("🌍 Content Across the World")

col1, col2 = st.columns(2)


# Chart 1: Movies vs TV Shows

with col1:

    st.markdown("#### Movies vs TV Shows")

    type_counts = filtered_df["Type"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=type_counts.index,
        y=type_counts.values,
        ax=ax
    )

    style_chart(fig, ax)

    ax.set_xlabel("Content Type")
    ax.set_ylabel("Number of Titles")
    ax.set_title("Content Type Distribution")

    if ax.containers:
        ax.bar_label(
            ax.containers[0],
            color="white",
            padding=3
        )

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


# Chart 2: Top 10 Countries

with col2:

    st.markdown("#### Top 10 Countries")

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

    style_chart(fig, ax)

    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Country")
    ax.set_title("Top Countries by Title Count")

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


# ==========================================================
# 12. GENRE DISTRIBUTION
# ==========================================================

st.divider()

st.subheader("🎭 Explore the Genres")

st.caption(
    "Compare the number of titles across different genres."
)


genre_counts = (
    filtered_df["Genre"]
    .value_counts()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=genre_counts.values,
    y=genre_counts.index,
    ax=ax
)

style_chart(fig, ax)

ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")
ax.set_title("Titles by Genre")

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)


# ==========================================================
# 13. CONTENT RATING DISTRIBUTION
# ==========================================================

st.divider()

st.subheader("🔞 Content Rating Breakdown")

st.caption(
    "Explore the distribution of content ratings."
)


rating_counts = (
    filtered_df["Rating"]
    .value_counts()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=rating_counts.values,
    y=rating_counts.index,
    ax=ax
)

style_chart(fig, ax)

ax.set_xlabel("Number of Titles")
ax.set_ylabel("Content Rating")
ax.set_title("Titles by Content Rating")

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)


# ==========================================================
# 14. RELEASE YEAR TIMELINE
# ==========================================================

st.divider()

st.subheader("📅 Travel Through the Years")

st.caption(
    "Explore how the release years of titles are distributed."
)


release_counts = (
    filtered_df["Release Year"]
    .dropna()
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

style_chart(fig, ax)

ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")
ax.set_title("Titles by Release Year")

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)


# ==========================================================
# 15. EXPLORE THE LIBRARY
# ==========================================================

st.divider()

st.subheader("🎬 Explore the Library")

st.caption(
    "Browse a selection of titles from your filtered dataset."
)


# Show the first 8 titles as native Streamlit cards.
# These use Streamlit components, not raw HTML.



search_text = st.text_input(
    "🔍 Search Movies & TV Shows",
    placeholder="Enter a title..."
)

if search_text:
    library_df = filtered_df[
        filtered_df["Title"].str.contains(
            search_text, case=False, na=False
        )
    ]
else:
    library_df = filtered_df


# Pagination settings
items_per_page = 8

total_items = len(library_df)
total_pages = max(1, (total_items + items_per_page - 1) // items_per_page)

page_number = st.number_input(
    "Page",
    min_value=1,
    max_value=total_pages,
    value=1,
    step=1,
    key="library_page"
)

# Select records for the current page
start_index = (page_number - 1) * items_per_page
end_index = start_index + items_per_page

card_df = library_df.iloc[start_index:end_index]

st.caption(
    f"Showing {start_index + 1}–{min(end_index, total_items)} "
    f"of {total_items} titles"
)



card_columns = st.columns(4)

for index, (_, row) in enumerate(card_df.iterrows()):
    with card_columns[index % 4]:
        with st.container(border=True):
            st.caption(str(row["Type"]).upper())
            st.subheader(str(row["Title"]))

            st.write(f"🎭 Genre: {row['Genre']}")
            st.write(f"🌍 Country: {row['Country']}")
            st.write(f"🔖 Rating: {row['Rating']}")

            if pd.notna(row["Release Year"]):
                st.write(f"📅 Release Year: {int(row['Release Year'])}")
            else:
                st.write("📅 Release Year: Unknown")



# ==========================================================
# 16. SEARCH AND EXPLORE CONTENT
# ==========================================================

st.divider()

st.subheader("🔎 Search the Content Library")

st.caption(
    "Search for a movie or TV show by its title."
)


search_query = st.text_input(
    "Search by title",
    placeholder="Type a title here..."
)


table_df = filtered_df.copy()


if search_query.strip():

    table_df = table_df[
        table_df["Title"]
        .astype(str)
        .str.contains(
            search_query.strip(),
            case=False,
            na=False
        )
    ]


display_columns = [
    "Title",
    "Type",
    "Genre",
    "Country",
    "Rating",
    "Release Year",
    "Year Added"
]


st.write(
    f"**{len(table_df):,} titles found**"
)


st.dataframe(
    table_df[display_columns],
    use_container_width=True,
    hide_index=True,
    height=400
)


# ==========================================================
# 17. DOWNLOAD FILTERED DATA
# ==========================================================

st.divider()

st.subheader("📥 Export Your Analysis")

st.caption(
    "Download the filtered and searched results as a CSV file."
)


csv_data = table_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv_data,
    file_name="netflix_filtered_content.csv",
    mime="text/csv"
)


# ==========================================================
# 18. ABOUT THE PROJECT
# ==========================================================

st.divider()

with st.expander("ℹ️ About This Dashboard"):

    st.markdown(
        """
        ### Netflix Content Analytics Dashboard

        An interactive analytics project built with Python.

        **Features**

        - Interactive content filters
        - KPI cards
        - Country distribution analysis
        - Genre distribution analysis
        - Content rating analysis
        - Release-year trends
        - Searchable content library
        - CSV downloads

        **Technologies**

        Python, Pandas, Matplotlib, Seaborn and Streamlit.

        **Dataset Disclaimer**

        This dashboard analyzes the supplied dataset of 1,500
        records. The results should not be interpreted as verified
        statistics for Netflix's complete content catalog.
        """
    )


# ==========================================================
# 19. FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
    <div class="footer-text">
        NETFLIX CONTENT ANALYTICS<br><br>
        Built with Python, Pandas, Matplotlib, Seaborn and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
