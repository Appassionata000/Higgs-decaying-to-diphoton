import ROOT as r
from ShowHistogram import histogram
from ShowHistogram import histogram_2D
from cuts import Cuts


def Analyse(t, weighting):

    t.SetAlias("invMass",
               "sqrt((2 * photon_pt[0] * photon_pt[1]) * (cosh(photon_eta[0] - photon_eta[1]) \
                - cos(photon_phi[0] - photon_phi[1])  ))")
    t.SetAlias("ptconerel0", "photon_ptcone30[0] / photon_pt[0]")
    t.SetAlias("ptconerel1", "photon_ptcone30[1] / photon_pt[1]")
    t.SetAlias("etconerel0", "photon_etcone20[0] / photon_pt[0]")
    t.SetAlias("etconerel1", "photon_etcone20[1] / photon_pt[1]")
    t.SetAlias("photon_p_tot", "sqrt(\
                                 (photon_pt[0] * cos(photon_phi[0]) + photon_pt[1] * cos(photon_phi[1]))**2+\
                                 (photon_pt[0] * sin(photon_phi[0]) + photon_pt[1] * sin(photon_phi[1]))**2+\
                                 (photon_pt[0] * sinh(photon_eta[0]) + photon_pt[1] * sinh(photon_eta[1]))**2)")
    t.SetAlias("photon_pt_tot", "sqrt(\
                                 (photon_pt[0] * cos(photon_phi[0]) + photon_pt[1] * cos(photon_phi[1]))**2+\
                                 (photon_pt[0] * sin(photon_phi[0]) + photon_pt[1] * sin(photon_phi[1]))**2)")
    t.SetAlias("jet_invMass",
               "sqrt((2 * jet_pt[0] * jet_pt[1]) * (cosh(jet_eta[0] - jet_eta[1]) - cos(jet_phi[0] - jet_phi[1])))")

    t.SetAlias("photon_px0", "photon_pt[0] * cos(photon_phi[0])")
    t.SetAlias("photon_py0", "photon_pt[1] * cos(photon_phi[1])")
    t.SetAlias("e_by_invMass0", "photon_pt[0] / invMass")
    t.SetAlias("e_by_invMass1", "photon_pt[1] / invMass")

    cut_10 = Cuts(photon_pt_min=[40e3, 30e3]).tot_cuts()
    cut_11 = Cuts(photon_pt_min=[35e3, 25e3]).tot_cuts()

    cut_20 = Cuts(photon_eta_exclude=True).tot_cuts()

    cut_30 = Cuts(photon_num=2).tot_cuts()
    cut_31 = Cuts(photon_num=2, lepton_num=0).tot_cuts()
    cut_32 = Cuts(lepton_num=0).tot_cuts()

    cut_40 = Cuts(etcone_max=4e3).tot_cuts()
    cut_41 = Cuts(etconerel_max=0.065).tot_cuts()
    cut_42 = Cuts(ptconerel_max=0.065).tot_cuts()
    cut_43 = Cuts(etconerel_max=0.065, ptconerel_max=0.065).tot_cuts()
    cut_44 = Cuts(etconerel_max=0.033, ptconerel_max=0.033).tot_cuts()

    cut_5 = Cuts(e_by_invMass=True).tot_cuts()

    cut_6 = Cuts(photon_isTight=True).tot_cuts()

    cut_comb_1 = Cuts(etcone_max=4e3, photon_isTight=True).tot_cuts()
    cut_comb_2 = Cuts(etcone_max=4e3, photon_isTight=True,
                      photon_eta_exclude=True, photon_pt_min=[40e3, 30e3]).tot_cuts()
    cut_comb_3 = Cuts(etconerel_max=0.065, ptconerel_max=0.065,
                      photon_isTight=True).tot_cuts()
    cut_comb_4 = Cuts(etconerel_max=0.065, ptconerel_max=0.065, photon_isTight=True,
                      photon_eta_exclude=True, photon_pt_min=[40e3, 30e3]).tot_cuts()
    cut_comb_5 = Cuts(etconerel_max=0.065, ptconerel_max=0.065, photon_isTight=True,
                      photon_eta_exclude=True, photon_pt_min=[40e3, 30e3], e_by_invMass=True).tot_cuts()

    cut_pt_tot = Cuts(etconerel_max=0.065, ptconerel_max=0.065, photon_isTight=True, photon_eta_exclude=True,
                      photon_pt_min=[40e3, 30e3], e_by_invMass=True, photon_pt_tot_IN=[120e3, 350e3]).tot_cuts()
    cut_pt_tot_2 = Cuts(etconerel_max=0.065, ptconerel_max=0.065, photon_isTight=True,
                        photon_eta_exclude=True, photon_pt_min=[40e3, 30e3], photon_pt_tot_IN=[120e3, 350e3]).tot_cuts()
    cut_VBF = Cuts(etconerel_max=0.065, ptconerel_max=0.065, photon_isTight=True, photon_eta_exclude=True,
                   photon_pt_min=[40e3, 30e3], e_by_invMass=True, VBF_Enhanced=True).tot_cuts()

    cut_ptcone_1 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.05).tot_cuts()
    cut_ptcone_2 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.055).tot_cuts()
    cut_ptcone_3 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.06).tot_cuts()
    cut_ptcone_4 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.065).tot_cuts()
    cut_ptcone_5 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.07).tot_cuts()
    cut_ptcone_6 = Cuts(photon_pt_min=[40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.075).tot_cuts()
    cut_ptcone_7 = Cuts(photon_pt_min=[
                        40e3, 30e3], photon_eta_exclude=True, photon_isTight=True, ptconerel_max=0.08).tot_cuts()

    cut_cone_1 = Cuts(ptconerel_max=0.060, etconerel_max=0.060).tot_cuts()
    cut_cone_2 = Cuts(ptconerel_max=0.065, etconerel_max=0.065).tot_cuts()
    cut_cone_3 = Cuts(ptconerel_max=0.070, etconerel_max=0.070).tot_cuts()

    ptconecut1 = Cuts(ptconerel_max=0.025).tot_cuts()
    ptconecut_10 = Cuts(ptconerel_max=0.026).tot_cuts()
    ptconecut_11 = Cuts(ptconerel_max=0.027).tot_cuts()
    ptconecut_12 = Cuts(ptconerel_max=0.028).tot_cuts()
    ptconecut_13 = Cuts(ptconerel_max=0.029).tot_cuts()

    ptconecut2 = Cuts(ptconerel_max=0.030).tot_cuts()
    ptconecut_20 = Cuts(ptconerel_max=0.031).tot_cuts()
    ptconecut_21 = Cuts(ptconerel_max=0.032).tot_cuts()
    ptconecut_22 = Cuts(ptconerel_max=0.033).tot_cuts()
    ptconecut_23 = Cuts(ptconerel_max=0.034).tot_cuts()

    ptconecut3 = Cuts(ptconerel_max=0.035).tot_cuts()
    ptconecut_30 = Cuts(ptconerel_max=0.036).tot_cuts()
    ptconecut_31 = Cuts(ptconerel_max=0.037).tot_cuts()
    ptconecut_32 = Cuts(ptconerel_max=0.038).tot_cuts()
    ptconecut_33 = Cuts(ptconerel_max=0.039).tot_cuts()

    ptconecut4 = Cuts(ptconerel_max=0.040).tot_cuts()
    ptconecut5 = Cuts(ptconerel_max=0.045).tot_cuts()
    ptconecut6 = Cuts(ptconerel_max=0.050).tot_cuts()
    ptconecut7 = Cuts(ptconerel_max=0.055).tot_cuts()
    ptconecut8 = Cuts(ptconerel_max=0.060).tot_cuts()
    ptconecut9 = Cuts(ptconerel_max=0.065).tot_cuts()
    ptconecut10 = Cuts(ptconerel_max=0.070).tot_cuts()

    etconecut00 = Cuts(etconerel_max=0).tot_cuts()
    etconecut01 = Cuts(etconerel_max=0.01).tot_cuts()
    etconecut02 = Cuts(etconerel_max=0.02).tot_cuts()
    etconecut03 = Cuts(etconerel_max=0.03).tot_cuts()
    etconecut04 = Cuts(etconerel_max=0.04).tot_cuts()
    etconecut05 = Cuts(etconerel_max=0.05).tot_cuts()
    etconecut06 = Cuts(etconerel_max=0.06).tot_cuts()
    etconecut07 = Cuts(etconerel_max=0.07).tot_cuts()

    cut_final_1 = Cuts(photon_pt_min=[40e3, 30e3], photon_num=2, etconerel_max=0.03, ptconerel_max=0.033,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_2 = Cuts(photon_pt_min=[40e3, 30e3], photon_num=2, etconerel_max=0.055, ptconerel_max=0.055,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_3 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.055, ptconerel_max=0.055,
                        e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_4 = Cuts(photon_pt_min=[35e3, 25e3], photon_num=2, etconerel_max=0.055, ptconerel_max=0.055,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_5 = Cuts(photon_pt_min=[35e3, 25e3], etconerel_max=0.055, ptconerel_max=0.055,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_6 = Cuts(photon_pt_min=[35e3, 25e3], etconerel_max=0.055,
                       ptconerel_max=0.055, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_7 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.05,
                        ptconerel_max=0.065, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_8 = Cuts(photon_pt_min=[40e3, 30e3], photon_num=2, etconerel_max=0.065, ptconerel_max=0.065,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_9 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.065, ptconerel_max=0.065,
                       e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_10 = Cuts(photon_pt_min=[40e3, 30e3], photon_num=2, etconerel_max=0.055,
                       ptconerel_max=0.055, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    cut_final_11 = Cuts(photon_pt_min=[35e3, 25e3], photon_num=2, lepton_num=0, etconerel_max=0.055,
                       ptconerel_max=0.055, e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()

    isolation_comb_1 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.05, ptconerel_max=0.05,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_2 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.055, ptconerel_max=0.055,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_3 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.06, ptconerel_max=0.06,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_4 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.065, ptconerel_max=0.065,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_5 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.07, ptconerel_max=0.07,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_6 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.05, ptconerel_max=0.065,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()
    
    isolation_comb_7 = Cuts(photon_pt_min=[40e3, 30e3], etconerel_max=0.08, ptconerel_max=0.08,
                            e_by_invMass=True, photon_eta_exclude=True, photon_isTight=True).tot_cuts()

    histogram(t=t, weighting=weighting, variable="invMass",  hist_id="invMass",
              n_bins=80, xmin=0, xmax=160e3, cuts="1")
    

    