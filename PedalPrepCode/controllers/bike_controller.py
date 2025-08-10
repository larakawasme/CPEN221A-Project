from models.bike_model import BikeModel
class BikeController:
    def __init__(self, bike_model: BikeModel):
        """
        Summary: Initializes the controller with a reference to the BikeModel.

        Precondition: bike_model is an instance of BikeModel.
        """
        self.bike_model = bike_model

    def handle_bike_submission(self, bike_type: str, brand: str, model: str = "", year: str = "") -> tuple[bool, str]:
        """
        Summary: Handles bike registration form submission.

        Precondition: `bike_type` and `brand` are strings from the user's form input.
        Postcondition: Returns (True, "") on success, or (False, error_message) on failure.
        """
        
        return self.bike_model.create_or_update_bike(bike_type=bike_type, brand=brand, model=model)
 
    def get_bike_info(self) -> dict:
        """
        Summary: Retrieves bike information from the model.

        Postcondition: Returns a dictionary with bike details to populate the view.
        """
        return self.bike_model.get_bike_info()

