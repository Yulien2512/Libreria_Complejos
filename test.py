import unittest
import libreria_complejos as cplx

class TestCplxMethods(unittest.TestCase):

    def test_suma(self):
        tsuma = cplx.suma((5.6, -8),(3.4, 5.2))
        self.assertAlmostEqual(tsuma[0],9.0)
        self.assertAlmostEqual(tsuma[1],-2.8)

    def test_suma2(self):
        tsuma = cplx.suma((2.3,6.5),(1.4, -5.2))
        self.assertAlmostEqual(tsuma[0],3.69, places = 1)
        self.assertAlmostEqual(tsuma[1],1.29, places = 1)

    def test_producto(self):
        produ1 ,produ2 = cplx.producto((5.6, -8),(3.4, 5.2))
        self.assertAlmostEqual(produ1, 60.64)
        self.assertAlmostEqual(produ2,-54.4)
        

    def test2_producto2(self):
        prod1,prod2 = cplx.producto((2.3,6.5),(1.4, -5.2))
        self.assertAlmostEqual(prod1,37.02)
        self.assertAlmostEqual(prod2,18.2)

    def test_resta(self):
        res1,res2 = cplx.resta((5.6,-8),(3.4,5.2))
        self.assertAlmostEqual(res1,2.19, places = 1)
        self.assertAlmostEqual(res2,-13.2, places = 1)

    def test_resta2(self):
        res1,res2 = cplx.resta((2.3,6.5),(1.4, -5.2))
        self.assertAlmostEqual(res1,0.89, places = 1)
        self.assertAlmostEqual(res2,11.7, places = 1)

    def test_division(self):
        div1,div2 = cplx.division((5.6,-8),(3.4, 5.2))
        self.assertAlmostEqual(div1,-0.58, places = 1)
        self.assertAlmostEqual(div2,-1.45, places = 1)

    def test_division2(self):
        div1,div2 = cplx.division((2.3,6.5),(1.4, -5.2))
        self.assertAlmostEqual(div1,-1.05, places = 1)
        self.assertAlmostEqual(div2,0.72, places = 1)
    
    def test_modulo(self):
        mod = cplx.modulo((5.6,-8))
        self.assertAlmostEqual(mod,9.76, places = 1)
        
    def test_modulo2(self):
        mod = cplx.modulo((2.3,6.5))
        self.assertAlmostEqual(mod,6.89, places = 1)
        
    def test_conjugado(self):
        conj1 = cplx.conjugado((5.6, -8))
        self.assertAlmostEqual(conj1,(5.6, 8))
        

    def test_conjugado2(self):
        conj1 = cplx.conjugado((2.3,6.5))
        self.assertAlmostEqual(conj1,(2.3, -6.5))
        
    
    def test_polar(self):
        pol = cplx.polar((5.6, -8))
        self.assertAlmostEqual(pol[0],9.76, places = 1)
        self.assertAlmostEqual(pol[1],-55.0, places = 1)

    def test_polar2(self):
        pol = cplx.polar((2.3,6.5))
        self.assertAlmostEqual(pol[0],6.89, places = 1)
        self.assertAlmostEqual(pol[1],70.51, places = 1)
    
    def test_cartesiano(self):
        car = cplx.cartesiano((5.6,-8))
        self.assertAlmostEqual(car[0],5.54, places = 1)
        self.assertAlmostEqual(car[1],-0.77, places = 1)

    def test_cartesiano2(self):
        car = cplx.cartesiano((2.3,6.5))
        self.assertAlmostEqual(car[0],2.28, places = 1)
        self.assertAlmostEqual(car[1],0.26, places = 1)

    def test_fase(self):
        fas = cplx.fase((5.6,-8))
        self.assertAlmostEqual(fas,-55.00, places = 1)
        

    def test_fase2(self):
        fas = cplx.fase((2.3,6.5))
        self.assertAlmostEqual(fas,70.51, places = 1)
        

    

if __name__ == '__main__':
    unittest.main()