#Calculate overlap between BNS waveforms using the A-LIGO noise curve w/ m1 = m2 = 1.4M_0
#Let lambda1 = most likely tidal deformability of GW170817, vary lambda2, calculate the overlap

#(The A-LIGO noise curve uses the SEOBNRv4_ROM waveform approximant.) The most likely tidal deformability of GW170817 is lambda1 <= 970 with a 95% upper bound on low spin priors: lambda1. Two waveforms with this approximant are plotted over one another, both with this lambda value



%matplotlib inline

from pycbc.waveform import get_td_waveform
from pycbc.psd import interpolate, inverse_spectrum_truncation
from pycbc.filter import overlap
import pylab
import math

hp, hc = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 970, lambda2 = 970)

pylab.plot(hp.sample_times, hp, label = 'Plus Polarization')
pylab.xlabel('Time(s)')
pylab.xlim(-0.05, 0.05)
pylab.legend()
pylab.grid()
pylab.show()



lambda_values = [970, 1000, 1300]

for l in lambda_values:
    hp, hc = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 970, lambda2 = l)
    pylab.plot(hp.sample_times, hp, label = 'lambda2 = %s' % l)

pylab.xlabel('Time(s)')
pylab.xlim(-0.05, 0.01)
pylab.legend()
pylab.grid()
pylab.show()



Lambda Tilde is a quantity calculated using lambda1, lambda2, and the mass ratio(m2/m1 <= 1). This quantity describes how tidal deformations(effects) are impranted on the gravitational wave signal detected.
Lambda Tilde = (16/13)(((12q + 1)lambda1) + (12 + q)*q^4 * lambda2))/(1 + q)^5)


q = mass2 / mass1

for l in lambda_values:
    lambda_tilde = (16/13) * (((12*q + 1)*lambda1 + l*(12 + q)*pow(q, 4))/(pow((1 + q), 5)))
    print "lambda1 = ", lambda1, "lambda2 = ", l, "lambda_tilde = ", lambda_tilde



#In order to calculate a Matched Filter (which is needed to calculate overlap), a psd must be calculated.
#The psd of the varying lambda (lambda2) will be calculated as lambda1 acts as a template while lambda2 acts as the data
#After S_n(f) is calculated for lambda2, PyCBC's matched_filter() function can be used to calculate overlap between waveforms of varying lambda values




#lamda1 = 222, lambda2 = 222
hp_L2_222, hc_L2_222 = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 222.0, lambda2 = 222.0)
psd_L2_222 = hp_L2_222.psd(4)
psd_L2_222 = interpolate(psd_L2_222, hp_L2_222.delta_f)
psd_L2_222 = inverse_spectrum_truncation(psd_L2_222, 4*hp_L2_222.sample_rate, low_frequency_cutoff = 15.0)
print "psd_L2_222:", psd_L2_222
print ""

#lamda1 = 222, lambda2 = 300
hp_L2_300, hc_L2_300 = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 222.0, lambda2 = 300.0)
psd_L2_300 = hp_L2_300.psd(4)
psd_L2_300 = interpolate(psd_L2_300, hp_L2_300.delta_f)
psd_L2_300 = inverse_spectrum_truncation(psd_L2_300, 4*hp_L2_300.sample_rate, low_frequency_cutoff = 15.0)
print "psd_L2_300:", psd_L2_300
print ""

#lambda1 = 222, lambda2 = 400
hp_L2_400, hc_L2_400 = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 222.0, lambda2 = 400.0)
psd_L2_400 = hp_L2_400.psd(4)
psd_L2_400 = interpolate(psd_L2_400, hp_L2_400.delta_f)
psd_L2_400 = inverse_spectrum_truncation(psd_L2_400, 4*hp_L2_400.sample_rate, low_frequency_cutoff = 15.0)
print "psd_L2_400:", psd_L2_400
print ""

#lambda1 = 222, lambda2 = 500
hp_L2_500, hc_L2_500 = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 222.0, lambda2 = 500.0)
psd_L2_500 = hp_L2_500.psd(4)
psd_L2_500 = interpolate(psd_L2_500, hp_L2_500.delta_f)
psd_L2_500 = inverse_spectrum_truncation(psd_L2_500, 4*hp_L2_500.sample_rate, low_frequency_cutoff = 15.0)
print "psd_L2_500:", psd_L2_500
print ""

#lambda1 = 222, lambda2 = 600
hp_L2_600, hc_L2_600 = get_td_waveform(approximant = "TaylorF2", mass1 = 1.4, mass2 = 1.4,  
                                                       delta_t = 1.0/4096, f_lower = 30,
                                                       lambda1 = 222.0, lambda2 = 600.0)
psd_L2_600 = hp_L2_600.psd(4)
psd_L2_600 = interpolate(psd_L2_600, hp_L2_600.delta_f)
psd_L2_600 = inverse_spectrum_truncation(psd_L2_600, 4*hp_L2_600.sample_rate, low_frequency_cutoff = 15.0)
print "psd_L2_600:", psd_L2_600
print ""


overlaps = []

#Overlap between lambda1 = lambda2 = 222
overlap_lambda2_222 = overlap(hp, hp, psd_L2_222, low_frequency_cutoff = 15.0)
overlaps.append(overlap_lambda2_222)

#Overlap between lambda1 = 222, lambda2 = 300
overlap_lambda2_300 = overlap(hp, hp_L2_300, psd_L2_300,low_frequency_cutoff = 15.0)
overlaps.append(overlap_lambda2_300)

#Overlap between lambda1 = 222, lambda2 = 400
overlap_lambda2_400 = overlap(hp, hp_L2_400, psd_L2_400,low_frequency_cutoff = 15.0)
overlaps.append(overlap_lambda2_400)

#Overlap between lambda1 = 222, lambda2 = 500
overlap_lambda2_500 = overlap(hp, hp_L2_500, psd_L2_500,low_frequency_cutoff = 15.0)
overlaps.append(overlap_lambda2_500)

#Overlap between lambda1 = 222, lambda2 = 600
overlap_lambda2_600 = overlap(hp, hp_L2_600, psd_L2_600,low_frequency_cutoff = 15.0)
overlaps.append(overlap_lambda2_600)

print overlaps


