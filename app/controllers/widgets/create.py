from app.models.widgets import Widget


def create(db, data):
    db_widget = Widget(**data)
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)

    return {
        "id": db_widget.id,
        "name": db_widget.name,
        "description": db_widget.description,
        "config": db_widget.config
    }
