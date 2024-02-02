from app.models.widgets import Widget
from sqlalchemy.orm.exc import NoResultFound


def read(db, record_id):
    try:
        # Retrieve the record from the database based on the ID
        db_widget = db.query(Widget).filter(
            Widget.id == record_id).one()
        return {
            "id": db_widget.id,
            "name": db_widget.name,
            "description": db_widget.description,
            "config": db_widget.config,
        }
    except NoResultFound:
        # Handle the case where the record with the given ID is not found
        return None


# find all records
def read_all(db):
    # Retrieve all records from the database
    db_widgets = db.query(Widget).all()

    records_list = [
        {
            "id": widget.id,
            "name": widget.name,
            "description": widget.description,
            "config": widget.config
        }
        for widget in db_widgets
    ]

    return records_list
