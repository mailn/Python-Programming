#!/usr/bin/env python

# TestClassChinaCoin.py
import ClassicalChinaCoin, Square
import Metal as Metal
import sys, getopt

def usage():
    print ('Usage: TestClassChinaCoin.py -h')
    print ('Usage: TestClassChinaCoin.py -r <radius> -s <side> -a <age> -m <material>')
    print ('Usage: TestClassChinaCoin.py --radius=<radius> --side=<side> --age=<age> --material=<material>')

def main(argv):
    radius = ''
    side = ''
    age = ''
    material = ''   

    try:
        opts, args = getopt.getopt(argv,"hr:s:a:m:",["radius=", "side=", "age=", "material="])
    except getopt.GetoptError:
        usage()
            
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-r", "--radius"):
            radius = arg
        elif opt in ("-s", "--side"):
            side = arg
        elif opt in ("-a", "--age"):
            age = arg
        elif opt in ("-m", "--material"):
            material = arg    

    print("***** My Coin by default *****")
    square = Square.Square(1)
    metal = Metal.Metal('cupper')
    myCoin = ClassicalChinaCoin.ClassicalChinaCoin(3, square, 600, metal)
    print (myCoin.toString())
    if myCoin.isValid():
        print("My coin is valid.")
    else:
        print("My coin is invalid.")
    print("------------------")
    
    print("***** Change my coin *****")
    myCoin.setRadius(radius)
    myCoin.getSquare().setSide(side)
    myCoin.setAge(age)
    myCoin.getMetal().changeMaterial(material);
    print (myCoin.toString())
    if myCoin.isValid():
        print("My coin is valid.")
    else:
        print("My coin is invalid.")
    print("-----------")

    print("***** Destroy my coin *****")
    myCoin.destroy()
    print (myCoin.toString())
    if myCoin.isValid():
        print("My coin is valid.")
    else:
        print("My coin is invalid.")
    print("-----------")

if __name__ == '__main__':
    main(sys.argv[1:])
