from app.model.user import User
from app.model.database import Database


class UserDao:

  def find(self, login):
    conn = Database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, password FROM user WHERE name = ?;",
                   (login, ))
    row = cursor.fetchone()
    if row:
      user = User(row[0], row[1])
    else:
      user = None

    # Close the cursor and connection
    cursor.close()
    conn.close()
    return user

#  def register_user(self, registered_user):
#    conn = Database.get_connection()
#    cursor = conn.cursor()

#    cursor.execute("ADD user name = ?, password = ?;", (registered_user.name, 
#                                                        registered_user.password))

#    cursor.close()
#    conn.close()

  def register_user(self, user):
    conn = Database.get_connection()
    cursor = conn.cursor()
    new_user = (user.name, user.password)
    cursor.execute("INSERT INTO user (name, password) VALUES (?, ?);", new_user)
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()