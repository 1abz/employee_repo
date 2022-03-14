class Devices:
    def __init__(self, make_, model_):
        self.make = make_
        self.model = model_

    def get_make(self):
        return self.make

    def set_make(self, new_make):
        if len(new_make.strip()) >= 1:
            self.make = new_make

    def get_model(self, new_model):
        return self.model
