import os


print("Jenkins Credentials")
username = os.getenv("JENKINS_USERNAME")
password = os.getenv("JENKINS_PASSWORD")

print('Username: ', username)
print('Password: ', password)