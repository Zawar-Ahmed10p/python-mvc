
from execute import app,render_template,request,UserService

@app.route('/')
def login():
    return render_template('login_page.html')

@app.route("/authenticate",methods=['POST'])
def login_authentication():
    data=request.form
    if UserService().authenticate_user(data)==True:
        return render_template('home_page.html')
    else:
        return render_template('login_page.html',error="Name or Password incorrect")

@app.route('/signup',methods=['POST'])
def signup():
    return render_template('signup_page.html')
@app.route("/signup_user",methods=['POST'])
def signup_user():
    data=request.form
    if UserService().signup_user(data):
        return render_template('home_page.html')
    else:
        return render_template('login_page.html')

@app.route('/create',methods=['POST'])
def create():
    return render_template('create_page.html')

@app.route('/update',methods=['POST'])
def update():
    return render_template('update_page.html')

@app.route('/delete',methods=['POST'])
def delete():
    return render_template('delete_page.html')

@app.route('/search',methods=['POST'])
def search():
    return render_template('search_page.html')

@app.route('/create_user',methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        print(data['Name'])
        if UserService().create_user(data):
            return render_template('index.html', title="User Created", user=data)
        else:
            return "User not created"

@app.route('/update_user', methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        try:
            data = request.form
            print(data['Name'])
            UserService().update_user(data)
            return "User Updated"
        except:
            return "User not updated!"

@app.route('/delete_user', methods=['GET','POST'])
def delete_user():
    if request.method == 'POST':
        data = request.form
        print(data['Name'])
        UserService().delete_user(data["Id"])
    return "dele"


@app.route('/search_user', methods=['GET','POST'])
def search_user():
    if request.method == 'POST':
        data = request.form
        search_res=UserService().search_user(data)
        '''for it in search_res:
            print(it)'''
        return render_template('search_result.html', title="Search", segment_details=search_res)
    return "Not found!"


if __name__ == '__main__':
    app.run(debug=True)
