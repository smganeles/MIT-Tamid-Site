from flask import Flask, request, redirect, url_for, render_template, request
from flask import session # as login_session

from databases import add_Member, All_Members, is_Member, is_Name, remove_Member

app = Flask(__name__, static_folder="static")
app.secret_key = "MY_SUPER_SECRET_KEY"

####################################################

####################################################

@app.route('/') #this is URL
def main():
	if not ('username' in session):
		session['username'] = ''
	return render_template('home.html', animate="True", Name=session['username']) #this page loads

@app.route('/home')
def home():
	if not ('username' in session):
		session['username'] = ''
	return render_template('home.html', animate="False", Name=session['username'])

@app.route('/about')
def about():
	return render_template("about.html") 

@app.route('/board')
def board():
	return render_template("board.html") 

@app.route('/portal', methods = ['GET','POST'])
def portal():
	if request.method == 'GET':
		return render_template("portal.html", Name=session['username']) 
	else:
		if request.form['action'] == "Sign Out":
			session['username'] = ''
			return redirect('home')

		elif request.form['action'] == "Remove Member":
			name = request.form['Name']
			remove_Member(name)
			print(name)
			return redirect('members')

		else:  #sign in or sign up
			name = request.form['Name']
			password = request.form['Password']

			if request.form['action']=="Sign Up Here":
				return render_template("portal.html", input_name=name, input_password=password)

			elif request.form['action']=="Sign Up":
				if not is_Name(name):	
					add_Member(name, password)
					return redirect('home')
				else:
					return render_template("portal.html", msg="That Name is Taken")

			elif request.form['action']=="Sign In":
				if is_Member(name, password):
					session['username'] = name
					return redirect('home')
				else:
					return render_template("portal.html", msg="Incorrect Name or Password") 

@app.route('/contact')
def contact():
	return render_template("contact.html") 

@app.route('/members')
def members():
	if request.method == 'GET':
		members_list = []
		for member in All_Members():
			members_list.append([member.Name, member.Password])
		return render_template("members.html", members = members_list)

####################################################

if __name__ == '__main__':
    app.run(debug=True, port=5019, threaded=False)