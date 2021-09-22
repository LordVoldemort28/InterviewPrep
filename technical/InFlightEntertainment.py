def can_two_movies_fill_flight(movie_lengths, flight_length):

    second_movie = [(flight_length-movie) for movie in movie_lengths]

    for second in second_movie:
        if second in movie_lengths:
            return True

    return False


result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
print(result)
