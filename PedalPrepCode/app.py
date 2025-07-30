from flask import Flask, render_template
from controllers.home_controller import HomeController
from controllers.bike_controller import BikeController
from controllers.checklist_controller import ChecklistController
from controllers.maintenance_controller import MaintenanceController
from views.home_view import HomeView
from models.bike_model import BikeModel
from models.maintenance_model import MaintenanceModel
from models.checklist_model import ChecklistModel
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
@app.route('/')
def home():
    # let the HomeView handle building and returning the HTML
    return home_view.display_home_screen()

if __name__ == "__main__":
    app.run(debug=True)
