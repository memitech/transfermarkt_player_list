import pandas as pd
from requests_html import HTMLSession


# Replace Your Required Club URL
club_url = 'https://www.transfermarkt.com/fc-liverpool/startseite/verein/31/saison_id/2022'

session = HTMLSession()
r = session.get(club_url)
r.html.render(timeout=10000)
player_names = r.html.find('table.items table.inline-table')
player_urls = r.html.find('table.items')

player_name_list = []
player_url_list = []

print('Start')

if player_names:
    player_name = player_names[0].find('tr td.hauptlink .nowrap span.hide-for-small a.spielprofil_tooltip')
    for i in player_names:
        player_name_list.append(i.text.partition('\n')[0])

if player_urls:
    player_url = player_urls[0].find('tr td.hauptlink .nowrap span.hide-for-small a')
    try:
        for i in player_url:
            url = 'https://www.transfermarkt.com' + str(i.attrs['href'])
            player_url_list.append(url)
    except:
        player_url_list.append('NO URL')


dict = {'Player_Name': player_name_list, 'Player_Url': player_url_list} 
df = pd.DataFrame(dict) 
df.to_csv('test.csv')

print('Completed!')