import pandas as pd 
import numpy as np 
import neattext.functions as nfx
from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import tkinter as tk 


def read_data():
    df = pd.read_csv("C:\\Users\\ashwa\\projects\\nlp_project\\books.csv", on_bad_lines='skip', encoding="ISO-8859-1")
    return df


def cosine_simat(vec):
    return cosine_similarity(vec)


def get_vec(df):
    countvec = CountVectorizer()
    vec = countvec.fit_transform(df['clean_title'])
    return vec

def get_clean_title(df):
    df['title'] = df['title'].str.lower().str.strip()
    df['clean_title'] = df['title'].apply(nfx.remove_stopwords)
    df['clean_title'] = df['clean_title'].apply(nfx.remove_special_characters)
    return df



def recommend_books(df, title_name, cosine_sim, num_rec):
    book_index = pd.Series(df.index, index = df['title']).drop_duplicates()
    index = book_index[title_name]
    scores = list(enumerate(cosine_sim[index]))
    sorted_scores = sorted(scores, key=lambda x:x[1] , reverse = True)
    selected_book_index = [i[0] for i in sorted_scores[1:num_rec]]
    selected_book_score = [i[1] for i in sorted_scores[1:num_rec]]
    rec_df = df.iloc[selected_book_index].copy()
    rec_df['Similarity_Score'] = selected_book_score
    final_recommended_books = rec_df[['bookID', 'title', 'authors', 'average_rating', 'language_code', 'Similarity_Score']]

    return final_recommended_books



df = read_data()
df = get_clean_title(df)
vec = get_vec(df)
num_rec = 6
cosine_sim = cosine_simat(vec)


root = tk.Tk()
root.title("Personalized Book Recommendation System")
root.geometry("600x400")

def submit_title():
    title_name = entry.get()
    print(f"Title entered: {title_name}")
    
    rec_df = recommend_books(df, title_name, cosine_sim, num_rec)
    
    if not rec_df.empty:
        result_text = "\n\n".join([f"{row['title']}   by   {row['authors']}  -  Score: {row['Similarity_Score']:.2f}" for _, row in rec_df.iterrows()])
        label_result.config(text=result_text)
        print(result_text)  
    else:
        result_text = "Book not found"
        label_result.config(text=result_text)
        print(result_text)  



label_prompt = tk.Label(root, text="Enter the book title:")
label_prompt.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button_submit = tk.Button(root, text="Submit", command=submit_title)
button_submit.pack()

label_result = tk.Label(root, text="", justify="left")
label_result.pack()

root.mainloop()