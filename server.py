from flask import Flask, render_template, url_for,request,redirect
import csv

app = Flask(__name__)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,delimiter=',', quotechar=':' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        #read about above line in csv documentation online

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')     #page changes according to the username and post_id provided
def hello(username=None, post_id=None):
    return render_template('firstWebsite.html', name=username, post_id=post_id)


@app.route('/<page>')  #we kept page as variable so it changes dynamically
def page_fuct(page):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()   #we receive data in form of dictionary {email,subject,message} which users submit in the contact page
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return "Something went wrong try again"
    return "form submitted"

