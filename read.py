import os

username = os.environ.get("USERNAME_ENV")
password = os.environ.get("PASSWORD_ENV")

print("Username:", username)
print("Password:", password)