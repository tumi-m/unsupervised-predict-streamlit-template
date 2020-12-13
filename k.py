"""

	Streamlit webserver-based Recommender Engine.

	Author: Explore Data Science Academy.

	Note:
	---------------------------------------------------------------------
	Please follow the instructions provided within the README.md file
	located within the root of this repository for guidance on how to use
	this script correctly.

	NB: !! Do not remove/modify the code delimited by dashes !!

	This application is intended to be partly marked in an automated manner.
	Altering delimited code may result in a mark of 0.
	---------------------------------------------------------------------

	Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
	and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Pickle dependencies
import pickle

#Image dependenices
from PIL import Image

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')


st.markdown('<style>body{background-color: #E5E0E0;}</style>',unsafe_allow_html=True)

#Simple Generic Title Tag function Generator
st.cache(suppress_st_warning=True,allow_output_mutation=True)
def title_tag(title):
	html_temp = """<div style="background-color:{};padding:10px;border-radius:10px; margin-bottom:15px;"><h2 style="color:white;text-align:center;">"""+title+"""</h2></div>"""
	st.markdown(html_temp, unsafe_allow_html=True)

#Simple Subheading style function
st.cache(suppress_st_warning=True,allow_output_mutation=True)
def subheading(title):
	html_temp = """<div style="background-color:{};padding:10px;margin-bottom:10px;"><h3 style="color:white;text-align:center;">"""+title+"""</h3></div>"""
	st.markdown(html_temp, unsafe_allow_html=True)

# App declaration
def main():
	 

	# DO NOT REMOVE the 'Recommender System' option below, however,
	# you are welcome to add more options to enrich your app.
	page_options = [ "Solution Overview", "Insights", "Recommender System", "About Us", "Contact Page"]
	st.markdown(
		"""
		<style>
		.sidebar .sidebar-content{
		background-image: linear-gradient(white, red);
		font-color: white;
		}
		</style>
		""",
		unsafe_allow_html=True,
		)
	
	# -------------------------------------------------------------------
	# ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
	# -------------------------------------------------------------------
	page_selection = st.sidebar.selectbox("Choose Option", page_options)
	if page_selection == "Recommender System":
		# Header contents
		st.write('# Movie Recommender Engine')
		st.write('### EXPLORE Data Science Academy Unsupervised Predict')
		st.image('resources/imgs/Image_header.png',use_column_width=True)
		# Recommender System algorithm selection
		sys = st.radio("Select an algorithm",
					   ('Content Based Filtering',
						'Collaborative Based Filtering'))

		# User-based preferences
		st.write('### Enter Your Three Favorite Movies')
		movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
		movie_2 = st.selectbox('Second Option',title_list[25055:25255])
		movie_3 = st.selectbox('Third Option',title_list[21100:21200])
		fav_movies = [movie_1,movie_2,movie_3]

		# Perform top-10 movie recommendation generation
		if sys == 'Content Based Filtering':
			if st.button("Recommend"):
				try:
					with st.spinner('Crunching the numbers...'):
						top_recommendations = content_model(movie_list=fav_movies,
															top_n=10)
					st.title("We think you'll like:")
					for i,j in enumerate(top_recommendations):
						st.subheader(str(i+1)+'. '+j)
				except:
					st.error("Oops! Looks like this algorithm does't work.\
							  We'll need to fix it!")


		if sys == 'Collaborative Based Filtering':
			if st.button("Recommend"):
				try:
					with st.spinner('Crunching the numbers...'):
						top_recommendations = collab_model(movie_list=fav_movies,
														   top_n=10)
					st.title("We think you'll like:")
					for i,j in enumerate(top_recommendations):
						st.subheader(str(i+1)+'. '+j)
				except:
					st.error("Oops! Looks like this algorithm does't work.\
							  We'll need to fix it!")


	# -------------------------------------------------------------------

	# ------------- SAFE FOR ALTERING/EXTENSION -------------------
	#Solution Overview Page
	if page_selection == "Solution Overview":
		st.title(page_selection)
		st.write('Introduction')
		html_temp = """<div style="background-color:{};padding:10px;margin-bottom:10px;"><h3 style="color:white;text-align:center;></div>"""
		st.markdown(html_temp, unsafe_allow_html=True)
		st.subheader("Recommender systems are systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the user is most likely to purchase and are of interest. Companies like Netflix and Amazon use recommender systems to help their users to identify the correct product or movies for them. Recommender systems are an important class of machine learning algorithms that offer relevant suggestions to users. The suggested items are as relevant to the user as possible so that the user can engage with those items: YouTube videos, news articles, online products, movie and series recommendation. Items are ranked according to their relevancy, and the most relevant ones are shown to the user. The relevance is determined by the recommender system, mainly based on historical data. For example, If you've recently watched YouTube videos about elephants, then YouTube is going to start showing you many elephant videos with similar titles and themes. Recommender systems are generally divided into two main categories: collaborative filtering and content-based systems.")

	#About Us page
	if page_selection == "About Us":
		st.title("TEAM 4 is a group of six members from EDSA comprising of Lesedi, Chuene, Kgomotso, Thabisile, Charles and Tumelo")
		st.subheader("Visit our Contact Page and lets get in touch!")

	if page_selection == "Insights":
		#title_tag("Insights extracted from the data")
		visual_options = [ "The top 15 movies", "Genres with the most number movies", "A count of films by directors", "Top 10 ratings", "Genre distribution", "Wordcloud", "Wordcloud analysis", "Model accuracy"]
		visual_selection = st.selectbox("Choose Exploratory Data Analaysis Visuas Option", visual_options)

		if visual_selection == "The top 15 movies":
			subheading('Top 15 movies by number of Ratings')
			st.image('resources/imgs/top_15_titles.png',use_column_width=True)
		elif visual_selection == "Genres with the most number movies":
			subheading('Genres with the most number movies')
			st.image('resources/imgs/Genres.png',use_column_width=True)
		elif visual_selection == "A count of films by directors":
			subheading('A count of films by directors')
			st.image('resources/imgs/director.png',use_column_width=True)
		elif visual_selection == "Wordcloud":
			subheading('Most Popular Movie Keywords')
			st.image('resources/imgs/wordcloud.png',use_column_width=True)
		elif visual_selection == "Top 10 ratings":
			subheading('Top 10 Movie Ratings')
			st.image('resources/imgs/top_10_ratings.png',use_column_width=True)
		elif visual_selection == "Genre distribution":
			subheading('Number of times a genre appears')
			st.image('resources/imgs/Genres_2.png',use_column_width=True)
		elif visual_selection == "Wordcloud analysis":
			subheading('Most Popular Movie Keywords analysis')
			st.image('resources/imgs/wordcloud_2.png',use_column_width=True)
		elif visual_selection == "Model accuracy":
			subheading('Model accuracy by means of RMSE score')
			st.image('resources/imgs/model_accuracy.png',use_column_width=True)
   
   
	#Building out the Contact Page
	if page_selection == "Contact Us":
		st.info("Lets get in touch for all your ML needs")
		firstname = st.text_input("Enter your Name", "Type Here Please...")
		lastname = st.text_input("Enter your last Name", "Type Here Please..")
		contactdetails = st.text_input("Enter your contact details here", "Type Here Please...")
		message = st.text_area("Tell us about your compaby's Data Science needs", "Type here Please..")
  
		if st.button("Submit"):
			result = message.title()
			st.success(result)


	

# Required to let Streamlit instantiate our web app. 
if __name__ == '__main__':
	main()