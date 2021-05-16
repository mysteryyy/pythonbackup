import unittest
import pandas as pd
import numpy as np
import slintraday

class TestTrades(unittest.TestCase):
    
    pr = pd.DataFrame(columns=["open","high","low","close","signal",],data=np.ones((20,5)))

    def sl_shortl(self,pr):
        pr=self.pr
        pr['signal']=0
        pr.loc[10,'signal']=-1
        pr.loc[12,'high']=1.05
        pr.loc[13,'low']=0.97
        pr.loc[15,'close']=1.012

        self.assertEqual(slintraday().extract_signal_trades(pr), -1, "Should be -1")










if __name__=='__main__':
    unittest.main()
