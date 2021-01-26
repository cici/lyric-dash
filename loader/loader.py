import lyricsgenius
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

adminClient = FaunaClient(secret="fnADqi0R_9ACE5_l_utgLTNc-uy7KYwuz1_HWNAy")
serverClient = FaunaClient(secret="fnADqi1i0SACFFenB-oGz8_GdXheECGNdCioMw-L")

serverClient.query(q.create_collection({"name": "songs"}))
serverClient.query(
    q.create_index(
        {
            "name": "songs_by_title",
            "source": q.collection("songs"),
            "terms": [{"field": ["data", "title"]}]
        }
    )
)

genius = lyricsgenius.Genius(
    "OpOERhcnrqUngJ3m79Q8FM0FqNAEAExyIG7ccbA1XuyH64V5XTYb6zm_mp1XY-fJ")
genius.verbose = False
genius.remove_section_headers = True
genius.excluded_terms = ["(Remix)", "(Live)", "Digital Album Version",
                         "Sam Smith", "(Piano Version)", "(Austin cello version)", "new album version", "The rock is my foundation", "Hiding My Heart Away", "All You Need Is Love", "Creep", "I didn’t", "Murder In The City", "Folsom Prison Blues", "Hallelujah", "Heaven", "Sixty Years On", "Take Me Home\, Country Roads", "The Sound Of Silence"]

# 110 will get all of the songs
artist = genius.search_artist("Brandi Carlile", max_songs=110, sort="title")

for song in artist._songs:
    serverClient.query(
        q.create(
            q.collection("songs"),
            {"data": {"title": song.title, "artist": artist.name, "album": song.album, "year": song.year, "lyrics": song.lyrics}
             }
        )
    )
    print("\nLoaded " + song.title)

print("\nDataload complete")
