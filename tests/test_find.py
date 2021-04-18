from unithash import find

def test_get_unithash():
        assert find.get_unithash(1234567) == 1

def test_set_unithash():
        assert find.set_unithash('1234567812345678',4) == 1818
