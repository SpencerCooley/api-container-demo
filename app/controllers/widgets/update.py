from app.models.widgets import Widget
from sqlalchemy.orm.exc import NoResultFound


def update(db, data, record_id):
    try:
        # Retrieve the existing record from the database
        widget = db.query(Widget).filter(
            Widget.id == record_id).one()

        # Update the attributes based on the provided data
        for key, value in data.items():
            setattr(widget, key, value)

        # Commit the changes to the database
        db.commit()
        db.refresh(widget)

        return {
            "id": widget.id,
            "name": widget.name,
            "description": widget.description,
            "config": widget.config
        }

    except NoResultFound:
        return None
