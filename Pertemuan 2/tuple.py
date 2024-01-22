mapel = ("matematika", "DDJ", "Olahraga", "Jepang")

mapel_list = list(mapel)
print("tuple =", mapel)
print("LIst =", mapel_list)
mapel_list.append("English")
mapel_list[0]="Informatika"
del mapel_list[2]
print(mapel_list)
mapel_tuple = tuple(mapel_list)
print(mapel_tuple)