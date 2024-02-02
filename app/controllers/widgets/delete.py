from app.models.widgets import Widget
from sqlalchemy.orm.exc import NoResultFound


def delete(db, record_id):
    try:
        # Retrieve the existing record from the database
        db_widget = db.query(Widget).filter(
            Widget.id == record_id).one()

        # Delete the record
        db.delete(db_widget)
        db.commit()

        return {
            "message": "Record deleted successfully",
            "id": record_id
        }
    except NoResultFound:
        # Handle the case where the record with the given ID is not found
        return {
            "message": "Record not found",
            "id": record_id
        }
