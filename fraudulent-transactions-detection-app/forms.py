"""Sign-up, query & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    Length,
    DataRequired
)

class Request(FlaskForm):
    """Transaction's Properties Form."""
    TX_TIME_DAYS = StringField(
        'day of month',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW = StringField(
        'customer average amount - day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW = StringField(
        'customer average amount - 7 day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW = StringField(
        'customer average amount - 30 day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    TERMINAL_ID_RISK_1DAY_WINDOW = StringField(
        'terminal id risk - 1 day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    TERMINAL_ID_RISK_7DAY_WINDOW = StringField(
        'terminal id risk - 7 day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )
    TERMINAL_ID_RISK_30DAY_WINDOW = StringField(
        'terminal id risk - 30 day window',
        validators=[
            Length(min=1, message='Must be a number'),
            DataRequired()
        ]
    )

    submit = SubmitField('Classify Transaction')