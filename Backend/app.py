from flask import Flask

# Importing sub routes
from views.user import user_view
from views.expense import expense_view
from views.category import category_view

app = Flask(__name__)

@app.route("/" ,methods=['get'])
def index():
    return "Welcome to our expense tracker"

app.register_blueprint(user_view)
app.register_blueprint(expense_view)
app.register_blueprint(category_view)

if(__name__ == "__main__"):
    app.run(debug = True)