class ListKeeper(dict):
    def __init__(self):
        example_list = [1,2,3,4,5]
        self._dict = {'example': example_list}
    def show(self):
        print(self.keys)
    def add(self,name, new_list):
        self[name]=new_list
    def delete(self,name):
        self.pop(name)
    def sort(self,name):
        print(self[name].sort())
    def append(self,name,list):
        self[name].append(list)


