from fillInitialBrands import createNextID

#Show Initial Models
def initialModels():
    modelsList = []
    return modelsList


#Add initial Models
def addModels(modelsList, newModel):
    nextID = createNextID(modelsList)
    newModel = {"id": nextID, "brandID": nextID, "model": newModel}
    modelsList.append(newModel)

    return newModel

myModels = initialModels()
addModels(myModels, "Clio")
addModels(myModels, "3008")
addModels(myModels, "A3")
addModels(myModels, "Kaptur")


brandsID = [i["brandID"] for i in myModels]
