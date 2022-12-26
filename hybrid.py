""" volume
        |    |
        cone  sphere
         |     |
        (large volume)
"""
class volume:
    def get(self):
        self.r=float(input("Enter radius="))
        self.h=float(input("Enter height="))
class cone(volume):
    def volcon(self):
        volume.get(self)
        self.vc=0.3*3.14*(self.r**2)*self.h
class sphere(volume):
    def volsph(self):
        volume.get(self)
        self.vs=1.33*3.14*(self.r**3)
class large(cone,sphere):
    def display(self):
        cone.volcon(self)
        sphere.volsph(self)
        if self.vc < self.vs:
            print('cone has large volume')
o=large()
o.display()
           
        
