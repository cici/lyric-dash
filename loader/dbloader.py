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

serverClient.query(
    q.create(
        q.collection("songs"),
        {"data": {"title": "The Story", "artist": "Brandi Carlile", "album": "The Story", "lyrics": """All of these lines across my face
                  Tell you the story of who I am
                  So many stories of where I've been
                  And how I got to where I am

                  But these stories don't mean anything
                  When you've got no one to tell them to
                  It's true
                  I was made for you

                  I climbed across the mountaintops
                  Swam all across the ocean blue
                  I crossed all the lines and I broke all the rules
                  But baby I broke them all for you

                  Oh because even when I was flat broke
                  You made me feel like a million bucks
                  You do
                  I was made for you

                  You see the smile that's on my mouth
                  It's hiding the words that don't come out
                  And all of my friends who think that I'm blessed
                  They don't know my head is a mess

                  No they don't know who I really am
                  And they don't know what I've been through
                  Like you do, and I was made for you

                  All of these lines across my face
                  Tell you the story of who I am
                  So many stories of where I've been
                  And how I got to where I am

                  Oh but these stories don't mean anything
                  When you've got no one to tell them to
                  It's true
                  I was made for you
                  Oh yeah, well it's true
                  That I was made for you"""}}
    )
)
