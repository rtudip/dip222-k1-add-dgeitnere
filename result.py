#Darja Geitnere, 221rdb227
# atkaartors pd1
#Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?
import pandas as pd
data = pd.read_csv('data.txt')
filtered_data = data[data['Country'] == 'Oman']
column = filtered_data['Founded'].min()
print(column)

#Kāds ir darbinieku skaits, kas strādā Latvijā?
#import pandas as pd
#data = pd.read_csv('data.txt')
#filtered_data = data[data['Country'] == 'Latvia']
#len = len(filtered_data)
#print(len)

#Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?
#import pandas as pd
#data = pd.read_csv('data.txt')
#filtered_data = data[data['Country'] == 'Latvia']
#column = filtered_data[filtered_data['Industry'] == 'Telecommunications']
#len = len(column)
#print(len)

#Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)
# import pandas as pd
#data = pd.read_csv('data.txt')
#filtered_data = data[data['Country'] == 'Latvia'] #region
#web = filtered_data[filtered_data ['Website'].str.contains('https://')] #contains teksta dāļu
#len = len(web)
#print(len)

#Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?
# import pandas as pd
#data = pd.read_csv('data.txt')
#filtered_data = data[data['Country'] == 'Latvia'] #region
#web = filtered_data[filtered_data ['Website'].str.contains('.org')] #contains teksta dāļu
#len = len(web)
#print(len)