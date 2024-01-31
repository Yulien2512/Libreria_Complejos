import unittest
import libreria_complejos as cplx

class TestCplxOperations(unittest.TestCase):

    def test_suma(self):
        tsuma = cplx.suma((5.6, -8),(3.4, 5.2))
        self.assertAlmostEqual(tsuma[0],9.0)
        self.assertAlmostEqual(tsuma[1],-2.8)

    def test2_suma(self):
        tsuma = cplx.suma((5,1),(7,10.2))
        self.assertAlmostEqual(tsuma[0],12)
        self.assertAlmostEqual(tsuma[1],11.2)

    def test_producto(self):
        produ1 ,produ2 = cplx.producto((5.6, -8),(3.4, 5.2))
        self.assertAlmostEqual(produ1, 60.64)
        self.assertAlmostEqual(produ2,-54.4)
        

    def test2_producto(self):
        produ1,produ2 = cplx.producto((5,1),(7,10.2))
        self.assertAlmostEqual(produ1,24.8)
        self.assertAlmostEqual(produ2,58)

    def test_resta(self):
        res1,res2 = cplx.resta((3,2),(-5,5.2))
        self.assertAlmostEqual(res1,8)
        self.assertAlmostEqual(res2,-3.2)

    def test2_resta(self):
        res1,res2 = cplx.resta((5,1),(7,10.2))
        self.assertAlmostEqual(res1,-2)
        self.assertAlmostEqual(res2,-9.2)

    def test_division(self):
        div1,div2 = cplx.division((3,2),(-5,5.2))
        self.assertAlmostEqual(div1,-1.3)
        self.assertAlmostEqual(div2,-1.0)

    def test2_division(self):
        div1,div2 = cplx.division((5,1),(7,10.2))
        self.assertAlmostEqual(div1,0.6)
        self.assertAlmostEqual(div2,-0.1)
    
    def test_modulo(self):
        mod = cplx.modulo((3,2))
        self.assertAlmostEqual(mod,3.60)
        
    def test2_modulo(self):
        mod = cplx.modulo((5,1))
        self.assertAlmostEqual(mod,5.1)
        
    def test_conjugado(self):
        conj1,conj2 = cplx.conjugado((3,2),(-5,5.2))
        self.assertAlmostEqual(conj1[0][1],-2)
        self.assertAlmostEqual(conj2[1][1],-5.2)

    def test2_conjugado(self):
        conj1,conj2 = cplx.conjugado((5,1),(7,10.2))
        self.assertAlmostEqual(conj1[0][1],-1)
        self.assertAlmostEqual(conj2[1][1],-10.2) 
    
    def test_polar(self):
        pol = cplx.polar((3,2))
        self.assertAlmostEqual(pol[0],3.6)
        self.assertAlmostEqual(pol[1],0.8)

    def test2_polar(self):
        pol = cplx.polar((5,1))
        self.assertAlmostEqual(pol[0],5.09)
        self.assertAlmostEqual(pol[1],0.19)
    
    def test_cartesiano(self):
        car = cplx.cartesiano((3,2))
        self.assertAlmostEqual(car[0],3.0)
        self.assertAlmostEqual(car[1],1.9)

    def test2_cartesiano(self):
        car = cplx.cartesiano((5,1))
        self.assertAlmostEqual(car[0],4.9)
        self.assertAlmostEqual(car[1],0.96)

    def test_fase(self):
        fas = cplx.fase((3,2))
        self.assertAlmostEqual(fas,0.6)
        

    def test2_fasecplx(self):
        fas = cplx.fase((5,1))
        self.assertAlmostEqual(fas,0.2)
        

    

if __name__ == '__main__':
    unittest.main()