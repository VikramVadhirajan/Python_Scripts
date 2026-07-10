class Movie:
    '''Movie class created for understanding the concept of class and object'''
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero  = hero
        self.heroine  = heroine

    def info(self):
        print("the movie name: ", self.title)
        print("the Hero name: ", self.hero)
        print("the heroine name:", self.heroine)


list_of_movies=[]
while True:
    title=input("Enter Movie Name: ")
    hero=input("Enter Hero Name: ")
    heroine=input("Enter heroine Name: ")
    m=Movie(title, hero, heroine)
    list_of_movies.append(m)
    print("Movie added to list sucessfully")
    option=input("Do you want to add another movie [Yes/No]")
    if option.strip().lower()=="no":
        break

print("All Movie infromation")
print("#"*40)

for movie in list_of_movies:
    movie.info()
    print("#"*40)



