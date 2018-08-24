import music
import matplotlib.pyplot as plt
list_of_music = music.get_songs()

year2005 = []
year1974 = []
year1980 = []
year1990 = []
year1995 = []
sum = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

for music in list_of_music:
    song = music["song"]
    for year in song:
        year = song["year"]
        if year == 2005:
            tempo = song["tempo"]
            year2005.append(tempo)
            sum = sum + tempo
        elif year == 1974:
            tempo = song["tempo"]
            year1974.append(tempo)
            sum2 = sum2 + tempo
        elif year == 1980:
            tempo = song["tempo"]
            year1980.append(tempo)
            sum3 = sum3 + tempo
        elif year == 1990:
            tempo = song["tempo"]
            year1990.append(tempo)
            sum4 = sum4 + tempo
        elif year == 1995:
            tempo = song["tempo"]
            year1995.append(tempo)
            sum5 = sum5 + tempo
        else:
            continue
average = sum/len(year2005)
average2 = sum2/len(year1974)
average3 = sum3/len(year1980)
average4 = sum4/len(year1990)
average5 = sum5/len(year1995)
plt.plot([1974,1980,1990,2005],[average2,average3,average4,average])
# plt.plot([74.81,97.70,104.83,114.64,122.83,154.95])
plt.xlabel('year')
plt.ylabel('tempo')
plt.title('tempos throughout the years')
plt.axis([1970,2007,110,140])
plt.grid(False)
plt.show()
