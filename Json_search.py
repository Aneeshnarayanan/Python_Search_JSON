import json # Importing Json Library
# variable declaration and Keyword input
cnt = 0
json_file = open("Json_data.txt")
data = json.loads(json_file.read())
movies = data['Movies']
keyword = input("Enter the key word to search the Movies ")
type(keyword)
print ("Search Term is: "+keyword)
print ("Movies",end=" :: ")
keyword=keyword.lower()
#logic for the Json search
for movie in movies:

    if (keyword in str(movie['title']).lower() or keyword in str(movie['cast']).lower() or keyword in str(movie['genres']).lower() or keyword == str(
            movie['year']).lower()):
        cnt = cnt + 1
        print(movie['title'],end=",")

print ("\n"+ str(cnt)+" Movies found from the list that matches the Key Word")
if cnt == 0: print("Key word doesnt match, Please enter a Matching Keyword")

















