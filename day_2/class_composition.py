#! /usr/bin/env python3
from collections import namedtuple

AutomobileTuple = namedtuple('AutomobileTuple', ['fuel_type'])

class Engine:
    def __init__(self, cylinders):
        self.cylinders = cylinders


# create instance of engine object and bind it to engine_1
engine_1 = Engine(cylinders=4)
id(engine_1)

class Automobile:
    def __init__(self, fuel_type='diesel', engine=Engine(cylinders=4)):
        self.fuel_type = fuel_type
        self.engine = engine

    def get_octane(self):
        if self.fuel_type == 'a':
            return 80
        elif self.fuel_type == 'b':
            return 90

# composition - 1 form of encapsulation
a = Automobile(fuel_type='diesel', engine=Engine(cyclinders='v6'))
a.get_octane()
b = Automobile(fuel_type='biodiesel')
b.get_octane()

# inheritance Truck is Automobile
class Truck(Automobile):
    pass

c = Truck()

# encapsulation - interface to a class - how it looks from a user's perspective

class EndPoint:
    def get_ip_address(self):
        return 192, 168, 100, 1

class Server(EndPoint):
    pass

class Client(EndPoint):
    pass


class ServerFarm():
    def __init__(self, endpoints):
        """ Constructor method """
        self.endpoints = endpoints




my_endpoints = [Client(), Client(), Server()]

server_farm = ServerFarm(endpoints=my_endpoints)


################## POLYMORPHISM
class RobotArm:
    def move(self,x,y,z):
        pass


class AnotherIndustrialRobot(RobotArm):
    def move(self, x,y,z):
        pass


class Yamaha(RobotArm):
    def __init__(self,x0,y0,z0):
        pass

    def set_max_speed(self, speed):
        pass

    def move(self, x,y,z):
        pass

#
yamaha_robot_arm = Yamaha(x0=2, y0=2.3, z0=0.2)
yamaha_robot_arm.set_max_speed(speed=2)
yamaha_robot_arm.move(x=3,y=3,z=0.2)

standard_robot = AnotherIndustrialRobot()
standard_robot.move(x=3,y=2,z=0.2)

def move_robot(some_robot_object, x,y,z):
    some_robot_object.move(x,y,z)

def add_bool_or_int(bool_or_int, b):
    sum = bool_or_int + b
    return sum


# INFORMATION HIDING
class MyAwesomeObject():
    def __init__(self,a,b):
        pass

    def really_good_method(self, blah):
        self._do_not_touch_this__(42)


    # private,
    def _do_not_touch_this__(self, please_leave_me_alone):
        pass

awesome_object = MyAwesomeObject(1,2)
awesome_object.really_good_method()

# class methods
class MyBlueprint():
    def __init__(self, constructor_params):
        self.params = constructor_params

    def some_special_method(self):
        print(id(self))
        pass

    @classmethod
    def blue_print_change(cls, x,y,z):
        print(id(cls))

object_from_blueprint1 = MyBlueprint('something')
object_from_blueprint1.some_special_method()
object_from_blueprint2 = MyBlueprint('something')
object_from_blueprint3 = MyBlueprint('something')

MyBlueprint.blue_print_change(1,2,3)
id(MyBlueprint)

# static methods
class NetworkUtilityFunctions():
    @staticmethod
    def parse_ip_address(ip_address):
        o1, o2, o3, o4 = ip_address
        return (bin(o1),bin(o2),bin(o3),bin(o4))


from class_composition import NetworkUtilityFunctions

NetworkUtilityFunctions.parse_ip_address()