#UnitConverter

def converter():
    measurementDictionary = {1: 'Length', 2: 'Weight',3:'Temperature',4:'Volume',5:'Area'}
    print("Select choice of unit converter from below : ","\n")
    printChoices(measurementDictionary)
    choice = int(input("\n""Enter your choice : "))

    lengthUnits = {1: 'Milimeter', 2: 'Centimeter',3:'Foot',4:'Meter',5:'Kilometer',6:'Mile'}
    weightUnits = {1: 'Miligram', 2: 'Gram',3:'Kilogram',4:'Pound',5:'MetricTon'}
    temperatureUnits = {1:'Celsius',2:'Kelvin',3:'Fahrenheit'}
    volumeUnits = {1: 'CubicMilimeter', 2: 'CubicCentimeter',3:'CubicFoot',4:'CubicMeter',5:'CubicKilometer',6:'CubicMile'}
    areaUnits = {1: 'SquareMilimeter', 2: 'SquareCentimeter',3:'SquareFoot',4:'SquareMeter',5:'SquareKilometer',6:'SquareMile'}
    fileName = measurementDictionary[choice]
    

    if measurementDictionary[choice] == 'Length': 
        print("\n","Select current unit from below -",sep='')
        printChoices(lengthUnits)
        fromUnit = int(input("\n""Current unit of Lenght : "))

        print("Select unit to which you want to convert the Length: ")
        printChoices(lengthUnits)
        toUnit = int(input("\n""Unit of Length You want to convert to : "))

        value = float(input("\n""Enter value of Lenght for conversion : "))
        lines = readFile(fileName)

        convertUnit(lines, lengthUnits, fromUnit, toUnit, value)
    
    elif measurementDictionary[choice] == 'Weight':
                
        print("\n","Select current unit from below -",sep='')
        printChoices(weightUnits)
        fromUnit = int(input("\n""Current unit of Weight : "))

        print("Select unit to which you want to convert the Weight: ")
        printChoices(weightUnits)
        toUnit = int(input("\n""Unit of Weight You want to convert to : "))

        value = float(input("\n""Enter value of Weight for conversion : "))
        lines = readFile(fileName)
        
        convertUnit(lines, weightUnits, fromUnit, toUnit, value)

    elif measurementDictionary[choice] == 'Temperature':
                
        print("\n","Select current unit from below -",sep='')
        printChoices(temperatureUnits)
        fromUnit = int(input("\n""Current unit of Temperature : "))

        print("Select unit to which you want to convert the Temperature: ")
        printChoices(temperatureUnits)
        toUnit = int(input("\n""Unit of Temperature You want to convert to : "))

        value = float(input("\n""Enter value of Temperature for conversion : "))
        lines = readFile(fileName)
        
        convertTempUnit(lines, temperatureUnits, fromUnit, toUnit, value)

    elif measurementDictionary[choice] == 'Volume':
                
        print("\n","Select current unit from below -",sep='')
        printChoices(volumeUnits)
        fromUnit = int(input("\n""Current unit of Volume : "))

        print("Select unit to which you want to convert the Volume: ")
        printChoices(volumeUnits)
        toUnit = int(input("\n""Unit of Volume You want to convert to : "))

        value = float(input("\n""Enter value of Volume for conversion : "))
        lines = readFile(fileName)
        
        convertUnit(lines, volumeUnits, fromUnit, toUnit, value)

    elif measurementDictionary[choice] == 'Area':
                
        print("\n","Select current unit from below -",sep='')
        printChoices(areaUnits)
        fromUnit = int(input("\n""Current unit of Area : "))

        print("Select unit to which you want to convert the Area: ")
        printChoices(areaUnits)
        toUnit = int(input("\n""Unit of Area You want to convert to : "))

        value = float(input("\n""Enter value of Area for conversion : "))
        lines = readFile(fileName)
        
        convertUnit(lines, areaUnits, fromUnit, toUnit, value)


def printChoices(choices):
    for choice in choices:
        print(str(choice)+"."+choices[choice])


def readFile(fileName):
    with open(fileName.lower()+'.txt') as p:
        lines = p.readlines()
        p.close()
    return lines


def convertUnit(lines, Units, fromUnit, toUnit, value):
    for line in lines:
        s = line.split(" ")
        if s[1] == Units[fromUnit] and s[4] == Units[toUnit]:
            print('\n')
            print(f"{value} {Units[fromUnit]} = {value*float(eval(s[3]))} {Units[toUnit]}","\n")


def convertTempUnit(lines, Units, fromUnit, toUnit, value):
    for line in lines:
        s = line.split(" ")
        if s[1] == Units[fromUnit] and s[4] == Units[toUnit]:          
            
            if (s[1] == 'Celsius' or s[1] == 'Kelvin') and (s[4] == 'Celsius' or s[4] == 'Kelvin'):
                print('\n')
                print(f"{value} {Units[fromUnit]} = {value+float(s[3])} {Units[toUnit]}","\n")
            
            elif s[1] == 'Celsius' and s[4] == 'Fahrenheit':
                print('\n')
                print(f"{value} {Units[fromUnit]} = {value*1.8+float(s[3])} {Units[toUnit]}","\n")
            
            elif s[1] == 'Fahrenheit' and s[4] == 'Celsius':
                print('\n')
                print(f"{value} {Units[fromUnit]} = {(value+float(s[3]))*(5/9)} {Units[toUnit]}","\n")
            
            elif s[1] == 'Kelvin' and s[4] == 'Fahrenheit':
                print('\n')
                print(f"{value} {Units[fromUnit]} = {(value-273.15)*1.8+float(s[3])} {Units[toUnit]}","\n")
            
            else:
                print('\n')
                print(f"{value} {Units[fromUnit]} = {(value+float(s[3]))*(5/9)+273.15} {Units[toUnit]}","\n")

converter()


