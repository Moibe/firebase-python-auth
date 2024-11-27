import firebase_admin
import json

#data_python = json.loads("config.json")

# build credentials with the service account dict
creds = firebase_admin.credentials.Certificate("config.json")


app = firebase_admin.initialize_app(creds)

if __name__ == "__main__":
    print(app)