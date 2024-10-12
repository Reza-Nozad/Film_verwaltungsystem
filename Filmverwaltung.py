from test_mysql_connection import create_connection

def add_movie(title, director, genre, release, rating):
    connection = create_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO Film (title, director, genre, releaseyear, rating) VALUES (%s, %s, %s, %s, %s)"
    values = (title, director, genre, release, rating)

    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

def delete_movie(movie_id):
    connection = create_connection()
    cursor = connection.cursor()
    
    sql = "DELETE FROM Film WHERE id = %s"
    cursor.execute(sql, (movie_id,))
    
    connection.commit()
    cursor.close()
    connection.close()

def update_movie(movie_id, title=None, director=None, genre=None, release=None, rating=None):
    connection = create_connection()
    cursor = connection.cursor()
    
    sql = "UPDATE Film SET title = COALESCE(%s, title), director = COALESCE(%s, director), genre = COALESCE(%s, genre), releaseyear = COALESCE(%s, releaseyear), rating = COALESCE(%s, rating)  WHERE id = %s"
    values = (title, director, genre, release, rating, movie_id)
    
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

def search_movies(criteria, value):
    allowed_criteria = ['title', 'director', 'genre', 'releaseyear', 'rating']
    if criteria not in allowed_criteria:
        raise ValueError("Invalid criterion. Allowed criterion: " + ", ".join(allowed_criteria))
        # print("Invalid criterion. Allowed criterion:",allowed_criteria)
    connection = create_connection()
    cursor = connection.cursor()
    
    sql = f"SELECT * FROM Film WHERE {criteria} = %s"
    cursor.execute(sql, (value,))
    results = cursor.fetchall()
    
    for row in results:
        print(f"Titel: {row[1]}, Director: {row[2]}, Genre: {row[3]}, Release Year: {row[4]}, Rating: {row[5]}")
    
    cursor.close()
    connection.close()

def show_movies():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Film')
    filmlist = cursor.fetchall()
    for row in filmlist:
        print(f"Number: {row[0]}, Title: {row[1]}, Director: {row[2]}, Genre: {row[3]}, Release Year: {row[4]}, Rating: {row[5]}")
    cursor.close()
    connection.close()

def sort_movies(order_by):
    allowed_order = ['rating', 'releaseyear']
    if order_by not in allowed_order:
        raise ValueError("Invalid sort option. Allowed options: " + ", ".join(allowed_order))
    
    connection = create_connection()
    cursor = connection.cursor()
    
    sql = f"SELECT * FROM Film ORDER BY {order_by} DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for row in results:
        print(f"Title: {row[1]}, Director: {row[2]}, Genre: {row[3]}, Release Year: {row[4]}, Rating: {row[5]}")
    
    cursor.close()
    connection.close()

def main():
    while True:
        print("\n--- Film Collection Administration ---")
        print("1. Add Movie")
        print("2. Delete movie")
        print("3. Update movie")
        print("4. Search for movies")
        print("5. Sorting movies")
        print("6. Show Movies list")
        print("7. Finish")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            title = input("Title of the film: ")
            director = input("Director: ")
            genre = input("Genre: ")
            release = int(input("Release Year: "))
            rating = float(input("Rating (0-10): "))
            add_movie(title, director, genre, release, rating)

        elif choice == '2':
            movie_id = int(input("ID of the movie to be deleted: "))
            delete_movie(movie_id)

        elif choice == '3':
            movie_id = int(input("ID of the movie to be updated: "))
            print("Leave the fields you do not want to change blank.")
            title = input("New title (or leave blank): ") or None
            director = input("New Director (or leave blank): ") or None
            genre = input("New Genre (or leave blank): ") or None
            release = input("New Releaseyear (or leave blank): ")
            release = int(release) if release else None
            rating = input("New rating (or leave blank): ")
            rating = float(rating) if rating else None
            update_movie(movie_id, title, director, genre, release, rating)

        elif choice == '4':
            criteria = input("Which criteria to search for? (title, director, genre, releaseyear, rating): ")
            value = input("Search value: ")
            if criteria in ['releaseyear', 'rating']:
                value = int(value) if criteria == 'releaseyear' else float(value)
            search_movies(criteria, value)

        elif choice == '5':
            order_by = input("By which criterion to sort? (rating, releaseyear): ")
            sort_movies(order_by)

        elif choice == '6':
        
            show_movies()

        elif choice == '7':
            print("program is terminated.")
            break

        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()

