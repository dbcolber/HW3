from flask import Flask, request, render_template
import json
import requests
import re
import omdb
import wikipedia

app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

#Route 1 / FORM that sends data to be used in next view function

@app.route('/form')
def artist_form():
	return render_template('form1.html')

#Route 2 // view function

@app.route('/formresults', methods=["POST", "GET"])
def getting_results():
	if request.method == 'GET':
		result = request.args
		user_query = result.get('movie_title')
		user_query += ' (film)'
		movie_data = wikipedia.search(user_query)

		wiki_page = wikipedia.WikipediaPage(movie_data[0])

		wiki_summary = wiki_page.summary

		return render_template('datamanip.html', result=wiki_summary)

if __name__ == '__main__':
	app.run(debug=True)
