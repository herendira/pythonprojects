from final_final2 import capacity, montant_loan
import pytest

def test_capacity():
     assert capacity (1500,500)==400


def test_montant_loan():
   
    assert montant_loan(45000, 30, 3, 20000)==90.27777777777777
    assert montant_loan(45000, 30, 4, 20000)==97.22222222222223
    assert montant_loan(45000, 30, 5, 20000)==104.16666666666667
    assert montant_loan(45000, 30, 6, 20000)==111.1111111111111
    assert montant_loan(45000, 30, 7, 20000)==118.05555555555556

    assert montant_loan(45000, 15, 3, 20000)==180.55555555555554 
    assert montant_loan(45000, 15, 4, 20000)==194.44444444444446 
    assert montant_loan(45000, 15, 5, 20000)==208.33333333333334
    assert montant_loan(45000, 15, 6, 20000)==222.2222222222222
    assert montant_loan(45000, 15, 7, 20000)==236.11111111111111
        
    
    
          

pytest.main(["-v", "--tb=line", "-rN", __file__])