class Manoj:
    def __init__(self,model,camera):
        self.model = model
        self.camera = camera

    def make_call(self, number):
        print("calling....{}".format(number))

manoj_obj = Manoj(
    "Samsung Galaxy","64 MP")
print(id(manoj_obj))
manoj_obj1= Manoj(
    "samsung 56j","56MP"
)
print(id(manoj_obj1))