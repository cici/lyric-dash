import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import nltk
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from wordcloud import WordCloud

# for NLP purpose
from nltk.corpus import stopwords
nltk.download('stopwords')

pd.options.plotting.backend = 'plotly'
tips = px.data.tips()

FONT_AWESOME = 'https://use.fontawesome.com/releases/v5.10.2/css/all.css'
CUSTOM_CSS = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

external_stylesheets = [dbc.themes.SPACELAB, FONT_AWESOME, CUSTOM_CSS]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash('Lyrics Analysis', external_stylesheets=[
#                'https://codepen.io/chriddyp/pen/bWLwgP.css'])
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


def get_songs_with_most_words(lyrics, n=None):
    df['word_count'] = df['lyrics'].apply(lambda x: len(str(x).split(" ")))
    sorted = df.sort_values(by=['word_count'], ascending=False)
    return sorted[['title', 'word_count']]


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

most_words = get_songs_with_most_words(df['lyrics'])

markdown_desc = '''
The is a music lyric analysis interactive dashboard.  Currently, all analysis is done using lyrics from Brandi Carlile.
The first tab does textual analysis on the lyrics of her 103 published songs.Using the second tab, you can analyse the sentiment of those lyrics.
'''

words_used_fig = px.bar(df, x=common_words.index,
                        y=common_words.values,
                        labels={'x': 'Word Used', 'y': 'Number of Times Used'})

most_words_fig = px.bar(df, x=most_words['title'], y=most_words['word_count'], labels={
                        'x': 'Song Title', 'y': 'Number of Words in Song'})

app.layout = html.Div([html.H1("Lyric Data Analysis", style={"textAlign": "center"}),
                       dcc.Markdown(markdown_desc),
                       dcc.Tabs(id="tabs", children=[
                           dcc.Tab(label='Text Analysis Tab', children=[
                               html.Div([
                                   html.H1("Song Lyrics Word Frequency", style={
                                       'textAlign': 'center', 'padding-top': 5}),
                                   dcc.Graph(
                                       id='frequency_word_bargraph',
                                       figure=words_used_fig)
                               ]),  # End of Div
                               html.Div([
                                   html.H1("Songs With Most Words", style={
                                       'textAlign': 'center', 'padding-top': 5}),
                                   dcc.Graph(
                                       id='most_used_bargraph',
                                       figure=most_words_fig)
                               ])  # End of Div
                           ]),  # End of Tab
                           dcc.Tab(label='Sentiment Analysis Tab', children=[])
                       ])  # End of Tabs
                       ])

"""
==========================================================================
Callbacks
"""

if __name__ == '__main__':
    app.run_server(debug=True)
