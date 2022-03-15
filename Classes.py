class Devices:

    def __init__(self, brand, model,):
        self.bd = brand
        self.ml = model

    def set_b_name(self, brand):
        self.bd = brand

    def set_m_name(self, model):
        self.ml = model

    def get_b_name(self):
        return self.bd

    def get_m_name(self):
        return self.ml

    def battery_included(self):
        print('This device includes battery')

class Television(Devices):

    def __init__(self, brand, model, screen_size, weight):
        super().__init__(brand, model)
        self.screensize_t = screen_size
        self.weight_t = weight

    def set_screen_size_t(self, screen_size):
        self.screensize_t = screen_size

    def get_screen_size_t(self):
        return self.screensize_t

    def set_weight_t(self, weight):
        self.weight_t = weight

    def get_weight_t(self):
        return self.weight_t

    def two_pin_plug(self):
        print("This device has european plug")


class Laptop(Devices):

    def __init__(self, brand, model, screen_size, weight):
        super().__init__(brand, model)
        self.screensize_l = screen_size
        self.weight_l = weight

    def set_screen_size_l(self, screen_size):
        self.screensize_l = screen_size

    def get_screen_size_l(self):
        return self.screensize_l

    def set_weight_l(self, weight):
        self.weight_l = weight

    def get_weight_l(self):
        return self.weight_l

    def touchscreen(self):
        print('The device is touch screen')

class Monitors(Devices):

    def __init__(self, brand, model, screen_size, weight):
        super().__init__(brand, model)
        self.screensize_m = screen_size
        self.weight_m = weight

    def set_screen_size_m(self, screen_size):
        self.screensize_m = screen_size

    def get_screen_size_m(self):
        return self.screensize_m

    def set_weight_m(self, weight):
        self.weight_m = weight

    def get_weight_m(self):
        return self.weight_m

    def free_mouse_keyboard(self):
        print('This monitor comes with a free mouse and keyboard')

