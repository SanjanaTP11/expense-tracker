from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

FILE = 'expenses.json'

# Load data from JSON
def load_expenses():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except:
        return []

# Save data to JSON
def save_expenses(expenses):
    with open(FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

expenses = load_expenses()



@app.route('/')
def home():
    total = sum(int(exp['amount']) for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add():
    amount = request.form['amount']
    category = request.form['category']

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)