from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *
import numpy as np
from MABreakoutAlphaModel import MABreakoutAlphaModel           
from Risk.MaximumDrawdownPercentPerSecurity import MaximumDrawdownPercentPerSecurity
from Risk.TrailingStopRiskManagementModel import TrailingStopRiskManagementModel
from QuantConnect.Data.UniverseSelection import * 
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel
from Selection.UncorrelatedUniverseSelectionModel import UncorrelatedUniverseSelectionModel

class BasicTemplateFrameworkAlgorithm(QCAlgorithmFramework):

    def Initialize(self):
        
        # Set requested data resolution     
        self.UniverseSettings.Resolution = Resolution.Daily         
        self.SetStartDate(2010, 1, 1)   #Set Start Date         
        self.SetEndDate(2018, 12, 31)    #Set End Date               
       
        self.cash = 20000        
        self.riskPercentage = 0.02 
        self.SetCash(self.cash) #Set Strategy Cash  
        
        self.trigger = False       
        self.Settings.RebalancePortfolioOnInsightChanges = False
        
        self.SetUniverseSelection( MyUniverseSelectionModel(symbols) )    
           
        self.alpha = MABreakoutAlphaModel(resolution=Resolution.Daily, lookback=250, consolidationPeriod=1)
        
        self.SetAlpha(self.alpha)    
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.03))
                
    def CustomSecurityInitializer(self, security):
        security.SetLeverage(1.5)
        security.SetDataNormalizationMode(DataNormalizationMode.Raw)
          
    def RebalanceFunction(self, time):
        trigger = self.alpha.GetTrigger()     
        # self.Debug(f"trigger in alpha: {trigger}")
        if trigger:
            trigger = False
            self.alpha.SetTrigger(trigger)
            return time    
            
        return None
    
    def OnOrderEvent(self, orderEvent):
        if orderEvent.Status == OrderStatus.Filled:
            pass

class MyUniverseSelectionModel(FundamentalUniverseSelectionModel):

    def __init__(self):
        super().__init__(True, None, None)
  
    def SelectCoarse(self, algorithm, coarse):
        filtered = [x for x in coarse if x.HasFundamentalData > 0 and x.Price > 0]
        sortedByDollarVolume = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume][:15]

