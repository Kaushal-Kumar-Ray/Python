class hunam_body:
    def body(self,eye,mouth,leg):
        self.eye=eye
        self.mouth=mouth
        self.leg=leg    
        print(id(self))
    def disp(self):
        print(f"eye={self.eye},mouth={self.mouth},leg={self.leg}")

Ankit=hunam_body()
Ayush=hunam_body()
Prema=hunam_body()
Ankit.body(2,1,2)
Ayush.body(2,4,7)
Prema.body(6,6,3)
Ankit.disp()
Ayush.disp()
Prema.disp()

             