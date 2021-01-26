import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import nltk
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn.feature_extraction.text import CountVectorizer

# for NLP purpose
from nltk.corpus import stopwords
nltk.download('stopwords')

pd.options.plotting.backend = "plotly"
app = dash.Dash()
server = app.server

df = pd.read_csv("./data/lyrics_corpus.csv")


markdown_desc = '''
The is a music lyric interactive dashboard.  In the first one you can choose whith which other companies to compare Facebook Stock Prices to anaylise main trends.
Using the second tab, you can analyse the distributions each of the Facebook Metrics Data Set features. Particular interest is on how paying to advertise posts can boost posts visibility. Finally, in the third tab a Machine Learning analysis of the considered datasets is proposed.
All the data displayed in this dashboard is fetched, processed and updated using Python (eg. ML models are trained in real time!).
'''

app.layout = html.Div([html.H1("Lyric Data Analysis", style={"textAlign": "center"}),
                       dcc.Markdown(markdown_desc),
                       dcc.Tabs(id="tabs", children=[
                           dcc.Tab(label='Text Analysis', children=[
                               html.Div([
                                   html.H1("Facebook Stocks High vs Lows", style={
                                       'textAlign': 'center', 'padding-top': 5}),
                                   dcc.Dropdown(id='my-dropdown', options=[{'label': 'Tesla', 'value': 'TSLA'}, {'label': 'Apple', 'value': 'AAPL'}, {'label': 'Facebook', 'value': 'FB'}, {'label': 'Microsoft', 'value': 'MSFT'}],
                                                multi=True, value=['FB'], style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "80%"}),
                                   dcc.Graph(id='highlow'),  dash_table.DataTable(
                                       id='table2',
                                       columns=[{"name": i, "id": i}
                                                for i in df.describe().reset_index().columns],
                                       data=df.describe().reset_index().to_dict("rows"),
                                   ),
                                   html.H1("Facebook Market Volume", style={
                                       'textAlign': 'center', 'padding-top': 5}),
                                   dcc.Dropdown(id='my-dropdown2', options=[{'label': 'Tesla', 'value': 'TSLA'}, {'label': 'Apple', 'value': 'AAPL'}, {'label': 'Facebook', 'value': 'FB'}, {'label': 'Microsoft', 'value': 'MSFT'}],
                                                multi=True, value=['FB'], style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "80%"}),
                                   dcc.Graph(id='volume'),
                                   html.H1("Scatter Analysis", style={
                                       'textAlign': 'center', 'padding-top': -10}),
                                   dcc.Dropdown(id='my-dropdown3',
                                                options=[{'label': 'Tesla', 'value': 'TSLA'}, {'label': 'Apple', 'value': 'AAPL'},
                                                         {'label': 'Facebook', 'value': 'FB'}, {'label': 'Microsoft', 'value': 'MSFT'}],
                                                value='FB',
                                                style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "45%"}),
                                   dcc.Dropdown(id='my-dropdown4',
                                                options=[{'label': 'Tesla', 'value': 'TSLA'}, {'label': 'Apple', 'value': 'AAPL'},
                                                         {'label': 'Facebook', 'value': 'FB'}, {'label': 'Microsoft', 'value': 'MSFT'}],
                                                value='AAPL',
                                                style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "45%"}),
                                   dcc.RadioItems(id="radiob", value="High", labelStyle={'display': 'inline-block', 'padding': 10},
                                                  options=[{'label': "High", 'value': "High"}, {
                                                      'label': "Low", 'value': "Low"}, {'label': "Volume", 'value': "Volume"}],
                                                  style={'textAlign': "center", }),
                                   dcc.Graph(id='scatter')
                               ], className="container"),
                           ]),
                           dcc.Tab(label='Sentiment Analysis', children=[

                           ])
                       ])
                       ])


def get_top_words(lyrics, n=None):
    stop = stopwords.words('english')
    # convert to lower
    lowerLyrics = lyrics.apply(lambda x: ' '.join(
        [word for word in x.lower().split() if word not in (stop)]))
    # Remove Punctuations
    #df['lowerLyricsRemove'] = df['lowerLyrics'].str.replace('[^\w\s]', '')
    # Count Words
    countFreq = lowerLyrics.str.split(
        expand=True).stack().value_counts()[:100]
    return countFreq[:n]


def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


common_words = get_top_n_words(df['lyrics'], 20)
for word, freq in common_words:
    print(word, freq)
df1 = pd.DataFrame(common_words, columns=['lyrics', 'count'])
df1.groupby('lyrics').sum()['count'].sort_values(ascending=False).iplot(
    kind='bar', yTitle='Count', linecolor='black', title='Top 20 words in review before removing stop words')

if __name__ == '__main__':
    app.run_server(debug=True)
