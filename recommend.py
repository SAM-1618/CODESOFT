import sys
import dask.dataframe as dd
from dask import delayed
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class MovieRecommenderApp(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Movie Recommender System")
        self.setGeometry(300, 100, 400, 300)

        
        layout = QVBoxLayout()

        
        self.label = QLabel("Enter your preferred genre:")
        self.genre_input = QLineEdit(self)
        layout.addWidget(self.label)
        layout.addWidget(self.genre_input)

        
        self.recommend_button = QPushButton("Recommend Movies", self)
        self.recommend_button.clicked.connect(self.recommend_movies)
        layout.addWidget(self.recommend_button)

      
        self.movie_list = QListWidget(self)
        layout.addWidget(self.movie_list)

        self.setLayout(layout)

       
        try:
            self.movies_df = dd.read_csv('movie_dataset/movies.csv')  
        except FileNotFoundError:
            self.show_error_message("Error", "The movie dataset CSV file could not be found.")
            sys.exit()

    def recommend_movies(self):
        
        genre = self.genre_input.text().strip().lower()

        if not genre:
            self.show_error_message("Input Error", "Please enter a genre.")
            return

        
        recommended_movies = self.filter_movies_by_genre(genre)

        
        self.movie_list.clear()
        if recommended_movies:
            self.movie_list.addItems(recommended_movies)
        else:
            self.movie_list.addItem(f"No movies found for genre: {genre}")

    def filter_movies_by_genre(self, genre):
        
        @delayed
        def filter_movies(df, genre):
            return df[df['genre'].str.contains(genre, case=False, na=False)]

        
        filtered_movies = filter_movies(self.movies_df, genre)

        
        filtered_movies = self.movies_df[self.movies_df['genre'].str.contains(genre, case=False, na=False)]

        return filtered_movies['movie name'].tolist()

    def show_error_message(self, title, message):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    window = MovieRecommenderApp()
    window.show()

    sys.exit(app.exec_())
