from fillInitialModels import myModels

def showAllModels(modelsList):
    allModels = [i["model"] for i in modelsList]
    return allModels

allInitialModels = showAllModels(myModels)
print(allInitialModels)