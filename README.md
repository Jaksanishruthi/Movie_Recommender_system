# 🎬 Movie Recommender System Using Machine Learning

This project is a movie recommender web app built with **Streamlit** and based on movie similarity (from TMDB data and machine learning). It lets users enter a movie and get movie recommendations with poster images.

---

## Demo

![Demo Screenshot](Demo/c:\Users\jaksa\OneDrive\Pictures\Screenshots\Screenshot 2025-10-27 121510.png)

---

## Features

- Search for a movie and get 5 recommendations.
- Uses TMDB API to fetch movie posters.
- Modern, responsive web interface with Streamlit.
- Secure API key management.
- Error handling and graceful fallbacks for missing posters.

---

## How to Run

### 1. Clone the repository

git clone https://github.com/Jaksanishruthi/Movie_Recommender_system
cd Movie_Recommender_system


### 2. Set up your environment

It’s recommended to use a virtual environment.

python -m venv env
env\Scripts\activate # (Windows)


### 3. Install requirements


### 4. Get TMDB API Key

- Create a [TMDB account](https://www.themoviedb.org/signup)
- Go to [TMDB API settings](https://www.themoviedb.org/settings/api) and copy your **API Key (v3 auth)**

### 5. Set up your `.env` file

Create a `.env` file in your project root:

TMDB_API_KEY=your_tmdb_api_key_here

### 6. Run the app

Open your browser at the URL shown (e.g., http://localhost:8501)

---

## Folder Structure

- **app.py**: Main application code
- **artifacts/**: Preprocessed files (`movie_list.pkl`, `similarity.pkl`)
- **requirements.txt**: All dependencies
- **README.md**: This documentation
- **.env**: _Not tracked in version control!_ (holds your TMDB API key)

---

## Attributions

- Data: [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Code: Built with [Streamlit](https://streamlit.io)
- *This product uses the TMDB API but is not endorsed or certified by TMDB.*

---

## License

MIT License. See [LICENSE](LICENSE) for more details.

---

## Troubleshooting

- If posters are not showing, check your TMDB API key and network.
- Make sure `.env` is **not** uploaded to GitHub.
- For questions, raise an issue or contact the repository maintainer.



