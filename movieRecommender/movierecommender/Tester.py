# movie_app.py
import streamlit as st
import pandas as pd

# Function to add movie to CSV file
def add_movie_to_csv(movie_data, csv_file='movies.csv'):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Movie Name", "Movie Image URL", "Rating", "Genre", "Plot", "Certificate", "Country", "Director"])

    new_movie = pd.DataFrame([movie_data])
    df = pd.concat([df, new_movie], ignore_index=True)
    df.to_csv(csv_file, index=False)

# Main function for Streamlit app
def main():
    st.title("Movie Management App")

    # Input fields for adding a movie
    st.header("Add Movie")
    movie_name = st.text_input("Movie Name")
    movie_image_url = st.text_input("Movie Image URL")
    rating = st.number_input("Rating", min_value=0.0, max_value=10.0, step=0.1)
    genre = st.text_input("Genre")
    plot = st.text_area("Plot")
    certificate = st.text_input("Certificate")
    country = st.text_input("Country")
    director = st.text_input("Director")

    # Add movie button
    if st.button("Add Movie"):
        movie_data = {
            "Movie Name": movie_name,
            "Movie Image URL": movie_image_url,
            "Rating": rating,
            "Genre": genre,
            "Plot": plot,
            "Certificate": certificate,
            "Country": country,
            "Director": director
        }
        add_movie_to_csv(movie_data)
        st.success("Movie added successfully!")

    # # Display existing movies
    # st.title("Existing Movies")
    # try:
    #     movies_df = pd.read_csv('movies.csv')
    #     for index, row in movies_df.iterrows():
    #         st.subheader(row['Movie Name'])
    #         st.image(row['Movie Image URL'], caption=row['Movie Name'], use_column_width=True)
    #         st.write(f"Rating: {row['Rating']}")
    #         st.write(f"Genre: {row['Genre']}")
    #         st.write(f"Plot: {row['Plot']}")
    #         st.write(f"Certificate: {row['Certificate']}")
    #         st.write(f"Country: {row['Country']}")
    #         st.write(f"Director: {row['Director']}")
    #         st.write("----")
    # except FileNotFoundError:
    #     st.warning("No movies added yet.")

if __name__ == "__main__":
    main()
