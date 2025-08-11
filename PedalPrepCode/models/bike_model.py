from database import get_db


class BikeModel:
    def __init__(self):
        """
        Summary: Initializes the BikeModel and connects to the SQLite database.
        """
        pass

    def get_bike_info(self) -> dict:
        """
        Summary: Retrieves the user's registered bike information.

        Postcondition: Returns a dictionary with keys like 'type', 'brand', 'model',
                       or None if no bike is registered.
        """
        con = get_db()
        cursor = con.cursor()
        cursor.execute("SELECT bike_type, brand, model, year FROM bike_info LIMIT 1")
        row = cursor.fetchone()
        cursor.close()

        if row:
            return {"Type": row[0], "Brand": row[1], "Model": row[2], "Year": row[3]}
        else:
            return {}

    def create_or_update_bike(
        self, bike_type: str, brand: str, model: str = "", year: str = ""
    ) -> tuple[bool, str]:
        """
        Summary: Creates or updates the user's bike information in the database.

        Precondition: bike_type and brand are non-empty strings.
        Model and year are optional

        Postcondition: Saves the bike info and returns True if successful, False otherwise.
                        Also returns str with status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()
            if self.bike_exists():
                # Update the first existing row
                cursor.execute(
                    """
                    UPDATE bike_info
                    SET bike_type = ?, brand = ?, model = ?, year = ?
                    WHERE id = (SELECT id FROM bike_info LIMIT 1)
                """,
                    (bike_type, brand, model, year),
                )
            else:
                # Insert a new row
                cursor.execute(
                    """
                    INSERT INTO bike_info (bike_type, brand, model, year)
                    VALUES (?, ?, ?, ?)
                """,
                    (bike_type, brand, model, year),
                )

            con.commit()
            cursor.close()
            message = "Bike added sucessfully!, redirecting to home page..."
            return True, message

        except Exception as e:
            message = f"Error occured while trying to create or update the bike: {e}"
            return False, message

    def bike_exists(self) -> bool:
        """
        Summary: Checks if a bike is registered.

        Postcondition: Returns True if bike exists, False otherwise.
        """
        con = get_db()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM bike_info")  # Run queury to count the rows
        count = cursor.fetchone()[0]  # Fetch first column of first row
        cursor.close()
        return count > 0
