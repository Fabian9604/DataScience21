# class ListKeeper inherits from dict. It contains additional methods to be able to store named lists
class ListKeeper(dict):
    # each object of ListKeeper contains an example list [1,2,3,4,5]
    def __init__(self):
        dict.__init__(self)
        self['example'] = [1,2,3,4,5]
        #to check the type, it is printed
        print (type(self))
    # the method show returns all list names     
    def show(self):
        return self.keys()
    # the method add, adds a new list to the ListKeeper object
    def add(self,name, new_list):
        self[name]=new_list
    # delete is able to delete a list in the ListKeeper object, specified by its name
    def delete(self,name):
        self.pop(name)
    # sort returns the names of the lists, but sorted
    def sort(self,name):
        return self[name].sort()
    # append extends the specified list with the new_list
    def append(self,name,new_list):
        self[name].extend(new_list)


# noch kommentieren und Aufgabe nochmal durchlesen!