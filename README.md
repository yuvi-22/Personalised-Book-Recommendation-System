# Personalised-Book-Recommendation-System


A system that recommends books of same type based on cosine similarity

The dataset used here is the books.csv from kaggle.


# Flow of code :
1) Reading data
2) preprocessing the 'title'  column in dataset ( converting to lower case and removing stopwords to get better cosine correlation
3) converting the cleaned 'title' column to vectors
4) finding cosine similarity of these vectors
5) taking user input
6) enumerating the cosine similarities of the given book with respect to all other books in dataset
7) sorting the books in descending order based on cosine similarities
8) taking the 'title', 'author', and 'Similarity Score' of the top 5 books
9) printing the recommended books

for the GUI , I used the tkinter library ( cause I dont know html , CSS, and javascript and i dont want to learn also  unless , in the future , my job role requires me to , 
L me )


