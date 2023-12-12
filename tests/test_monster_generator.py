from unittest import TestCase
from libs.monster_generator import Monster



class TestMonster(TestCase):

    def test__init__(self):
        monster = Monster()
        monster1 = Monster(5, "gaetan", 10)
        monster2 = Monster(0, "gaetan", 100)
        monster3 = Monster(5, "gaetan", 1)

        # default value
        self.assertEquals(monster.damage, 2, "__init__ : defaulf value")
        self.assertEquals(monster.name, "no_name", "__init__ : defaulf value")
        self.assertEquals(monster.life, 100, "__init__ : defaulf value")

        # normal value
        self.assertEquals(monster1.damage, 5, "__init__ : normal value")
        self.assertEquals(monster1.name, "gaetan", "__init__ : normal value")
        self.assertEquals(monster1.life, 10, "__init__ : normal value")

        # normal : zero domage
        self.assertEquals(monster2.damage, 0, "__init__ : zero domage")
        self.assertEquals(monster2.name, "gaetan", "__init__ : zero domage")
        self.assertEquals(monster2.life, 100, "__init__ : zero domage")

        # normal : live = 1
        self.assertEquals(monster3.damage, 5, "__init__ : live = 1")
        self.assertEquals(monster3.name, "gaetan", "__init__ : live = 1")
        self.assertEquals(monster3.life, 1, "__init__ : live = 1")

        # raises valueError: domage = -10
        self.assertRaises(ValueError, Monster, -10, "gaetan", 10)

        # raises valueError: live  = 0
        self.assertRaises(ValueError, Monster, 5, "gaetan", 0)

        # raises valueError: live = -10
        self.assertRaises(ValueError, Monster, 5, "gaetan", -10)


    def test_every_day_life(self):

        #normal
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster()]
        colony_dict = {}

        main_monster.every_day_life(colony_dict, monster_list, 0, 2)
        self.assertEquals(monster_list[0].life,  99 ,"every_day_life : normal")

        # monster zero live (die)
        main_monster = Monster(5, "gaetan", 1)
        monster_list = [main_monster, Monster(), Monster()]
        colony_dict = {}

        main_monster.every_day_life(colony_dict, monster_list, 0, 2)
        self.assertEquals(len(monster_list),  2 ,"every_day_life : normal")



    def test_attack_colony(self):

        #deflault domages = 2
        colony = {'test' : {'workers' :{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20}}}
        self.assertEquals(len(Monster().attack_colony(colony)["test"]["workers"]), 18,"attack_colony : deflault domages = 2")

        #domange = 10
        colony = {'test' : {'workers' :{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20}}}
        self.assertEquals(len(Monster(10).attack_colony(colony)["test"]["workers"]), 10,"attack_colony : domange = 10")

        #domange = 0
        colony = {'test' : {'workers' :{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20}}}
        self.assertEquals(len(Monster(0).attack_colony(colony)["test"]["workers"]), 20,"attack_colony : domange = 0")

        #domange = 20 == nbr de fourmis
        colony = {'test' : {'workers' :{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20}}}
        self.assertEquals(len(Monster(20).attack_colony(colony)["test"]["workers"]), 0,"attack_colony : domange = 20 = nbr defourmis")

        #domange = 21 > nbr de fourmis
        colony = {'test' : {'workers' :{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20}}}
        self.assertEquals(len(Monster(21).attack_colony(colony)["test"]["workers"]), 0,"attack_colony : domange = 21 > nbr de fourmis")

        #domange = -1 (monster error)
        self.assertRaises(ValueError, Monster, -1)

        # no colony
        colony = {}
        self.assertEquals(Monster(10).attack_colony(colony), {},"attack_colony : no colony")

    def test_do_damage(self):
        monster = Monster()
        monster1 = Monster(11, "gaetan", 10)
        monster2 = Monster(11, "gaetan", 1)

        #default value
        monster.do_damage(1)
        self.assertEquals(monster.life, 99,"do_damage : default value")

        #live = 10
        monster1.do_damage(1)
        self.assertEquals(monster1.life, 9,"do_damage : live = 10")

        #live = 1
        monster2.do_damage(1)
        self.assertEquals(monster2.life, 0,"do_damage : live = 1")

        # domange = 0 (monster error)
        self.assertRaises(ValueError, Monster, -5)

        #domange = -5 (monster error)
        self.assertRaises(ValueError, Monster, -5)


    def test_attack_monsters(self):

        #default damage to the other monsters
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster()]

        main_monster.attack_monsters(monster_list,0)
        self.assertEquals(monster_list[1].life,98, 'attack_monsters : default damage to the other monsters' )
        self.assertEquals(monster_list[2].life, 98, 'attack_monsters : default damage to the other monsters')

        #defaulf, no domage to yourself
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster()]
        main_monster.attack_monsters(monster_list,0)

        self.assertEquals(monster_list[0].life, 100, 'attack_monsters : defaulf, no domage to yourself')
        self.assertEquals(monster_list[1].life,98, 'attack_monsters : defaulf, no domage to yourself' )
        self.assertEquals(monster_list[2].life, 98, 'attack_monsters : defaulf, no domage to yourself') #no domage to himself

        # one monster, no domage to yourself
        main_monster = Monster()
        monster_list = [main_monster]
        main_monster.attack_monsters(monster_list, 0)

        self.assertEquals(monster_list[0].life, 100, 'attack_monsters : one monster, no domage to yourself')


    def test_change_region(self):

        #test 3 monsters in list
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster()]
        main_monster.change_region(monster_list, 0)

        self.assertEquals(len(monster_list), 2, "change_region : test 3 monsters in list")

        # test 1 monsters in list
        main_monster = Monster()
        monster_list = [main_monster]
        main_monster.change_region(monster_list, 0)

        self.assertEquals(len(monster_list), 0, "change_region : test 1 monsters in list")


    def test_reproduce(self):
        # test 3 monsters in list
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster()]
        main_monster.reproduce(monster_list)

        self.assertEquals(len(monster_list), 4, "reproduce : test 3 monsters in list")

        # test 10 monsters in list
        main_monster = Monster()
        monster_list = [main_monster, Monster(), Monster(), Monster(), Monster(), Monster(), Monster(), Monster(), Monster(), Monster()]
        main_monster.reproduce(monster_list)

        self.assertEquals(len(monster_list), 11, "reproduce : test 10 monsters in list")

