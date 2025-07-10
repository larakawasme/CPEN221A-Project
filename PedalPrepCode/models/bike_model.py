class BikeModel:
    def __init__(self):
        """
        Summary: Initializes the BikeModel and connects to the SQLite database.
        """
        # Initialize database connection here (placeholder)
        pass

    def get_bike_info(self) -> dict:
        """
        Summary: Retrieves the user's registered bike information.

        Postcondition: Returns a dictionary with keys like 'type', 'brand', 'model',
                       or None if no bike is registered.
        """
        return {"Type": "Road",
                "Brand": "Fuji",
                "Model": "Sportif 1.1",
                "Year": 2023}

    def create_or_update_bike(self, bike_type: str, brand: str, model: str="", year: str="") -> bool:
        """
        Summary: Creates or updates the user's bike information in the database.

        Precondition: bike_type and brand are non-empty strings.
        Model and year are optional

        Postcondition: Saves the bike info and returns True if successful, False otherwise.
        """
        self.bike_exists() # Checks if bike exists to decided if need to update or create new one

        return True

    def bike_exists(self) -> bool:
        """
        Summary: Checks if a bike is registered.

        Postcondition: Returns True if bike exists, False otherwise.
        """
        return False
