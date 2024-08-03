# #!/usr/bin/env python3

# from app import app
# from models import db # models go here
# from faker import Faker

# faker = Faker()

# if __name__ == '__main__':
#     with app.app_context():
#         print("Seeding database...")

#         # write your seeds here!

#         print("Seeding complete!")

#!/usr/bin/env python3

from app import app
from models import db , Items
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")



        Items.query.delete()
        items = []

        # write your seeds here!

        i = Items(image="image/boba.png", category="Artsy", name="Boba", price="4")
        items.append(i)

        i = Items(image="image/cat.png", category="Artsy", name="Cat with Flowers", price="4")
        items.append(i)

        i = Items(image="image/chatting.png", category="Artsy", name="Chill dude", price="4")
        items.append(i)

     
     

        db.session.add_all(items)
        db.session.commit()

        print("Seeding complete!")



        








