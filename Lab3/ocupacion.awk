BEGIN { 
		         print "Nivel de ocupación" 
		 } 
		 /^\/dev\/hd/ { 
				          print "Partición ",$6,": ", $5 
				  } 
				  END { print "Terminado" }
