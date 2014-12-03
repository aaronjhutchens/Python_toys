class dynamicPatient:
     def __init__(self, **kwVitals):
         for name, value in kwVitals.items():
             setattr(self, name, value)
