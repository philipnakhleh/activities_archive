import pandas as pd
from fastapi import FastAPI
from urllib.parse import urlparse, parse_qs

app = FastAPI()


def extract_id_from_drive_link(drive_link):
    parsed_url = urlparse(drive_link)
    query_params = parse_qs(parsed_url.query)

    if 'id' in query_params:
        return query_params['id'][0]
    else:
        return None

@app.get('/get_all_games')
def get_all_games():
    games_sheet_id = '1O0ozz4Jl9bbXrU2CiSW1N-apaPSaP21_eZ_KElV8SaI'

    games = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{games_sheet_id}/export?format=csv')
    return_list = []

    for idx, game in games.iterrows():
        dic = {}
        dic['id'] = idx
        dic['name'] = game.get('اسم اللعبة', 'بلا اسم')
        dic['age'] = game.get('العمر', 'غير محدد')
        dic['number'] = game.get('العدد', 'غير محدد')
        dic['time'] = game.get('\nالمدة', 'غير محدد')
        dic['goal'] = game.get('الهدف', 'لا يوجد')
        dic['sigle_or_team'] = game.get('لعبة فردية أو فرق', 'فرق')
        pictures_str = game.get('صور توضيحية', '')
        pictures_list = pictures_str.split(',')
        for picture in pictures_list:
            id = extract_id_from_drive_link
            pic = f'https://drive.google.com/uc?id={id}'
            dic['pics'] = pic
            break

        return_list.append(dic)

    return {
        'data': return_list
    }

@app.get('/get_game_by_id')
def get_game_by_id(id: int):
    games_sheet_id = '1O0ozz4Jl9bbXrU2CiSW1N-apaPSaP21_eZ_KElV8SaI'

    games = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{games_sheet_id}/export?format=csv')

    dic = {}
    game = games.iloc[id]
    dic['name'] = game.get('اسم اللعبة', 'بلا اسم')
    dic['place'] = game.get('المكان', 'غير محدد')
    dic['age'] = game.get('العمر', 'غير محدد')
    dic['number'] = game.get('العدد', 'غير محدد')
    dic['time'] = game.get('\nالمدة', 'غير محدد')
    dic['judges'] = int(game.get('عدد الحكام', 'غير محدد'))
    dic['objects'] = game.get('الحاجيات', 'لا شيء')
    dic['formation'] = game.get('التشكيل', 'عشوائي')
    dic['gameplay'] = game.get('طريقة اللعب', 'عشوائي')
    dic['winner'] = game.get('الفائز', 'لا يوجد')
    dic['goal'] = game.get('الهدف', 'لا يوجد')
    dic['single_or_team'] = game.get('لعبة فردية أو فرق', 'فرق')
    pictures_str = game.get('صور توضيحية', '')
    pictures_list = pictures_str.split(',')
    dic['pics'] = []
    for picture in pictures_list:
        id = extract_id_from_drive_link
        pic = f'https://drive.google.com/uc?id={id}'
        dic['pics'].append(pic)


    return dic

@app.get('/get_items')
def get_items():
    itmes_sheet_id = '1Nt7CYJETs3M6-YF5b-fVTZNMZhNCNJEwGupquTQPs2A'

    items = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{itmes_sheet_id}/export?format=csv')

    return_list = []

    for idx, item in items.iterrows():
        dic = {}
        dic['id'] = idx
        dic['name'] = item.get('اسم الغرض', 'بلا اسم')
        dic['unit'] = item.get('الوحدة', 'قطعة')
        dic['quantity'] = str(item.get('الكمية', 0))

        return_list.append(dic)

    return {
        'data': return_list
    }