html_layout = '''
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            <link type="text/css" rel="stylesheet" href="/static/css/font-awesome-4.1.0.min.css" />
            <link type="text/css" rel="stylesheet" href="/static/css/bootstrap-3.1.1.min.css">
            <link type="text/css" rel="stylesheet" href="/static/css/bootstrap-theme-3.1.1.min.css" />
            <link type="text/css" rel="stylesheet" href="/static/css/layout.main.css" />
            <link type="text/css" rel="stylesheet" href="/static/css/main.css" />
            <link type="text/css" rel="stylesheet" href="/static/css/main.responsive.css" />
            <link type="text/css" rel="stylesheet" href="/static/css/main.quickfix.css" />

            <link rel="shortcut icon" href="/static/ico/favicon.png">
            <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/ico/apple-touch-icon-144-precomposed.png">
            <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/ico/apple-touch-icon-114-precomposed.png">
            <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/ico/apple-touch-icon-72-precomposed.png">
            <link rel="apple-touch-icon-precomposed" href="/static/ico/apple-touch-icon-57-precomposed.png">
            <link rel="shortcut icon" href="/static/ico/favicon.png">
            <script src="/static/js/libs/modernizr-2.8.2.min.js"></script>

            {%favicon%}
            {%css%}
        </head>
        <body>

        <div id="wrap">
            <!-- Fixed navbar -->
            <div class="navbar navbar-default navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Project name</a>
                </div>
                <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li><a href="{{ url_for('home') }}">Home</a></li>
                    <li><a href="{{ url_for('about') }}">About</a></li>
                    <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        <li><a>Action</a></li>
                        <li><a>Another action</a></li>
                        <li><a>Something else here</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Nav header</li>
                        <li><a>Separated link</a></li>
                        <li><a>One more separated link</a></li>
                    </ul>
                    </li>
                </ul>
                <ul class="nav navbar-nav pull-right">
                    <li><a href="{{ url_for('register') }}">Signup</a></li>
                    <li><a href="{{ url_for('login') }}">Login</a></li>
                </ul>
                </div><!--/.nav-collapse -->
            </div>
            </div>


            {%app_entry%}

            </div>

            <footer>
              <div id="footer">
                    <div class="container">
                    <p>Your Company &copy; All Rights Reserved.</p>
                    </div>
                </div>
                {%config%}
                {%scripts%}

                <script src="{{ url_for('static', filename='js/plots.js') }}"></script>
                <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                <script>window.jQuery || document.write('<script type="text/javascript" src="/static/js/libs/jquery-1.11.1.min.js"><\/script>')</script>
                <script type="text/javascript" src="/static/js/libs/bootstrap-3.1.1.min.js" defer></script>
                <script type="text/javascript" src="/static/js/plugins.js" defer></script>
                <script type="text/javascript" src="/static/js/script.js" defer></script>
                <script>
                window._gaq = [['_setAccount','UAXXXXXXXX1'],['_trackPageview'],['_trackPageLoadTime']];
                Modernizr.load({
                    load: ('https:' == location.protocol ? '//ssl' : '//www') + '.google-analytics.com/ga.js'
                });
                </script>
                {%renderer%}
            </footer>

        </body>
    </html>
'''
