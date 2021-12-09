import numpy  as  np
import  matplotlib.pyplot  as  pp

class smith:
    def  __init__ (self, Z0 = 50 ):
        pp.ioff()
        self.Z0 = Z0
        self.fig = pp.figure(figsize=( 8.0 , 8.0 ))
        pp.axes().set_axis_off()
        self.drawGrid()

    def show(self): 
        pp.figure(self.fig.number)
        pp.show()

    def save(self,filename ):
        self.fig.savefig('smithchart.pdf')

    def  drawZList ( self , l , c = 'b' ):
        pp.figure(self.fig.number)
        xlst  = [ self.z2gamma( z ).real  for  z  in  l ]
        ylst  = [ self.z2gamma( z ).imag  for  z  in  l ]
        pp.plot( xlst , ylst , c )
        pp.draw()

    def  drawXCircle ( self , x , npts = 200 ):

        zlst = [ x ] + [  complex( x , z ) for  z  in  np.logspace( 0 , 6 , npts )]
        self.drawZList ( zlst , 'k' )
        zlst  = [ x ] + [ complex( x , - z ) for  z  in  np.logspace( 0 , 6 , npts )]
        self.drawZList( zlst , 'k' )

    def  drawYCircle ( self , y , npts = 200 ):

        zlst  = [ complex( 0 , y )] + [  complex( z , y ) for  z  in  np.logspace( 0 , 6 , npts )]
        self.drawZList( zlst , 'k' )

    def markZ( self , z , text = None , c = 'b' , size = 1 ):

        pp.figure(self.fig.number)
        g  =  self.z2gamma( z )
        pp.plot( g.real , g.imag , 'o' + c )
        if text:
            pp.text( g.real + 0.02 , g.imag + 0.02 , text , color = c , weight = 'demi' )
        pp.draw()
 
    def  drawGrid (self):
      
        "Dibuja la cuadrícula de Smith Chart."
        
        self.drawXCircle(0)
        self.drawXCircle (self.Z0/5 )
        self.drawXCircle (self.Z0/2 )
        self.drawXCircle (self.Z0)
        self.drawXCircle (self.Z0*2)
        self.drawXCircle (self.Z0*5)
        self.drawYCircle ( 0 )
        self.drawYCircle (self.Z0/5)
        self.drawYCircle (-self.Z0/5)
        self.drawYCircle (self.Z0/2)
        self.drawYCircle (-self.Z0/2)
        self.drawYCircle (self.Z0)
        self.drawYCircle (-self.Z0)
        self.drawYCircle (self.Z0*2)
        self.drawYCircle (-self.Z0*2)
        self.drawYCircle (self.Z0*5)
        self.drawYCircle (-self.Z0*5)

    def  z2gamma ( self , zl ):
        return  complex ( zl - self.Z0 ) / ( zl + self.Z0 )

if  __name__  ==  '__main__' :
    smith=smith()
    smith.markZ( 20 + 30j )
    smith.markZ( 130 - 60j , text = 'Z1' , c = 'r' )
    smith.drawZList([ 0 , 50j , 10000j , - 50j , 0 ])
    smith.show()