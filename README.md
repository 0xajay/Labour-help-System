# RESONANCE BACKEND

## usage
```
git clone
cd working_directory
```
Activate the Virtual Environment
```
virtualenv -p python3 [Environment_name]
source [Environment_name]/bin/activate
```
install the modules required
```
pip3 install -r requirements.txt
```
Database setup
```
1. Install a postgresql client(All Platforms) and create a database
2. assign the database details to the Environmental variables in run.sh file
3. SQLALCHEMY_DATABASE_URI='postgresql://[username_here]:[password_here]@localhost/[database_name]' as like
    'postgresql://postgres:1234@localhost/resonancedb'
```
run setup
```bash
export FLASK_APP=app.py
flask db init
source run.sh
```
