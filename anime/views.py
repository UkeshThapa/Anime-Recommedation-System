from django.http.response import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd

similarity = pickle.load(open('E:\Project\Anime_Recommendation_System\model\similarity.pkl','rb'))
model = pickle.load(open('E:\Project\Anime_Recommendation_System\model/anime.pkl','rb'))
model = pd.DataFrame(model)

def animeRecommend(anime):

    anime_index = model[model['Anime_name'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommends = []
    for i in anime_list:
        recommends.append(model.iloc[i[0]].Anime_name)
    return recommends


def recommend(request):
    if 'search' in request.GET:
        search = request.GET['search']
        recommended = animeRecommend(search)

        context = {'search':recommended}
        print(recommended)

    else:
        context={'search':'else'}
    return render(request,'anime/main.html',context)

