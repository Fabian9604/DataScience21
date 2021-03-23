class ListKeeper(dict):
    def __init__(self):
        dict.__init__(self)
        self['example'] = [1,2,3,4,5]
        print (type(self))
    def show(self):
        #print(self)
        print (self.keys())
        print('a')
    def add(self,name, new_list):
        self[name]=new_list
    def delete(self,name):
        self.pop(name)
    def sort(self,name):
        print(self[name].sort())
    def append(self,name,new_list):
        self[name].extend(new_list)


# noch kommentieren und Aufgabe nochmal durchlesen!