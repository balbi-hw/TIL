# .get() 메서드를 활용해 dictionary를 조금 더 깔끔하게 생성할 수 있음

# 다음 두 코드는 같은 기능을 수행하는 다른 함수를 잘라온 것인데 위는 아래보다 변수가 두배가 들어가기에 성능적으로 예쁘지 못하다.
# 그냥 한 눈에 보기에도 차이가 난다는 게 보인다.
# 함수의 key 값을 재정의 할 때 사용한다.
# 상황에 따라 둘 중 하나를 선택해서 사용하면 좋을 듯 하다.

data_list = []
for i in range(len(movies)):
    data_dict = {} 
    data_dict['id'] = movies[i]['id']
    data_dict['title'] = movies[i]['title']
    data_dict['revenue'] = movies[i]['revenue']
    data_dict['overview'] = movies[i]['overview']
    data_dict['genre_ids'] = movies[i]['genre_ids']
    data_dict['poster_path'] = movies[i]['poster_path']

    for i in range(len(data_dict['genre_ids'])):
        for id in genres:
            if data_dict['genre_ids'][i] == id['id']:
                data_dict['genre_ids'][i] = id['name']

    data_list.append(data_dict)

#---------------------#

artist_data_list = []   
for artist in artists:
    artist_data_dict = {
        'id' : artist.get('id'),
        'name' : artist.get('name'),
        'images' : artist.get('images'),
        'type' : artist.get('type')
    }
    
    genres_name_list = []
    for id in range(len(genres)):
        for i in artist['genres_ids']:
            if genres[id]['id'] == i:
                genres_name_list.append(genres[id]['name'])
        artist_data_dict['genres_names'] = genres_name_list
            
    artist_data_list.append(artist_data_dict)