from BC.Timeseries import Timeseries
from BC.getAmbientBC import getAmbientBC
from datetime import datetime, timedelta

def case_default():
    Parameters = dict()
    Parameters['tf'] = 60*60  # 1 hour in seconds
    Parameters['ts'] = .1     # time step = seconds

    # Time Series Boundary Conditions
    BC=dict()
    BC['temp']     = Timeseries([0, 1], [0, 0])

    # Get Ambient conditions
    Parameters['geolocation'] = [33.456506143111966, -111.68313649552813]
    start_naive = datetime(2021, 8, 30, 8,0,0)
    end_naive = start_naive + timedelta(seconds=Parameters['tf'])
    [BC['Tamb_degR'], BC['Pamb_Pa']] = getAmbientBC(start_naive, end_naive)


    IC=dict()
    # Constants
    IC['tf'] = 100
    IC['ts'] = .1

    # Plant properties
    #Contents defintion
    Contents = dict()
    Contents['h'] = .2
    Contents['As']= 1
    Contents['rho']=100
    Contents['V'] = .9*.9*.9 # m^3 = 3*3*3ft^2
    Contents['c'] = 1
    Parameters['contents'] = Contents

    # Air definition
    Air = dict()
    Air['h'] = .1
    Air['As']= 1
    Air['rho']=1
    Air['V'] = 3.35*3.35*3.35 #m^3 = 11*11*11ft^3
    Air['c'] = 1
    Parameters['air'] = Air





    # Initial Conditions
    IC = dict()
    IC['T0'] = 0
    IC['Tinf0'] = 0
    Parameters['IC'] = IC

    # Other Parameters
    Parameters['geolocation'] = [33.456506143111966, -111.68313649552813]

    return [BC, Parameters]

if __name__ == "__main__":
    case_default()