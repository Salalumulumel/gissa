import random
print("\n.:GissaTalet:.\n\n")

print("Gissa talet tre gånger för att få chansen att vinna en anka!")
slumptal = random.randint(1, 10)
antalgissningar = 1

print(slumptal)

while antalgissningar < 4 :
    antalgissningar = antalgissningar + 1
    spelarensval = input("gissa ett tal:")
    
    print(slumptal)
    print(spelarensval)
    
    if slumptal == int(spelarensval):
    print("Du vann en anka!")
    
    print(spelarensval)
    
    