import os
from flask_script import Manager

from blog import app
from blog.database import session, Entry

# creates an instance of the manager object using our app
manager = Manager(app)

@manager.command # adds a command to the manager object
def run(): # primarily for testing, ensuring that everything was configured correctly
    port = int(os.environ.get('PORT', 8080)) # tries to retrieve a port number from the environment, falling back to port 8080 if it is unavailable
    app.run(host='0.0.0.0', port = port) # this runs the server
    
@manager.command
def seed():
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    
    for i in range(25):
        entry = Entry(
            title="Test Entry #{}".format(i), content=content
        )
        session.add(entry)
    session.commit()
    print("entries added")
            
    
if __name__ == "__main__":
    manager.run()
    
# note, it is useful to use environment variables as it allos us to deploy on servers which don't have a fixed outgoing port or deploy multiple servers each using a different outgoing port w/o having to change our code