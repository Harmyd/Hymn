import json
from .database import sessionlocal
from .models import Hymn,Lyrics


#loading the json file
with open("Utils/hymns_with_authors.json",encoding="utf-8") as f:
    #convert to dictionary
    data=json.load(f)
    #print (data["hymns"].items())


    # for hymn_key,hymn_value in hymn_details.items():
    #     print(hymn_key)

#creating a database session to communicate with my db   
db=sessionlocal()
#looping through the dictionary
try:
    for hymn_number,hymn_details in data["hymns"].items():
        new_hymn=Hymn(
            title=hymn_details["title"],
            chorus=hymn_details["chorus"],
            composer=hymn_details["author"]
        )
        verses=hymn_details["verses"]
        for i,verse in enumerate(verses,start=1):
            new_lyrics=Lyrics(stanza_number=i,content=verse)
            # this new_lyric belongs to this particular new_hymn is what i did with the append
            #saving me the stress of new_lyric.hymn_id = new_hymn.id
            new_hymn.lyrics.append(new_lyrics)
        db.add(new_hymn)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()
        


