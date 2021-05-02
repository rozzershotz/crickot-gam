from hashlib import new
import random

class Randomiser:
    
    __first_names_m = ["Jack","Lewis","Ryan","Cameron","James","Andrew","Liam","Matthew","Jamie","Callum","Ross","Jordan","Daniel","Kieran","Connor","Scott","Kyle","David","Adam","Dylan","Michael","Ben","Thomas","Craig","Nathan","Sean","John","Aaron","Calum","Christopher","Alexander","Robert","Euan","Joshua","Declan","Aidan","Mark","Robbie","Luke","Fraser","Reece","William","Ewan","Joseph","Paul","Brandon","Lee","Owen","Josh","Samuel","Finlay","Stuart","Rhys","Stephen","Rory","Jake","Steven","Sam","Jay","Benjamin","Ethan","Harry","Shaun","Aiden","Darren","Blair","Marc","Dean","Taylor","Angus","Gregor","Conor","Jonathan","Patrick","Ciaran","Greg","Jason","George","Logan","Peter","Bradley","Max","Arran","Mohammed","Morgan","Oliver","Gary","Murray","Louis","Martin","Alan","Alistair","Grant","Joe","Keir","Duncan","Leon","Mitchell","Nicholas","Tyler"]

    _first_names_f = ["Chloe","Amy","Lauren","Emma","Rebecca","Megan","Caitlin","Rachel","Erin","Hannah","Sophie","Lucy","Emily","Shannon","Katie","Nicole","Sarah","Courtney","Anna","Morgan","Eilidh","Kirsty","Niamh","Laura","Olivia","Ellie","Abbie","Jennifer","Holly","Jade","Bethany","Louise","Beth","Zoe","Robyn","Heather","Aimee","Cara","Leah","Jessica","Charlotte","Rachael","Jodie","Samantha","Georgia","Natasha","Taylor","Iona","Eve","Molly","Kayleigh","Stephanie","Claire","Melissa","Danielle","Gemma","Chelsea","Natalie","Amber","Abby","Caitlyn","Lauryn","Catherine","Lisa","Brooke","Elizabeth","Isla","Nicola","Jenna","Abigail","Alexandra","Jordan","Rebekah","Katherine","Victoria","Kelsey","Carly","Kate","Fiona","Mhairi","Grace","Alice","Cerys","Skye","Demi","Alana","Ciara","Kirsten","Kiera","Paige","Chantelle","Jasmine","Morven","Kimberley","Jemma","Ashleigh","Casey","Eva","Sara","Siobhan"]

    __surnames = ["SMITH","JONES","BROWN","TAYLOR","WILSON","DAVIES","EVANS","JOHNSON","THOMAS","ROBERTS","WALKER","WRIGHT","THOMPSON","ROBINSON","WHITE","HALL","HUGHES","GREEN","EDWARDS","MARTIN","WOOD","CLARKE","HARRIS","JACKSON","LEWIS","CLARK","TURNER","SCOTT","HILL","MOORE","WILLIAMS","COOPER","WARD","MORRIS","KING","WATSON","HARRISON","BAKER","YOUNG","ALLEN","MORGAN","ANDERSON","MITCHELL","PHILLIPS","JAMES","BELL","CAMPBELL","LEE","KELLY","DAVIS","PARKER","BENNETT","MILLER","SHAW","COOK","SIMPSON","RICHARDSON","PRICE","MARSHALL","COLLINS","CARTER","STEWART","BAILEY","GRIFFITHS","GRAY","MURPHY","MURRAY","COX","ADAMS","RICHARDS","GRAHAM","ELLIS","WILKINSON","FOSTER","RUSSELL","CHAPMAN","ROBERTSON","MASON","WEBB","ROGERS","POWELL","GIBSON","HUNT","MILLS","HOLMES","PALMER","MATTHEWS","REID","FISHER","BARNES","KNIGHT","OWEN","HARVEY","LLOYD","BUTLER","THOMSON","BARKER","PEARSON","STEVENS","JENKINS"]

    def get_player_name(self, gender):
        if gender.upper() == "M":
            return random.choice(self.__first_names_m) + " " + random.choice(self.__surnames)
        if gender.upper() == "W":
            return random.choice(self._first_names_f) + " " + random.choice(self.__surnames)
        return random.choice(self._first_names_f + self.__first_names_m) + " " + random.choice(self.__surnames)
        
    def ball_type(self):
        types = "....111122446W"
        newtypes = list(types)
        edq = random.choice(newtypes)
        return edq
        
    def dismissal_type(self):
        tipes = ["bowled", "caught", "stumped", "run out", "caught and bowled", "hit wicket"]
        das = random.choice(tipes)
        return das