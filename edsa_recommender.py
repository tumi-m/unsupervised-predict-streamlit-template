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

# App declaration
def main():
	 
	html_temp = """
	<div style="background-image:#025246 ;padding:5px">
	</div>
	"""
	st.markdown(html_temp, unsafe_allow_html = True)
	st.markdown('<style>body{background-color: Grey;}</style>',unsafe_allow_html=True)
 
   
	# DO NOT REMOVE the 'Recommender System' option below, however,
	# you are welcome to add more options to enrich your app.
	page_options = [ "EDA", "Solution Overview", "Recommender System", "About Us", "Contact Page"]
	st.markdown(
		"""
		<style>
		.sidebar .sidebar-content{
		background-image: linear-gradient(white, red);
		font color: white;
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
	if page_selection == "Solution Overview":
		st.title("Solution Overview")
		st.write("Describe your winning approach on this page")

	#About Us page
	if page_selection == "About Us":
		st.subheader("TEAM 4 is a group of six members from EDSA comprising of Lesedi, Chuene, Kgomotso, Thabisile, Charles and Tumelo")
		st.subheader("Visit our Contact Page and lets get in touch!")
	# You may want to add more sections here for aspects such as an EDA,
	# or to provide your business pitch.
	
	#Contact Page 
	if page_selection == "Contact Page":
		st.info("Lets get in touch for all your Machine Learning needs")
		firstname = st.text_input("Enter your Name", "Type Here Please...")
		lastname = st.text_input("Enter your last Name", "Type Here Please..")
		contactdetails = st.text_input("Enter your contact details here", "Type Here Please...")
		message = st.text_area("Tell us about your company's Data Science needs", "Type here Please..")

		if st.button("Submit"):
			result = message.title()
			st.success(result)
   
	if page_selection == "EDA":
		if st.checkbox("Film directors"):
			st.subheader("A count of films by directors")
			st.image('resources/imgs/director.png')
   
	
		if st.checkbox("Wordcloud"):
			st.subheader("Most common words")
			st.image('resources/imgs/wordcloud.png')
					 
		if st.checkbox("number of titles per year.png"):
			st.subheader("Number of movies every year from 1978 to 2015")
			st.image('resources/imgs/number_of_titles_per_year.png.png')
			
			
		if st.checkbox("Top genres"):
			st.subheader("Genres with the most number movies")
			st.image('resources/imgs/Genres.png')
					 
		if st.checkbox("Top 15"):
			st.subheader("The top 15 movies")
			st.image('resources/imgs/top_15_titles.png')


	

# Required to let Streamlit instantiate our web app. 
if __name__ == '__main__':
	main()
