# Query 1 -----------------------------------------------------------------------------------------
"""Query 1:  Give me the artist, song title and song's length in the music app history
that was heard during sessionId = 338, and itemInSession = 4"""

QUERY_1 = """
    SELECT artist, song_title, song_length
    FROM songs_by_user_session_item
    WHERE session_id=338 AND item_in_session=4;
    """

CREATE_TABLE_1 = """
    CREATE TABLE IF NOT EXISTS songs_by_user_session_item (
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        song_length float,
        PRIMARY KEY (session_id, item_in_session)
    )
"""

INSERT_1 = """
    INSERT INTO songs_by_user_session_item (
        session_id,
        item_in_session,
        artist,
        song_title,
        song_length
    )
    VALUES (%s, %s, %s, %s, %s)
"""

# Query 2 -----------------------------------------------------------------------------------------
"""Query 2:
Give me only the following:
- name of artist
- song (sorted by itemInSession)
- user (first and last name)

for userid = 10, sessionid = 182
"""

QUERY_2 = """
    SELECT artist, song_title, first_name, user_last_name
    FROM songs_by_user_in_session
    WHERE user_id=10 AND session_id=182
    ORDER BY item_in_session;
    """

CREATE_TABLE_2 = """
    CREATE TABLE IF NOT EXISTS songs_by_user_in_session (
        user_id int,
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        first_name text,
        user_last_name text,
        PRIMARY KEY ((user_id, session_id), item_in_session)
    )
"""

INSERT_2 = """
    INSERT INTO songs_by_user_in_session (
        user_id,
        session_id,
        item_in_session,
        artist,
        song_title,
        first_name,
        user_last_name
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Query 3 -----------------------------------------------------------------------------------------
"""Query 3:
Give me every user name (first and last) in my music app history who listened
to the song 'All Hands Against His Own'"""

QUERY_3 = """
    SELECT first_name, user_last_name
    FROM user_by_song
    WHERE song_title='All Hands Against His Own';
    """

CREATE_TABLE_3 = """
    CREATE TABLE IF NOT EXISTS user_by_song (
        song_title text,
        user_id int,
        first_name text,
        user_last_name text,
        PRIMARY KEY ((song_title), user_id)
        )
"""

INSERT_3 = """
    INSERT INTO user_by_song (
        song_title,
        user_id,
        first_name,
        user_last_name
    )
    VALUES (%s, %s, %s, %s)
"""
