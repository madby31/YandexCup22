import pandas as pd
df_qid_query = pd.read_csv(filepath_or_buffer='open_task\\qid_query.tsv', sep='\\t',engine ='python', names=['id_request', 'text_request'])
df_qid_url = pd.read_csv(filepath_or_buffer='open_task\\qid_url_rating.tsv', sep='\\t',engine ='python', names=['id_request', 'url_request','url_relevance'])
df_hostid_url = pd.read_csv(filepath_or_buffer='open_task\\hostid_url.tsv', sep='\\t',engine ='python', names=['id_host', 'url_request'])

pBreak = 0.15
best_pFound = 0
for text_request in df_qid_query['text_request']: # Перебираем текст запроса
    id_request = list(df_qid_query['id_request'].loc[df_qid_query['text_request'] == text_request]) # Получаем id текста запроса
    df = df_qid_url.loc[df_qid_url['id_request'].isin(id_request)].copy() # Выделяем датафрейм с одинаковым id запроса
    df = pd.merge(df, df_hostid_url, on=['url_request']).sort_values(by='url_relevance', ascending= False) # Добавляем к датафрейму значение id host
    pFound = 0
    ind = 0
    list_rel = []
    for vol in list(df['id_host'].unique())[:10]: # Перебираем первые 10 уникальных значений id host, отсортированных по убыванию по значению релевантности
        list_rel.append(df['url_relevance'].loc[df['id_host'] == vol].max()) # Если id host содержит несколько документов, выбираем наибольший и записываем в список
        if ind == 0:
            pLook = 1
        else:
            pLook = pLook*(1-list_rel[ind-1])*(1-pBreak)
        pFound = pFound + list_rel[ind]*pLook
        ind += 1
    if pFound > best_pFound: # Если текущее значение pFound максимальное, записываем в переменные для вывода
        out_text_request = text_request
        best_pFound = pFound
print('Лучший текст запроса - "'+out_text_request+'", с максимальным значением метрики pFound: '+str(best_pFound))
