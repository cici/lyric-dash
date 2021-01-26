import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import nltk
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# for NLP purpose
from nltk.corpus import stopwords
nltk.download('stopwords')

pd.options.plotting.backend = "plotly"
app = dash.Dash('Lyrics Analysis', external_stylesheets=[
                'https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

df = pd.read_csv("./data/lyrics_corpus.csv")


def createStopWordList():
    # select english stopwords
    cachedStopWords = set(stopwords.words("english"))
    removeFromStopWords = {
        'against', 'myself', 'above', 'under', 'myself', 'himself', 'herself', 'yourselves', 'themselves', 'ourselves', 'between'}

    # add custom words
    cachedStopWords.update(
        ('i\'m', 'i\'ve', 'i\'ll', 'da', 'oh', 'ba', 'like', 'let'))
    finalStopWords = cachedStopWords - removeFromStopWords

    return finalStopWords


def get_top_words(lyrics, n=None):
    stops = createStopWordList()
    # convert to lower
    lowerLyrics = lyrics.apply(lambda x: ' '.join(
        [word for word in x.lower().split() if word not in (stops)]))
    # Remove Punctuations
    # df['lowerLyricsRemove'] = df['lowerLyrics'].str.replace('[^\w\s]', '')
    # Count Words
    countFreq = lowerLyrics.str.split(
        expand=True).stack().value_counts()[:100]
    return countFreq[:n]


common_words = get_top_words(df['lyrics'], 20)

markdown_desc = '''
The is a music lyric interactive dashboard.  In the first one you can choose whith which other companies to compare Facebook Stock Prices to anaylise main trends.
Using the second tab, you can analyse the distributions each of the Facebook Metrics Data Set features. Particular interest is on how paying to advertise posts can boost posts visibility. Finally, in the third tab a Machine Learning analysis of the considered datasets is proposed.
All the data displayed in this dashboard is fetched, processed and updated using Python (eg. ML models are trained in real time!).
'''
app.layout = html.Div([html.H1("Lyric Data Analysis", style={"textAlign": "center"}),
                       dcc.Markdown(markdown_desc),
                       dcc.Tabs(id="tabs", children=[
                           dcc.Tab(label='Text Analysis Tab', children=[
                               html.Div([
                                   html.H1("Song Lyrics Word Frequency", style={
                                       'textAlign': 'center', 'padding-top': 5}),
                                   dcc.Graph(
                                       id='frequency_word_bargraph',
                                       figure={
                                           'data': [
                                               {
                                                   'x': common_words.index,
                                                   'y': common_words.values,
                                                   'name': 'most used words',
                                                   'type': 'bar'
                                               }
                                           ],
                                           'layout': {
                                               'title': 'Song Lyrics Word Frequency',
                                               'x': 'Word Count',
                                               'y': 'Word Used'
                                           }
                                       })  # End of Graph
                               ], id='dash-container')
                           ]),  # End of Tab
                           dcc.Tab(label='Sentiment Analysis Tab', children=[])
                       ])  # End of Tabs
                       ])


if __name__ == '__main__':
    app.run_server(debug=True)
