

# google

1. neues projekt bei google:

console.cloud.google.com/cloud-resource-manager

neues projekt "rpi1"

2. api manager dashbord: enable 
search "google assistant" and enable

3. zugangsdaten für ga erstellen
download oauth json file


# install:

sudo apt install python3-dev  python3-venv

sudo apt install portaudio19-dev libffi-dev libssl-dev 


python3 -m venv env

env/bin/pip install pip setuptools --upgrade

source env/bin/activate

# in ubuntu i had to:
python -m pip install wheel

python -m pip install google-assistant-sdk[samples]


# authenticate 
python -m googlesamples.assistant.auth_helpers --client-secrets [pathToJson]

# try example: 
python -m googlesamples.assistant



# install soco
python -m pip install soco


# start webserver in folder:
python3 -m http.server 8080

http://patrick-thinkpad-x230.local:8080/out.wav


