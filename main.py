from orkg import ORKG, Hosts
from dotenv import load_dotenv
import os

# Load the .env file so that we can access the environment variables with getenv()
load_dotenv() 

email = os.getenv("ORKG_EMAIL") 
password = os.getenv("ORKG_PASSWORD") 

if not (email and password):
    exit("Please set ORKG_EMAIL and ORKG_PASSWORD")

orkg = ORKG(host=Hosts.SANDBOX, creds=(email, password))

assert orkg.ping()

print("Connected to ORKG SandBox")

orkg.templates.materialize_template("R2127025")
print("Template materialized")

tp = orkg.templates

instance = tp.nlp4re_id_card(
    label="Dummy NLP4RE instance",
    _problem_tackled="Dummy problem",
    solution_proposed="Dummy solution",
    input_granularity="Dummy granularity",
    output_type="Dummy output",
    data_and_dataset="Dummy dataset",
    annotation_process="Dummy annotation",
    tool="Dummy tool",
    evaluation="Dummy evaluation"
)

result = instance.save()
print("Saved instance successfully:", result.content["id"])