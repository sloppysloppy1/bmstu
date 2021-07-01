import pyodbc
from time import sleep
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Output, State, Input
from dash.exceptions import PreventUpdate
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api


counter = 0
str_to_write = ''


print("Идет загрузка БД, пожалуйста, подождите...")
cnxn = pyodbc.connect(driver='{SQL Server}', Server='DESKTOP-IEVL6PF', database='course_project',
                     trusted_connection='yes')
    
cursor = cnxn.cursor()
print("БД была успешно загружена")



cursor.execute("select id, name, first_author, year, extra_info from book")
books = cursor.fetchall()


columns_of_books = ['id','name','author','year','extra_info']


def print_books(input_str):
    
    global cursor, str_to_write, counter
    
    cursor.execute("select * from book where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1
    amount_of_authors = book[0][2]

    if amount_of_authors == 1:
        str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
        if book[0][7] != None:
            str_to_write += u": {} / {} — {}: {}, {}. — {} с.".format(book[0][7], book[0][3], book[0][8], book[0][10],
                                                                     book[0][11], book[0][12])
        else:
            str_to_write += u" / {} — {}: {}, {}. — {} с.".format(book[0][3], book[0][8], book[0][10],
                                                                     book[0][11], book[0][12])

    elif amount_of_authors == 2:
        str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
        if book[0][7] != None:
            str_to_write += u": {} / {}, {} — {}: {}, {}. — {} с.".format(book[0][7], book[0][3], book[0][4], book[0][8], book[0][10],
                                                                     book[0][11], book[0][12])
        else:
            str_to_write += u" / {}, {} — {}: {}, {}. — {} с.".format(book[0][3], book[0][4], book[0][8], book[0][10],
                                                                     book[0][11], book[0][12])

    elif amount_of_authors == 3:
        str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
        if book[0][7] != None:
            str_to_write += u": {} / {}, {}, {} — {}: {}, {}. — {} с.".format(book[0][7], book[0][3], book[0][4],
                                                                        book[0][5], book[0][8], book[0][10],
                                                                        book[0][11], book[0][12])
        else:
            str_to_write += u" / {}, {}, {} — {}: {}, {}. — {} с.".format(book[0][3], book[0][4], book[0][5],
                                                                 book[0][8], book[0][10],
                                                                 book[0][11], book[0][12])
    elif amount_of_authors == 4:
        str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
        if book[0][7] != None:
            str_to_write += u": {} / {}, {}, {}, {} — {}: {}, {}. — {} с.".format(book[0][7], book[0][3], book[0][4],
                                                                        book[0][5], book[0][6],book[0][8], book[0][10],
                                                                        book[0][11], book[0][12])
        else:
            str_to_write += u" / {}, {}, {}, {}  — {}: {}, {}. — {} с.".format(book[0][3], book[0][4], book[0][5],
                                                                 book[0][6],book[0][8], book[0][10],
                                                                 book[0][11], book[0][12])


def print_regdoc(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from regulatory_doc where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} [Текст]".format(book[0][1])
    str_to_write += u": {} // {}. — {}. — № {}. — Ст. {}.".format(book[0][3], book[0][4], book[0][5], book[0][6],book[0][8])


def print_regtechdoc(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from regulatory_tech_doc where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} [Текст]".format(book[0][1])
    str_to_write += u": {}. — {}: {}, {}. — {} c.".format(book[0][3], book[0][5], book[0][6], book[0][7],book[0][8])


def print_patent(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from patent where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} [Текст]".format(book[0][1])
    str_to_write += u"/ {}; {} — {} c.".format(book[0][3], book[0][7], book[0][10])


def print_infosheet(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from info_sheet where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
    str_to_write += u"/ {}. — {}, {}. — [{}] c. — {}.".format(book[0][3], book[0][8], book[0][9],book[0][10], book[0][7])
 
 
def print_manypages(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from multi_volume where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{}. {} [Текст]".format(book[0][3], book[0][1])
    str_to_write += u": {} / {}; {} — {}, {}. — {} c. — {} т.".format(book[0][7], book[0][3], book[0][9], book[0][8],  book[0][10], book[0][10],book[0][11], book[0][12])


def print_elec_internet(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from elec_internet where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{}. {} [Электронный ресурс]".format(book[0][3], book[0][1])
    str_to_write += u": / {}. — {}. — {}: {}, {}. — Режим доступа: {}, свободный.".format(book[0][3], book[0][7], book[0][8], book[0][9],book[0][11],book[0][12])


def print_elec_cd(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from elec_local where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} {} [Электронный ресурс]".format(book[0][3], book[0][1])
    str_to_write += u":{} / {} — {}. — {}: {}, {}. — {}.".format(book[0][7], book[0][3], book[0][8], book[0][9], book[0][10],book[0][12],book[0][13])
  
  
def print_review(input_str):
    global cursor, str_to_write, counter
    
    cursor.execute("select * from book_article where name = '{}'".format(input_str))
    book = cursor.fetchall()
    str_to_write += "\n\\bibitem{{litlink{}}} ".format(counter)
    
    counter += 1

    str_to_write += u"{} {} [Текст]".format(book[0][3], book[0][1])
    str_to_write += u" / {} // {}. — {}, {} — C. {} - {}.".format(book[0][3], book[0][7], book[0][8], book[0][9],  book[0][10], book[0][11])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, )

server = Flask('my_app')
app = dash.Dash(server=server, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
api = Api(server)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello')


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    html.H1(
        children='Курсовой проект,',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }
    ),

    html.Div(children='позволяющий сформировать список литературы для TeX', style={
        'textAlign': 'center',
        'color': '#7FDBFF'
    }),

    html.Label('Для начала следует создать файл:'),
    html.Button(children = 'Создать файл', id='first_button', n_clicks = 0),
    html.Div(id="output0", children=' '),
    
    html.Label('Введите название желаемой книги/документа/статьи etc.:'),
    dcc.Input(id = 'input1', type='text'),
    
    html.Label('Выберите тип источника:'),
    dcc.Dropdown(id = 'input2',
        options=[
            {'label': u'Книга', 'value': '1'},
            {'label': u'Нормативно-правовой документ', 'value': '2'},
            {'label': u'Нормативно-технический документ', 'value': '3'},
            {'label': u'Авторское свидетельство, патент', 'value': '4'},
            {'label': u'Информационные листки', 'value': '5'},
            {'label': u'Многотомные издания', 'value': '6'},
            {'label': u'Диссертации', 'value': '7'},
            {'label': u'Электронный ресурс локального доступа (CD)', 'value': '8'},
            {'label': u'Электронный ресурс удаленного доступа (Internet)', 'value': '9'},
            {'label': u'Статья из книги', 'value': '10'},
            {'label': u'Статья  из журнала', 'value': '11'},
            {'label': u'Рецензия', 'value': '12'}
        ]
    ),
    html.Br(),
    html.Button(children = 'Добавить книгу', id='button', n_clicks = 0),
    html.Div(id="output", children=' '),

    html.Label('После того, как все книги добавлены:'),
    html.Button(children = 'Получить файл', id='last_button', n_clicks = 0),
    html.Div(id="output2", children=' '),
    html.Br(),
    html.Label('Тут можно посмотреть, что есть в БД:'),
    dcc.Dropdown(id = 'input3',
        options=[
            {'label': u'Книга', 'value': '1'},
            {'label': u'Нормативно-правовой документ', 'value': '2'},
            {'label': u'Нормативно-технический документ', 'value': '3'},
            {'label': u'Авторское свидетельство, патент', 'value': '4'},
            {'label': u'Информационные листки', 'value': '5'},
            {'label': u'Многотомные издания', 'value': '6'},
            {'label': u'Диссертации', 'value': '7'},
            {'label': u'Электронный ресурс локального доступа (CD)', 'value': '8'},
            {'label': u'Электронный ресурс удаленного доступа (Internet)', 'value': '9'},
            {'label': u'Статья из книги', 'value': '10'},
            {'label': u'Статья  из журнала', 'value': '11'},
            {'label': u'Рецензия', 'value': '12'}
        ], value = '1'
    ),
    
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in columns_of_books],
    data=[dict(zip(columns_of_books, d)) for d in books],
    editable=True
    ),

    html.Br(),
    dcc.Link('Добавить запись в БД', href='/add'),
    ])


add_layout = html.Div([
    html.H1(
        children='Добавление записей в БД',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF'
        }
    ),

    html.Label('Здесь можно добавить источник информации в БД.'),
    html.Br(),
    html.Label('Выберите, какой тип документа Вы хотите добавить:'),
    dcc.Dropdown(id = 'input4',
        options=[
            {'label': u'Книга', 'value': '1'},
            {'label': u'Нормативно-правовой документ', 'value': '2'},
            {'label': u'Нормативно-технический документ', 'value': '3'},
            {'label': u'Авторское свидетельство, патент', 'value': '4'},
            {'label': u'Информационные листки', 'value': '5'},
            {'label': u'Многотомные издания', 'value': '6'},
            {'label': u'Диссертации', 'value': '7'},
            {'label': u'Электронный ресурс локального доступа (CD)', 'value': '8'},
            {'label': u'Электронный ресурс удаленного доступа (Internet)', 'value': '9'},
            {'label': u'Статья из книги', 'value': '10'},
            {'label': u'Статья  из журнала', 'value': '11'},
            {'label': u'Рецензия', 'value': '12'}
        ], value = '1'
    ),
    html.Br(),
    html.Label('Тут можно посмотреть, что есть в БД:'),
    dcc.Dropdown(id = 'input3',
        options=[
            {'label': u'Книга', 'value': '1'},
            {'label': u'Нормативно-правовой документ', 'value': '2'},
            {'label': u'Нормативно-технический документ', 'value': '3'},
            {'label': u'Авторское свидетельство, патент', 'value': '4'},
            {'label': u'Информационные листки', 'value': '5'},
            {'label': u'Многотомные издания', 'value': '6'},
            {'label': u'Диссертации', 'value': '7'},
            {'label': u'Электронный ресурс локального доступа (CD)', 'value': '8'},
            {'label': u'Электронный ресурс удаленного доступа (Internet)', 'value': '9'},
            {'label': u'Статья из книги', 'value': '10'},
            {'label': u'Статья  из журнала', 'value': '11'},
            {'label': u'Рецензия', 'value': '12'}
        ], value = '1'
    ),
    
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in columns_of_books],
    data=[dict(zip(columns_of_books, d)) for d in books],
    editable=True
    ),
    html.Br(),
    dcc.Link('Вернуться назад', href='/'),
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    
    if pathname == '/add':
        return add_layout
    else:
        return index_page


@app.callback(Output('table', 'data'),
    [Input('input3', 'value')])
def load_table(value):
    
    global cursor, columns_of_books

    if value == '1':
    
        cursor.execute("select id, name, first_author, year, extra_info from book")
        books = cursor.fetchall()
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '2':
    
        cursor.execute("select id, name, first_author, year, extra_info from regulatory_doc")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '3':
    
        cursor.execute("select id, name, first_author, year, extra_info from regulatory_tech_doc")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '4':
    
        cursor.execute("select id, name, first_author, year, journal_num from patent")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '5':
    
        cursor.execute("select id, name, first_author, year, extra_info from info_sheet")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '6':
    
        cursor.execute("select id, name, first_author, year, extra_info from multi_volume")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '7':
    
        cursor.execute("select id, name, author, year, extra_info from not_published_yet")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '8':
    
        cursor.execute("select id, name, first_author, year, extra_info from elec_local")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]
    
    if value == '9':
    
        cursor.execute("select id, name, first_author, year, extra_info from elec_internet")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]
        
    if value == '10':
    
        cursor.execute("select id, name, first_author, year, extra_info from book_article")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '11':
    
        cursor.execute("select id, name, first_author, year, extra_info from newspaper_article")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

    if value == '12':
    
        cursor.execute("select id, name, first_author, year, extra_info from book_review")
        books = cursor.fetchall()
    
        return [dict(zip(columns_of_books, d)) for d in books]

   
@app.callback(Output('output', 'children'),
    [Input('button','n_clicks')],
    [State('input1', 'value'), State('input2', 'value')],
)
def update_output(n_clicks, input_str, type_of):
    global str_to_write, f
    
    if int(n_clicks) >= 1:
        if int(type_of) == 1: 
            cursor.execute("select * from book where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_books(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][3])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."

        if int(type_of) == 2: 
            cursor.execute("select * from regulatory_doc where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_regdoc(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][4])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."
            
        if int(type_of) == 3: 
            cursor.execute("select * from regulatory_tech_doc where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_regtechdoc(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][4])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."

        if int(type_of) == 4: 
            cursor.execute("select * from patent where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_patent(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][4])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."
            
        if int(type_of) == 5: 
            cursor.execute("select * from info_sheet where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_infosheet(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][4])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."

        if int(type_of) == 6: 
            cursor.execute("select * from multi_volume where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_manypages(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][4])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."
            
        if int(type_of) == 8: 
            cursor.execute("select * from elec_local where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_elec_cd(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][3])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."
            
        if int(type_of) == 9: 
            cursor.execute("select * from elec_internet where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_elec_internet(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][3])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."

        if int(type_of) == 10: 
            cursor.execute("select * from book_article where name = '{}'".format(input_str))
            book = cursor.fetchall()
            if book != []:
                n_clicks = 0
                print_review(input_str)
                return "Вы добавили '" + str(book[0][1]) + "', автор - " + str(book[0][3])
            else:
                return "К сожалению, такого источника в нашей библиотеке (еще) нет.."


@app.callback(Output('output2', 'children'),
    [Input('last_button','n_clicks')],
)
def get_the_file(n_clicks):
    global str_to_write, f
    
    if int(n_clicks) >= 1:
        str_to_write += "\n\\end{thebibliography}"
        f.write(str_to_write)
        f.close()
        str_to_write = ''
        return("Запись в файл прошла успешно!")


@app.callback(Output('output0', 'children'),
    [Input('first_button','n_clicks')],
)
def get_the_file2(n_clicks):
    global str_to_write, f
    
    if int(n_clicks) >= 1:
        f = open("list_references.txt", "w")
        str_to_write += ("\\newpage \n\\addcontentsline{toc}{section}{" +
        "\\tocsecindent{Список литературы}} \n\n\\begin{thebibliography}{}")
        return("Файл был успешно создан!")
    

if __name__ == '__main__':
    
    app.run_server(debug=True)
    


