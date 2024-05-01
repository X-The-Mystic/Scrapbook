# Prerequisites
* `python3 -v` == `3.x`
* `pip install google-api-python-client`
* `pip install google-auth-httplib2`
* `pip install google-auth-oauthlib`
* Google account with GMail
* Browser (*somewhere*)

# Quickstart
```
git clone https://github.com/py660/RickMail.git
cd RickMail
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#### Download credentials.json
python3 main.py
```

# How to get `credentials.json`
1. Go to the [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Click <kbd>[Create Credentials](#null)</kbd>, then <kbd>[OAuth client ID](#null)</kbd>
3. Select <kbd>[Desktop](#null)</kbd>, then name the OAuth client something descriptive, such as `Email Rick-roll Bot`
4. Click <kbd>[Create](#null)</kbd>, then save the credentials as a JSON file (resulting in `credentials.json` being downloaded)
5. Ensure the `credentials.json` is in the same directory as `main.py`
