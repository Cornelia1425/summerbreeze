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

        i = Items(image="image/cool-monkey.png", category="Monkeys", name="Cool monkey", price="3")
        items.append(i)

        i = Items(image="image/creativity (1).png", category="Artsy", name="Creative journal", price="5")
        items.append(i)

        i = Items(image="image/creativity.png", category="Artsy", name="Spark of creativity", price="6")
        items.append(i)

        i = Items(image="image/dab-monkey.png", category="Monkeys", name="Dab monkey", price="5")
        items.append(i)

        i = Items(image="image/done.png", category="Quotes", name="It's always possible", price="4")
        items.append(i)

        i = Items(image="image/dream-big.png", category="Quotes", name="Dream big", price="6")
        items.append(i)

        i = Items(image="image/eat.png", category="Artsy", name="Ramen eater", price="6")
        items.append(i)

        i = Items(image="image/glass-of-lemon.png", category="Artsy", name="Summer day", price="6")
        items.append(i)

        i = Items(image="image/idea.png", category="Artsy", name="Cutesy pencil", price="6")
        items.append(i)

        i = Items(image="image/kind.png", category="Quotes", name="Be kind to yourself", price="5")
        items.append(i)

        i = Items(image="image/live.png", category="Quotes", name="Live, Laugh, Love", price="5")
        items.append(i)

        i = Items(image="image/new-ideas-in-process.png", category="Artsy", name="New Ideas In Process", price="6")
        items.append(i)

        i = Items(image="image/photo-editing.png", category="Artsy", name="Let's take pics", price="5")
        items.append(i)

        i = Items(image="image/pinata-monkey.png", category="Monkeys", name="Pinata monkey", price="4")
        items.append(i)

        i = Items(image="image/planet.png", category="Artsy", name="Planet", price="6")
        items.append(i)

        i = Items(image="image/progress.png", category="Quotes", name="Progress Not Perfection", price="5")
        items.append(i)

        i = Items(image="image/proud.png", category="Quotes", name="Keep Going", price="5")
        items.append(i)

        i = Items(image="image/rainbow.png", category="Artsy", name="Rainbow", price="5")
        items.append(i)

        i = Items(image="image/ramen-monkey.png", category="Monkeys", name="Ramen monkey", price="4")
        items.append(i)

        i = Items(image="image/self.png", category="Quotes", name="Take time for yourself", price="6")
        items.append(i)

        i = Items(image="image/slay.png", category="Quotes", name="Wake up & slay", price="6")
        items.append(i)

        i = Items(image="image/smore.png", category="Quotes", name="Cutesy S'more", price="7")
        items.append(i)

        i = Items(image="image/space.png", category="Quotes", name="Enjoying my space", price="5")
        items.append(i)

        i = Items(image="image/spirit.png", category="Quotes", name="That's the spirit", price="5")
        items.append(i)

        i = Items(image="image/time.png", category="Quotes", name="Great things take time", price="6")
        items.append(i)

        i = Items(image="image/vibes.png", category="Quotes", name="Only Good Vibes", price="6")
        items.append(i)

        i = Items(image="image/watermelon-monkey.png", category="Monkeys", name="Watermelon monkey", price="5")
        items.append(i)

        i = Items(image="image/you-are.png", category="Quotes", name="Be Proud", price="6")
        items.append(i)

        i = Items(image="image/you-can.png", category="Quotes", name="You can do anything", price="7")
        items.append(i)

        i = Items(image="image/yum-monkey.png", category="Monkeys", name="Yum monkey", price="5")
        items.append(i)

        db.session.add_all(items)
        db.session.commit()

        print("Seeding complete!")



        








