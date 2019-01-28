from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

from . import views
from . import models

models.create_table(models.Feed)
models.create_table(models.Device)
