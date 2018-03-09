class Perscription:

    def __init__(self, withFood, timesPerDay, timeOfDay, perscriptionNumber, pharmacy, drugName ):
        self.withFood = withFood   # this is a way to type a variable.
        self.timesPerDay = timesPerDay
        self.timeOfDay = timeOfDay
        self.perscriptionNumber = perscriptionNumber
        self.pharmacy = pharmacy
        self.drugName = drugName
        self.id_front = ''
        self.id_back = ''
        self.shape = ''


    def setDrugName(self, drugName): ## how to set the internal self variable.
        self.setDrugName(drugName)


class PillDispencer():

    def __init__(self)
        self.perscriptions = []  #  a empty list for the perscriptions that it holds.
        self.daysOfWeek = [Monday, Tuesday, Wednesday, Thursday, Friday]
        self.daysOfWeekend = [Saturday, Sunday]
        self.fullWeek = [self.daysOfWeek, self.daysOfWeekend]



