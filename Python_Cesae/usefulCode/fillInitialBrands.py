#Show initial brands
def fillInitialBrand():
    brandList = []
    return brandList

#Add Next ID
def createNextID(list):
    nextID = len(list) + 1
    return nextID

#Add initial brands
def addBrandToList(brandList, brandName):
    nextID = createNextID(brandList)
    newBrand = {"id": nextID, "brand": brandName}
    brandList.append(newBrand)

initialBrands = fillInitialBrand()

addBrandToList(initialBrands, "Renaul")
addBrandToList(initialBrands, "Pegeot")
addBrandToList(initialBrands, "Audi")
addBrandToList(initialBrands, "BMW")