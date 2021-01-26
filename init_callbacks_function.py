def init_callbacks(app, countFreq):
    @app.callback(
        [dash.dependencies.Output('frequency_word_bargraph', 'figure'),
         dash.dependencies.Output('matplotlib-graph', 'src')],
        [dash.dependencies.Input('range_frequency_number', 'value')])
    def update_graph(value):

        newGraph = countFreq[value[0]:value[1]]
        wordcloud = WordCloud(height=500, width=500, background_color="white",
                              contour_color='white', colormap="magma").generate_from_frequencies(newGraph)
        buf = io.BytesIO()  # in-memory files
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig(buf, format="png", dpi=600, bbox_inches='tight',
                    pad_inches=0)  # save to the above file object
        data = base64.b64encode(buf.getbuffer()).decode(
            "utf8")  # encode to html elements
        plt.close()

        return [
            {
                'data': [
                    {
                        'x': newGraph.index,
                        'y': newGraph.values,
                        'name': 'first example in Dash',
                                'type': 'bar'
                    }
                ],
                'layout': {
                    'title': 'Coronvirus Tweet Word Frequency.'
                }
            },
            "data:image/png;base64,{}".format(data)
        ]
