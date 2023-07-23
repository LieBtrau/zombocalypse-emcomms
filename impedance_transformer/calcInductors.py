import math
import numpy as np

def calc_toroid_max_turns(ID, d):
    '''
    Calculate the number of turns so that there's no overlap
    Reference : [https://www.had2know.org/technology/calculate-toroidal-coil-inductor-wire.html]
    ID = inner diameter of the core in [m]
    d = diameter of the wire in [m]
    '''
    return math.ceil(math.pi/math.asin(d/(ID-d)))
    
def calc_inductor_turns(Al, L, turns_ratio):
    '''
    Calculate the required number of primary and secondary turns for the given inductance factor and inductance
    value according to L = Al * N² (see also ARRL §5.7.3)
    Al = Inductance factor in [nH/N²]
    L = Inductance value in [H]
    return = [number of turns for primary winding, number of turns for secondary winding]
    ''' 
    Np = math.ceil(math.sqrt(L/(Al*1e-9)))
    Ns = math.ceil(Np*turns_ratio)
    return [Np, Ns]

def calc_toroid_wirelength(OD, ID, d, h, N):
    '''
    Calculate the needed wire length for winding a toroid.
    Reference : Wire length, calculation from (How To Calculate Toroid Winding Length)[http://www.how2power.com/newsletters/1309/H2PowerToday1309_FocusOnMagnetics.pdf]
    OD = outer diameter of the toroid in [m]
    ID = inner diameter of the toroid in [m]
    d = wire diameter in [m]
    h = height of the toroid [m]
    N = number of turns
    '''
    ri = ID/2 # inside radius
    rcw = d/2 # insulated wire radius
    w = (OD/2 - ID/2) # toroid width
    L = ri / (2*rcw)
    Nw = math.pi * math.pow(L,2)
    M = L - math.sqrt((Nw-N)/math.pi)
    return round(2 * math.pi * M * ((2*(h+w)+8*rcw*M)*(L-M/2)+4/3*rcw*(1-math.pow(M,2))),2)
    
def calc_max_flux_density(Ae, Pmax, Zin, fmin, Np):
    # Maximum coil voltage
    Erms = math.sqrt( Pmax * Zin)
    # Maximum flux density
    return Erms / (4.44 * Ae * Np * fmin) # [T]

def transformer_bandwidth_calculation(f, SRF, Np, Zs, Z_open, Z_closed):
    '''
    @f [Hz] = measuring frequency (typ. 500kHz)
    @SRF [Hz] = measured self resonant frequency (= frequency where imaginary part of impedance is zero)
    @Np [] = number of primary turns
    @Zs [Ω] = source impedance (typ. 50)
    @Z_open [Ω] = Measured impedance at frequency f of primary coil, with secondary coil open
    @Z_closed [Ω] Measured impedance at frequency f of primary coil, with secondary coil short-circuited
    '''
    Ll = Z_closed.imag / (2*math.pi*f) # [H] Leakage inductance (with secondary transferred to primary)
    print('Leakage inductance = {:.3}H'.format(Ll))
    Lm = Z_open.imag / (2*math.pi*f) - Ll # [H] magnetization inductance
    print('Magnetization inductance = {:.3}H'.format(Lm))
    Rw = Z_open.real # [Ω] winding resistance
    Al = Lm / math.pow(Np,2) * 1e9
    print('Al = {:.3} nH/N²'.format(Al))
    Cw = 1 / (math.pow(2*math.pi*SRF,2)*Lm) # [F] winding capacitance
    print('Cw = {:.3} F'.format(Cw))
    fl = Zs / (2*math.pi*Lm) # Low frequency cut-off
    print('Low frequency cut-off (fl) = {:.3}Hz'.format(fl))
    fh_cw = 1 / (2*math.pi*Zs*Cw) # High-frequency cut-off due to winding capacitance alone
    print('High frequency cut-off due to winding capacitance = {:.3}Hz'.format(fh_cw))
    fh_cw_Ll = 1 / (2*math.pi*math.sqrt(Ll*Cw))
    print('High frequency cut-off due to resonance of winding capacitance and leakage inductance = {:.3}Hz'.format(fh_cw_Ll))

def calcSRF(nw):
    '''
    Find resonant frequency
    nw = scikit-rf network
    return [real impedance at SRF, SRF]
    '''
    return [nw.z_re.max(), nw.f[np.argmax(nw.z_re)]]

