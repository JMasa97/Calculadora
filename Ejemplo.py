import  smith
smith=smith.smith()
smith.markZ(25 + 20j , 'Z1' )
smith.drawZList([ 0 , 50j , 1e6j , - 50j , 0 ])
smith.save('smithchart.pdf')