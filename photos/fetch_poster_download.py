import requests
import pickle
import pandas as pd
import time

movie_poster_url = pickle.load(open('movie_poster_url.pkl','rb'))
recommended_movies_dict = pickle.load(open('recommend_movies.pkl','rb'))
recommended_movies_df = pd.DataFrame(recommended_movies_dict)

cnt=1
for i in movie_poster_url:
    if movie_poster_url[i]==None:
        continue
    url=movie_poster_url[i]
    r = requests.get(url,allow_redirects=True)
    start=time.time()
    open(str(i), 'wb').write(r.content)
    cnt+=1
    print(cnt)
#4762 movies posters are there, 32 movies do not have posters!

