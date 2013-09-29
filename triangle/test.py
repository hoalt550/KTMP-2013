from math import sqrt
import unittest
from triangle import detect_triangle

class TriangleTest(unittest.TestCase):
        #Test du lieu nhap vao
        def testInput1(self):
                result = detect_triangle("a", 9, 4)
                self.assertEquals(result, 'Input invalid!')
        
        def testInput2(self):
                result = detect_triangle(6, "a", 4)
                self.assertEquals(result, 'Input invalid!')
        
        def testInput3(self):
                result = detect_triangle(5, 9, "a")
                self.assertEquals(result, 'Input invalid!')
        
        def testInput4(self):
                result = detect_triangle("a", "a", 4)
                self.assertEquals(result, 'Input invalid!')
        
        def testInput5(self):
                result = detect_triangle("a", 9, "a")
                self.assertEquals(result, 'Input invalid!')
        
        def testInput6(self):
                result = detect_triangle(8, "a", "a")
                self.assertEquals(result, 'Input invalid!')
        
        def testInput7(self):
                result = detect_triangle("a", "a", "a")
                self.assertEquals(result, 'Input invalid!')
        
        #Nhap chuoi
        def testInput8(self):
                result = detect_triangle("4", 4, 6)
                self.assertEqual(result, "Tam giac can")
        def testInput9(self):
                result = detect_triangle("4", "4", 6)
                self.assertEqual(result, "Tam giac can")
        def testInput10(self):
                result = detect_triangle("4", "4", "6")
                self.assertEqual(result, "Tam giac can")
        
        #Test khoang gia tri cua bien
        
        def test_max1(self):
                result = detect_triangle(pow(2,32), 2 , 4)
                self.assertEquals(result, 'Input invalid!')
        def test_max2(self):
                result = detect_triangle(pow(2,32), pow(2,32) , 4)
                self.assertEquals(result, 'Input invalid!')
        def test_max3(self):
                result = detect_triangle(pow(2,32), pow(2,32) , pow(2,32))
                self.assertEquals(result, 'Input invalid!')
                
        def test_min1(self):
                result = detect_triangle(-1, 9, 9)
                self.assertEquals(result, 'Input invalid!')
        def test_min2(self):
                result = detect_triangle(-1, -1, 9)
                self.assertEquals(result, 'Input invalid!')
        def test_min3(self):
                result = detect_triangle(-1, -1, -1)
                self.assertEquals(result, 'Input invalid!')
                
        #Test nhan dang
        def test_Deu(self):
                result = detect_triangle(2, 2, 2)
                self.assertEquals(result, 'Tam giac deu')

        def test_Can(self):
                result = detect_triangle(2, 2, 1)
                self.assertEquals(result, 'Tam giac can')

        def test_Thuong(self):
                result = detect_triangle(3, 4, 6)
                self.assertEquals(result, 'Tam giac thuong')

        def test_KhongLaTamGiac(self):
                result = detect_triangle(0, 0, 5)
                self.assertEquals(result, 'Input invalid!')

        def test_VuongCan(self):
                result = detect_triangle(sqrt(pow(9, 2)*2), 9, 9)
                self.assertEquals(result, 'Tam giac vuong can')
                
if __name__ == '__main__':
    unittest.main()
