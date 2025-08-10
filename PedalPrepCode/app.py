from flask import Flask
from controllers.home_controller import HomeController
from controllers.bike_controller import BikeController
from controllers.checklist_controller import ChecklistController
from controllers.maintenance_controller import MaintenanceController
from views.home_view import HomeView
from views.add_bike_view import AddBikeView
from models.bike_model import BikeModel
from models.maintenance_model import MaintenanceModel
from models.checklist_model import ChecklistModel
from database import initialize_tables
from database import close_db

app = Flask(__name__)
# Initialize models
bike_model = BikeModel()
maintenance_model = MaintenanceModel()
checklist_model = ChecklistModel()

# Initialize Controllers
home_controller = HomeController(bike_model=bike_model, maintenance_model=maintenance_model)
bike_controller = BikeController(bike_model=bike_model)
checklist_controller = ChecklistController(checklist_model=checklist_model, maintenance_model=maintenance_model)
maintenance_controller = MaintenanceController(maintenance_model=maintenance_model)

# Initialize Views
home_view = HomeView(controller=home_controller)
add_bike_view = AddBikeView(controller=bike_controller)

@app.route('/')
def home():
    # let the HomeView handle building and returning the HTML
    return home_view.display_home_screen()

@app.route("/add-bike", methods=["GET", "POST"])
def add_bike():
    return add_bike_view.display_bike_registration_form()

@app.teardown_appcontext
def teardown_db(exception):
    close_db()

if __name__ == "__main__":
    initialize_tables()
    app.run(debug=True)


