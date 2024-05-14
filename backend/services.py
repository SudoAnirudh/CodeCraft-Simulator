from models import db, User, Quest
import subprocess

def create_user(username, email):
    new_user = User(username=username, email=email, progress={})
    db.session.add(new_user)
    db.session.commit()
    return {"id": new_user.id, "username": new_user.username}

def run_code(user_id, code):
    try:
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        return {"output": output, "error": error}
    except Exception as e:
        return {"error": str(e)}
