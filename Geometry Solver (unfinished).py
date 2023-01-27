#imports
import math
#stop undefined variable errors
stage1 = ("none")
stage2a = ("none")
stage2b = ("none")
stage2ab = ("none")
stage2ba = ("none")
#function defining
def angle_solver():
  stage2a = input("triangle, or other? ")
  if stage2a == ("triangle"):
    angle1 = input("What is your first angle measure? ")
    angle2 = input("What is your second angle measure? ")
    sumofangle = int(angle1) + int(angle2)
    anglemeasure = 180 - int(sumofangle)
    print("The missing angle measure of the triangle is " + str(anglemeasure))
  if stage2a == ("other"):
    numofsides = input("How many sides does your shape have? ")
    typeofangle = input("What angle do you need to solve for? (interior or exterior) ")
    exteriorangle = 360 / int(numofsides)
    if typeofangle == ("interior"):
      interiorangle = 180 - int(exteriorangle)
      print("Your shapes interior angles are " + str(interiorangle) + " degrees")
    if typeofangle == ("exterior"):
      print("Your shapes exterior angles are " + str(exteriorangle) + " degrees")
def side_solver():
  stage2b = input("Missing side length of a triangle or other shape? ")
  if stage2b == ("triangle"):
    stage2ab = input("Are you missing the hypotenuse length? (yes or no) ")
    if stage2ab == ("yes"):
      sideyes1 = input("What is your first side length? ")
      sideyes2 = input("What is your second side length? ")
      sideyes1s = int(sideyes1) ** 2
      sideyes2s = int(sideyes2) ** 2
      sidesiguessyes = sideyes1s + sideyes2s
      actualsideyes = math. sqrt(sidesiguessyes)
    print("The missing side length is " + str(actualsideyes))
    if stage2ab == ("no"):
      sideno1h = input("What is your hypotenuse length? ")
      sideno2 = input("What is your other side length? " )
      sideno1s = int(sideno1h) ** 2
      sideno2s = int(sideno2) **2
      sidesiguessno = sideno1s - sideno2s
      actualsideno = math. sqrt(sidesiguessno)
    print("The missing side length is " + str(actualsideno))
def area_solver():
  stage2ba = input("What type of shape do you have? (Supported shapes are triangle, square, pentagon, hexagon, octagon, nonagon, decagon) ")
  if stage2ba == ("triangle"):
    tribase = input("What is the length of the base of the triangle? ")
    triheight = input("What is the length of the height of the triangle? ")
    trimath1 = float(tribase) * float(triheight)
    triarea = float(trimath1) / float(2)
    print(str(triarea))
    if stage2ba == ("square"):
      sqrsidelength = input("What is the length of a side of the square? ")
      sqrarea = float(sqrsidelength) ** float(2)
      print(str(sqrarea))
    if stage2ba == ("hexagon"):
      hexsidelength = input("What is the length of one of the sides of the hexagon? ")
      hexmath1 = float(3) * math. sqrt(3)
      hexmath2 = float(hexmath1) / float(2)
      hexsidelength2 = float(hexsidelength) ** float(2)
      hexarea = hexmath2 * hexsidelength2
      print(str(hexarea))
    if stage2ba == ("octagon"):
      octsidelength = input("What is the length of one of the sides of the octagon? ")
      octsidelength2 = float(octsidelength) ** float(2)
      octmath1 = float(1) + math. sqrt(2)
      octmath2 = float(2) * float(octmath1)
      octarea = octmath2 * octsidelength2
      print(str(octarea))

    if stage2ba == ("nonagon"):
      nonsidelength = input("What is the length of one of the sides of the nonagon? ")
      nonsidelength2 = float(nonsidelength) ** float(2)
      nonmath1 = float(2.7474774194546)
      nonmath2 = float(9) / float(4)
      nonarea = nonmath2 * nonsidelength2 * nonmath1
      print(str(nonarea))
    if stage2ba == ("decagon"):
      decsidelength = input("What is the length of one of the sides of the decagon? ")
      decsidelength2 = float(decsidelength) ** float(2)
      decmath1 = math.sqrt(5)
      decmath2 = math.sqrt(5+2*decmath1)
      decmath3 = 5/2
      decarea = decmath3 * decsidelength2 * decmath2
      print(decarea)
def perimeter_solver():
  if stage1 == "perimeter":
    shape = input("What shape do you need the perimeter of? (Supported shapes are triangle, rectangle (rectangle also works for square), regular pentagon, regular hexagon, regular octagon: ")
    if shape == "triangle":
      side1 = input("What is the first side length of the triangle?: ")
      side2 = input("What is the second side length of the triangle?: ")
      side3 = input("What is the third side length of the triangle?: ")
      triperimeter = int(side1) + int(side2) + int(side3)
      print("The perimeter of the triangle is " + str(triperimeter))
    if shape == "rectangle":
      side1 = input("What is the length of the rectangle?: ")
      side2 = input("What is the width of the rectangle?: ")
      rectperimeter = int(side1) + int(side1) + int(side2) + int(side2)
      print("The perimeter of the rectangle is" + str(rectperimeter))
    if shape == "pentagon":
      side1 = input("What is the length of one of the sides of the pentagon?: ")
      pentperimeter = 5 * int(side1)
      print("The perimeter of the pentagon is: " + str(pentperimeter))
    if shape == "hexagon":
      side1 = input("What is the side length of one of the sides of the hexagon?: ")
      hexperimeter = 6 * int(side1)
      print("The perimeter of the hexagon is " + str(hexperimeter))
stage1 = input("Do you need to solve for angle measures, side lengths, area, or perimiter? (Hint: Must be typed exactly): ")
if stage1 == ("angle measures"):
  angle_solver()
if stage1 == ("side lengths"):
  side_solver()
if stage1 == ("area"):
  area_solver()

if stage1 == ("perimeter"):
  perimeter_solver()