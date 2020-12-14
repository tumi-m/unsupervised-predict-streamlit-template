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
	page_options =  ["Solution Overview", "Insights", "Recommender System", "Why Choose Us?", "About Us", "Contact Us"]
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
	#Home Page
	#if page_selection == "Home": 
	
	#Solution Overview Page
	if page_selection == "Solution Overview":
		overview_options = ["Problem Statement", "Introduction", "Conclusion"]
		overview_selection = st.selectbox("Please select an option to get an overview of the project", overview_options)
  
		if overview_selection == "Problem Statement":
			st.title('Problem Statement')
			break_h = """
				<br>
				<br>
				"""
			st.markdown(break_h, unsafe_allow_html=True)

			st.write('Accurately predict unseen movie ratings gathered from thousands of users based on their historic preferences. The objective of this App is to construct a recommendation algorithm based on content and collaborative filtering, capable of accurately predicting how a user will rate a movie they have not watched yet based on their historical preference.')
			
			break_h = """
				<br>
				<br>
				<br>
				"""
	
			st.markdown(break_h, unsafe_allow_html=True)

			st.image("resources/imgs/researcjh.png")
   
		if overview_selection == "Introduction":
			st.title('Introduction')
			break_h = """
				<br>
				<br>
				"""
			st.markdown(break_h, unsafe_allow_html=True)

			st.write('Recommender systems are systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the user is most likely to purchase and are of interest. Companies like Netflix and Amazon use recommender systems to help their users to identify the correct product or movies for them. Recommender systems are an important class of machine learning algorithms that offer relevant suggestions to users. The suggested items are as relevant to the user as possible so that the user can engage with those items: YouTube videos, news articles, online products, movie and series recommendation. Items are ranked according to their relevancy, and the most relevant ones are shown to the user. The relevance is determined by the recommender system, mainly based on historical data. For example, If you have recently watched YouTube videos about elephants, then YouTube is going to start showing you many elephant videos with similar titles and themes. Recommender systems are generally divided into two main categories: collaborative filtering and content-based systems. Both users and service providers have benefited from these kinds of systems. Intelligent algorithms can help viewers find great titles from tens of thousands of options. This notebook will construct a recommendation algorithm based on content and collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed based on their historic preferences. Providing an accurate and robust solution will have immense economic potential, with users of the system being exposed to content they would like to view or purchase - generating revenue and platform affinity.')
			
			break_h = """
				<br>
				<br>
				<br>
				"""
	
			st.markdown(break_h, unsafe_allow_html=True)

			st.image("resources/imgs/data.png")
   
		if overview_selection == "Conclusion":
			st.title('Conclusion')
			break_h = """
				<br>
				<br>
				"""
			st.markdown(break_h, unsafe_allow_html=True)
			
            st.write("Facebook, YouTube, LinkedIn are among the most used websites on the internet today that use recommender systems. Facebook suggests us to make more friends using the 'People You May Know' section. Similarly, LinkedIn recommends you connect with people you may know, and YouTube suggests relevant videos based on your previous browsing history. All of these are recommender systems in action. While most of the people are aware of these features, only a few know that the algorithms used behind these features are known as 'Recommender Systems'. They 'recommend' personalised content based on user's past / current preference to improve the user experience. We were tasked with accurately predicting unseen movie ratings gathered from thousands of users based on their historic preferences. Broadly, there are two types of recommendation systems: Content-Based and Collaborative filtering based as mention. In the notebook, we observation algorithms of both content-based and collaborative filtering. When we used the linear regression model (content-based) on the test data, it produced an RMSE score of 0.82565. However, the Singular Value Decomposition (collaborative-filtering) performed better on the test data with an RMSE score of 0.80773, which is our final score on the Kaggle leaderboard.")
			break_h = """
				<br>
				<br>
				<br>
				"""
	
			st.markdown(break_h, unsafe_allow_html=True)

			st.image("resources/imgs/dota.png")
	
	#About Us page
	if page_selection == "About Us":
		title = """
				<h2 style="color:black;text-align:center;">TEAM Four is a group of data scientists from EDSA</h2>
				"""
		st.markdown(title, unsafe_allow_html=True)
		
		st.image("resources/imgs/team.png",use_column_width=True)
	
	if page_selection == "Insights":
		#title_tag("Insights extracted from the data")
		visual_options = ["The top 15 movies", "Genres with the most number movies", "A count of films by directors", "Top 10 ratings", "Genre distribution", "Wordcloud", "Wordcloud analysis", "Model accuracy"]
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
   
   
   #Building out the business pitch
	if page_selection == "Why Choose Us?":
		st.title("Why Choose Us?")
  
		break_h = """
				<br>
				<br>
				"""
	
		st.markdown(break_h, unsafe_allow_html=True)
  
		st.write("Our team can help your organisation find interesting patterns and inisghts from available data. One such data science project we proud on working on is a recommender system. Recommender systems can mean big business for your organisation. Research shows that recommender systems can increase an organisation's turnover by up to 30%")
		  
		break_h = """
				<br>
				"""
	
		st.markdown(break_h, unsafe_allow_html=True)
  
		st.image('resources/imgs/data-science.png')
		
		
		
	#Building out the Contact Page
	if page_selection == "Contact Us":
		title = """
		<div style="background-color:#464e5f00;padding:5px;border-radius:10px;margin:10px;">
		<h3 style="color:black;text-align:center;">Lets get in touch for all your Machine Learning needs!</h3>
  		"""
		
		st.markdown(title, unsafe_allow_html=True)
		firstname = st.text_input("Enter your Name", "Type Here Please...")
		lastname = st.text_input("Enter your last Name", "Type Here Please..")
		contactdetails = st.text_input("Enter your contact details here", "Type Here Please...")
		message = st.text_area("What is company trying to achieve through data", "Type here Please..")
  
		if st.button("Submit"):
			result = message.title()
			st.success(result)


	

# Required to let Streamlit instantiate our web app. 
if __name__ == '__main__':
	main()
