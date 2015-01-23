
class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastes_like(self):
        raise NotImplementedError("Subclasses are responsible for creating this method")


class HotDog(Food):
    def tast_like(self):
        print('%s is type %s ' % (self.name, HotDog))
        print('has %s calories' % self.calories)
        print('and tastes like Extremely processed meat')

class Hamburger(Food):
    def tast_like(self):
        print('%s is type %s ' % (self.name, Hamburger))
        print('has %s calories' % self.calories)
        print('and tastes like grilled goodness')


class ChickenPatty(Food):
    def tast_like(self):
        print('%s is type %s ' % (self.name, ChickenPatty))
        print('has %s calories' % self.calories)
        print('and tastes like chicken')

dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Mickey Mouse shaped Chicken Tenders', 170))

for course in dinner:
    course.tast_like()