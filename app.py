from flask import Flask,render_template

app = Flask(__name__)

JOBS = [ {
    'id' : 1,
    'title' : 'Data Analyst',
    'Location' : 'Bangluru',
    'salary' : 'Rs. 10,00,000'
},
{
    'id' : 2,
    'title' : 'Web Developer',
    'Location' : 'Ahmedabad',
    'salary' : 'Rs. 6,00,000'
},
{
    'id' : 3,
    'title' : 'Cyber security Expert',
    'Location' : 'Remote',
    'salary' : 'Rs. 20,00,000'
}]

@app.route("/")
def helloworld():
    return render_template("home.html",jobs = JOBS,company_name = "Jovian")

if __name__ == "__main__":
    app.run(debug=True)