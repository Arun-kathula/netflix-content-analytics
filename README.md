# 🎬 Netflix Content Analytics Dashboard

An interactive content analytics dashboard built using **Python, Pandas, Matplotlib, Seaborn, and Streamlit** to explore movie and TV show data.

The dashboard helps users investigate content distribution, compare movies and TV shows, explore country and genre trends, and analyze ratings and release years through interactive visualizations.

## 📌 Project Overview

This project demonstrates how Python and data visualization tools can transform a structured dataset into an interactive analytics dashboard.

Users can apply filters, search for titles, browse content cards, and explore charts that summarize the dataset.

## ✨ Features

* **Interactive Dashboard:** Explore content through a Netflix-inspired interface.
* **Key Performance Indicators:** View total titles, movies, TV shows, and unique genres.
* **Content Type Analysis:** Compare the number of movies and TV shows.
* **Country Analysis:** Explore the countries represented in the dataset.
* **Genre Analysis:** Compare content distribution across genres.
* **Rating Analysis:** Examine the distribution of content ratings.
* **Release Year Analysis:** Explore content by release year.
* **Sidebar Filters:** Filter titles by available attributes, including type, country, genre, and release year.
* **Title Search:** Search for movies and TV shows by title.
* **Content Library:** Browse individual content records.
* **Pagination:** Navigate through filtered results in manageable groups.
* **CSV Export:** Download filtered data for further analysis.

## 🛠️ Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Core programming language                 |
| Pandas     | Data loading, filtering, and manipulation |
| Matplotlib | Data visualization                        |
| Seaborn    | Statistical charts and visualizations     |
| Streamlit  | Interactive web application               |
| OpenPyXL   | Reading Excel datasets                    |

## 📂 Project Structure

```text
netflix-content-analytics/
│
├── data/
│   └── Netflix_Content_Analysis_1500_Records.xlsx
│
├── notebooks/
│   └── 01_data_understanding.ipynb
│
├── screenshots/
│
├── app.py
├── requirements.txt
└── README.md
```

## 📊 Dataset

The project currently uses an Excel dataset containing **1,500 sample records**.

The dataset includes fields such as:

* Show ID
* Title
* Type
* Genre
* Country
* Rating
* Date Added
* Year Added
* Release Year
* Duration
* Director
* Description

**Dataset note:** The records are used for project development and demonstration. The dataset has not been verified as a complete or authoritative representation of Netflix's actual catalog. Therefore, dashboard statistics should be interpreted as statistics of the supplied dataset, not official Netflix statistics.

## ⚙️ Installation and Setup

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/netflix-content-analytics.git
```

### 2. Navigate to the project folder

```bash
cd netflix-content-analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The application should open in your default browser.

### Dataset requirement

Make sure the Excel dataset is available at:

```text
data/Netflix_Content_Analysis_1500_Records.xlsx
```

If the dataset is not included in the repository, obtain an authorized copy and place it at that location before running the application.

## 🔍 Example Analyses

The dashboard supports exploration of questions such as:

* How many movies and TV shows are present in the dataset?
* Which countries have the most records?
* Which genres appear most frequently?
* How are content ratings distributed?
* How are titles distributed across release years?
* Which records match the selected filters or a title search?

## 📸 Screenshots

Screenshots of the running dashboard can be added to the `screenshots/` directory.

To display a screenshot on GitHub, save an image there and add a Markdown reference like this:

```markdown
![Netflix Content Analytics Dashboard](screenshots/dashboard.png)
```

Replace `dashboard.png` with the actual screenshot filename.

## 🚀 Future Improvements

* Add richer title details and descriptions.
* Improve the content browsing experience.
* Add additional data-quality checks.
* Introduce more advanced exploratory data analysis.
* Deploy the dashboard so users can access it online.
* Explore additional datasets and authorized data sources.

## 👨‍💻 Author

Developed as a data analytics project to practice Python, data manipulation, exploratory data analysis, visualization, and interactive dashboard development.

## 📄 Disclaimer

This is an independent educational project. It is not affiliated with, endorsed by, or sponsored by Netflix. Any Netflix-related branding or references are used only to describe the theme of the project.
