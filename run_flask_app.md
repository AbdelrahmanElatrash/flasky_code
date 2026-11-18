use 
if __name__==("__main__):
    app.run(port=5000)

>> python app.py

or set env variable
FLASK_APP=app.py FLASK_DEBUG=true flask run


## get user data mvc patern
3 way 
1-  query parameter  
  url/foo ? key1=value1 ,key2=value2       request.args.get('key1')

2 form data 
 @app.route('/create')
 <form action="/create" method="POST,GET">  , action="name of the route"
 <input type=" " id=" " name="name">
 The name attribute on a form control element is the key used to retrieve data from request.get(<key>).
 request.form.get('name')  // request.form['name']

3 json data com via api
  request.data  --> str
  json.loads(request.data) --> convert to python object(dict)