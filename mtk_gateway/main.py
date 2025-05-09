from fastapi import FastAPI
from mtk_refusals.main import app as refusals_app
from mtk_craft.main import app as craft_app

app = FastAPI()

app.mount("/refusals", refusals_app)
app.mount("/craft", craft_app)
